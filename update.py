# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:14:42 2016

@author: Guest1
"""
import pickle
import sqlite3
import numpy as np
import os
import pdb

# import HashingVectorizer from local dir
from vectorizer import vect

def update_model(db_path, model, batch_size=10000):

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * from sentiment_review')
    
    results = c.fetchmany(batch_size)
    while results:
        data = np.array(results)
        X = data[:, 1]
        y = data[:, 2].astype(int)
        classes = np.array([0, 1, 2])
        X_train = vect.transform(X)
        clf.partial_fit(X_train, y, classes=classes)
        results = c.fetchmany(batch_size)
    
    conn.close()
    return None

#pdb.set_trace()
    
"""Update the model"""
# cur_dir = '.'

# Use the following path instead if you embed this code into
# the app.py file


# import os
cur_dir = os.path.dirname(__file__)

clf = pickle.load(open(os.path.join(cur_dir,
                 'pkl_objects',
                 'classifier.pkl'), 'rb'))
db = os.path.join(cur_dir, 'mydb.sqlite3')

update_model(db_path=db, model=clf, batch_size=10000)

# Uncomment the following lines to update your classifier.pkl file

pickle.dump(clf, open(os.path.join(cur_dir, 
            'pkl_objects', 'classifier.pkl'), 'wb')
            , protocol=4)