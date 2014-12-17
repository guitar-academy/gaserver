from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    notation = models.TextField()
    skills = models.ManyToManyField('Skill', through='SongSkill')

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class SongSkill(models.Model):
    song = models.ForeignKey('Song')
    skill = models.ForeignKey('Skill')
    value = models.IntegerField()

    def __str__(self):
        return "{} ({}: {})".format(song, skill, value)


class WarmUp(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    entries = models.ManyToManyField('Song', through='WarmUpSong')

    def __str__(self):
        return self.name

class WarmUpSong(models.Model):
    warm_up = models.ForeignKey('WarmUp')
    song = models.ForeignKey('Song')
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return "{}. {} - {}".format(self.order, self.warm_up, self.song)

