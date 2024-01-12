from rest_framework import serializers
from . models import employee

class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=100)
    password=serializers.CharField(max_length=100)
    phone=serializers.CharField(max_length=10)

    # def create(self, validated_data):
    #     return employee.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.email = validated_data.get('email',instance.email)
    #     instance.password = validated_data.get('password',instance.password)
    #     instance.phone = validated_data.get('phone',instance.phone)
    #     instance.save()
    #     return instance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields='__all__'
    

