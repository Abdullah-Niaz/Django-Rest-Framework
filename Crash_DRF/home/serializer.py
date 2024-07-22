from rest_framework import serializers
from .models import Todo

class TodoSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['title','description','is_done','uid']
        

        def validate(self,validated_data):
            print(validated_data)
            if(validated_data.get('todo_title')):
                print("valid")

                todo_title = validated_data['todo_title']
                