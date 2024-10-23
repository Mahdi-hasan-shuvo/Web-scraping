##------------------------------------#
__DEVOLPER__ = '___MAHDI HASAN SHUVO___'
__FACEBOOK__ =' MAHDI HASAN'
__DEVOLPER__ = '___MAHDI HASAN SHUVO___'
__FACEBOOK__ =  'MAHDI HASAN'
___V___= 1
__WHATSAPP___=+8801616406924
#-----------------------------------------------------------#
# from mahdix import *
# clear()
import threading
from time import sleep
import requests,re,random
import json,os
from urllib.parse import parse_qs

try:
    file=open('cookes.json','r',encoding='utf-8').read()
except:
    print('File Not Fount');exit()

lop_time=0
loping_limite=3
#def profile_scrept(user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets):

data_profile=[]
def get_profile_uid(cookies,user_name,headers):
        try:
            params = {
            'variables': '{"screen_name":"%s"}'%(user_name),
            }
            response = requests.get(
                'https://twitter.com/i/api/graphql/_pnlqeTOtnpbIL9o-fS_pg/ProfileSpotlightsQuery',
                params=params,cookies=cookies,headers=headers)
            data=(response.json())
            rest_id = data['data']['user_result_by_screen_name']['result']['rest_id']
            return rest_id 
        except : return "invaid"
def felteringx(post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post):
    try:
        #print(post_url)
        if int(reaction_numbr)>=int(reaction_limite) and int(connnt_num) >= int(comment_limite) and int(viwes) >= int(viwes_limite):  
            # print(post_url)
            data_profile.append({"post_url" : post_url,
        "date_of_post": date_post,
        "tweet": chaption,
        "likes":reaction_numbr,
        "comments": connnt_num,
        "views":viwes})
    except:pass
def scretpt(user_name,tweet_text,reaction_limite,viwes_limite,comment_limite):
    r"""
    This function parsing All data from the Responce or Inputed Text
    """
    try:
        # print(user_name)
        ddata = re.findall(f'"count":"(\d+)",(.*?)"created_at":"(.*?)",(.*?)https://twitter.com/{user_name}/status/(\d+)/(.*?)"favorite_count":(\d+),"favorited":false,"full_text":"(.*?)",(.*?),"reply_count":(\d+)', str(tweet_text))
        for viwes,xx,date_post,eccc,urx ,x,reaction_numbr, chaption ,f ,connnt_num in ddata:
            post_url=f'https://twitter.com/{user_name}/status/{urx}'
            felteringx(post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post.replace('+0000',''))            
            #data_profile.append([post_url,reaction_numbr,connnt_num,chaption,viwes])
    except Exception as e:print(e);pass


def loping(rest_id,user_name,tweet_text,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,headers):
    global messag,lop_time
    lop_time+=1
    scretpt(user_name,tweet_text,reaction_limite,viwes_limite,comment_limite)
    """
    this a lop for send request gto get more data or Scrolling
    """
    try:
        cursor=re.findall('"value":"(.*?)","cursorType',str(tweet_text))[1]
        params = {
            'variables': '{"userId":"%s","count":100,"cursor":"%s","includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}'%(rest_id,cursor),
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
        }
        response = requests.get(
            'https://twitter.com/i/api/graphql/NBWKw7od2So5qClZpLyQ0w/UserTweets',
            params=params,cookies=cookies,headers=headers,allow_redirects=False).text
        s=len(data_profile)
        if lop_time<loping_limite:
            if s > int(nb_tweets):
                messag = "Done"
                return messag
            else:
                loping(rest_id,user_name,response,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,headers)
        else:
            messag = "Done"
            return messag
    except Exception as messag: het_coookes(user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets)
    
