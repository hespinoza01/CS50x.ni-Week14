from flask import Flask, render_template
from comment import Comment


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/array')
def array():
    lista = ['Hola', 'desde', 'una', 'lista', 'de', 'python']
    return render_template('array.html', lista=lista)


@app.route('/ifelse')
@app.route('/ifelse/<age>')
def ifelse(age=0):
    _age = int(age)
    number = type(_age) is int
    return render_template('ifelse.html', age=_age, number=number)


@app.route('/usemacros')
def usemacros():
    return render_template('usemacros.html', comments=comments_list())


# Funciones utilitarias

def comments_list():
    return [
        Comment('Harold', 'Hola, soy el primer comentario.'),
        Comment('Benito', 'Hola, soy el segundo comentario'),
        Comment('Espinoza', 'Hola, soy el tercer comentario'),
        Comment('Trujillo', 'Hola, soy el cuarto comentario')
    ]


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000
    )