def registration():
email=input()
password=input()
special_characters = "!@#$%^&*()-+?_=,<>/"
sp_x=int(email.index("@"))
email_flag=0
sp_y=int(email.index("."))
invalid_email=0
if int(sp_x) > int(sp_y):
    email_flag="Invalid"
elif email[0].isalnum() == False:
    email_flag = "Invalid"
else:
    for i in range(len(email)):
        if i==0 and email[i] == "@":
            email_flag="Invalid"

        elif email[i] == "@" and email[i + 1] == ".":
            email_flag="Invalid"

        else:
            email_flag="Valid"
password_flag=0

if int(len(password))<5 or int(len(password)>16):
    password_flag="Invalid"
else:
    password_flag="valid"

uppercount=0
lowercount=0
digitcount=0
spcount=0

for i in password:
    if i.isalnum()==True and i.isupper():
        uppercount+=1
    if i.isalnum()==True and i.islower():
        lowercount+=1
    if i.isnumeric()==True:
        digitcount+=1
    if i in special_characters:
        spcount+=1

if uppercount>=1 and lowercount>=1 and digitcount>=1 and spcount>=1:
     password_flag="Valid"
else:
    print("Password format is wrong")
if email_flag=="Valid" and password_flag=="Valid":
    with open("users.txt",'w',encoding='utf8') as f:
        f.write(email)
        f.write(" ")
        f.write(password)


