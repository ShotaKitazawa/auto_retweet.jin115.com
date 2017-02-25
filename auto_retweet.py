#!/usr/bin/env python
import subprocess
import re
import twitter
import settings
import time

with open("count", "r") as file:
    count = int(file.readline())

try: 
    while True:
        tweet = subprocess.check_output(["python", "./scraping.py", "http://jin115.com/archives/{0}.html".format(count)]).decode('utf-8')

        if tweet[0] == "[" and tweet[1] == "]":
            print("{0} is NotTweet.".format(count))
            count += 1
            continue
        #elif tweet == "NotFound":
        elif tweet[0] == "N":
            print("{0} is NotFound.".format(count))
            time.sleep(60)
            continue

        tweet_list = tweet.split('"')
        id_list = []
        for i in tweet_list:
            if re.match("https://twitter.com/*", i):
                url = list(i)
                tmp_list = url
                for j in range(len(url)):
                    if re.match("^[0-9]*$", "".join(tmp_list)):
                        # print("".join(tmp_list))
                        tmp = "".join(tmp_list)
                        id_list.append(tmp)
                        break
                    else:
                        tmp_list.pop(0)

        api = twitter.Api(
            consumer_key=settings.CONSUMER_KEY,
            consumer_secret=settings.CONSUMER_SECRET,
            access_token_key=settings.ACCESS_TOKEN,
            access_token_secret=settings.ACCESS_TOKEN_SECRET,
        )
        try:
            for i in id_list:
                api.PostRetweet(i)
            count += 1
        except twitter.error.TwitterError:
            print ("Already retweet.")
            count += 1
            continue

finally:
    with open("count", "w")as file:
        file.write(str(count))
    print("END")
