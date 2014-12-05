import os
import unittest

from config import basedir
from application import app, db
from application.models.core import Song, Skill, Warmup, WarmupEntry, Skillpoint

class DatabaseTest(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' #+ os.path.join(basedir, 'gaserver_testing.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_song(self):
        s = Song('Recuerdos de la Alhambra',
                 'The beauty of alhambra expressed in tremolo',
                 'E E E E E E')
        db.session.add(s)
        db.session.commit()
        assert Song.query.get(1) == s

    def test_add_skillpoints(self):
        song = Song('a', 'b', 'c')
        skill = Skill('name', 'desc')
        skillpoint = Skillpoint(1, 1, 500)
        db.session.add(song)
        db.session.add(skill)
        db.session.add(skillpoint)
        db.session.commit()
        assert skill.relevant_songs[0] == song
        assert song.skillpoints[0] == skillpoint

    def test_add_warmup(self):
        s1 = Song('a', 'b', 'c')
        s2 = Song('d', 'e', 'f')
        warmup = Warmup('name', 'desc')
        db.session.add(s1)
        db.session.add(s2)
        db.session.add(warmup)
        db.session.commit()
        warmup.entries.append(WarmupEntry(1))
        warmup.entries.insert(0, WarmupEntry(2))
        db.session.commit()
        assert warmup.entries[0].song == s2
        assert warmup.entries[1].song == s1

if __name__ == '__main__':
    unittest.main()
