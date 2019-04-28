# Finance Tracker API
## Commands
### Start
```
sudo docker-compose up
```
### Migrate
```
sudo docker-compose run web python3 manage.py makemigrations
sudo docker-compose run web python3 manage.py migrate
```