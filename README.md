# HackBU
Code for HackBU 2017

# Problem
What if you didn't know what to get for your friend on their birthday?

# What it does
Alexa provides you with a birthday gift suggestion for your friend!

# How it does it
1. Alexa receives the name of the person to find a gift for
2. In the backend, call the Facebook Graph API to find the likes associated with the person
3. Prioritize the likes based on categories (as of now) to construct a keyword phrase to use to search Ebay
4. Call the Ebay API with the keyword phrase to retrieve the most relevant item
5. Alexa mentions the item and price

# Technologies used
Amazon Alexa
Python Flask (backend framework)

# APIs
Facebook Graph API - retrieves likes for a specified friend
Ebay API - retrieves an item most relevant to the keywords of the like contents

# Future
Functionalities:
- Improve the logic for prioritizing which likes can help determine what gift would be appriopriate for your friend
- Given a question inquiring about when someone's bday is, respond with a certain number of days till then
Filtering improvements:
- Filter items based on proximity, sort by seller reviews, look up which items have free and fast shipping
- More filtering parameters available with the findItemsByKeywords function
- Implement searching by category then using keywords

Technical API improvements:
- Consider Amazon

# Issues faced
- Surveying the available APIs.
- The constraint with using the Amazon API was that we needed Amazon's permission to complete the registration of an Amazon Associate Account which we thought wouldn't be feasilble in the given time frame. Also the Amazon Product Advertising API only returns 10 products.
- We found out Google Shopping API has been deprecated since 2013 and is no longer public.
- Ebay API documentation needs more sample code and tutorials of the use of their product search API
