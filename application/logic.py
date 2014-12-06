from flask import jsonify

from application import db
from application.models.core import Song, Skill, Skillpoint
from application.models.core import Warmup, WarmupEntry

def add_to_db(obj):
    db.session.add(obj)
    db.session.commit()

def delete_from_db(obj):
    db.session.delete(obj)
    db.session.commit()

# Songs
def get_all_songs():
    songs = Song.query.all()
    return jsonify(songs=[s.serialize for s in songs])

def get_song_by_title(title):
    s = Song.query.filter_by(title=title).first()
    return jsonify(song=s.serialize)

def create_song(obj):
    title = obj['title']
    description = obj['description']
    notation = obj['notation']
    s = Song(title, description, notation)
    add_to_db(s)

def update_song(obj):
    title = obj['title']
    s = Song.query.filter_by(title=title).first()
    s.description = obj['description']
    s.notation = obj['notation']
    db.session.commit()

def delete_song(title):
    song = Song.query.filter_by(title=title).first()
    delete_from_db(song)

# Skills
def get_all_skills():
    skills = Skill.query.all()
    return jsonify(skills=[s.serialize for s in skills])

def get_skill_by_name(name):
    skill = Skill.query.filter_by(name=name).first()
    return jsonify(skill=skill.serialize)

def create_skill(obj):
    name = obj['name']
    desc = obj['description']
    s = Skill(name, desc)
    add_to_db(s)

def update_skill(obj):
    name = obj['name']
    skill = Skill.query.filter_by(name=name).first()
    skill.description = obj['description']
    db.session.commit()

def delete_skill(name):
    skill = Skill.query.filter_by(name=name).first()
    delete_from_db(skill)

# Warmups
def get_all_warmups():
    warmups = Warmup.query.all()
    return jsonify(warmups=[w.serialize for w in warmups])

def get_warmup_by_name(name):
    warmup = Warmup.query.filter_by(name=name).first()
    return jsonify(warmup=warmup.serialize)

def create_warmup(obj):
    name = obj['name']
    desc = obj['description']
    w = Warmup(name, desc)
    add_to_db(w)

def update_warmup(obj):
    name = obj['name']
    warmup = Warmup.query.filter_by(name=name).first()
    warmup.description = obj['description']
    db.session.commit()

def delete_warmup(name):
    warmup = Warmup.query.filter_by(name=name).first()
    delete_from_db(warmup)

