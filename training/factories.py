import factory
from factory.django import DjangoModelFactory
from . import models


class SongFactory(DjangoModelFactory):
    class Meta:
        model = models.Song
    title = factory.Sequence(lambda n: 'Song {0}'.format(n))
    description = factory.LazyAttribute(
            lambda obj: 'Description for {0}'.format(obj.title))


class SkillFactory(DjangoModelFactory):
    class Meta:
        model = models.Skill

    name = factory.Sequence(lambda n: 'Skill {0}'.format(n))
    description = factory.LazyAttribute(
            lambda obj: 'Description for {0}'.format(obj.name))


class WarmUpFactory(DjangoModelFactory):
    class Meta:
        model = models.WarmUp

    name = factory.Sequence(lambda n: 'Warm Up {0}'.format(n))
    description = factory.LazyAttribute(
            lambda obj: 'Description for {0}'.format(obj.name))


class SongSkillFactory(DjangoModelFactory):
    class Meta:
        model = models.SongSkill

    song = factory.SubFactory(SongFactory)
    skill = factory.SubFactory(SkillFactory)
    value = 10


class WarmUpSongFactory(DjangoModelFactory):
    class Meta:
        model = models.WarmUpSong

    warm_up = factory.SubFactory(WarmUpFactory)
    song = factory.SubFactory(SongFactory) 
    order = factory.Sequence(lambda n: n)


class SongWith2SkillsFactory(SongFactory):
    songskill1 = factory.RelatedFactory(SongSkillFactory, 'song')
    songskill2 = factory.RelatedFactory(SongSkillFactory, 'song')


class WarmUpWith2SongsFactory(WarmUpFactory):
    warmupsong1 = factory.RelatedFactory(WarmUpSongFactory, 'warm_up')
    warmupsong2 = factory.RelatedFactory(WarmUpSongFactory, 'warm_up')

