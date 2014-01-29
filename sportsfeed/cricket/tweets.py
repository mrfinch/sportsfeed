from twython import Twython
APP_KEY='I9YraKHyOWQDgJ4gFPfA'
APP_SECRET='oU1VKYCYzWg4Jt0ulmPhGOe48uvF4rtjpDHct5JktU'


def gettweets():
	tweet=[]
	name=[]

	twitter=Twython(APP_KEY,APP_SECRET,oauth_version=2)
	ACCESS_TOKEN=twitter.obtain_access_token()
	twitter=Twython(APP_KEY,access_token=ACCESS_TOKEN)
	tweets=twitter.search(q="#cricket",count=5)

	for status in tweets['statuses']:
		for info in status:
			if info=="text": 
				tweet.append(status[info])
			if info=="user":
				for detail in status[info]:
					if detail=="screen_name":
						name.append(status[info][detail])	

	return (tweet,name)
				