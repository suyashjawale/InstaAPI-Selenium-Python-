from InstaAPI import InstaAPI

username=""            #Enter your instagram username
password=""            #Enter your instagram password
target_user=""         #Enter the username to whom you want to send message

api=InstaAPI(username,password)
api.login()
records=api.getuserfollowing(target_user)
j=1
for i in records:
    print(f"{j} \tAccount Link : {i}")
    j+=1
api.logout()