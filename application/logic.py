from flask import jsonify

from application import db
from application.models.core import Song, Skill, Skillpoint
from application.models.core import Warmup, WarmupEntry

def get_all_songs():
    songs = Song.query.all()
    return jsonify(songs=[s.serialize for s in songs])
