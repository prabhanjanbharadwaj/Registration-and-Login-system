def login()
email=input()
password=input()
f=open("../users.txt", "r")
if email in f.read():
    return ("Email exists, proceed to login")
else:
    return ("Proceed to register")

