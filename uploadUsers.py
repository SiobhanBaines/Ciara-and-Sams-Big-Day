# from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, PBKDF2PasswordHasher
# from django.conf import settings
import uuid
import json

# def setUserPassword(self):
#     self.User = get_user_model()
#     # Create UUID as username
#     for user in self.User.objects.all():
#         user.set_username(uuid.uuid4().hex[:6].upper())
#         user.set_password(user.password)
#         user.save()


# def updateUsersFile():
jsonFile = open(
    "/workspace/Ciara-and-Sams-Big-Day/users/fixtures/users.json", "r")
users = json.load(jsonFile)
for user in users:
    print(user["fields"]["username"])
    user["fields"]["username"] = uuid.uuid4().hex[:6].upper()
    print(user["fields"]["username"])
    print(user)
    pwd = user["fields"]["password"]
    print(pwd)
    p_word = make_password(pwd)
    print(p_word)
    # # user["fields"]["password"] = make_password(pwd)
    # print(p_word)
    # print(user["fields"])
    # print(user)
    # print(user["password"])

jsonFile.close()
# print(users)

# jsonFile = open(
#     "/workspace/Ciara-and-Sams-Big-Day/users/fixtures/users.json", "w+")
# jsonFile.write(json.dumps(users))
# jsonFile.close()
