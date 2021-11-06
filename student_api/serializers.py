from rest_framework import serializers
from .models import Student

# class StudentSerializerWithSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'first_name', 'last_name', 'number']
    # fields = '__all__'
    # excude = ['number']