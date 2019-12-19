# this is code to obtain search results of a search into youtube

# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python
import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def jprint(obj):
	print(json.dumps(obj, sort_keys = True, indent = 4))

def getResponse(words):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_906498750487-rt7nntae6g8me9dpo7e4uqoju3p73tb8.apps.googleusercontent.com.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q=words
    )

    response = request.execute()

    # using jprint rather than normal print for beauty purposes
    # jprint(response)
    return response['items']

def getType(item):
    rawKind = item['id']['kind']
    endKind = rawKind[8:].capitalize()
    return endKind

def getChannel(item):
    return item['snippet']['channelTitle']

def getTitle(item):
    return item['snippet']['title']

def printVideos(itemList):
    for item in itemList:
        print(getType(item) + ":", getChannel(item), "–", getTitle(item))

def main():
    searchPhrase = input("What would you like to search for?: ")
    results = getResponse(searchPhrase)
    printVideos(results)

if __name__ == "__main__":
    main()

# remaining tasks
# have to obtain the keywords from the user and then input them where searching is (don't know the format for that yet)
# have to beautify the output so that it doesn't look like shit
# maybe use flask/django to put it up on a website