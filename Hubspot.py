import urllib2
import json

# Change the APIKEY_VALUE by your API key
APIKEY_VALUE = ""
APIKEY = "?hapikey=" + APIKEY_VALUE
HS_API_URL = "http://api.hubapi.com"


def getTotalNumberOfContacts():
    # First, we build the correct url
    xurl = "/contacts/v1/contacts/statistics"
    url = HS_API_URL + xurl + APIKEY
    # Now we use urllib2 to open the url and read it
    response = urllib2.urlopen(url).read()
    # Transform the response, a JSON object, into a Python dictionary object
    statistics = json.loads(response)
    # Finally, return the number of contacts
    return statistics["contacts"]

# print "The total number of contacts:" + str(getTotalNumberOfContacts())


def getPublishingChannels():

    xurl = '/broadcast/v1/channels/setting/publish/current'
    url = HS_API_URL + xurl + APIKEY

    response = urllib2.urlopen(url).read()

    channels = json.loads(response)
    listofchannels = json.dumps(channels, indent=4, sort_keys=True)

    return listofchannels

# print "The list of channels are:" + str(getPublishingChannels())


def getBlogPosts():

    xurl = '/content/api/v2/blog-posts'
    url = HS_API_URL + xurl + APIKEY

    response = urllib2.urlopen(url).read()

    blog_posts = json.loads(response)

    return blog_posts['total_count']

# print "The total number of blog posts: " + str(getBlogPosts())


def getBlogTopics():

    xurl = '/blogs/v3/topics'
    url = HS_API_URL + xurl + APIKEY

    response = urllib2.urlopen(url).read()

    blog_topics = json.loads(response)

    return blog_topics

# print "The blog topics are: " + str(getBlogTopics())


def getKeywordList():
    xurl = '/keywords/v1/keywords'
    url = HS_API_URL + xurl + APIKEY

    response = urllib2.urlopen(url).read()

    list_of_keywords = json.loads(response)

    for i in list_of_keywords['keywords']:
        return i['keyword']


# print "The list of keywords are: " + str(getKeywordList())


def getEvents():

    TRACK_URL = 'http://track.hubspot.com/'
    xurl = 'v1/event/'
    url = TRACK_URL + xurl + APIKEY

    response = urllib2.urlopen(url).read()

    list_of_events = json.loads(response)

    return list_of_events


def getEngagements():

    xurl = '/engagements/v1/engagements/:engagementId'
    url = HS_API_URL + xurl + APIKEY

    response = urllib2.urlopen(url).read()
    list_of_engagements = json.loads(response)

    return list_of_engagements


def getListLayouts():
    xurl = '/content/api/v2/layouts'

    url = HS_API_URL + xurl + APIKEY

    response = urllib2.urlopen(url).read()
    list_of_layouts = json.loads(response)

    return list_of_layouts


if __name__ == '__main__':
    print getListLayouts()
    # lambda *args: None
