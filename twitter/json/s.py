##------------------------------------#
__DEVOLPER__ = '___MAHDI HASAN SHUVO___'
__FACEBOOK__ =' MAHDI HASAN'
__DEVOLPER__ = '___MAHDI HASAN SHUVO___'
__FACEBOOK__ =  'MAHDI HASAN'
___V___= 1
__WHATSAPP___=+8801616406924
#-----------------------------------------------------------#
# from mahdix import *
import datetime

import json,os
from mahdix import *
clear()
reaction_limite,viwes_limite,comment_limite=1,1,1
def felteringx(post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post):
    r"""
    from the getting data use a logic(>=) create a list of json
    """
    try:
        #print(post_url
        if int(reaction_numbr)>=int(reaction_limite) and int(connnt_num) >= int(comment_limite) and int(viwes) >= int(viwes_limite):  
            print({"post_url" : post_url,
        "date_of_post": date_post,
        "tweet": chaption,
        "likes":reaction_numbr,
        "comments": connnt_num,
        "views":viwes})
    except:pass
file_op=open('data_twixxxxxxxxx.json','r',encoding='utf-8').read()
loads_data=json.loads(file_op)
entry_id = loads_data["data"]["search_by_raw_query"]["search_timeline"]["timeline"]["instructions"][0]["entries"]
for data in entry_id:
    try:
        date_post=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["created_at"]
        connnt_num=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["reply_count"]
        chaption=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["full_text"]
        reaction_numbr=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["favorite_count"]
        viwes=data["content"]["itemContent"]["tweet_results"]["result"]["views"]["count"]
        post_url=data["content"]["itemContent"]["tweet_results"]["result"]["legacy"]["entities"]["media"][0]["expanded_url"]
        felteringx(post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post)
    except:pass

