from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
import datetime

import MovieClassifier3.forms as CustomForms
from django.core.mail import send_mail

from django.template import loader, RequestContext

# import update function from local dir
from update import update_model

# import HashingVectorizer from local dir
from vectorizer import vect

import pickle
import sqlite3
import os
import numpy as np
import pdb


######## Preparing the Classifier
cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, '..', 'pkl_objects/classifier.pkl'), 'rb'))
db = os.path.join(cur_dir,  '..', 'mydb.sqlite3')



def classify(document):
    label = {0: 'negative', 1: 'neutral', 2: 'positive'}
    X = vect.transform([document])
    y = clf.predict(X)[0]
    allproba = clf.predict_proba(X)
    proba = np.max(allproba)
    return label[y], proba, allproba

classrange = np.array([0, 1, 2])
def train(document, y):
    X = vect.transform([document])
    clf.partial_fit(X, [y], classes=classrange)
    
def sqlite_entry(path, document, y):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("INSERT INTO sentiment_review(review, sentiment, date) "\
    " VALUES (?, ?, DATETIME('now'))", (document, y))
    conn.commit()
    conn.close()



""" """
# @app.route('/')
def index(request):
    return HttpResponse("TEST")


def review_form(request):
    if request.method == 'POST':
        form = CustomForms.ReviewForm(request.POST)
        if form.is_valid():
            return sentiment_form(request)
    else:
        form = CustomForms.ReviewForm(
            initial={'review': 'I LOVE YOUR MOVIE!'}
        )
    return render(request, 'reviewform.html', {'form':form}) 
            


    
def sentiment_form(request):
    if request.method == 'POST':
        form = CustomForms.ReviewForm(request.POST)
        if form.is_valid():
#            cd = form.cleaned_data
            review = request.POST.get("review")
            y, proba, allproba = classify(review)
            probability = round(proba*100,2)
            proba1 = round(allproba[0,0]*100,2)
            proba2 = round(allproba[0,1]*100,2)
            proba3 = round(allproba[0,2]*100,2)
            return render(request, 'sentimentform.html', {'review': review, 'prediction': y, 'probability': probability,
                                                          'proba1': proba1, 'proba2': proba2, 'proba3': proba3})

def forward_sentiment(request):
#    pdb.set_trace()
    if request.method == 'POST':
        form = CustomForms.ReviewForm(request.POST)
        if form.is_valid():
            feedback = request.POST.get('feedback_button')
#            review = request.POST.get('review')
#            prediction = request.POST.get('prediction')
            
            if feedback == 'Incorrect':
                return sentiment_evaluation(request)
            else:
                return thanks(request)
    
            
   
def sentiment_evaluation(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        prediction = request.POST.get('prediction')
        return render(request, 'sentimentevaluation.html', {'review': review, 'prediction': prediction})


def thanks(request):
    if request.method == 'POST':
#        form = CustomForms.ReviewForm(request.POST)
#        if form.is_valid():
#            cd = form.cleaned_data
        review = request.POST.get('review')
        prediction = request.POST.get('prediction')
        
        inv_label = {'negative':0,'neutral':1, 'positive':2}
        y = inv_label[prediction]

        train(review, y)
        sqlite_entry(db, review, y)
#        update_model(db_path=db, model=clf, batch_size=10000)
#        message = "Sentiment: " + str(y) + " The review '" + review + "' has been uploaded to the database"
        message = ""
    return render(request, 'thanks.html', {'message': message})
    

    
    
    
""" References"""
def testnavpage(request):
    return render(request, 'testnavpage.html', {'title': "Prototype navigation page", 'current_section': datetime.datetime.now()})
    
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': next_time})

    

# View (in reviews/views.py)
def page(request, num="1"):
    # Output the appropriate page of review entries, according to num.
    return HttpResponse('Default View Based on Arguments. This is page ' + num)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form':form})

   