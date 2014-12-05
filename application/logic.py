from flask import jsonify

from application import db
from application.models.core import Song, Skill, Skillpoint
from application.models.core import Warmup, WarmupEntry

def add_to_db(obj):
    db.session.add(obj)
    db.session.commit()

def get_all_songs():
    songs = Song.query.all()
    return jsonify(songs=[s.serialize for s in songs])

def save_song(dict):
    title = dict['title']
    description = dict['description']
    notation = dict['notation']
    s = Song(title, description, notation)
    add_to_db(s)

def get_all_skills():
    skills = Skill.query.all()
    return jsonify(skills=[s.serialize for s in skills])

def save_skill(dict):
    name = dict['name']
    desc = dict['description']
    s = Skill(name, desc)
    add_to_db(s)

def get_all_warmups():
    warmups = Warmup.query.all()
    return jsonify(warmups=[w.serialize for w in warmups])

def save_warmup(dict):
    name = dict['name']
    desc = dict['description']
    w = Warmup(name, desc)
    add_to_db(w)
    