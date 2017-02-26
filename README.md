# HackBU
Code for HackBU 2017

# Problem
What if you didn't know what to get for your friend on their birthday?

# What it does
Alexa provides you with a birthday gift suggestion for your friend!

# How it does it
1. Alexa receives the name of the person to find a gift for
2. In the backend, call the Facebook Graph API to find the likes associated with the person
3. Prioritize the likes and construct a keyword phrase to use to search Ebay
4. Take the keyword phrase and 

# Technologies used
Amazon Alexa - takes user input of who to find a gift for
Python - Flask backend framework for implementing logic to prioritize likes

# APIs
Facebook Graph API - retrieves likes for a specified friend
Ebay API - retrieves an item most relevant to the keywords of the like contents

# Future
Improve the logic for prioritizing which likes can help determine what gift would be appriopriate for your friend
Improve the accuracy search query by filtering on non relevant items
Find an alternative e-commerce website to search for items such as Amazon

# Issues faced
Surveying the available APIs.
The constraint with using the Amazon API was that we needed Amazon's permission to complete the registration of an Amazon Associate Account which we thought wouldn't be feasilble in the given time frame. Also the Amazon Product Advertising API only returns 10 products.
We found out Google Shopping API has been deprecated since 2013 and is no longer public.
Ebay API documentation needs more sample code and tutorials of the use of their product search API
