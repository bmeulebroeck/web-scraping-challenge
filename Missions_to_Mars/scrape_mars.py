from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd

mars_data = {}

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/downloads/chromedriver/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    # Scrape news article
    browser = init_browser()

    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    time.sleep(8)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_news = soup.find('div', class_='list_text')

    news_title = mars_news.find('div', class_='content_title').text
    news_p = mars_news.find('div', class_='article_teaser_body').text

    #Scrape JPL image
    #browser = init_browser()

    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    jpl = browser.html
    jpl_soup = BeautifulSoup(jpl, 'html.parser')

    feat_img_section = jpl_soup.find('div', class_='carousel_container')

    jpl_img_url = feat_img_section.find('article', class_='carousel_item')["style"].replace("background-image: url('", "").replace("');", "")
    
    jpl_base_url = 'https://www.jpl.nasa.gov'
    jpl_final_url = jpl_base_url + jpl_img_url

    #Scrape Mars Facts 
    mars_facts_url = 'https://space-facts.com/mars/'

    mars_facts = pd.read_html(mars_facts_url)

    mars_facts_df = mars_facts[0]
    mars_facts_df.columns = ["Measurement", "Mars"]
    mars_facts_df.set_index('Measurement', inplace=True)

    facts_html = mars_facts_df.to_html()

    # Scrape hemisphere images from USGS
    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)

    hemis = browser.html
    hemi_soup = BeautifulSoup(hemis, 'html.parser')

    hemi_sections = hemi_soup.find_all('div', class_='item')

    hemi_img_urls = []

    base_url = 'https://astrogeology.usgs.gov/'

    for hemi in hemi_sections:
        hemi_title = hemi.find('h3').text

        hemi_url = hemi.find('a', class_='itemLink product-item')['href']
        comb_url = base_url + hemi_url

        browser.visit(comb_url)

        # Use bs4 to get the html
        img_pg_html = browser.html
        img_pg_soup = BeautifulSoup(img_pg_html, 'html.parser')

        # Isolate the image download link section at the top
        link_section = img_pg_soup.find('div', class_='downloads')
        img_url = link_section.find('a')['href']

        hemi_img_urls.append({'title': hemi_title, 'img_url': img_url})

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "jpl_img_url": jpl_final_url,
        "mars_facts": facts_html,
        "hemi_img_urls": hemi_img_urls
    }

    browser.quit()

    return mars_data