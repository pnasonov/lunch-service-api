# lunch-service-api

API service for employers lunch management written in DRF

### Installing using GitHub

```shell
git clone https://github.com/pnasonov/lunch-service-api
cd lunch-service-api

docker-compose build
docker-compose up
```

### Getting access

Only staff user can create restaurants, menus, employees.
Common authenticated user can only visit pages.

To create staff user:
```shell
sudo docker exec -it <id_of_container> sh
python manage.py createsuperuser
```

Endpoints:
* /api/user/register/ - create common user via 
* /api/user/token/ - get access token via 
* /api/restaurants/ - create restaurant (only staff user) via 
* /api/menus/ - create menu (only staff user) via 
* /api/employees/ - create employee (only staff user) via 
* /api/restaurants/1/ get current day menu for restaurant (by id of restaurant)
* /api/voting/ - get result for current day for all restaurants 