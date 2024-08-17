from rest_framework import serializers
from crm.models import Lead, Origem

class OrigemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origem
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class LeadPostSerializer(serializers.Serializer):
    origem = serializers.CharField()
    leads = serializers.ListField(child=serializers.CharField())
