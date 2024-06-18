from rest_framework import serializers
from api.models import Annonce, ConditionColocation


class AnnonceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Annonce
        fields = ('id', 'title', 'description', 'price', 'location', 'conditions_colocations',)

class ConditionColocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ConditionColocation
        fields = ('id', 'condition')