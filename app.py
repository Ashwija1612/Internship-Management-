import connection
from flask import Flask, render_template, request

import mysql.connector

app = Flask(__name__)
try:
    connection = mysql.connector.connect(host='localhost', user='root', password='', database='internship_portal')
    cursor = connection.cursor()
    cursor.execute('USE internship_portal')
    print("Connected to database")
except:
    print("Error while connecting")


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/loginstudent')
def loginstudent():
    return render_template('loginstudent.html')


@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get("email")
    password = request.form.get("pass")

    try:
        query = "SELECT * FROM USERS WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))
        data = cursor.fetchall()
        role = data[0][1]
        print(role)

        if role == 1:
            return render_template('home.html')
        elif role == 2:
            return render_template('home1.html')
        else:
            print("Error")

    except:
        print("error")


@app.route('/main')
def main():
    query1 = f"SELECT DISTINCT D.name, C.profile,C.duration, S.skills, S.interest, C.id , D.id FROM COMPANY_DETAILS D INNER JOIN INTERNSHIP_DETAILS C ON C.id = D.id INNER JOIN STUDENT_DETAILS S ON S.interest=C.profile OR S.skills=C.profile "
    cursor.execute(query1)
    data = cursor.fetchall()
    print(f'Data to be printed is: {data}')
    return render_template('home11.html', data=data)

#@app.route('/page')
# def page():
#      queries = f"SELECT S.interest, S.skills, C.profile FROM STUDENT_DETAILS S INNER JOIN INTERNSHIP_DETAILS C ON S.interest=C.profile AND S.skills=C.profile"
#      cursor.execute(queries)
#      data = cursor.fetchall()
#      print(f'Data to be printed is: {data}')
#      return render_template('home11.html', data =data)


@app.route('/logincompany')
def logincompany():
    return render_template('logincompany.html')


@app.route('/submited', methods=['POST'])
def submited():
    email = request.form.get("mail")
    password = request.form.get("password")

    try:
        query = "SELECT * FROM USERS WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))
        data = cursor.fetchall()
        role = data[0][1]
        print(role)

        if role == 1:
            return render_template('home.html')
        elif role == 2:
            return render_template('home1.html')
        else:
            print("Error")

    except:
        print("error")


@app.route('/mainpage')
def mainpage():
    query = f"SELECT DISTINCT S.name, S.skills, S.interest, C.profile FROM STUDENT_DETAILS S INNER JOIN INTERNSHIP_DETAILS C ON S.interest=C.profile OR S.skills=C.profile"
    cursor.execute(query)
    data = cursor.fetchall()
    print(f'Data to be printed is: {data}')
    return render_template('home.html', data=data)


@app.route('/registration_form')
def registration_form():
    return render_template('registration_form.html')


@app.route('/studregister', methods=['POST'])
def studregister():
    email = request.form.get("email")
    password = request.form.get("password")

    # return render_template('student_detail.html')
    cursor.execute("INSERT INTO USERS (email,password) VALUES(%s,%s)", (email, password))
    connection.commit()
    return render_template('student_detail.html')


@app.route('/student_detail')
def student_detail():
    return render_template('student_detail.html')


@app.route('/studentregister', methods=['POST'])
def studentregister():
    firstname = request.form.get("firstname")
    gender = request.form.get("gender")
    college_name = request.form.get("company")
    course = request.form.get("course")
    dob = request.form.get("dob")
    phone = request.form.get("phone")
    interest = request.form.get("subject")
    skills = request.form.get("skills")
    experience = request.form.get("experience")
    # insertion query for student detail

    cursor.execute("INSERT INTO STUDENT_DETAILS(name, gender, dob, college_name, phoneNumber, courseName, interest,skills,experience) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(firstname, gender, dob, college_name, phone, course, interest, skills, experience))
    connection.commit()
    # return render_template('login.html')
    return render_template('loginstudent.html')


@app.route('/registration_form1')
def registration_form1():
    return render_template('registration_form1.html')


@app.route('/companyregister', methods=['POST'])
def companyregister():
    email = request.form.get("email")
    password = request.form.get("password")
    # query
    cursor.execute("INSERT INTO USERS(email,password) VALUES(%s,%s)", (email, password))
    connection.commit()
    return render_template('company_details.html')


@app.route('/company_details')
def company_details():
    return render_template('company_details.html')


@app.route('/register', methods=['POST'])
def register():
    first_name = request.form.get("first_name")
    manager_name = request.form.get("manager_name")
    manager = request.form.get("manager")
    phone = request.form.get("phone")
    description = request.form.get("description")
    profile = request.form.get("profile")
    duration = request.form.get("duration")
    stipend = request.form.get("stipend")
    last = request.form.get("last")
    # insertion query for student details
    cursor.execute(
        "INSERT INTO COMPANY_DETAILS(name,manager_name, manager_designation, manager_contact, description) VALUES(%s,%s,%s,%s,%s)",
        (first_name, manager_name,manager, phone, description))
    connection.commit()
    cursor.execute("INSERT INTO INTERNSHIP_DETAILS(profile,duration,isStipend,last_date) VALUES(%s,%s,%s,%s)",
                   (profile, duration, stipend, last))
    connection.commit()
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
