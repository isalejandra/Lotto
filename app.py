from flask import Flask, render_template, request, session, jsonify
import random
import json

app = Flask(__name__)
app.secret_key = 'lotto_secret_key'  # For session management

@app.route('/', methods=['GET', 'POST'])
def lotto():
    if 'history' not in session:
        session['history'] = []

    result = None
    if request.method == 'POST':
        try:
            user_numbers = [int(request.form[f'num{i}']) for i in range(1, 6)]
            # Validate uniqueness and range
            if len(set(user_numbers)) != 5 or any(n < 1 or n > 50 for n in user_numbers):
                result = "Invalid input: Choose 5 unique numbers between 1 and 50."
            else:
                # Generate 5 unique random numbers
                draw_numbers = random.sample(range(1, 51), 5)
                matches = len(set(user_numbers) & set(draw_numbers))
                prize = 0
                if matches == 3:
                    prize = 1000000  # 1 Million Euros
                elif matches == 4:
                    prize = 20000000  # 20 Million Euros
                elif matches == 5:
                    prize = 200000000  # 200 Million Euros
                
                result = {
                    'user_numbers': user_numbers,
                    'draw_numbers': draw_numbers,
                    'matches': matches,
                    'prize': prize
                }
                # Save to history
                session['history'].append(result)
                session.modified = True
        except ValueError:
            result = "Invalid input: All entries must be numbers."

    return render_template('index.html', result=result, history=session['history'])

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    user_numbers = set(data.get('user_numbers', []))
    max_attempts = int(data.get('max_attempts', 1000))
    
    results = []
    attempt = 0
    
    while attempt < max_attempts:
        attempt += 1
        draw_numbers = random.sample(range(1, 51), 5)
        matches = len(user_numbers & set(draw_numbers))
        
        results.append({
            'attempt': attempt,
            'draw_numbers': draw_numbers,
            'matches': matches
        })
        
        if matches >= 3:
            prize = 0
            if matches == 3:
                prize = 1000000
            elif matches == 4:
                prize = 20000000
            elif matches == 5:
                prize = 200000000
            
            result = {
                'user_numbers': list(user_numbers),
                'draw_numbers': draw_numbers,
                'matches': matches,
                'prize': prize,
                'attempts': attempt,
                'results': results
            }
            session['history'].append(result)
            session.modified = True
            return jsonify({'status': 'won', 'data': result})
    
    return jsonify({'status': 'lost', 'data': {'attempts': max_attempts, 'results': results}})

if __name__ == '__main__':
    app.run(debug=True)