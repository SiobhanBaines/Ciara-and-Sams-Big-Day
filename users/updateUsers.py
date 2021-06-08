# from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, PBKDF2PasswordHasher
# from django.conf import settings
import uuid
import json


jsonFile = open(
    "/workspace/Ciara-and-Sams-Big-Day/users/fixtures/users.json", "r")
users = json.load(jsonFile)
for user in users:
    if not (user["fields"]["is_staff"]):
        print(user["fields"]["username"])
        user["fields"]["username"] = uuid.uuid4().hex[:6].upper()
        print(user["fields"]["username"])
        print(user)
    # u = user.objects.get(username = user["fields"]["username"])
    # u = user["fields"]["username"]
    # user["fields"]["username"].set_password(user["fields"]["password"])
    # # u.set_password(user["fields"]["password"])
    # print(user["fields"]["password"])

    # pwd = user["fields"]["password"]
    # print(pwd)
    # p_word = make_password(pwd)
    # print(p_word)

jsonFile.close()
# print(users)

# jsonFile = open(
#     "/workspace/Ciara-and-Sams-Big-Day/users/fixtures/users.json", "w+")
# jsonFile.write(json.dumps(users))
# jsonFile.close()
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher'
)
