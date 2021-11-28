#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd


# In[12]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[13]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[14]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[15]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[16]:


slide_elem.find('div', class_='content_title')


# In[17]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[18]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[19]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[20]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[21]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[22]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[23]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[24]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[25]:


df.to_html()


# In[26]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[27]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[28]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# In[29]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[30]:


# browser.find_by_css('a.product-item h3')[0].click()
# element = browser.find_link_by_text('Sample').first
# print(element['href'])
# browser.find_by_css("h2.title").text


# In[31]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

#items = browser.find_by_css('a.product-item h3')
# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    #create empty dictionary
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.find_link_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[32]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[33]:


# 5. Quit the browser
browser.quit()


# In[ ]:




