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

****************************************************************************
Text Mining mailbox and MongoDB queries

* MongoDB is a document-oriented database, by loading .json file into this database, you do text mining through its query. And the query can be written in Python by using pymongo client, or you can write queries directly through MongoDB shell.
* The email data set is from Enron Email Dataset: http://www.cs.cmu.edu/~enron/   Download the latest version.

1. convert_emails_to_mbox.py
  * This is a way to standardize emails to .mbox format. 
  * You need to change the file locations in the code (see comments).
  * The folder_path is the location of your downloaded Enron Email Dataset.

2. mbox_to_JSON.py
  * Convert .mbox output generated from convert_emails_to_mbox.py to JSON so that you can load the .json file to MongoDB.
  * Change the file locaions in the code (see comments).
  
3. Load your .json file into MongoDB
  * In MongoDB shell, type: (change [enron.mbox.json path] as the path on your machine)
  `mongoimport --db enron --collection mbox --drop --file [enron.mbox.json path]`

4. Basic_MongoDB_queries.py
  * Done step 3 first.
  * Make sure a MongoDB instance is running before running this code.
  * This file include the basic queries written through Python.

5. MongoDB_aggregate_queries.py
  * Done step 3 first.
  * Make sure a MongoDB instance is running before running this code.
  * This file include the aggregate queries written through Python.

6. MongoDB_key_word_search.py
  * method 1: creating a text index and search the emails contain the keyword
  * method 2: using aggregate to do keyword search
  * method 3: using the index with find() function to do the search
