import re,os
from time import sleep
from requests import Session ,get,post
from re import search,findall
from json import loads,dumps,dump
from random import choice
from mahdix import clear
from uuid import uuid4
from logging import basicConfig ,getLogger,exception
basicConfig(level=20, format='%(asctime)s - %(levelname)s - %(message)s')
logger = getLogger(__name__)
logger.propagate = False

clear()
# os.environ['ALL_PROXY'] = "socks5h://3Ixf4HKMEZ-zone-star-region-US:39179679@na.a79a246354fe7beb.abcproxy.vip:4950"


__formate_coki__ = lambda x: {cookie.split('=', 1)[0].strip(): cookie.split('=', 1)[1].strip() for cookie in x.split(';') if '=' in cookie}
cookies_list=[
'g_state={"i_l":0}; kdt=jGNElafmEcYga174fbaTkgItLZjh6EJNwyUPzbkm; cf_clearance=24IGAlS3H3jEHsWm3XZ5h2gieQNYVByw6A.ro2Pb._s-1745870549-1.2.1.1-78pbifCXMJrnqGD7r.QHTihL269AQTRtfwLcD.DzLiruaztteHzgk7tCwI4k64NDtSkU49TgP5qU1_5khlED5asSU6Iw78hG9qf8SCk22zzFn34xTBALdVmZVKjfBH9k5clWD6.V4f9NNcpmhkVUXscrT4TPTTzxhnJVdGTMZdC9sbvUWgin6Ti5Al9iGp2vT5byPBu6hyYsDKmTy7sDcCCX2kTBCEzP8.k.NRAidHzS.05MVTqFMegEIPR3zotzfHe_t5JaiBB1wQeAnPfQ1i2tDbfGnrHEmluQ1bNWLGrFto7m3ybgO0WxrFcyx9rRdyFH4G3_VPF4T9_9ezALsnJK99PWQnbXuEoh7EPbftzQh8RfdYiuJ7uq6uCHBmGd; dnt=1; guest_id=v1%3A174603111800362173; guest_id_marketing=v1%3A174603111800362173; guest_id_ads=v1%3A174603111800362173; personalization_id="v1_sF8xh1p63hlu4ja54j590w=="; auth_token=aa65c4df197c9b3ce824519284d31e337c9faad0; ct0=228432fd730eb3828b7262a36b7f0b063db8126bf29608f9e69782de9d1a82bada4bc67aa3550b6d5db1b08c060c9d87b4f9c59a302e729207cd15afa5d6baaf0659fb2b35bef0914df2e579fee19172; twid=u%3D1754223523516784640; lang=en; _twitter_sess=BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74; __cf_bm=BsNk3RRcO7YQq6nddg9OBZ8rr0Sl9m1uICWoDcUIdIU-1746188069-1.0.1.1-MpVbkvUAtrjhsoUq8VX0qJkyCIJNl3JNQKCd4viRWb3wWuk91lWS82KwMd7HyWDYEAWmpPYDOg2RzxOTwGewuGjJBNRhWZGOxGWdkpW0wuI'

#'guest_id_marketing=v1%3A174587032162439099; guest_id_ads=v1%3A174587032162439099; guest_id=v1%3A174587032162439099; personalization_id="v1_VoSs3SOWPUihzw3IynwktQ=="; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; g_state={"i_l":0}; kdt=jGNElafmEcYga174fbaTkgItLZjh6EJNwyUPzbkm; auth_token=738b96b25e7d0428584bc847ece66b9148a7cb16; ct0=96ecda9f54d7c41ba54365eea5bfc01ff9d83ecd6ea5bbd14b0698b9c890faeeb0f74728f5b9fc863a6577915acb7bc81860b633ccaa3014c3f6a9edf1faa2fbd13a8eeb9c2b70da81084ba20d90fb60; twid=u%3D1908186837774180352; cf_clearance=24IGAlS3H3jEHsWm3XZ5h2gieQNYVByw6A.ro2Pb._s-1745870549-1.2.1.1-78pbifCXMJrnqGD7r.QHTihL269AQTRtfwLcD.DzLiruaztteHzgk7tCwI4k64NDtSkU49TgP5qU1_5khlED5asSU6Iw78hG9qf8SCk22zzFn34xTBALdVmZVKjfBH9k5clWD6.V4f9NNcpmhkVUXscrT4TPTTzxhnJVdGTMZdC9sbvUWgin6Ti5Al9iGp2vT5byPBu6hyYsDKmTy7sDcCCX2kTBCEzP8.k.NRAidHzS.05MVTqFMegEIPR3zotzfHe_t5JaiBB1wQeAnPfQ1i2tDbfGnrHEmluQ1bNWLGrFto7m3ybgO0WxrFcyx9rRdyFH4G3_VPF4T9_9ezALsnJK99PWQnbXuEoh7EPbftzQh8RfdYiuJ7uq6uCHBmGd; dnt=1; att=1-kvIggNlhtOzM6dtCg0XR6gBJdCplzb5pPSwSyb4s; lang=en; _twitter_sess=BAh7BiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7AA%253D%253D--1164b91ac812d853b877e93ddb612b7471bebc74; __cf_bm=6zjmxA5iEAMvyyu9v4w062CQItL77cFFJGpowaj4Gs0-1746030812-1.0.1.1-x3CMU3B._uFgmKODMPLMyhUnnERgWF6B8Ik2ox1bpon4zEhe_vbVZIDe.9lXdlxuWE.8x6Q5P4GeclahvtDTSVneq2YJaa4cstuJhqeW9S5RER35E9zig7qg5fTvg.Nj'
              ] # list of cookies


