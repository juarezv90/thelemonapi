# Little Lemon API

>Make sure to make changes to settings file to allow it access to local database>

```
 DATABASES = {  
    'default': { 
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'restaurant',
        'USER': 'PUT YOUR USER',
        'PASSWORD': 'YOUR USER PASSWORD',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
} 
```

*Put your user id in*

*Put your user password*

*Make sure "resturant" database exist*


|Item|URL|function|
|-------|--------|-------|
|Restaurant Main Page|[/restaurant/](http://127.0.0.1:8000/restaurant/)| main index of site for littlelemon
|Booking Page|[/restaurant/book/](http://127.0.0.1:8000/restaurant/book/)| booking page of the site
|About Page| [/restaurant/about/](http://127.0.0.1:8000/restaurant/about/)|about page of the site
|View Reservations| [/restaurant/reservations/](http://127.0.0.1:8000/restaurant/reservations/)| loads all reservations in database and sorts in order from earliest date to last
|Bookings Django API| [/restaurant/booking/](http://127.0.0.1:8000/restaurant/booking/)| Allow direct access to reservations, requires admin priviliges [^1]
|Admin Django API|[/admin/](http://127.0.0.1:8000/admin)|Access to back end built in API management of database and priviliges[^1]
|Menu Item Backend API|[/restuarant/menu_add/](http://127.0.0.1:8000/restaurant/menu_add)| backend access to Django API for adding item to menu[^1]


[^1] must create super user or have user already assign privilege to view.