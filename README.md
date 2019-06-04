# Finance Tracker API
## Commands
### Start
```
sudo docker-compose up
```
### User
```
sudo docker-compose run web python3 manage.py createsuperuser 
```
### Migrate
```
sudo docker-compose run web python3 manage.py makemigrations quickstart
sudo docker-compose run web python3 manage.py migrate
```
### Shell
```
sudo docker container list
sudo docker exec -it HASH bash
```