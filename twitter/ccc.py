import requests,re
from mahdix import *
clear()

from urllib.parse import parse_qs

cooki='personalization_id="v1_sUAC3o+qvxM+zPRuyWa3QA==";lang=en;att=1-frUAoDnsqF8IGKqWl4FZzIOcgHdhtw8fHyxsT7QI;auth_token=2d68ccde77528c26463b9f9cbe1f0bebd6c78dea;ct0=a09c0139e2b163c1285e16b63b23b67f4f543ad7dc674bb34956a74923550bc7fe933e7be2d95fad78c517b8a738acb4b599e913aead39907b5b78990b1607aa43a2999ef0ea0afc83041428b7b26676;gt=1748065858096922678;_ga=GA1.2.1089818166.1705606352;kdt=Y7G0SNho8dSdeb7MvzDIOgXQarn1RRAwb4DeALJZ;_gid=GA1.2.1402223699.1705606352;twid=u%3D1745514902863929344;guest_id=v1%3A170560635269511367;guest_id_ads=v1%3A170560635269511367;_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCHWcDx6NAToMY3NyZl9p%250AZCIlMjIzZjAwNmNiZWJiMjE0MWU3Y2E2YTQyMzk4MDRjYzM6B2lkIiU3OGZh%250AYmI2ZTVlOWNhZjNiODM5ZmUwOWFjMTgxMzIwNw%253D%253D--3873fa7740a9701f16f8d47a39f22614aa545339;guest_id_marketing=v1%3A170560635269511367'


parsed_cookies = parse_qs(cooki.replace(' ',''), separator=';')

# Convert values from lists to strings
cookies= {key: value[0] for key, value in parsed_cookies.items()}


headers = {
    'authority': 'twitter.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'referer': 'https://twitter.com/Haqiqatjou',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': W_ueragnt(),
    'x-client-transaction-id': 'BVz3kb2LqtGYEhSPp3wEynvqiYCGRff9SjF37JH8htWXjiV5EGmxJM1qfuQKTa5UksI2VwTpdzt8BMp7gReDTRzgyOj4BA',
    'x-client-uuid': 'd145651c-dfcd-4e30-a8fd-abd1e72f3f86',
    'x-csrf-token':cookies['ct0'] ,
    'x-twitter-active-user': 'yes',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
}




def feltering(post_url,reaction_numbr,connnt_num,chaption,viwes,reaction_limite,viwes_limite,comment_limite):
    try:
        if int(reaction_numbr)>=int(reaction_limite) and int(connnt_num) >= int(comment_limite) and int(viwes) >= int(viwes_limite):
            print(f"post_url : {post_url}")             # Post Url
            print(f"Reaction : {reaction_numbr}")       # Post Number of Reaction
            print(f"Post Text : {chaption}")            # Post description
            print(f"Number Comment : {connnt_num}")     # Post Number of Comment
            print(f"{LI_YELLOW}Number views : {LI_WHITE}{viwes}")   # Post Number of Reach or viwes
            print(mahdilinx())

    except:pass
like_liite=20
viwes_limite=50
comment_limite=15


class scrap_profile:         # This class for scrap Data from Profile use any user name
    data_profile=[]
    def __init__(self):
        pass
    def get_profile_id(self,user_name,cookies):
        try:
            params = {
            'variables': '{"screen_name":"%s"}'%(user_name),
            }
            response = requests.get(
                'https://twitter.com/i/api/graphql/_pnlqeTOtnpbIL9o-fS_pg/ProfileSpotlightsQuery',
                params=params,cookies=cookies,headers=headers,)
            data=(response.json())
            rest_id = data['data']['user_result_by_screen_name']['result']['rest_id']
            return rest_id 
        except : return "user name or cookes invaid"
    def scretpt(self,user_name,tweet_text):
        
        """
        This function parsing All data from the Responce or Inputed Text
        """
        try:
            data = re.findall(f'"count":"(.*?)",(.*?)https://twitter.com/{user_name}/status/(.*?)/(.*?)"favorite_count":(\d+),"favorited":false,"full_text":"(.*?)",(.*?),"reply_count":(\d+)', str(tweet_text).strip())
            for viwes,xx,urx ,x,reaction_numbr, chaption ,f ,connnt_num in data:
                post_url=f'https://twitter.com/{user_name}/status/{urx}'
                # print(f'{LI_WHITE}url : {LI_YELLOW}{post_url}')
                # print(f"{LI_WHITE}Reaction: {reaction_numbr}")
                # print(f"{LI_WHITE}comment Number : {connnt_num}")
                # print(f"{LI_WHITE}Descreption:{chaption}")
                # print(f"Number views : {viwes}")
                self.data_profile.append([post_url,reaction_numbr,connnt_num,chaption,viwes])
        except Exception as e:print(e);pass
    def loping(self,rest_id,user_name,tweet_text,cookies,limite):
        """
        this a lop for send request gto get more data or Scrolling
        """
        try:
            cursor=re.findall('"value":"(.*?)","cursorType',str(tweet_text))[1]
            params = {
                'variables': '{"userId":"%s","count":20,"cursor":"%s","includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}'%(rest_id,cursor),
                'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
            }
            response = requests.get(
                'https://twitter.com/i/api/graphql/NBWKw7od2So5qClZpLyQ0w/UserTweets',
                params=params,
                cookies=cookies,
                headers=headers,
            ).text
            self.scretpt(user_name,tweet_text)
            self.s=len(self.data_profile)
            if self.s > int(limite):
                self.messag= "Done"
            else:
                self.loping(rest_id,user_name,response,cookies,limite)
            return self.messag
        except Exception as messag: return messag
        
    def screpeing_profile_post(self,user_name,limite,cookies):  #seach fast page and get data
        try:
            rest_id=self.get_profile_id(user_name,cookies)
            #print(rest_id)
            if "user name or cookes invaid" in rest_id:
                return "user name or cookes invaid"
            else:
                
                params = {
                'variables': '{"userId":"%s","count":20,"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}'%(rest_id),
                'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',}
                tweet_text = requests.get(
                    'https://twitter.com/i/api/graphql/NBWKw7od2So5qClZpLyQ0w/UserTweets',
                    params=params,
                    cookies=cookies,headers=headers).text

                get_data=self.loping(rest_id,user_name,tweet_text,cookies,limite)
                if "Done" in get_data:
                    self.unique_data = [list(t) for t in set(tuple(sublist) for sublist in self.data_profile)]
                    return self.unique_data
                else:
                    return "Something Is Wrong Or Invaid Cookes"
            
        except Exception as e: return e




