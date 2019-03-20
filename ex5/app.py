from flask import Flask, render_template as render, redirect, url_for, session, request, Markup


app = Flask(__name__)
app.config['SECRET_KEY'] = "AjJKIDSkcnskNVKDL3K"


@app.route('/')
def index():
    return render('index.html')


@app.route('/session', methods=['GET', 'POST'])
def withsession():
    if request.method == 'POST':
        session['name'] = request.form["name"]
        redirect(url_for('withsession'))

    return render('session.html', name=session.get('name'))


@app.route('/withoutsession', methods=['GET', 'POST'])
def withoutsession():
    if request.method == 'POST':
        redirect(url_for('withoutsession'))

    return render('session.html', name=session.get('name'))


@app.route('/clean')
def salir():
    if 'name' in session:
        session.pop('name')
        return redirect('/')
    else:
        return Markup("""
            <h1>Imposible eliminar session, no existe.</h1>
            <a href="/">Inicio</a>
            """)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000
    )