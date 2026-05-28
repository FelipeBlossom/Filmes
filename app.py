from flask import flash, render_template, redirect
from app import app

@app.route('/')
def raiz():
    return render_template('filmes.html')

if __name__ == '__main__':
    app.run(debug=True, port=3001)