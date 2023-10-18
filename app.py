from flask import Flask, request, jsonify, render_template, url_for, redirect
from db import db
from models import db, City, Country, Degree, Education, Skill, Specialization, State, User, UserSkills, UserSpecialization, JobExperience, Company
from functions import get_degree_id, get_specialization_id, get_skill_id, get_city_id, get_country_id, get_state_id

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:aditya@localhost:5432/job_portal"

db.init_app(app)

@app.route('/', methods=["GET", "POST"])
def checkuser():
    if request.method == "POST":
        usrtype = request.form.get("user_type")
        existuser = request.form.get("existing_user")
        existcompany = request.form.get("existing_company")
        if usrtype == "user":
            if existuser == "no":

                degrees = Degree.query.all()
                degree_names = [degree.name for degree in degrees]
                
                specializations = Specialization.query.all()
                specialization_names = [specialization.name for specialization in specializations]

                skills = Skill.query.all()
                skill_names = [skill.name for skill in skills]

                cities = City.query.all()
                city_names = [city.name for city in cities]

                states = State.query.all()
                state_names = [state.name for state in states]
                
                countries = Country.query.all()
                country_names = [country.name for country in countries]

                return render_template('user_profile.html', degree_names=degree_names, specialization_names=specialization_names, skill_names=skill_names, city_names=city_names, state_names=state_names, country_names=country_names)
            else:
                user_id = request.form.get("user_id")
                if user_id is not None:
                    user = User.query.filter_by(user_id=user_id).first()
                    usrid = user.user_id
                    if usrid:
                        return  redirect(url_for('view_user_profile',user_id=user_id))
                    else:
                        return jsonify({'error': 'User_Id not found'}), 404
                else:
                    return jsonify({'error': 'User_ID not provided'})
        else:
            if existcompany == "no":
                return render_template('company_profile.html')
            else:
                company_id = request.form.get("company_id")
                if company_id is not None:
                    company = Company.query.filter_by(company_id=company_id).first()
                    compid = company.company_id
                    if compid:
                        return  redirect(url_for('view_company_profile',company_id=company_id))
                    else:
                        return jsonify({'error': 'Company_Id not found'}), 404
                else:
                    return jsonify({'error': 'Company_ID not provided'})
    return render_template("usercomp.html")
    


@app.route('/user_profile', methods=["GET", "POST"])
def user_profile():
    if request.method == "POST":
        nm = request.form.get("name")
        con = request.form.get("contact")
        gen = request.form.get("gender")
        dob = request.form.get("dob")
        isact = request.form.get("isactive")
        marital_status = request.form.get("marital_status")
        country = request.form.get("country")
        state = request.form.get("state")
        city = request.form.get("city")
        degree = request.form.get("degree")
        perc = request.form.get("percentage")
        yearofpassing = request.form.get("yop")
        inst = request.form.get("instname")
        specialization = request.form.get("specialization")
        cert = request.form.get("certification")
        certid = request.form.get("cert_issue_date")
        descsp = request.form.get("descriptionsp")
        sk = request.form.get("skill")
        descsk = request.form.get("descriptionsk")
        std = request.form.get("start_date")
        cname = request.form.get("company_name")
        pst = request.form.get("post")
        sal = request.form.get("salary")
        resp = request.form.get("responsibility")
        endt = request.form.get("end_date")
        tt = request.form.get("total_time")

        usr_id = 200
        
        with db.session.begin():
            user = User(user_id=usr_id+1, name=nm, contact=con, gender=gen, birth_date=dob,
                        marital_status=marital_status, is_active=isact, country_id=get_country_id(country), state_id=get_state_id(state), city_id=get_city_id(city))
            edu = Education(user_id=usr_id+1, degree_id=get_degree_id(degree), percentage=perc, year_of_passing=yearofpassing, Institution_name=inst)
            userSpec = UserSpecialization(user_id=usr_id+1, specialization_id=get_specialization_id(specialization), certification=cert, certification_issue_date=certid, description=descsp)
            userSkill = UserSkills(user_id=usr_id+1, skill_id=get_skill_id(sk), description=descsk)
            job_experience = JobExperience(user_id=usr_id+1, start_date=std, company_name=cname, post=pst, salary=sal, responsibility=resp, end_date=endt, total_time=tt)
            db.session.add(user)
            db.session.commit()
        with db.session.begin():
            db.session.add(edu)
            db.session.add(userSpec)
            db.session.add(userSkill)
            db.session.add(job_experience)
            db.session.commit()
        return  redirect(url_for('view_user_profile',user_id=usr_id+1))
    return render_template('user_profile.html')

@app.route('/company_profile', methods = ["GET", "POST"])
def company_profile():
    if request.method == "POST":
        nm = request.form.get("name")
        addr = request.form.get("address")
        govid = request.form.get("govern_issued_id")
        con = request.form.get("contact")
        noemp = request.form.get("no_of_emp")
        est = request.form.get("established_years")
        abt = request.form.get("about")

        compid = 213

        company = Company(company_id=compid+1, name=nm, address=addr, govern_issued_id=govid, contact=con, no_of_emp=noemp, established_years=est, about=abt)
        with db.session.begin():
            db.session.add(company)
            db.session.commit()
        return  redirect(url_for('view_company_profile',company_id=compid+1))
    return render_template('company_profile.html')

# @app.route('/edit_user_profile', methods=["GET", "POST"])


@app.route('/delete_user_profile', methods = ["GET", "POST"])
def delete_user_profile():
    uid = request.form.get("delete_user_id")
    with db.session.begin():
        UserSkills.query.filter_by(user_id=uid).delete()
        UserSpecialization.query.filter_by(user_id=uid).delete()
        JobExperience.query.filter_by(user_id=uid).delete()
        usr = User.query.filter_by(user_id=uid).first()
        if usr:
            db.session.delete(usr)
            db.session.commit()
    return render_template("byebye.html")

# @app.route('/edit_company_profile', methods = ["GET", "POST"])
# def edit_company_profile():


@app.route('/delete_company_profile', methods = ["GET", "POST"])
def delete_company_profile():
    cid = request.form.get("delete_company_id")
    with db.session.begin():
        cmp = Company.query.filter_by(company_id=cid).first()
        if cmp:
            db.session.delete(cmp)
            db.session.commit()
    return render_template("byebye.html")

@app.route('/view_user_profile/<int:user_id>')
def view_user_profile(user_id):
    user = User.query.get(user_id)
    skills = UserSkills.query.filter_by(user_id=user_id).all()
    specializations = UserSpecialization.query.filter_by(user_id=user_id).all()
    experiences = JobExperience.query.filter_by(user_id=user_id).all()

    return render_template('view_user_profile.html', user=user, skills=skills, specializations=specializations, experiences=experiences)

@app.route('/view_company_profile/<int:company_id>')
def view_company_profile(company_id):
    company = Company.query.get(company_id)

    return render_template('view_company_profile.html', company=company) 

if __name__ == '__main__':
    app.debug = True
    app.run()
