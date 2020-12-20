# web-scraping-challenge

<h3>Objective: Scrape multiple websites about Mars to populate an html template.</h3>
<p>I built the scrape file in a jupyter notebook first, tackling one piece at a time.</p>
<p>Mars news was first. I used the Chrome inspector to locate the proper tag/class that held the info that I needed, then used BeautifulSoup to isolate the text for the headline and intro paragraph.</p>
<p>For the JPL featured image I was able to get the link fairly easily, but needed to spend some time stripping out the unnecessary parts I had pulled and then needed to set up a var for the base url. I then set it up to concatenate the base and img url for my final var that I pushed to the mars_data dict.</p>
<p>For the mars facts table I used the referenced documentation for pandas to_html. I read the site and identified which table I wanted (first one found) then set the columns/index in my dataframe. I used to_html to output my html data table.</p>
<p>The hemisphere images took some trial and error. I set up my base loop to visit each download page, isolate the image url and title, and then appended that to a dictionary.</p>
<p>I assigned all my scraped data to a mars_data dictionary at the end of the scrape.<p>

<h3>Setting up the Flask server page</h3>
<p>I utilized the class activites with Craigslist and Costa Rica weather as my initial template, and just changed what I neeed to in order to grab my mars_data and connect it to MongoDB.</p>

<h3>HTML render template</h3>
<p>I again utilized the class activities to set up my initial html template. The Costa Rica one was especially useful as I set it up to render the data stored in MongoDB.</p>
<p>My one major sticking point here was getting my mars_facts table to render as html. Initially I could only get it to load as a text string, with all the html tags displayed instead of being read by the browser. I partnered with my study group, where another student had found some code samples that referenced '| safe' in the call to the db for the html variable. Putting that in fixed my problem. I did some research and found that declaring it 'safe' told the browser that it was ok to display the code as html versus a string (the article called it 'htmlescaped' when it doesn't render). Sounds like this could be important as we do more with Javascript and further data rendering, so I'm glad I encountered it here.</p>