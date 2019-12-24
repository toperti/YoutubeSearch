
import requests
import json

def jprint(obj):
	print(json.dumps(obj, sort_keys = True, indent = 4))

def getKey():
	with open('creds.txt') as creds:
		key = creds.readline()
		key.rstrip()
	return key

def getResponse():
	searchPhrase = input('What would you like to search for?: ')
	params = {
		'part' : 'snippet',
		'q' : searchPhrase,
		'key' : getKey(),
		'maxResults' : 3
	}

	response = requests.get('https://www.googleapis.com/youtube/v3/search', params = params)
	
	# if you want to see the url that the requests.get accessed
	# print(response.url)

	response = response.json()

	# prints the response beautifully
	# jprint(response)
	return response['items']

def getImage(item):
	return item['snippet']['thumbnails']['default']['url']

def getType(item):
	rawKind = item['id']['kind']
	endKind = rawKind[8:].capitalize()
	return endKind

def getChannel(item):
	return item['snippet']['channelTitle']

def getTitle(item):
	return item['snippet']['title']

def generateURL(item):
	# get the video type
	itemType = getType(item)

	if itemType == "Video":
		# make URL for video
		URL = "https://www.youtube.com/watch?v="
		URL += item['id']['videoId']

	elif itemType == "Channel":
		# make URL for channel
		URL = "https://www.youtube.com/channel/"
		URL += item['id']['channelId']

	else:
		URL = "I Don't know how to make a URL for " + itemType + " yet"

	return URL

def printVideos(itemList):
	for item in itemList:
		print(getType(item) + ":", getChannel(item), "–", getTitle(item))
		print(generateURL(item))

def genResult(itemList):
	res = []
	for item in itemList:
		res.append(getType(item) + ": " + getChannel(item) + " – " + getTitle(item) + '\n')
		res.append(generateURL(item) + '\n')
		res.append(getImage(item))
	print(res)
	return res

def main():
	results = getResponse()
	response = genResult(results)
	return response

if __name__ == '__main__':
	print(main())
