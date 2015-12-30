# NaturalLanguageProcessing_Basic
Basic operations for Natural Language Processing (NLP)

1. Search use tf-idf scores:
* Given the certain query terms, do the searches based on the tf-idf scores for these terms
* Code:
  * Download googleplus.json and find the location on your machine. I pasred the data from google+ posts.
  * Update the f_path in tf_idf_term_search.py to the googleplus.json location on your machine. 


2. Extract entities
* Entities are phrases in the whole text.
* Why extract entities: often used for intelligent tagging, the extraced phrases serve as tags
* Code:
  * Run get_data.py and find the feed.json location on your machine. This file parses the blog posts from the provided URL, and generate posts into json format.
  * Update the f_path in extract_NN_entities.py to the feed.json location on your machine. The code provides the method to extract Noun Phrases


3. Extract interactions:
* Interactions in this folder means English phrases in each indivudual sentence, in my code, I have provided methods to extract Noun Phrases and Noun-Verb-Noun phrases.
* Why extract interactions: shorten the text, only leave words that allows readers scan and understand the general meaning.
* Note: all the interactions are extracted from each indivudual sentence, but by contrast, entities are extracted from the whole text.
* Code：
  * Run get_data.py and find the feed.json location on your machine. This file parses the blog posts from the provided URL, and generate posts into json format.
  * Update the f_path in extract_interactions.py to the feed.json location on your machine. The extract_interaction.py provides methods to extract Noun Phrases or Noun-Verb-Noun Phrases.
  

4. Generate Collocations:
* Collocations are a sequence of words or terms that co-occur more often than would be expected by chance.
* Why Collocations: if we only extract key words or frequent words, we may end up cutting a phase into multiple parts and get confusing results. By getting collocations, the results maybe more accurate.
* Note: here the way to generate collocations is still based on statistical methods. By contrast, the methods I used to extract entities, interactions are on the semantic level.
* Code:
  * Download googleplus.json and find the location on your machine. I pasred the data from google+ posts.
  * Update the f_path in get_collocations.py to the googleplus.json location on your machine. 
  

5. Evaluate Results using F1 score:
* F1 = 2* (precision*recall)/(precision+recall)
* precision = TP/(TP+FP)
* recall = TP/(TP+FN)


