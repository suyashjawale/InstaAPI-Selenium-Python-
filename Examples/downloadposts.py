from InstaAPI import InstaAPI


username=""            #Enter your instagram username
password=""            #Enter your instagram password
target_user=""         #Enter the username of the person who's posts you want to download
count=5                #Enter the number of posts you want to download.....to download all posts just do count="all"


api=InstaAPI(username,password)
api.login()
api.downloadposts(target_user,count)
api.logout()