

#create dependencies
import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
import pymongo
from pymongo import MongoClient
import pandas as pd
import pprint

# **NASA Mars News**


def init_browser():
    executable_path = {'executable_path':'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)




def scrape_mars():
    browser=init_browser()
    
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title =soup.find("div", class_="content_title").text
    news_p=soup.find("div", class_="article_teaser_body").text
   

 # **JPL Mars Space Images - Featured Image**



    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    base_url='https://www.jpl.nasa.gov/spaceimages/images/largesize/'
    browser.visit(url2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


    

# In[ ]:


    featured_image=soup.select('a[data-fancybox-href^="/spaceimages/images/mediumsize/"]')

    featured_image_url=base_url+'image_jpg'

# **Mars Weather**

# In[ ]:


    import tweepy
    import json
    from config import consumer_key, consumer_secret, access_token, access_token_secret


# In[ ]:


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[ ]:


    target_user = "MarsWxReport"


# In[ ]:


    public_tweets = api.user_timeline(target_user)


# In[ ]:


    for tweet in public_tweets:
        mars_weather = tweet["text"]
        


# **Mars Facts**

# In[ ]:


    #import pandas as pd





    #url = 'https://space-facts.com/mars/'




    #tables = pd.read_html(url)
   

 # **Mars Hemisperes**

# In[ ]:


    hemisphere = []



    base_url='https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/'
    cerberus_url='cerberus_enhanced.tif/full.jpg'
    schiaparelli_url='schiaparelli_enhanced.tif/full.jpg'


# In[ ]:


    Cerberus=dict({"title":"Cerberus Hemisphere","image_url1":base_url+cerberus_url})


# In[ ]:


    Schiaparelli=dict({"title":"Schiaparelli Hemisphere","image_url2":base_url+schiaparelli_url})
    Schiaparelli


# In[ ]:


    Syrtis_Major ={"title":"Syrtis Major\
    Hemisphere","image_url3":base_url+'syrtis_major_enhanced.tif/full.jpg.'}
    Syrtis_Major


    # In[ ]:


    Valles_Marineris={"title":"Valles Marineris\
    Hemisphere","image_url4":base_url+'valles_marineris_enhanced.tif/full.jpg'}
    Valles_Marineris


    # In[ ]:


    hemisphere=[Cerberus,Schiaparelli,Syrtis_Major,Valles_Marineris]
    mars_dict={"news_title":news_title,"news_p":news_p,"featured_image_url"\
    :featured_image_url,"mars_weather":mars_weather,"hemisphere":hemisphere}
    
    # Setup connection to mongodb
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

# Select database and collection to use
    db = client.app
    collection = db.mission_to_mars
    
    
            
      
    db.mission_to_mars.insert_one(mars_dict).inserted_id
     
    print(mars_dict)   