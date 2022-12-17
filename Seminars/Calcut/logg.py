from datetime import datetime as dt

def reset (some_str, result):
    time = dt.now().strftime('%H:%M')
    with open('logg_calc.txt', 'a') as file:
        file.write(f'{time}: {some_str} = {result}\n')
