# NaturalLanguageProcessing_Basic
Basic operations for Natural Language Processing (NLP)

Extract interactions:
* Interactions in this folder means English phrases, in my code, I have provided methods to extract Noun Phrases and Noun-Verb-Noun phrases
* Why extract interactions: shorten the text, only leave words that allows readers scan and understand the general meaning
* Code：
  a. run get_data.py and find the feed.json location on your machine. This file parses the blog posts from the provided URL, and generate posts into json format.
  b. Update the f_path in extract_interactions.py to the feed.json location on your machine. The extract_interaction.py provides methods to extract Noun Phrases or Noun-Verb-Noun Phrases
