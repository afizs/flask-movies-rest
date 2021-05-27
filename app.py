from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<name>')
@app.route('/')
def index(name: str = 'world'):
    return render_template('index.html', name=name.capitalize())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2345)
