from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exploits')
def exploits():
    return render_template('exploits.html')

@app.route('/Mitres')
def Mitres():
    return render_template('Mitres.html')

@app.route('/cheatsheets')
def cheatsheets():
    return render_template('cheatsheets.html')

@app.route('/wordlists')
def wordlists():
    return render_template('wordlists.html')

if __name__ == '__main__':
    app.run(debug=True, port=5007)