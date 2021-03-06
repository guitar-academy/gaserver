from application import db
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.orderinglist import ordering_list

# Declaring classes Song and Skill
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=True, index=True)
    description = db.Column(db.Text)
    notation = db.Column(db.Text)

    def __init__(self, title, description, notation):
        self.title = title
        self.description = description
        self.notation = notation

    def __repr__(self):
        return '<Song {0}: {1}>.format(self.id, self.title))'

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'notation': self.notation
        }
    #@serialize.setter
    #def serialize(self, value):
    #    self._serialize = value
    

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), unique=True, index=True)
    description = db.Column(db.Text)
    relevant_songs = association_proxy('skillpoints', 'song')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Skill {0}: {1}>'.format(self.id, self.name)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

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
        return '<Skillpoint for {0}: {1} of {2}'.format(self.song.title, self.value, self.skill.name)

# Declaring class WarmUp
class Warmup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), unique=True, index=True)
    description = db.Column(db.Text)
    entries = db.relationship('WarmupEntry', order_by='WarmupEntry.sort_order',
                              collection_class=ordering_list('sort_order'))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Warmup: {0}>'.format(self.name)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

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
    
    def __repr__(self):
        return '<WarmupEntry {0}: {1}>'.format(self.sort_order, self.song.title)

