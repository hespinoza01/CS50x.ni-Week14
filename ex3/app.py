from flask import Flask, render_template, request, Markup


app = Flask(__name__)

app.config['SECRET_KEY'] = "SoyUnaLLaveSecreta"


@app.route('/', methods=['GET', 'POST'])
def index_get():
    content = None

    if request.method == 'POST':
        name = request.form["name"]
        content = Markup(f"""
            <h1>Hola {name}, hemos recibido tus datos satisfactoriamente.</h1>
            <br>
            <a href="/">Regresar</a>
        """)

    return render_template('index.html', content=content)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000
    )