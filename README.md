## What is API?
An API is a application programming interface that allows two are are more applications to talk to each other. 
### Example
- When you visit a resturant. 
- There is shiff/Waitor that serves the food. That is API.

### Types of API in terms of Release Policies:-
- **Private** : it can be used within the organization.
- **Public** : it can be used by anyone.
- **Partner**: it can be used within Business Partners.
    
## REST
It is an architectural guideline to develop WEB API.

## REST API
The API which developed using REST is know as REST API/RESTful API.

### CRUD Operation:

| Action  | Method     | Description                                  |
|---------|------------|----------------------------------------------|
| Create  | POST       | Creating/Posting/Inserting Data              |
| Read    | GET        | Reading/Getting/Retrieving Data              |
| Update  | PUT, PATCH | Updating Data - Complete Update PUT - Partial Update PATCH |
| Delete  | DELETE     | Deleting Data                                |


# Django-Rest-Framework
Django rest framework is powerfull web API toolkit for building WEB APIs.
- The WEB browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1 and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular fucntion based views if you don't need the more powerful features.
- Extensive documentation, great community support.
- Used and trusted by internationally recognized companies including Mozilla, Red Hat, Heroku, and Eventbrite.

## Requirements to Learn REST Framework:
- Python 
- Django
- The following Pacakges are optional:
- PyYAML, uritemplate Schema Generation support.
- Markdown, Support for the browsable API.
- Pygments - Add syntax highlighting to Markdown processing.
- Django-filter - Support for filtering through the browsable API.
- Django-gurdian - Object level permission support.

## How to install Django-Rest-Framework (DRF)
- Install Using pip
    ` pip install djangorestframework `
- In order to Uninstall:
    ` pip uninstall djangorestframework `
- Installing DRF to Django Project
    `INSTALLED_APPS = [
        'rest_framework',
    ]`


## Python JSON
Python has a builtin package called json, which is used to work with json data.
- json.dumps() - This function converts a python object into a json string.
Example:-
- To use the json data first we need to import

```Python 
import json 
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
}
json_data = json.dumps(data)
print(json_data)
```
- json.loads() - This function converts a json string into a python object.
Example:-
```Python 
import json 
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
}
json_data = json.load(data)
print(json_data)
```


# Serializers
- In Django REST Framework, serializer are responsible for converting comples data suchas querysets and model instances to native Python Datatypes ( called serialization) that can be easily rendered into JSON, XML or other content types which is understandable by Frontend.
- Serializer are also responsible for taking data from a "deserialized" format ( like JSON) and converting
it into a complex data structure ( like a model instance or query set) for use in our application
( called deserialization).

## Serializer Class
- A serializer class is very similar to a Django Form and ModelForm class, and includes similar validation glags on the various fields, such as required, max_length and default.
-  DRF Provides a serializer class which gives youa powerfull, generic way to control the output of your responses,as wel as ModelSerializer class which provides a usefull shortcut for creating serializers that deal with model instances and querysets.

## How to Create Serializer Class
- Create a new file called serializer.py in your app directory.
- Create a new class called UserSerializer which inherits from the serializer class.
- Add a Meta class to the serializer class which contains the following attributes.
- model - The model class that this serializer is responsible for serializing.
- fields - A list of fields that should be included in the serialized output.
- Create a new method called create() which will be called when a POST request is made to the
viewset.
- Create a new method called update() which will be called when a PUT request is made to the
viewset.

``` python 
# serializer.py
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
```

``` Python
# models.py
class student(models.Model):
    name = serializers.CharField(max_length=100)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
```

Complex Data type --------------> Python Native DataType -------------------> Json Data
                   Serialization                           Render it to json

## Serialization:
The process of converting comples data such as querysets and model instances to native python datatypes are called as Serialization in DRF.
- Creating Model instance student
    student = Student.objects.get(id=1)
- Creating model instance student to python Dict/Serializing Objects
    serializer = StudentSerializer(student)
- creating QuerySet
    students = Student.objects.all()
- Creating QuerySet to python Dict/Serializing QuerySet
    serializer = StudentSerializer(students, many=True)

- Serialized Data printer
    serialized.data

- JsonRender
    This is used to render serialized data into json which is understandable by frontend.
``` python
    importing JSONRenderer
    from rest_framework.renderers import JSONRenderer
    json_data = JSONRenderer().render(serializer.data)
```