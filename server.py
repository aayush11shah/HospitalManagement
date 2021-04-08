import flask
import os
app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return flask.render_template("home.html")
    
@app.route('/<user_type>/<page_type>')
def page(user_type, page_type):
    return flask.render_template(page_type)
    
if __name__ == '__main__':
    app.run()