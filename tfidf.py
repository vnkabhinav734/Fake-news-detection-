from bs4 import BeautifulSoup
import requests
import re

import math
from .CountWords import CountWords
import sys


class TFIDF:

    def process(url, kwd):
        
        print('***********'+kwd)
        d = 0
        try:

            print("in process",url)
            # kwd= "python java"
            html = ""
            text = ""
            try:
                html = requests.get(url).content
                #1 Recoding
                unicode_str = html.decode("utf8")
                encoded_str = unicode_str.encode("ascii",'ignore')
                news_soup = BeautifulSoup(encoded_str, "html.parser")
                a_text = news_soup.find_all('p')
                #2 Removing
                y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
                html=y
            except:
                pass
            for h in html:
                text=text+" "+h

            
            #print(text)

            d = TFIDF.main(text, kwd)

        except Exception as e:
            print("try1")
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        return d


    def main(stmnts, cont):
        d = 0
        try:

            l = len(stmnts)
            tot = 0
            for w in cont.split():
                print('>>>>>>>>>>>>',w)
                c = CountWords.countOccurences(stmnts, w)
                print('CCCCCCCCCCCCCCCCC',c)
                tot = tot + c

            tot = tot / l
            idf = math.log(l)
            d = tot * idf



        except Exception as e:
            print("trY3")
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        print(d)
        return d


if __name__ == "__main__":
    r = TFIDF.process("https://www.ndtv.com/topic/bjp-modi",'modi')
    print(r)
