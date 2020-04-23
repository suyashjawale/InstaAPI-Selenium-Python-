from InstaAPI import InstaAPI

username=""            #Enter your instagram username
password=""           #Enter your instagram password

api=InstaAPI(username,password)
api.login()
records=api.getunfollowers(username)
j=1
for i in records:
    print(f"{j} \tAccount Link : {i}")
    j+=1

for i in records:
    api.unfollow(i.replace("https://www.instagram.com/","").replace("/",""))
api.logout()
