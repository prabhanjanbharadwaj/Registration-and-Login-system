#def forgot_password():
email=input()
for line in open("../users.txt", "r").readlines():
    login_info=line.split()
    if email==login_info[0]:
        print(login_info[1])
    else:
        print("Wrong email")