class TwitterSearchTimeline:
    def __init__(self):
        self.headers  = {
'accept': '*/*','accept-language': 'en-US,en;q=0.9',
'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
'cache-control': 'no-cache','content-type': 'application/json','dnt': '1','pragma': 'no-cache','priority': 'u=1, i','referer': 'https://x.com/search?q=chrepto&src=recent_search_click',
'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"','sec-ch-ua-arch': '"x86"','sec-ch-ua-bitness': '"64"','sec-ch-ua-full-version': '"135.0.7049.115"','sec-ch-ua-full-version-list': '"Google Chrome";v="135.0.7049.115", "Not-A.Brand";v="8.0.0.0", "Chromium";v="135.0.7049.115"',
'sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"',
'sec-ch-ua-platform-version': '"19.0.0"','sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
'x-client-transaction-id': 'vXQIrp6Wng0rgEYBD1107o3MWxJHxA9thn03YRjoiTvM/wV/8eex8Gal8itOWZT54Nn8eL5u629H2PbGkRN1QpYqmoJ3vg',
'x-client-uuid': str(uuid4()),
'x-twitter-active-user': 'yes','x-twitter-auth-type': 'OAuth2Session','x-twitter-client-language': 'en',
        }
        self.params={'features': dumps({"rweb_video_screen_enabled":False,"profile_label_improvements_pcf_label_in_post_enabled":True,"rweb_tipjar_consumption_enabled":True,"verified_phone_label_enabled":False,"creator_subscriptions_tweet_preview_api_enabled":True,"responsive_web_graphql_timeline_navigation_enabled":True,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":False,"premium_content_api_read_enabled":False,"communities_web_enable_tweet_community_results_fetch":True,"c9s_tweet_anatomy_moderator_badge_enabled":True,"responsive_web_grok_analyze_button_fetch_trends_enabled":False,"responsive_web_grok_analyze_post_followups_enabled":True,"responsive_web_jetfuel_frame":False,"responsive_web_grok_share_attachment_enabled":True,"articles_preview_enabled":True,"responsive_web_edit_tweet_api_enabled":True,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":True,"view_counts_everywhere_api_enabled":True,"longform_notetweets_consumption_enabled":True,"responsive_web_twitter_article_tweet_consumption_enabled":True,"tweet_awards_web_tipping_enabled":False,"responsive_web_grok_show_grok_translated_post":False,"responsive_web_grok_analysis_button_from_backend":True,"creator_subscriptions_quote_tweet_preview_enabled":False,"freedom_of_speech_not_reach_fetch_enabled":True,"standardized_nudges_misinfo":True,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":True,"longform_notetweets_rich_text_read_enabled":True,"longform_notetweets_inline_media_enabled":True,"responsive_web_grok_image_annotation_enabled":True,"responsive_web_enhance_cards_enabled":False}),
            } 
    def filter_search(self,response_json, return_data, reaction_count, comment_count, views_count,search_timeline=True):
        try:
            if search_timeline == True:
                entries = response_json["data"]["search_by_raw_query"]["search_timeline"]["timeline"]["instructions"][0]["entries"]
            if search_timeline == False:
                instructions = response_json["data"]["user"]["result"]["timeline"]["timeline"]["instructions"]
                entries = next((i.get("entries") for i in instructions if "entries" in i), [])
                # entries = response_json["data"]["user"]["result"]["timeline"]["timeline"]["instructions"][1]["entries"]
            for entry in entries:
                if "tweet" not in entry["entryId"] or "promoted-tweet" in entry["entryId"]:
                    continue
                try:
                    result = entry["content"]["itemContent"]["tweet_results"]["result"]
                    legacy = result["legacy"]
                    post_id = legacy["id_str"]
                    post_url = (
                        legacy.get("entities", {}).get("media", [{}])[0].get("expanded_url") or
                        legacy.get("extended_entities", {}).get("media", [{}])[0].get("expanded_url") or
                        f"https://x.com/topics/status/{post_id}"
                    )
                    views = result.get("views", {}).get("count", 0)
                    print(views)
                    if int(legacy["favorite_count"]) >= int(reaction_count) and int(legacy["reply_count"]) >= int(comment_count) and int(views) >= int(views_count):
                        return_data.append({
                            "post_id": post_id,
                            "post_url": post_url,
                            "date_of_post": legacy["created_at"],
                            "tweet": legacy["full_text"],
                            "likes": legacy["favorite_count"],
                            "comments": legacy["reply_count"],
                            "views": views
                        })
                except Exception:
                    print(entry.get("entryId"))
                    continue
        except Exception as e:
            print(e)
    def send_request(self,params,cookies,headers,quary='AIdc203rPpK_k_2KWSdm7g/SearchTimeline'):
        url =  'https://x.com/i/api/graphql/{}'.format(quary)
        return get(url, params=params, cookies=cookies, headers=headers)
    def TwitterSearchTimeline(self,query:str,count:int,reaction_count:int,views_count:int,comment_count:int,product='Top',number_lop=5):
        """This function is used to get search timeline from twitter
        rgs:
            query (str): Seach query
            count (int): Total count of tweets
            reaction_count (int): menimum reaction
            views_count (int):  minimum views
            comment_count (int):  minimum comments  
            product (str, optional): _description_. Defaults to 'Top' or 'Latest' 'People'.
            number_lop (int, optional): The lop times to get tweets. Defaults to 5.

        Returns:
             List: return data as lisf of  "post_id","post_url","date_of_post","tweet","likes","comments","views";
        """
        try:
            return_data=[] # list of data
            chuse_cookes=__formate_coki__(choice(cookies_list).replace(' ', '')) # random cookies
            # Print any error that occurs
            self.headers['x-csrf-token'] = chuse_cookes['ct0'] # csrf token
            self.params['variables']= dumps({"rawQuery":query,"count":50,"querySource":"recent_search_click","product":product})
          
            response = self.send_request(self.params,chuse_cookes,self.headers)
            if response.status_code == 200 and response.text.strip().startswith('{'):
                data = response.json()
                self.filter_search(data, return_data, reaction_count, comment_count, views_count)
                # print('------------------------------')
                for _ in range(number_lop):
                    try:
                        if len(return_data) >= count:
                            break
                        cursor = re.findall(r'"TimelineTimelineCursor","value":"(.*?)","cursorType', response.text)[1]
                        self.headers['x-client-transaction-id'] = 'GdCsCjoyOqmPJOKlq/nQSilo/7bjYKvJItmTxbxMLZ9oW6HbVUMVVMIBVo/q/TBdRH1S3BpH3WUQk9n04XIeT3BkqAJOGg'
                        self.params['variables']=dumps({"rawQuery":query,"count":20,"cursor":cursor,"querySource":"typed_query","product":"Top"})
                        response = self.send_request(self.params,chuse_cookes,self.headers)
                        if response.status_code == 200 and response.text.strip().startswith('{'):
                            # print( response.text )
                            data = response.json()
                            self.filter_search(data, return_data, reaction_count, comment_count, views_count)
                            # print('------------------------------')
                        if response.status_code != 200:
                            print(f'error and your status code : {response.status_code}')
                            self.TwitterSearchTimeline(query,count,reaction_count,views_count,comment_count,product,number_lop)
                    except Exception as e:
                        exception(f"error in TwitterSearchTimeline function {e}")
                        print(e)
                        sleep(2)
                        continue
            if response.status_code != 200:
                print(f'error and your status code : {response.status_code}')
                self.TwitterSearchTimeline(query,count,reaction_count,views_count,comment_count,product,number_lop)
        except Exception as e:
            exception(f"error in TwitterSearchTimeline function {e}")
            # print(e)
            sleep(1)
            self.TwitterSearchTimeline(query,count,reaction_count,views_count,comment_count,product,number_lop)
        except Exception as e:
            exception(f"error in profile_search function {e}")
            print(e)
        return return_data
            
class twter_profile(TwitterSearchTimeline):
    def __init__(self):
        super().__init__()
    def ge_profile_uid(self,cookies, headers, user_name):
        try:
            url = 'https://x.com/i/api/graphql/-0XdHI-mrHWBQd8-oLo1aA/ProfileSpotlightsQuery'
            params = {'variables': dumps({"screen_name": user_name})}
            res = get(url, params=params, cookies=cookies, headers=headers).json()
            return res['data']['user_result_by_screen_name']['result']['rest_id']
        except:
            return None
    def profile_search(self, user_name:str,count:int, reaction_count:int, views_count:int, comment_count:int, number_lop=5):
        try:
            """
            This function is used to get search User profile from twitter
            rgs:
                user_name (str): Seach query
                count (int): Total count of tweets
                reaction_count (int): menimum reaction
                views_count (int):  minimum views
                comment_count (int):  minimum comments  
                number_lop (int, optional): The lop times to get tweets. Defaults to 5.

            Returns:
                List: return data as lisf of  "post_id","post_url","date_of_post","tweet","likes","comments","views";
      
            """
            return_data=[]
            chuse_cookes=__formate_coki__(choice(cookies_list).replace(' ', '')) # random cookies
            self.headers['x-csrf-token'] = chuse_cookes['ct0'] # csrf token
            self.headers['x-client-transaction-id']= 'DSYpPVXK+eqbdVrvrlbIW/GsEJ9RCIQqhycPLmkhQN321un5NFTiaLhBlFl2JGM8ADl9yw6v6RILz0Ejo1nc4ntysBg5Dg'
            uid = self.ge_profile_uid(chuse_cookes, self.headers, user_name)
            if uid:
                self.params['variables'] = dumps({"userId":uid,"count":20,"includePromotedContent":True ,"withQuickPromoteEligibilityTweetFields":True,"withVoice":True})
                response = self.send_request(self.params, chuse_cookes, self.headers,quary='La9DvhvQhyCQeRGRZRkpHA/UserTweets')
                if response.status_code == 200 and response.text.strip().startswith('{'):
                    data = response.json()
                    self.filter_search(data, return_data, reaction_count, comment_count, views_count,search_timeline=False)
                    # print('------------------------------')
                    for _ in range(number_lop):
                        try:
                            if len(return_data) >= count:
                                break
                            cursor = re.findall(r'"TimelineTimelineCursor","value":"(.*?)","cursorType', response.text)[1]
                            self.headers['x-client-transaction-id'] = 'AikmMlrF9uWUelXgoVnHVP6jH5BeB4sliCgAIWYuT9L52eb2O1vtZ7dOm1Z5K2wzD/1xxAHOYVrEHQXBNfOr1sHuIzoOAQ'
                            self.params['variables']=dumps({"userId":"3247896487","count":20,"cursor":cursor,"includePromotedContent":True,"withQuickPromoteEligibilityTweetFields":True,"withVoice":True})
                            response = self.send_request(self.params, chuse_cookes, self.headers,quary='La9DvhvQhyCQeRGRZRkpHA/UserTweets')
                            if response.status_code == 200 and response.text.strip().startswith('{'):
                                data = response.json()
                                self.filter_search(data, return_data, reaction_count, comment_count, views_count,search_timeline=False)
                                # print('------------------------------')
                            if response.status_code != 200:
                                print(f'error and your status code : {response.status_code}')
                                self.profile_search(user_name, count, reaction_count, views_count, comment_count, number_lop)
                        except Exception as e:
                            print( f' error in profile_search function {e}' )
                            sleep(2)
                            continue

                if response.status_code != 200:
                    print(f'error and your status code : {response.status_code}')
                    self.profile_search(user_name, count, reaction_count, views_count, comment_count, number_lop)
        except Exception as e:
            exception(f"error in profile_search function {e}")
            return e

        return return_data






ck=twter_profile()
def main(search_topi:list,count,reaction_count,views_count,comment_count,mathods='TwitterSearchTimeline',number_lop=5):
    tweets = []
    for user_name in search_topi:
        if mathods == 'profile_search':
            responce= ck.profile_search(user_name,count,reaction_count,views_count,comment_count,number_lop)
        elif mathods == 'TwitterSearchTimeline':
            responce= ck.TwitterSearchTimeline(user_name,count,reaction_count,views_count,comment_count,number_lop)
        new_data = [{
            "type": "profile",
            "keyword": user_name,
            "tweets": []
            }]
        new_data[0]["tweets"].extend(responce)
        tweets.extend(new_data)

    return tweets


responce=main(['imVkohli','ProthomAlo'],10,100,100,100,mathods='profile_search',number_lop=5)
print(responce)
# open( "responce.json", "w", encoding="utf-8" ).write(dumps(responce))
with open(f'data_twi.json',"w",encoding="utf-8") as file:
    json_data = dump(responce ,file ,ensure_ascii=False, indent=4)
    file.close()
