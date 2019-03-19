from flask import Flask, request

app = Flask(__name__)       # Inicialización de la instancia de Flask

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    result = """
        <h1>Bienvenido</h1>
        <p>El navegador que estas usando es:</p>
        <p><strong>{}</strong></p>
    """.format(user_agent)

    return result


@app.route('/preader')
def paramsreader():
    param = request.args.get('name', 'Default name')
    if param == 'Default name':
        return "Ingrese el parametro \'name\' con su valor correspondiente"
    else:
        return f"Nombre: {param}"


@app.route('/user')
@app.route('/user/<name>')
def name(name=""):
    if name != "":
        return f"<h1>Hola {name}!</h1>"
    else:
        return "<h1>Hola usuario!</h1>"


if __name__=="__main__":
    app.run(debug=True)