# ---------------------------------------------------
# c=scrap_profile()        # calling the Class 
# user_name='imVkohli'     # user name wich are scraping
# limite=10       # the number of data you want
# ww=c.screpeing_profile_post(user_name,limite,cookies)
# for post_url,reaction_numbr,connnt_num,chaption,viwes in ww:
#     feltering(post_url,reaction_numbr,connnt_num,chaption,viwes,like_liite,viwes_limite,comment_limite)
"""
    print(f"post_url : {post_url}")             # Post Url
    print(f"Reaction : {reaction_numbr}")       # Post Number of Reaction
    print(f"Post Text : {chaption}")            # Post description
    print(f"Number Comment : {connnt_num}")  # Post Number of Comment
    print(f"{LI_YELLOW}Number views : {LI_WHITE}{viwes}")   # Post Number of Reach or viwes
    print(mahdilinx())

"""

class scrap_search:   # This class for scrap Data from the serach by name 
    data_search=[]
    def __init__(self):
        pass
    def parsing(self,tweet_text):
        #tweet_text=open('rarara.txt','w',encoding='UTF-8').write(tweet_text)
        """
        This function parsing All data from the Responce or Inputed Text
        """
        try:
            data = re.findall(f'"count":"(.*?)",(.*?)"expanded_url":"(https://twitter.com/.*?/status/.*?)/(.*?)"favorite_count":(\d+),"favorited":false,"full_text":"(.*?)",(.*?),"reply_count":(\d+)', str(tweet_text).strip())
            for viwes,cx,post_url ,x, reaction_numbr,chaption,v,comment_numbe in data:
                # print(f"post_url : {post_url}")
                # print(f"Reaction : {reaction_numbr}")
                # print(f"Post Text : {chaption}")
                # print(f"Number Comment : {comment_numbe}")
                # print(f"Number views : {viwes}")
                self.data_search.append([post_url,reaction_numbr,comment_numbe,chaption,viwes])
                #self.data_search.append([post_url,reaction_numbr,chaption,comment_numbe,viwes])
                #print(mahdilinx())
        except:pass
    def loping(self,tweet_text,cookies,limite):
        """
        this a lop for send request gto get more data or Scrolling
        """
        try:
            self.parsing(tweet_text)
            cursor=re.findall('"TimelineTimelineCursor","value":"(.*?)","cursorType',str(tweet_text))[1]
            params = {
            'variables': '{"rawQuery":"Cryptocurency","count":50,"cursor":"%s","querySource":"recent_search_click","product":"Latest"}'%(cursor),
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
            }
            response = requests.get(
                'https://twitter.com/i/api/graphql/PaIcTAgMdfWySgs3aVU5TA/SearchTimeline',
                params=params,
                cookies=cookies,
                headers=headers,
            ).text
            self.s=len(self.data_search)
            if self.s > int(limite):
                self.messag= "Done"
            else:
                self.loping(response,cookies,limite)
            return self.messag
        except Exception as e: return e
    def search_latest(self,cookies,chatagory,limite): #seach fast page and get data
        try:
            params = {
            'variables': '{"rawQuery":"%s","count":200,"querySource":"recent_search_click","product":"Latest"}'%(chatagory),
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
        }
            tweet_text = requests.get(
                'https://twitter.com/i/api/graphql/PaIcTAgMdfWySgs3aVU5TA/SearchTimeline',
                params=params,cookies=cookies,headers=headers,).text
            get_responces=self.loping(tweet_text,cookies,limite)
            if "Done" in get_responces:
                self.unique_data = [list(t) for t in set(tuple(sublist) for sublist in self.data_search)]
                return self.unique_data
            else:
                return "Something Is Wrong Or Invaid Cookes"

        except Exception as e: return e
    def search_Top(self,cookies,chatagory,limite):
        params = {
        'variables': '{"rawQuery":"%s","count":200,"querySource":"recent_search_click","product":"Top"}'%(chatagory),
        'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":false,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_media_download_video_enabled":false,"responsive_web_enhance_cards_enabled":false}',
        }
        response = requests.get('https://twitter.com/i/api/graphql/HgiQ8U_E6g-HE_I6Pp_2UA/SearchTimeline',
            params=params,cookies=cookies,headers=headers, ).text
        get_responces=self.loping(response,cookies,limite)
        if "Done" in get_responces:
            self.unique_data = [list(t) for t in set(tuple(sublist) for sublist in self.data_search)]
            return self.unique_data
        else:
            return "Something Is Wrong Or Invaid Cookes"
        






# ---------------------------------------------------
    

c=scrap_search()              # calling the Class 
chatagory='global warming'               # keyword name wich are scraping
limite=10                     # the number of data you want



x=c.search_Top(cookies,chatagory,limite)
for post_url,reaction_numbr,connnt_num,chaption,viwes in x:
    feltering(post_url,reaction_numbr,connnt_num,chaption,viwes,like_liite,viwes_limite,comment_limite)

