from flask import Flask

app = Flask(__name__) 

@app.route('/<name>')
def index(name: str = 'Afiz'):
    return f'<h2>Hello {name.capitalize()}!</h2>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2345)