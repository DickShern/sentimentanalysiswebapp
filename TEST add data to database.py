import sqlite3
import os
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
#c.execute('CREATE TABLE sentiment_'\
#' (review TEXT, sentiment INTEGER, date TEXT)')
example1 = 'I love this movie'
c.execute("INSERT INTO sentiment_review"\
" (review, sent_good, sent_neutral, sent_bad, date) VALUES"\
" (?, ?, ?, ?, DATETIME('now'))", (example1, 0.9,0.1,0))
example2 = 'I disliked this movie'
c.execute("INSERT INTO sentiment_review"\
" (review, sent_good, sent_neutral, sent_bad, date) VALUES"\
" (?, ?, ?, ?, DATETIME('now'))", (example2, 0,0.05,0.95))
conn.commit()
conn.close()