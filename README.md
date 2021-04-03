This simple site map is my first ever web-scraping project. 

I decided to scrape the helloworld website (root url = 'http://www.helloworldstudio.org') in order to create a dictionary dataset that contains all the pages of the helloworld dataset as keys, and saves the urls each key connects to as its values. Some pages connect to no other urls, while others connect to up to 59. 

The crawler.py file was used to scrape the website, and if you'd like to try out this software on a different website, just replace the 'http://www.helloworldstudio.org' link wherever it appears with your desired root link. I created a function called get_urls, which accesses all the the urls linked on a page and stores them as a value in a dictionary with the starting url as the key. Once all the urls have been scraped the function calls itself (recursion) to do the same for all the links found on that page (as long as they are not in the dictionary already) and so on and so on until the whole website has been scraped.

Once the crawler.py dictionary was created, I wrote it to a file called 'hello_world_urls.txt', however you can name your file whatever you'd like. 

From there in visualizer.py, I use matplotlib to create a simple graph demonstrating the number of hyperlinks each url had in a scaterplot (helloworld_sitemap.png). 

This project was a great introduction to wedscraping and matplotlib. 
