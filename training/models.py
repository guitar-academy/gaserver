from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    notation = models.TextField()
    skills = models.ManyToManyField('Skill', through='SongSkill', blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SongSkill(models.Model):
    song = models.ForeignKey('Song')
    skill = models.ForeignKey('Skill')
    value = models.IntegerField()

    class Meta:
        unique_together = ('song', 'skill')

    def __str__(self):
        return "{} ({}: {})".format(self.song, self.skill, self.value)


class WarmUp(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
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

