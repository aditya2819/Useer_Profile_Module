from models import Degree, Specialization, Skill, Country, State, City, User, Company
from flask import jsonify, render_template
import random

def get_degree_id(deg):
    degree_name = deg
    de = Degree.query.filter_by(name=degree_name).first()

    if de:
        return de.degree_id
    else:
        return jsonify({'error': 'Degree not found'}), 404

def get_specialization_id(spec):
    spec_name = spec
    spe = Specialization.query.filter_by(name=spec_name).first()

    if spe:
        return spe.specialization_id
    else:
        return jsonify({'error': 'Specialization_Id not found'}), 404

def get_skill_id(skill):
    skill_name = skill
    ski = Skill.query.filter_by(name=skill_name).first()

    if ski:
        return ski.skill_id
    else:
        return jsonify({'error': 'Skill_Id not found'}), 404

def get_city_id(city):
    city_name = city
    cit = City.query.filter_by(name = city_name).first()

    if cit:
        return cit.city_id
    else:
        return jsonify({'error': 'City_Id not found'}), 404

def get_state_id(state):
    state_name = state
    sta = State.query.filter_by(name = state_name).first()
    
    if sta:
        return sta.state_id
    else:
        return jsonify({'error': 'State_Id not found'}), 404

def get_country_id(country):
    country_name = country
    cou = Country.query.filter_by(name = country_name).first()

    if cou:
        return cou.country_id
    else:
        return jsonify({'error': 'State_Id not found'}), 404
