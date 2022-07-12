from rest_framework import serializers
from core.models import comidagato, comidaperro, accesorio
 

class comidagatoSerializer(serializers.ModelSerializer):   
    class Meta:
        model = comidagato
        fields = '__all__'

class comidaperroSerializer(serializers.ModelSerializer):   
    class Meta:
        model = comidaperro
        fields = '__all__'

class accesorioSerializer(serializers.ModelSerializer):   
    class Meta:
        model = accesorio
        fields = '__all__'

