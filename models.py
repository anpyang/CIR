#-*- coding:utf-8 -*-
from django.db import models

class CIRUser(models.model):
    class Meta:
        permission = (
            ('creat','task creater'),
            ('edit','epg editor'),
            ('audit','epg auditor'),
        )