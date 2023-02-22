from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@views.route('/blog/')
def blog():
    return render_template('blog.html')


@views.route('/pentest/')
def pentest():
    return render_template('pentest.html')


@views.route('/whoami/')
def preojects():
    return render_template('whoami.html')


@views.route('/necmo/')
def necmo_bot():
    return render_template('necmo.html')


@views.route('/100322/')
def kalp():
    return render_template('100322.html')


@views.route('/blog/network-protocols')
def article_network_protocols():
    return render_template('network-p.html')


@views.route('/blog/network-technologies')
def article_network_technologies():
    return render_template('network-technologies.html')

@views.route('/blog/cs-aviation')
def article_cs_aviation():
    return render_template('cs-aviation.html')


@views.route('/blog/whiplash')
def whiplash():
    return render_template('whiplash.html')

if __name__ == '__main__':
    freezer.freeze()