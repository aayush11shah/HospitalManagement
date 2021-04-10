from flask import Flask, request, render_template
import os
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/patient_register', methods=['POST'])
def register_patient():
    form = request.form
    if request.method == 'POST':
        print(form)
        return render_template("patient_login.html")
    
@app.route('/<page_type>', methods=['GET'])
def page(page_type):
    return render_template(page_type)
    
if __name__ == '__main__':
    app.run()