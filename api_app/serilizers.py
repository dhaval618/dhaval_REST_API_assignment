from rest_framework.serializers import ModelSerializer
from .models import *

class SerializerMachine(ModelSerializer):
    class Meta:
        model = User
        # fields = ('first_name', 'email')
        fields = '__all__'
        # exclude = 
