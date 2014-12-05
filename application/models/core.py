from application import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.orderinglist import ordering_list

# Declaring classes Song and Skill
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=True)
    description = db.Column(db.String(1000))
    notation = db.Column(db.String(1000))

    def __init__(self, title, description, notation):
        self.title = title
        self.description = description
        self.notation = notation

    def __repr__(self):
        return '<Song %r: %r>' % (self.id, self.title)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), unique=True)
    description = db.Column(db.String(1000))
    relevant_songs = association_proxy('skillpoints', 'song')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Skill %r: %r>' % (id, name)

# Association class between song and skill
class Skillpoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    value = db.Column(db.Integer)
    song = db.relationship('Song', backref='skillpoints')
    skill = db.relationship('Skill', backref='skillpoints')

    def __init__(self, song_id, skill_id, value):
        self.song_id = song_id
        self.skill_id = skill_id
        self.value = value

    def __repr__(self):
        return '<Skillpoint for %r: %r of %r>' % (self.song.title, self.value, self.skill.name)

# Declaring class WarmUp
class Warmup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), unique=True)
    description = db.Column(db.String(1000))
    entries = db.relationship('WarmupEntry', order_by='WarmupEntry.sort_order',
                              collection_class=ordering_list('sort_order'))

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Association class between song and warmup
# add new entry: Warmup.entries.insert(pos, WarmupEntry(song_id))
class WarmupEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'))
    warmup_id = db.Column(db.Integer, db.ForeignKey('warmup.id'))
    sort_order = db.Column(db.Integer)
    song = db.relationship('Song')

    def __init__(self, song_id):
        self.song_id = song_id
    
