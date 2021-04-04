import flask
import os
app = flask.Flask(__name__, template_folder='HTML')

@app.route('/')
def homepage():
    return flask.render_template("website_home.html")
    
@app.route('/<user_type>/<page_type>')
def page(user_type, page_type):
    return flask.render_template(user_type+"/"+user_type+"_"+page_type+".html")
    
if __name__ == '__main__':
    app.run()