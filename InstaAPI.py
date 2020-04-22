import urllib.request
from selenium import webdriver	 
import time

class InstaAPI:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username=username
        self.password=password

    def login(self):
        try: 
            self.browser.get('https://www.instagram.com/') 
            time.sleep(15)
            self.browser.find_element_by_name('username').send_keys(self.username)
            self.browser.find_element_by_name('password').send_keys(self.password)
            time.sleep(2)
            self.browser.find_element_by_xpath('//button[@type="submit"]').click()
            time.sleep(5)
            self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            time.sleep(2)
        except Exception as e:
            print("Login error : ",e)
            self.logout()

    def like(self,count,method):
        try:
            i=0
            while True:
                time.sleep(7)
                flag=self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
                res = flag.find_element_by_class_name("_8-yf5 ")
                if res.get_attribute("aria-label")=="Like":
                    flag.click()
                    if count!="all" and method=="dynamic":
                        i+=1
                    time.sleep(2)    
                if count!="all" and method=="static":
                    i+=1
                if i==count:
                    print("Completed the process of liking all the photos.")
                    break
                try:
                    self.browser.find_element_by_xpath('//a[@class=" _65Bje  coreSpriteRightPaginationArrow"]').click()
                except:
                    print("Completed the process of liking all the photos.")
                    break
        except Exception as e:
            print("OOPS,error occured while liking posts ! ! !")


    def popen(self,target):
        try:
            self.browser.get(f"https://www.instagram.com/{target}/")
            box=self.browser.find_element_by_class_name('ySN3v')
            links = box.find_elements_by_tag_name('a')
            names = [name.get_attribute("href") for name in links]
            string=names[0]
            string=string.replace("https://www.instagram.com","")
            self.browser.find_element_by_xpath("//a[contains(@href,'{}')]".format(string)).click()
        except Exception as e: 
            print("Open Exception: ",e)
            self.logout()


    def likeposts(self,target,count=2,method="static"):
        try:
            self.popen(target)
            self.like(count,method)
        except Exception as e: 
            print("Like Photos Exception: ",e)
            self.logout()

    def opentag(self,tagname):
        try:
            self.browser.get(f"https://www.instagram.com/explore/tags/{tagname}/")
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]').click()
        except Exception as e:
            print("Open Tag error : ",e)
            self.logout()

    def liketags(self,tagname,count=2,method="static"):
        try:
            self.opentag(tagname)
            self.like(count,method)    
        except Exception as e:
            print("Download Photos error : ",e)
            self.logout()

    def download(self,count):
        try:
            i=1
            j=1
            while True:
                time.sleep(10)
                links=[]                               
                vlinks=[]                              
                try:                                   
                    img=self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/img')
                    links.append(img.get_attribute("src"))
                except:
                    try:
                        img=self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/div[1]/img')
                        links.append(img.get_attribute("src"))
                    except:
                        try:                                     
                            video=self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/div/div/video')
                            vlinks.append(video.get_attribute("src"))
                        except:
                            try:
                                img=self.browser.find_elements_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div/div[1]/div[2]/div/div/div/ul/li')
                                for j in range(1,len(img)):
                                    try:
                                        newvideo=img[j].find_element_by_tag_name('video')
                                        vlinks.append(newvideo.get_attribute('src'))
                                    except:
                                        newimage=img[j].find_elements_by_tag_name('img')
                                        links.append(newimage[0].get_attribute("src"))
                            except:
                                print("")

                m=1
                for k in links:
                    if count!="all":
                        urllib.request.urlretrieve(k,f"img{i}-{m}.png")
                    else:
                        urllib.request.urlretrieve(k,f"img{j}-{m}.png")
                    m+=1
                m=1
                for k in vlinks:
                    if count!="all":
                        urllib.request.urlretrieve(k,f"img{i}-{m}.mp4")
                    else:
                        urllib.request.urlretrieve(k,f"img{j}-{m}.mp4")
                    m+=1
                if count!="all":
                    i+=1
                    if i>count:
                        print("Process of downloading posts has been completed.")
                        break
                else:
                    j+=1
                try:
                    self.browser.find_element_by_xpath('//a[@class=" _65Bje  coreSpriteRightPaginationArrow"]').click()
                except:
                    print("Downloaded all posts.")
                    break
        except Exception as e:
            print("Error occured while downloading")

    def downloadtags(self,target,count=2):
        try:
            self.opentag(target)
            self.download(count)    
        except Exception as e:
            print("Download tags error : ",e)
            self.logout()

    def downloadposts(self,target,count=2):
        try:
            self.popen(target)
            self.download(count) 
        except Exception as e: 
            print("Exception: ",e)


    def getnames(self):
        try:
            scroll_box = self.browser.find_element_by_xpath("/html/body/div[4]/div/div[2]")
            last_ht, ht = 0, 1
            while last_ht != ht:
                last_ht = ht
                time.sleep(1)
                ht = self.browser.execute_script("""
                    arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                    return arguments[0].scrollHeight;
                    """, scroll_box)
            l = scroll_box.find_elements_by_tag_name('a')
            names=[]
            for i in l:
                names.append(i.get_attribute('href'))
            names=list(set(names))
            self.browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
            return names
        except Exception as e:
            print("Error occured")


    def getuserfollowers(self,target_user):
        try:
            self.browser.get(f"https://www.instagram.com/{target_user}")
            try:
                ftext=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[1]/div/h2')
                print("Sorry the user is private")
                return
            except:
                followersLink=self.browser.find_element_by_css_selector('ul li a')
                followersLink.click()
                time.sleep(5)
                followers=self.getnames()
                return followers
        except Exception as e:
            print("Get followers error")


    def getuserfollowing(self,target_user):
        try:
            self.browser.get(f"https://www.instagram.com/{target_user}")            
            try:
                ftext=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[1]/div/h2')
                print("Sorry the user is private")
                return
            except:
                followingLink=self.browser.find_element_by_css_selector('ul li:nth-child(3) a')
                followingLink.click()
                time.sleep(5)
                following=self.getnames()
                return following
        except Exception as e:
            print("Get following error.")


    def sendmessage(self,msg,target_person):
        try:
            if len(msg.strip())>0 and len((target_person))>0:
                self.browser.get("https://www.instagram.com/direct/inbox/")
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[1]/div/div[2]/input').send_keys(target_person)
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/div/button').click()
                time.sleep(7)
                self.browser.find_element_by_xpath('//textarea[@placeholder="Message..."]').send_keys(msg)
                time.sleep(2)
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                time.sleep(10)
            else:
                print("Sorry..something went wrong.")
        except Exception as e:
            print("Send message error")

    def logout(self):
        try:
            self.browser.close()
            self.browser.quit()
        except:
            print("")

    def getunfollowers(self,target_user):
        try:
            try:
                ftext=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[1]/div/h2')
                print("Sorry the user is private")
                return
            except:
                followers=self.getuserfollowers(target_user)
                following=self.getuserfollowing(target_user)
                not_following_back = [user for user in following if user not in followers]
                return not_following_back
        except:
            print("error")

    def saveunfollowerstofile(self,target_user):
        lists=self.getunfollowers(target_user)
        myfile = open(f'Unfollowers - {target_user}.txt', 'w')
        for line in lists:
            myfile.write(line+"\n")
        myfile.close()


    def savefollowerstofile(self,target_user):
        lists=self.getuserfollowers(target_user)
        myfile = open(f'Followers - {target_user}.txt', 'w')
        for line in lists:
            myfile.write(line+"\n")
        myfile.close()

    def savefollowingtofile(self,target_user):
        lists=self.getuserfollowing(target_user)
        myfile = open(f'Following - {target_user}.txt', 'w')
        for line in lists:
            myfile.write(line+"\n")
        myfile.close()

    def unfollow(self,target_user):
        try:
            self.browser.get(f"https://www.instagram.com/{target_user}/")
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
            time.sleep(1)
            self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()  
            time.sleep(2)      
        except Exception as e:
            print("Error occured")


    def likemytimeline(self,count=8,ltype="static"):
        try:
            scroll_box = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[1]/div').click()
            cnt=0
            while 1:
                try:
                    tlist=self.browser.find_elements_by_xpath("//button[@class='wpO6b ']")
                    for i in tlist:
                        try:
                            res=i.find_element_by_tag_name('svg').get_attribute('aria-label')
                            if res=="Like":
                                i.click()
                                time.sleep(2)
                                if ltype=="dynamic":
                                    cnt+=1    
                            if ltype=="static" and (res=="Like" or res=="Unlike"):
                                cnt+=1
                            if count!="all":
                                if cnt>count:
                                    print("Process of liking timeline posts is completed.")
                                    return
                        except:
                            print("",end='')
                except:
                    print("not done")
                self.browser.execute_script("window.scrollTo(0, window.scrollY + 800)")
        except Exception as e:
            print("Like Timeline error")

    def followsuggestions(self):
        try:
            self.browser.get("https://www.instagram.com/explore/people/suggested/")
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/div/div').click()
            time.sleep(2)
            while 1:
                self.browser.find_element_by_xpath("//button[text()='Follow']").click()
                self.browser.execute_script("window.scrollTo(0, window.scrollY + 26)")
                time.sleep(2)
            time.sleep(10)
        except Exception as e:
            print("Follow limit has reached maximum level...Please try after some time.")
        

    def watch_all_stories(self,wtime=10):
        try:
            if isinstance(wtime,int) and wtime>10:
                self.browser.get('https://www.instagram.com/')
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a').click()
                time.sleep(wtime)
            else:
                print("Sorry can't open stories.")
        except Exception as e:
            print("No stories found",e)


