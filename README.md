Welcome! This is the DU Innovation Lab's Digital Display code. This repository has been copied onto a Rasberry Pi (which actually runs everything).

The digital display is really just a website with one page. This page shows who is currently working, current events, and encourages people to sign in.

I created this project using Django. It is Python based web development. There are lots of good resources on Django and the documentation for Django is here: https://docs.djangoproject.com/en/5.1/

I also used Bootstrap in this project to make my life significantly easier and the webpage prettier. Bootstrap documentation is here: https://getbootstrap.com/docs/5.3/getting-started/introduction/

This project connects with Sling Scheduling's API. API documentation here: https://api.getsling.com/

And as expected for a webpage, there are HTML, CSS, and JavaScript components as well.

If you are working on this project locally, make sure you Python is installed with the libraries django, requests, and dotenv.

Need to update or fix something about the digital display? Here's a few good places to start.

<b>Just Not Working</b>

The API key probably expired. This happens from time to time.

How to find API key:
> https://support.getsling.com/en/articles/6542253-api
  
> My preferred method is using the inspector tools.

Where to put API key:
> backend/.env
  
> There is a variable called "API_AUTH", update the token accordingly.
> As a side note, when I (Sariah) eventually graduates, you may need to update the "API_USER" as well.

<b>Need to Update Carousel</b>

Have new marketing content? Awesome! Save that flyer as a png and name it flyerOne, flyerTwo, or flyerThree. Which name you chose depends on which content the flyer is replacing.

Upload that flyer to the Raspberry Pi and put it in: homepage/static/images/Marketing

Make sure you delete the flyer you're replacing.

Want more than three flyers?

Go into homepage/templates/homepage/home.html

Go to the marketing div and from there into the carousel. In the carousel you should see a bunch of divs with the class "carousel-item"

Copy the HTML for a carousel item and paste it in line with the other carousel items. Rename the file accordingly. i.e. flyerFour.png

<b>Not Updating as Expected</b>

This happens on the Raspberry Pi sometimes and we are trying to fix it. It has to do with a time zone issue.

Go to display/settings.py

There should be a setting in there for time zones. Change it to either MST or default. Whichever one it isn't currently might fix the problem.

<b>Need to Update Webpage Content</b>

Update HTML here: homepage/templates/homepage/home.html

Update CSS here: homepage/static/css/home.css

<b>Need to Fix a Code Problem</b>

Django scripts live here: homepage/views.py

Scripts that deal with the API live here: backend
