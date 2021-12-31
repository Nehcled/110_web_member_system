# 110_web_member_system

# Re Create Database
1. delete db.sqlite3 file
2. run python manage.py makemigrations
3. run python manage.py migrate
register super user again.(cause database was rebuilded)
4. run python manage.py createsuperuser
5. run python manage.py shell
6. copy and run the following command
 ```
from django.contrib.auth.models import User
from member.models import UserProfile
user = User.objects.all()[0]
profile = UserProfile(user=user)
profile.save()
```
7. finish

# Install
pip install django-filter

# Todo
1. profile card
2. 
