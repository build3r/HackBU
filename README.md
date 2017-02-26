# HackBU #
Code for HackBU 2017

# The Problem #
What if you didn't know what to get for your friend on their birthday?

# What Gift Suggester Does #
Provides you with a birthday gift suggestion for your friend!

# How it does it #
1. Alexa receives the name of the person you want to find a gift for.
2. Utilizse the Facebook Graph API to retrieve interests and likes associated with that person's online presence.
3. Parses the info from Facebook to provide viable data that can then be used to construct keyword phrases.
4. Calls the eBay Finding API with our generated phrases in a manner designed to retrieve the most relevant results.
5. Parses the returned item and price info into a more conversational form, which Alexa then articulates to you.
6. The item info and price is also sent to the Alexa companion app on your smartphone.

# Technologies/APIs used #
- Amazon Alexa: user interface (voice and/or app)
- Facebook Graph API: used for retrieving your friends' relevant information
- eBay Finding API: used for querying the market price and specific sale listings for the item in question
- Python + Flask: Used for handling back-end logic/parsing and facilitates data-flow between the APIs used for this Alexa skill.
- ngrok: Provides seamless local hosting of our webserver and allows it to interface with Amazon Alexa

# Future #
- Apply a more intelligent approach to parsing through the retrieved information from facebook, and provide even more relevant results for the friend in question.
- Add knowledge of a friend's birthday, ideally so the user could ask something like, "What friends have birthdays next week, and what should I get them?"
  - This was a stretch goal for us, and due to time constraints, we were unable to accomplish this during HackBU.
- Filter items based on proximity, sort by seller reviews, look up which items have free and fast shipping
- More filtering parameters available with the findItemsByKeywords function provided by eBay's Finding API
- Implement searching by category in addition to using keywords

# Issues faced #
- We came into HackBU having absolutely no experience with Alexa skills or any of the APIs we ended up using.
- Our first challenge was coming up with what technologies could help us reach this project's end goal. We initially went down the wrong path, diving heavily into Google's Content API for Shopping. It was only several hours into this research that we discovered that Google no longer provided public endpoints for this API and our time had been wasted researching it. The other initial obvious choice was using Amazon's own shopping API to return sales listings, but we found out that required prior registration and approval from Amazon, so that was unfeasable.
- We ended up choosing eBay's Finding API, as that appeared to be the most viable option, despite its API's lack of clear documentation, which ended up taking quite of experimentation to figure out.
