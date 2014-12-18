from django.contrib import admin

from .models import Song, Skill, WarmUp, SongSkill, WarmUpSong

admin.site.register(Song)
admin.site.register(Skill)
admin.site.register(WarmUp)
admin.site.register(SongSkill)
admin.site.register(WarmUpSong)
