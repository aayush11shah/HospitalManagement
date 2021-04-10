from flask import Flask, request, render_template
import os
from database_connection import *
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/patient_register', methods=['POST'])
def register_patient():
    form = request.form
    if request.method == 'POST':
        pid = disp("select count(*) from patient")[0][0]
        password = form['pass']
        p_name = form['fname'] + " " + form['lname']
        blood_grp = "bl"
        age = 40
        gender = "M"
        ph_no = "1234567890"
        address = "ge"
        aadhar_id = 1234
        p_history = "NULL"
        execute_query("insert into patient values(" + str(pid) + ", '" + password + "', '" + p_name + "', '" + blood_grp + "', " + str(age) + ", '" + gender + "', '" + ph_no + "', '" + address + "', " + str(aadhar_id) + ", '" + p_history + "')")
        return render_template("patient_login.html")
    
@app.route('/<page_type>', methods=['GET'])
def page(page_type):
    return render_template(page_type)
    
if __name__ == '__main__':
    init()
    app.run(debug=True)