def screpeing_profile_post(user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets):  #seach fast page and get data
    try:
        headers = {'authority': 'twitter.com',
'accept': '*/*','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
'content-type': 'application/json','referer': 'https://twitter.com/Haqiqatjou','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',#W_ueragnt(),
'x-client-transaction-id': 'BVz3kb2LqtGYEhSPp3wEynvqiYCGRff9SjF37JH8htWXjiV5EGmxJM1qfuQKTa5UksI2VwTpdzt8BMp7gReDTRzgyOj4BA',
'x-client-uuid': 'd145651c-dfcd-4e30-a8fd-abd1e72f3f86',
'x-twitter-active-user': 'yes','x-twitter-auth-type': 'OAuth2Session','x-twitter-client-language': 'en',
'x-csrf-token':cookies['ct0'] ,
            }
        data_profile.clear()
        rest_id=get_profile_uid(cookies,user_name,headers)
        if "invaid" in rest_id:
            het_coookes(user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets)
        else:
            params = {
            'variables': '{"userId":"%s","count":20,"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}'%(rest_id),
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',}
            tweet_text = requests.get(
                'https://twitter.com/i/api/graphql/NBWKw7od2So5qClZpLyQ0w/UserTweets',
                params=params,
                cookies=cookies,headers=headers).text
            with open('data_twi.txt',"w",encoding="utf-8") as file:file.write(str(tweet_text))
            thread1 = threading.Thread(target=loping, args=(rest_id,user_name,tweet_text,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,headers))
            thread1.start()
            thread1.join()
            if "Done" in messag:
                return data_profile
            else:
                return  "Something Is Wrong Or Invaid Cookes"
    except Exception as e: return e 
def het_coookes(user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets):
    r"""
    If gets any error Change a new cookes and send all data as new on searching function
    """
    formatted_cookies = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    data_list = json.loads(file)
    cookes = [entry['cookes'] for entry in data_list]
    cookes.remove(formatted_cookies)
    cooki=random.choice(cookes)
    parsed_cookies = parse_qs(cooki.replace(' ',''), separator=';')
    cookiesx= {key: value[0] for key, value in parsed_cookies.items()}
    screpeing_profile_post(user_name,cookiesx,reaction_limite,viwes_limite,comment_limite,nb_tweets)

# return screpeing_profile_post(user_name,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets)




#================================================================================================================================
#def search_Top(cookies,chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets):# This function for scrap Data from the serach by name 
search_data=[]
def felteringx(post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post):
    r"""
    from the getting data use a logic(>=) create a list of json
    """
    try:
        #print(post_url
        if int(reaction_numbr)>=int(reaction_limite) and int(connnt_num) >= int(comment_limite) and int(viwes) >= int(viwes_limite):  
            search_data.append({"post_url" : post_url,
        "date_of_post": date_post,
        "tweet": chaption,
        "likes":reaction_numbr,
        "comments": connnt_num,
        "views":viwes})
    except:pass
def parsing(tweet_text,reaction_limite,viwes_limite,comment_limite):
    r"""
    This function parsing All data from the Responce or Inputed Text
    """ 
    try:
        ddata = re.findall(f'"count":"(.*?)",(.*?)"created_at":"(.*?)",(.*?)"expanded_url":"(https://twitter.com/.*?/status/.*?)/(.*?)"favorite_count":(\d+),"favorited":false,"full_text":"(.*?)",(.*?),"reply_count":(\d+)', str(tweet_text).strip())
        for viwes,xx,date_post,eccc,post_url ,x,reaction_numbr, chaption ,f ,connnt_num in ddata:
            felteringx(post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite,date_post.replace('+0000',''))
    except:pass

def loping_serch(tweet_text,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,chatagory,headers):
    parsing(tweet_text,reaction_limite,viwes_limite,comment_limite)
    global messag,lop_time
    lop_time+=1
    """
    this a lop for send request gto get more data or Scrolling
    """
    try:
        cursor=re.findall('"TimelineTimelineCursor","value":"(.*?)","cursorType',str(tweet_text))[1]
        params = {
        'variables': '{"rawQuery":"%s","count":50,"cursor":"%s","querySource":"recent_search_click","product":"Top"}'%(chatagory,cursor),
        'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
        }
        response = requests.get('https://twitter.com/i/api/graphql/PaIcTAgMdfWySgs3aVU5TA/SearchTimeline', params=params,cookies=cookies,headers=headers,).text
        s=len(search_data)
        if lop_time<loping_limite:
            if s >= int(nb_tweets):
                messag = "Done"
                return messag
            else:
                loping_serch(response,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,chatagory,headers)
        else:messag = "Done"    
    except Exception as e: 
        het_coookes(chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets)
        return e

def het_coookes(chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets,cookes_od):
    r"""
    If gets any error Change a new cookes and send all data as new on searching function
    """
    formatted_cookies = ";".join([f"{cookie['name']}={cookie['value']}" for cookie in cookes_od])
    data_list = json.loads(file)
    cookes = [entry['cookes'] for entry in data_list]
    cookes.remove(formatted_cookies)
    cooki=random.choice(cookes)
    parsed_cookies = parse_qs(cooki.replace(' ',''), separator=';')
    cookiesx= {key: value[0] for key, value in parsed_cookies.items()}
    search_Top(cookiesx,chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets)

def search_Top(cookies,chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets):
    search_data.clear()
    headers = {'authority': 'twitter.com',
    'accept': '*/*','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json','referer': 'https://twitter.com/Haqiqatjou','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',#W_ueragnt(),
    'x-client-transaction-id': 'BVz3kb2LqtGYEhSPp3wEynvqiYCGRff9SjF37JH8htWXjiV5EGmxJM1qfuQKTa5UksI2VwTpdzt8BMp7gReDTRzgyOj4BA',
    'x-client-uuid': 'd145651c-dfcd-4e30-a8fd-abd1e72f3f86',
    'x-twitter-active-user': 'yes','x-twitter-auth-type': 'OAuth2Session','x-twitter-client-language': 'en',
    'x-csrf-token':cookies['ct0'] ,
            }
    params = {
    'variables': '{"rawQuery":"%s","count":200,"querySource":"recent_search_click","product":"Top"}'%(chatagory),
    'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
    }
    response = requests.get('https://twitter.com/i/api/graphql/HgiQ8U_E6g-HE_I6Pp_2UA/SearchTimeline',
        params=params,cookies=cookies,headers=headers,).text
    with open('data_twi.json',"w",encoding="utf-8") as file:
        json_data = json.dump(response ,file ,ensure_ascii=False, indent=4)
        file.close()
    exit()
    loping_serch(response,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets,chatagory,headers)

    if "Done" in messag:
        return search_data
    else:
        return "Something Is Wrong Or Invaid Cookes"
    
    #return search_Top(cookies,chatagory,reaction_limite,viwes_limite,comment_limite,nb_tweets)




#xx=search_Top(cookies,keywords,reaction_limite,viwes_limite,comment_limite,nb_tweets)
# chatagory='global warming'               # keyword name wich are scraping
nb_tweets=2                     # the number of data you want
reaction_limite=5
viwes_limite=5
comment_limite=3
keywords=["munawar0018","therantinggola","therantinggola","therantinggola","therantinggola"]
type_search='pro'


def cookes(x):
    global cookies
    data_list = json.loads(file)
    cookes = [entry['cookes'] for entry in data_list]
    cooki=random.choice(cookes)
    parsed_cookies = parse_qs(cooki.replace(' ',''), separator=';')
    cookies= {key: value[0] for key, value in parsed_cookies.items()}
@cookes
def c():pass
def main(type_search, keywords, reaction_limite,viwes_limite,comment_limite,nb_tweets):
    tweets = []
    for keyword in keywords:
        # try:
            if 'profile' in str(type_search).lower():
                try:
                    sleep(.5)
                    tweet=screpeing_profile_post(keyword,cookies,reaction_limite,viwes_limite,comment_limite,nb_tweets)
                    #print(tweet)
                    new_data = [{
                        "type": "username",
                        "keyword": keyword,
                        "tweets": []
                    }]
                    new_data[0]["tweets"].extend(tweet)
                    tweets.extend(new_data)
                except:pass
                    #return data_profile
            else:
                try:
                    tweet=search_Top(cookies,keyword,reaction_limite,viwes_limite,comment_limite,nb_tweets)
                    new_data = [{
                        "type": "topic",
                        "keyword": keyword,
                        "tweets": []
                    }]
                    new_data[0]["tweets"].extend(tweet)
                    tweets.extend(new_data)
                except:pass
            #tweets += [tweet]
        # except Exception as e :print(e)
    return tweets

new_data=main(type_search, keywords, reaction_limite,viwes_limite,comment_limite,nb_tweets)
print(new_data)

with open('data_twi.json',"w",encoding="utf-8") as file:
        json_data = json.dump(new_data ,file ,ensure_ascii=False, indent=4)
        file.close()

