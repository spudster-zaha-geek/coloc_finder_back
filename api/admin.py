from django.contrib import admin

from api.models import Annonce, AnnonceImage, ConditionColocation

admin.site.register(Annonce)
admin.site.register(ConditionColocation)
admin.site.register(AnnonceImage)
