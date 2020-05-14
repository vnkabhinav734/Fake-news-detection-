from collections import Counter
from bs4 import BeautifulSoup
import requests
import re
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

import math

import sys


tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    

class LDA:

    def process(url, kwd):
        kwd = kwd.lower()
        tokens = tokenizer.tokenize(kwd)
        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in en_stop]
        # stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        # add tokens to list
        keytokens = stemmed_tokens
        #print(keytokens)

        #print('***********' + kwd)
        d = 0
        try:

            print("in process", url)
            # kwd= "python java"
            html = ""
            text = ""
            try:
                html = requests.get(url).content
                # 1 Recoding
                unicode_str = html.decode("utf8")
                encoded_str = unicode_str.encode("ascii", 'ignore')
                news_soup = BeautifulSoup(encoded_str, "html.parser")
                a_text = news_soup.find_all('p')
                # 2 Removing
                y = [re.sub(r'<.+?>', r'', str(a)) for a in a_text]
                html = y
            except:
                pass
            doc=''
            for stmt in html:
                doc=doc+" "+stmt
            
            p_t_d = LDA.main(doc, keytokens)
#ptd is topic in document
            res=0.0
            for stmt in html:
                #print(type(stmt))
                #pwd is word in topic
                p_w_d = LDA.main(stmt, keytokens)
                res=res+(p_w_d*p_t_d)

            print(res)



        except Exception as e:
            print("try1")
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        return res

    def main(stmnt, keytokens):
        raw = stmnt.lower()
        tokens = tokenizer.tokenize(raw)
        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in en_stop]
        # stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        # add tokens to list
        tokens = stemmed_tokens
        counts = Counter(tokens)
        #print(counts)
        tot = 0
        for x in counts.values():
            tot = tot + x
        t = 1
        for w in keytokens:
            if w in counts.keys():
                t = t * counts.get(w)
                #print(w,'----',counts.get(w))
            else:
                t=0
        r=0
        try:
            r=t / tot
        except:
            pass
        return r


if __name__ == "__main__":
    r = LDA.process("https://www.ndtv.com/topic/bjp-modi", 'modi bjp')
    print(r)
