from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'build'
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/whoami/')
def whoami():
    return render_template('whoami.html')

@app.route('/projects/')
def pentest():
    return render_template('projects.html')

@app.route('/multitool/')
def multitool():
    return render_template('multitool.html')

@app.route('/chatify/')
def chatify():
    return render_template('chatify.html')

@app.route('/necmo/')
def necmo_bot():
    return render_template('necmo.html')

@app.route('/network-protocols/')
def article_network_protocols():
    return render_template('network-p.html')

@app.route('/network-technologies/')
def article_network_technologies():
    return render_template('network-technologies.html')

@app.route('/cs-aviation/')
def article_cs_aviation():
    return render_template('cs-aviation.html')

@app.route('/whiplash/')
def whiplash():
    return render_template('whiplash.html')

@app.route('/chatGateway/')
def chatGateway():
    return render_template('chatGateway.html')

if __name__ == '__main__':
    freezer.freeze()