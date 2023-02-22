from flask import Flask, render_template
from flask_frozen import Freezer
from flask import Flask, render_template
from flask import Blueprint

from views import views

app = Flask(__name__)
app.register_blueprint(views)

freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    freeze()

