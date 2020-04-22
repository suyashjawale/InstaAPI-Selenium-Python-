from InstaAPI import InstaAPI

username=""         #Enter your instagram username
password=""         #Enter your instagram password
message=""          #Message you want to send
target_user=""      #Enter the username to whom you want to send message

api=InstaAPI(username,password)
api.login()
api.sendmessage(message,target_user)
api.logout()