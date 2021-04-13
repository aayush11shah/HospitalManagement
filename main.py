from flask import Flask, request, render_template, json
import os
from database_connection import *
app = Flask(__name__)
login = {}

@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/patient_register', methods=['POST'])
def register_patient():
    form = request.form
    if request.method == 'POST':
        pid = disp("select count(*) from patient")[0][0]
        password = form['pass']
        p_name = form['fname'] + form['lname']
        blood_grp = form['blood_grp']
        age = form['age']
        gender = form['gender']
        ph_no = form['ph_no']
        address = form['address']
        aadhar_id = form['adhar_id']
        p_history = "NULL"
        execute_query("insert into patient values(" + str(pid) + ", '" + password + "', '" + p_name + "', '" + blood_grp + "', " + str(age) + ", '" + gender + "', '" + ph_no + "', '" + address + "', " + str(aadhar_id) + ", '" + p_history + "')")
        return render_template("patient_login.html")

@app.route('/doctor_login', methods=['POST'])
def login_doctor():
    form = request.form
    if request.method == 'POST':
        doctor = disp("select * from doctor where doc_id=" + form['userid'] + " AND password='" + form['password'] + "';")
        if(len(doctor)):
            login[request.remote_addr] = 'd' + str(doctor[0][0])
            return render_template("doctor_home.html")
        return "Wrong password or username"
        
@app.route('/admin_login', methods=['POST'])
def login_admin():
    form = request.form
    if request.method == 'POST':
        admin = form['userid']
        passworda = form['passwd']
        if(len(admin)):
            login[request.remote_addr] = 'a'
            return render_template("admin_home.html")
        return "Wrong password or username"
        
@app.route('/patient_login', methods=['POST'])
def login_patient():
    form = request.form
    if request.method == 'POST':
        patient = disp("select * from patient where p_id=" + form['userid'] + " AND password='" + form['password'] + "';")
        if(len(patient)):
            login[request.remote_addr] = 'p' + str(patient[0][0])
            return render_template("patient_home.html", p_name=str(patient[0][2]))
        return "Wrong password or username"

@app.route('/<page_type>', methods=['GET'])
def page(page_type):
    if(page_type == "patient_register.html"):
        userid = str(disp("select count(*) from patient")[0][0])
        return render_template(page_type, value=userid)
    elif(login[request.remote_addr] == 'a'):
        if(page_type == 'admin_manage_doctor.html'):
            return render_template(page_type, doctor_table=json.jsonify(disp("select doc_id, first_name, last_name, aadhar_id, chamber, salary, dept_id, timeslot from doctor")))
        elif(page_type == 'admin_manage_patient.html'):
            return render_template(page_type, patient=json.jsonify(disp("select p_id, p_name, blood_grp, age, gender, ph_no, address, aadhar_id, p_history from patient")))
        elif(page_type == 'admin_manage_pharmacy.html'):
            return render_template(page_type, pharmacy=json.jsonify(disp("select item_id, item_name, qty, price from expense")))
    elif(login[request.remote_addr][0] == 'p'):
        m_status = login[request.remote_addr]
        p_name = str(disp("select p_name from patient where p_id = " + m_status[1:]))
        if(page_type == 'patient_book_appointment.html'):
            return render_template(page_type, p_name=p_name)
        elif(page_type == 'patient_book_room.html'):
            return render_template(page_type, p_name=p_name)
        elif(page_type == 'patient_home.html'):
            return render_template(page_type, p_name=p_name)
        elif(page_type == 'patient_shop.html'):
            return render_template(page_type, p_name=p_name)
        elif(page_type == 'patient_transaction_history.html'):
            return render_template(page_type, p_name=p_name)
    elif(login[request.remote_addr][0] == 'd'):
        m_status = login[request.remote_addr]
        d_name = str(disp("select first_name, last_name from patient where p_id = " + m_status[1:]))
        d_name = d_name[0] + " " + d_name[1]
        if(page_type == 'doctor_appointments.html'):
            return render_template(page_type, d_name=d_name)
        elif(page_type == 'doctor_home.html'):
            return render_template(page_type, d_name=d_name)
    else:
        return render_template(page_type)

    
if __name__ == '__main__':
    init()
    app.run(debug=True)