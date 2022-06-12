import json


with open('input.json') as f:
    with open('output.txt', 'w') as out:
        data = json.load(f)

        for coin in data:
            name = coin.get('currency')
            history = coin.get('history')
            minimum = min(history)
            maximum = max(history)
            current = history[len(history)-1]
        
            out.write(f"{name} {minimum} {maximum} {current}\n")