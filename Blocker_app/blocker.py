import time
from datetime import datetime as dt 

hosts_temp="hosts"
hosts_path = "/private/etc/hosts" 
redirect = "127.0.0.1"
websites = ["www.instagram.com", "instagram.com", "www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.twitter.com", "twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 6) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 10):
        print("Working hours..")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+ "\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("fun hours...")
    time.sleep(5)

 
