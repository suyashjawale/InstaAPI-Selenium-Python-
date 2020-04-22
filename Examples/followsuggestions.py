from InstaAPI import InstaAPI

username=""            #Enter your instagram username
password=""	           #Enter your instagram password

api=InstaAPI(username,password)
api.login()
api.followsuggestions()
api.logout()