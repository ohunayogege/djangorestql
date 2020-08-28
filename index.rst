![](https://res.cloudinary.com/practicaldev/image/fetch/s--xYea1j2Z--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/dmnrunxnjsudmpm1bby7.png)

**DjangorestQL** is a python library which allows you to turn your API made with **Django REST Framework(DRF)** into a GraphQL like API. 
With **DjangorestQL** you will be able to

* Send a query to your API and get exactly what you need, nothing more and nothing less.

* Control the data you get, not the server.

* Get predictable results, since you control what you get from the server.

* Get nested resources in a single request.

* Avoid Over-fetching and Under-fetching of data.

* Write(create & update) nested data of any level with flexibility.

_am sure you will enjoy it. Isn't it cool?_

Want to see how this library is making all that possible? 

Check out the full documentation at https://djangorestql.ohunayogege.com


## Requirements
* Python >= 3.5
* Django >= 1.11
* Django REST Framework >= 3.5


## Installing
```py
pip install djangorestql
```


## Getting Started
Using **DjangorestQL** to query data is very simple, you just have to inherit the ```DynamicFieldsMixin``` class when defining a serializer that's all.
```py
from rest_framework import serializers
from django.contrib.auth.models import User
from djangorestql.mixins import DynamicFieldsMixin


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
```

**Django RESTQL** handle all requests with a ```query``` parameter, this parameter is the one used to pass all fields to be included/excluded in a response. For example to select ```id``` and ```username``` fields from User model, send a request with a ``` query``` parameter as shown below.

```GET /users/?query={id, username}```
```js
[
    {
        "id": 1,
        "username": "ohunayo"
    },
    ...
]
```

**Django RESTQL** support querying both flat and nested resources, so you can expand or query nested fields at any level as defined on a serializer. In an example below we have ```location``` as a nested field on User model.

```py
from rest_framework import serializers
from django.contrib.auth.models import User
from django_restql.mixins import DynamicFieldsMixin

from app.models import GroupSerializer, LocationSerializer


class LocationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'country',  'city', 'street']


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    location = LocationSerializer(many=False, read_only=True) 
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'location']
```

If you want only ```country``` and ```city``` fields on a ```location``` field when retrieving users here is how you can do it

```GET /users/?query={id, username, location{country, city}}```
```js
[
    {
        "id": 1,
        "username": "ohunayo",
        "location": {
            "contry": "Nigeria",
            "city": "Lagos"
        }
    },
    ...
]
```

![](https://res.cloudinary.com/practicaldev/image/fetch/s--xYea1j2Z--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/dmnrunxnjsudmpm1bby7.png)

## [Documentation ![Documentation](https://img.shields.io/static/v1?label=&message=Visit%20Now&color=blue)](https://djangorestql.ohunayogege.com)
You can do a lot with **DjangorestQL** apart from just querying data, full documentation for this project is available at https://https://djangorestql.ohunayogege.com, you are encouraged to read it inorder to utilize this library to the fullest.


## Running Tests
```python runtests.py```


## Credits
> * [GraphQL](https://graphql.org/) Usage was an idea introduced to me by a friend of mine on JavaScript, so i decided to use it on Django.
> * My intention is to extend the capability of [drf-dynamic-fields](https://github.com/dbrgn/drf-dynamic-fields) library to support more functionalities like allowing to query nested fields both flat and iterable at any level and allow writing on nested fields while maintaining simplicity and to also relief developer stress.


## Contributing [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

> We welcome all contributions. Please read our [CONTRIBUTING.md](https://github.com/ohunayogege/djangorestql/blob/master/CONTRIBUTING.md) first. You can submit any ideas as [pull requests](https://github.com/ohunayogege/djangorestql/pulls) or as [GitHub issues](https://github.com/ohunayogege/djangorestql/issues). If you'd like to improve code, check out the [Code Style Guide](https://github.com/ohunayogege/djangorestql/blob/master/CONTRIBUTING.md#styleguides) and have a good time!.
![](https://res.cloudinary.com/practicaldev/image/fetch/s--xYea1j2Z--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/dmnrunxnjsudmpm1bby7.png)
