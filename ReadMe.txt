User Guide
1)Create Virtualenv : virtualenv env
2)Activate virtualenv : env\scripts\activate
3) Install requirements : pip install -r requirements.txt
4) Navigate to manage.py file
5)Make migrations : python manage.py migrate
6)Create superuser : python manage.py createsuperuser
7)Run project : python manage.py runserver
------------------------------------------------------------------------
------------------------------------------------------------------------
API Guide
Now after running server hit : http://127.0.0.1:8000
this will open all the available api links for each Tabel
where we can perform CRUD operations 

we have following Tabels 
i) Magazine
ii) Author
ii) Article

Relationships as fallows
Author -->Article { One to Many}
Article -->Magazine {Many to Many}
----------------------------------------------------------------------
----------------------------------------------------------------------
Endpoints 

##GET

To GET all Articles 
>>http://127.0.0.1:8000/articles

To GET all Authors
>>http://127.0.0.1:8000/Authors

To GET all Magazines
>>http://127.0.0.1:8000/Magazine
---------------------------------------------------------------------
##Retrieve

All articles related to the Author with<pk>
>> http://127.0.0.1:8000/authors/<pk>/articles

All articles related to the Magazine with <pk>
>>http://127.0.0.1:8000/magazines/<pk>/articles
---------------------------------------------------------------------
---------------------------------------------------------------------




