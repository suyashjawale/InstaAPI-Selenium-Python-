from InstaAPI import InstaAPI

username=""           #Enter your instagram username
password=""           #Enter your instagram password
count=10              #Enter number of posts you want to like...to like all posts just do count="all"
method=""             #Types of liking are - static and dynamic (static means it can count posts that are already liked and dynamic means it will count posts that it liked)

api=InstaAPI(username,password)
api.login()
api.likemytimeline(count,method)
api.logout()