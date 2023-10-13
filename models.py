from flask_sqlalchemy import SQLAlchemy
from db import db

db = SQLAlchemy()

class City(db.Model):
    __tablename__ = 'city'

    city_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    state_id = db.Column(db.Integer, nullable=False)
    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id


class Country(db.Model):
    __tablename__ = 'country'

    country_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    def __init__(self, name):
        self.name = name

class Degree(db.Model):
    __tablename__ = 'degree'

    degree_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    level = db.Column(db.String(20), nullable=False)

    def __init__(self, name, level):
        self.name = name
        self.level = level

class Education(db.Model):
    __tablename__ = 'education'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True, nullable=False)
    degree_id = db.Column(db.Integer, db.ForeignKey('degree.degree_id'), primary_key=True, nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    year_of_passing = db.Column(db.Integer, nullable=False)
    Institution_name = db.Column(db.String(200), nullable=False)

    def __init__(self, user_id, degree_id, percentage, year_of_passing, Institution_name):
        self.user_id = user_id
        self.degree_id = degree_id
        self.percentage = percentage
        self.year_of_passing = year_of_passing
        self.Institution_name = Institution_name

class Skill(db.Model):
    __tablename__ = 'skills'

    skill_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

class Specialization(db.Model):
    __tablename__ = 'specialization'

    specialization_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

class State(db.Model):
    __tablename__ = 'state'

    state_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('country.country_id'), nullable=False)

    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(70), nullable=False)
    contact = db.Column(db.String(13))
    gender = db.Column(db.String(20), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    marital_status = db.Column(db.String(15))
    is_active = db.Column(db.String(3), nullable=False)
    country_id = db.Column(db.Integer, nullable=False)
    state_id = db.Column(db.Integer, nullable=False)
    city_id = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, name, contact, gender, birth_date, marital_status, is_active, country_id, state_id, city_id):
        self.user_id = user_id
        self.name = name
        self.contact = contact
        self.gender = gender
        self.birth_date = birth_date
        self.marital_status = marital_status
        self.is_active = is_active
        self.country_id = country_id
        self.state_id = state_id
        self.city_id = city_id

class UserSkills(db.Model):
    __tablename__ = 'user_skills'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True, nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.skill_id'), primary_key=True, nullable=False)
    description = db.Column(db.String(200))

    def __init__(self, user_id, skill_id, description=None):
        self.user_id = user_id
        self.skill_id = skill_id
        self.description = description

class UserSpecialization(db.Model):
    __tablename__ = 'user_specialization'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True, nullable=False)
    specialization_id = db.Column(db.Integer, db.ForeignKey('specialization.specialization_id'), primary_key=True, nullable=False)
    certification = db.Column(db.String(100))
    certification_issue_date = db.Column(db.Date)
    description = db.Column(db.String(200))

    def __init__(self, user_id, specialization_id, certification=None, certification_issue_date=None, description=None):
        self.user_id = user_id
        self.specialization_id = specialization_id
        self.certification = certification
        self.certification_issue_date = certification_issue_date
        self.description = description

class JobExperience(db.Model):
    __tablename__ = 'job_experience'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    post = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float)
    responsibility = db.Column(db.String(300))
    end_date = db.Column(db.Date)
    total_time = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, start_date, company_name, post, total_time, salary=None, responsibility=None, end_date=None):
        self.user_id = user_id
        self.start_date = start_date
        self.company_name = company_name
        self.post = post
        self.salary = salary
        self.responsibility = responsibility
        self.end_date = end_date
        self.total_time = total_time

class Company(db.Model):
    __tablename__ = 'companies'

    company_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    govern_issued_id = db.Column(db.String(30), nullable=False, unique=True)
    contact = db.Column(db.String(15), nullable=False)
    no_of_emp = db.Column(db.Integer)
    established_years = db.Column(db.Integer, nullable=False)
    about = db.Column(db.String(500), nullable=False)

    def __init__(self, company_id, name, address, govern_issued_id, contact, no_of_emp, established_years, about):
        self.company_id = company_id
        self.name = name
        self.address = address
        self.govern_issued_id = govern_issued_id
        self.contact = contact
        self.no_of_emp = no_of_emp
        self.established_years = established_years
        self.about = about
