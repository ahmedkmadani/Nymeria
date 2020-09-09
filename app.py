from flask import Flask, render_template


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/lava')
def lava():
    return render_template('lava.html')

@app.route('/gester')
def gester():
    return render_template('gester.html')

@app.route('/alnfaj')
def alnfaj():
    return render_template('alnfaj.html')

@app.route('/medzone')
def medzone():
    return render_template('medzone.html')

if __name__ == '__main__':
    app.run(debug=True)