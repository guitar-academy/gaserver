from database import db

songskill_table = db.Table('SongSkill',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('song_id', db.Integer, db.ForeignKey('song.id')),
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id')),
    db.Column('value', db.Integer)
)

warmupsong_table = db.Table('WarmupSong',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('warmup_id', db.Integer, db.ForeignKey('warmup.id')),
    db.Column('song_id', db.Integer, db.ForeignKey('song.id')),
    db.Column('sort_order', db.Float)
)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), unique=True)
    description = db.Column(db.String(1000))
    notation = db.Column(db.String(1000))
    skills = db.relationship('Skill', secondary=songskill_table,
        backref=db.backref('songs', lazy='dynamic'))

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), unique=True)
    description = db.Column(db.String(1000))

class Warmup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), unique=True)
    description = db.Column(db.String(1000))
    songs = db.relationship('Song', secondary=warmupsong_table)

