from InstaAPI import InstaAPI

username=""            #Enter your instagram username
password=""            #Enter your instagram password
target_user=""         #Enter the username to track 

api=InstaAPI(username,password)
api.login()
records=api.getunfollowers(target_user)
j=1
for i in records:
    print(f"{j} \tAccount Link : {i}")
    j+=1
api.logout()