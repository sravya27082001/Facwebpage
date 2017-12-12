# -*- coding: utf-8 -*-
from django.contrib import admin

from fac.models import Faculty,Qualification,Projects,Teaching,Experience,Question

admin.site.register(Faculty)

admin.site.register(Qualification)
admin.site.register(Projects)
admin.site.register(Teaching)

admin.site.register(Experience)
admin.site.register(Question)