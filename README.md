# tlc
This is a python package designed to enable the Taxi and limousine Commission(TLC) to track posts on social media to better allocate their taxi services

### Installation

1. git clone the [tlc package](https://github.com/rybo449/tlc)

2. Type the following in the terminal
```
git clone https://github.com/rybo449/tlc.git
```

3. cd into the folder and navigate to `tlc/settings/` and create a file called `secret.py`

4. Fill in the details of `secret.py` following the format of `secret.py.default` found in the settings folder.

5. These details can be created by making an application on each of the APIs listed, or just filling in the ones you intend to use.

6. Now go back to the main folder and type
```
python setup.py develop
```

### API Endpoints

This package supports the following public APIs.

1. [Google Maps API](https://developers.google.com/maps/) for geocoding and reverse geocoding.

2. [Factual API](http://developer.factual.com/) for location services.

3. [Instagram API](https://instagram.com/developer/?hl=en) for getting real time instagram posts based on location and other services.

4. [Twitter API](https://dev.twitter.com/overview/documentation) for realtime tweets by location.

5. [Clarifai API](http://www.clarifai.com/api) for image tagging of instagram images.

6. [Foursquare API](https://developer.foursquare.com/) for getting trending venues and information by location.

### Example Usage

```
from tlc.services import Geocode
gcode = Geocode()
lat,lng = gcode.geocode('Times Square, New York')

from tlc.services import FactualService
api = FactualService()
print api.get_landmarks(lat, lng)

from tlc.services import InstagramService
api = InstagramService()
print api.posts_in_new_york() #returns posts from each zip-code in new york in the past few hours
print api.hashtag(lat, lng) #returns a dictionary of hashtags and their counts in the current location
location = 'Times Square, New York'
print api.get_tags(location) # returns a dictionary of tags of the images posted on instagram and their counts, in the nearby location by using the Clarifai API

from tlc.services import TwitterService
api = TwitterService()
print api.get_tweets(lat, lng) #returns a list of tweets in a 1 mile radius around the lat, lng

from tlc.services import FoursquareService
api = FoursquareService()
query = 'coffee'
print api.get_venues(lat, lng, query) # returns a list of coffee shops in the vicinity of that lat, lng
```
For more functionality see the code in `tlc/services/__init__.py`

This package is aimed at people new to data science and want to start collecting data in a quick and easy manner and do analysis. It helps people who want to start analyzing data and do not want to read through the entire documentation of each of the above APIs.

It is intended at academics who do not want to spend time on building their own data collection infrastructure. Please feel free to download and modify the code as per your needs and add more functionalities as you wish.

Happy coding!