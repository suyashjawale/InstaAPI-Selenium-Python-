from InstaAPI import InstaAPI


username=""            #Enter your instagram username
password=""            #Enter your instagram password
target_user=""         #Enter the tagname you want to like
count=3                #Enter the number of posts you want to like.....to like all posts just do count="all"
action_type=""         #The types are - static and dynamic(static will count the posts serially and dynamic will count the posts which are getting liked.)

api=InstaAPI(username,password)
api.login()
api.liketags(target_user,count,action_type)
api.logout()