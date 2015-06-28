import sqlite3 as sql
import numpy as np

conn = sql.connect('lda_50bins_1/doc_topics.db')
c = conn.cursor()
c.execute('''CREATE TABLE doc(id TEXT, topicid INTEGER, proportion SINGLE);''')
conn.commit()

f = open('lda_data_6_24/lda_50bins_1/doc_topics.txt', 'r');

conn = sql.connect('lda_data_6_24/lda_50bins_1/doc_topics.db')
c = conn.cursor()

for line in f:
    a = line
    b = a.strip('\n').split('\t')
    title = b[1].split("/")[-1].rstrip('.abs')
    if len(title) < 8:
        title = 'cond-mat/' + title
    title
    singles = [single(i) for i in b[2:]]
    for i in range(50):
        c.execute("""insert or ignore into doc values""" + \
                str(tuple([title] +[i, singles[i]])))
f.close()
conn.commit()