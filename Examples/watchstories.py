from InstaAPI import InstaAPI

username=""            #Enter your instagram username
password=""            #Enter your instagram password
count_time=30          #Time for which you want to watch the posts..Time must be in seconds


api=InstaAPI(username,password)
api.login()
api.watch_all_stories(count_time)
api.logout()