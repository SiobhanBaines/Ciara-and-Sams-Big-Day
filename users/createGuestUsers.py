from django.contrib.auth.models import User
from django.conf import settings

import os
import uuid
import json

settings.configure()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ciara_and_sams_big_day.settings")

jsonFile = open(
    "/workspace/Ciara-and-Sams-Big-Day/users/fixtures/guest-users.json", "r")
users = json.load(jsonFile)

for user in users:
    if user["password"]:
        print(user["password"])
        unique_code = uuid.uuid4().hex[:6].upper()
        print(unique_code)
        User.objects.create_user(
            username=unique_code, password=user["password"])

jsonFile.close()
