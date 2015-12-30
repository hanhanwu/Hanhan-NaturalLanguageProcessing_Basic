'''
Created on Dec 29, 2015
@author: hanhanwu
shorten the text - extract interactions, 
interactions are all sentence-based
'''
import nltk
import json

def get_NN_interactions(txt):
    sentences = nltk.tokenize.sent_tokenize(txt)
    token_sets = [nltk.tokenize.word_tokenize(s) for s in sentences]
    pos_tagged_tokens = [nltk.pos_tag(t) for t in token_sets]
    
    all_interactions = []
    for sentence in pos_tagged_tokens:
        all_entities = []
        previous_pos = None
        current_entities = []
        for (entity, pos) in sentence:
            if previous_pos == pos and pos.startswith('NN'):
                current_entities.append(entity)
            elif pos.startswith('NN'):
                if current_entities != []:
                    all_entities.append((' '.join(current_entities), pos))
                current_entities = [entity]
            previous_pos = pos
        
        if len(all_entities) >= 1:
            all_interactions.append(all_entities)
        else:
            all_interactions.append([])
            
    assert len(all_interactions) == len(sentences)
    
    return dict(all_interactions = all_interactions,
                sentences = sentences)


def get_NNVBNN_interactions(txt):
    sentences = nltk.tokenize.sent_tokenize(txt)
    token_sets = [nltk.tokenize.word_tokenize(s) for s in sentences]
    pos_tagged_tokens = [nltk.pos_tag(t) for t in token_sets]
    
    all_interactions = []
    for sentence in pos_tagged_tokens:
        all_entities = []        
        current_entities = []
        
        i = 2
        while i < len(sentence):
            fst_previous_pos = sentence[i-2][1]
            snd_previous_pos = sentence[i-1][1]
            current_pos = sentence[i][1]
            if fst_previous_pos.startswith('NN') and snd_previous_pos.startswith('VB') and current_pos.startswith('NN'):
                current_entities.append(sentence[i-2][0])
                current_entities.append(sentence[i-1][0])
                current_entities.append(sentence[i][0])
                all_entities.append((' '.join(current_entities), 'NNVBNN'))
                current_entities = []
            i += 1
             
        
        if len(all_entities) >= 1:
            all_interactions.append(all_entities)
        else:
            all_interactions.append([])
            
    assert len(all_interactions) == len(sentences)
    
    return dict(all_interactions = all_interactions,
                sentences = sentences)
    

def main():
    f_path = '[change to your feed.json location]'
    blog_data = json.loads(open(f_path).read())
    
    for blog in blog_data:
        txt = blog['content']
#         blog.update(get_NN_interactions(txt))     # for NN interactions
        blog.update(get_NNVBNN_interactions(txt))   # for NN, VB, NN interaction
        print blog['title']
        print '-' * len(blog['title'])
        for interactions in blog['all_interactions']:
            if interactions == []:
                continue
            print '; '.join(e[0] for e in interactions)
        print
        
        
if __name__ == '__main__':
    main()
