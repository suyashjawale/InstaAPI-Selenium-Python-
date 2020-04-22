from InstaAPI import InstaAPI

username=""            #Enter your instagram username
password=""            #Enter your instagram password
target_user=""         #Enter the username to track

api=InstaAPI(username,password)
api.login()
api.savefollowerstofile(target_user)
api.logout()