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