'''
Created on Dec 21, 2015
@author: hanhanwu
nltk provides tf-idf itself
Note: in practical, tf-idf is a method to narrow down corpus based on search terms
'''
import nltk
import json

def main():
    f_path = '[change to your googleplus_posts.json location]'
    data = json.loads(open(f_path).read())
    
    QUERY_TERMS = ['mobile']   # You can change the search terms here
    
    activities = [activity['object']['content'].lower().split() for activity in data if activity['object']['content'] != '']
    
    # nltk TextCollection has tf-idf itself
    tc = nltk.TextCollection(activities)
    
    relevant_activities = []
    
    for i in range(len(activities)):
        score = 0
        for term in QUERY_TERMS:
            score += tc.tf_idf(term.lower(), activities[i])
        if score > 0:
            relevant_activities.append({'score': score, 'title': data[i]['title'], 'url': data[i]['url']}) 
        
    relevant_activities = sorted(relevant_activities, key = lambda a: a['score'], reverse = True)
    for ra in relevant_activities:
        print 'title: ', ra['title']
        print 'url: ', ra['url']
        print 'score: ', ra['score']
    
if __name__ == '__main__':
    main()
