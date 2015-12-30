'''
Created on Dec 29, 2015
@author: hanhanwu
extract NN phrases
'''
import nltk
import json

def get_NN_entities(txt):
    sentences = nltk.tokenize.sent_tokenize(txt)
    token_sets = [nltk.tokenize.word_tokenize(s) for s in sentences]
    pos_tagged_token_sets = [nltk.pos_tag(t) for t in token_sets]
    pos_tagged_tokens = [t for v in pos_tagged_token_sets for t in v]
    
    all_entities = []
    previous_pos = None
    current_entities = []
    for (entity, pos) in pos_tagged_tokens:
        if previous_pos == pos and pos.startswith('NN'):
            current_entities.append(entity)
        elif pos.startswith('NN'):
            if current_entities != []:
                all_entities.append((' '.join(current_entities), pos))
            current_entities = [entity]
        previous_pos = pos
    return all_entities
    

def main():
    f_path = '[change to your feed.json location]'
    blog_data = json.loads(open(f_path).read())
    
    for blog in blog_data:
        txt = blog['content']
        all_entities = get_NN_entities(txt)
        
        blog['entities'] = {}
        # Get the frequency of each entity chunk, and use each chunk as the index
        for c in all_entities:
            blog['entities'][c] = blog['entities'].get(c,0) + 1
        
        print blog['title']
        print '-' * len(blog['title'])
        
        # just print the title case entities and their frequency
        for (entity, pos) in blog['entities']:
            if entity.istitle():
                print '\t%s (%s)' % (entity, blog['entities'][(entity, pos)])
        
if __name__ == '__main__':
    main()
