#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<paramater>')
def print_string(paramater):
    print(paramater)
    return f'{paramater}'

@app.route('/count/<int:paramater>')
def count(paramater):
    numbers = []
    for i in range(paramater):
        numbers.append(i)
    result = "\n".join(map(str, numbers))
    return result + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    parsed1 = int(num1)
    parsed2 = int(num2)
    result = None
    if operation == '+':
        result = num1 + num2
        
    elif operation == '-':
        result = num1 - num2
        
    elif operation == '*':
        result = num1 * num2 
        
    elif operation == 'div':
        result = num1 / num2
        
    elif operation == '%':
        result = num1 % num2
        
    else:
        "Invalid operation"
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
