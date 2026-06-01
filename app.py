from flask import Flask,flash, render_template, redirect
from flask_wtf import FlaskForm

app= Flask(__name__)

app.config['secret-key'] = 'Supersecreto'

FILMES = {
    1: {'id': 1, 'titulo': 'O Senhor dos Anéis', 'ano': 2001, 'duracao': 178},
    2: {'id': 2, 'titulo': 'Interestelar',       'ano': 2014, 'duracao': 169},
    3: {'id': 3, 'titulo': 'Parasita',           'ano': 2019, 'duracao': 132},
    4: {'id': 4, 'titulo': 'Cidade de Deus',     'ano': 2002, 'duracao': 130},
}

@app.route('/')
def raiz():
    return render_template('filmes.html')

@app.route('/filme')
def filmes():
    return render_template('filmes.html')

@app.route('/assistir')
def watchlist():
    return render_template('watchlist.html')

if __name__ == '__main__':
    app.run(debug=True, port=3001)