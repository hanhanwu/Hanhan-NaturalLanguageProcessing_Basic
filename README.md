# NaturalLanguageProcessing_Basic
Basic operations for Natural Language Processing (NLP)

Extract entities
* Entities are phrases in the whole text.
* Why extract entities: often used for intelligent tagging, the extraced phrases serve as tags
* Code:
  * Run get_data.py and find the feed.json location on your machine. This file parses the blog posts from the provided URL, and generate posts into json format.
  * Update the f_path in extract_NN_entities.py to the feed.json location on your machine. The code provides the method to extract Noun Phrases

Extract interactions:
* Interactions in this folder means English phrases in each indivudual sentence, in my code, I have provided methods to extract Noun Phrases and Noun-Verb-Noun phrases.
* Why extract interactions: shorten the text, only leave words that allows readers scan and understand the general meaning.
* Note: all the interactions are extracted from each indivudual sentence, but by contrast, entities are extracted from the whole text.
* Code：
  * Run get_data.py and find the feed.json location on your machine. This file parses the blog posts from the provided URL, and generate posts into json format.
  * Update the f_path in extract_interactions.py to the feed.json location on your machine. The extract_interaction.py provides methods to extract Noun Phrases or Noun-Verb-Noun Phrases.

Evaluate Results using F1 score:
* F1 = 2* (precision*recall)/(precision+recall)
* precision = TP/(TP+FP)
* recall = TP/(TP+FN)


