from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'title' : 'Index',
        'header' : 'CALCULADORA GESTION DE RIESGO LUIS'
    }
    return render_template('index.html', data = data)

@app.route('/bolsa')
def bolsa():
    data = {
        'title' : 'Bolsa',
        'header' : 'Bolsa Calculator',
        'body' : 'bolsa'
    }
    return render_template('bolsa.html', data=data)

@app.route('/crypto')
def crypto():
    data = {
        'title' : 'Crypto',
        'header' : 'Crypto Calculator',
        'body' : 'Crypto'
    }
    return render_template('crypto.html', data=data)

def page_not_found(error):
    data = {
        'title' : 'Crypto',
        'header' : 'Crypto Calculator',
        'body' : 'Crypto'
    }
    return render_template('crypto.html', error)

if __name__ == '__main__':
    app.error_handler_spec(page_not_found, 404)
    app.run(debug=True, port=5006)
