from rest_framework import serializers
from objectives.models import Objective, DOG

class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = '__all__'

class DOGSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOG
        fields= '_all__'

