import json

# Your JSON data
json_text = '''
{
    "data": {
        "search_by_raw_query": {
            "search_timeline": {
                "timeline": {
                    "instructions": [
                        {
                            "type": "TimelineAddEntries",
                            "entries": [
                                {
                                    "entryId": "toptabsrpusermodule-1754049494594355200",
                                    "sortIndex": "1754049494594355200",
                                    "content": {
                                        "entryType": "TimelineTimelineModule",
                                        "__typename": "TimelineTimelineModule",
                                        "items": [
                                            {
                                                "entryId": "toptabsrpusermodule-1754049494594355200-user-1247139898689064960",
                                                "item": {
                                                    "itemContent": {
                                                        "itemType": "TimelineUser",
                                                        "__typename": "TimelineUser",
                                                        "user_results": {
                                                            "result": {
                                                                "__typename": "User",
                                                                "id": "VXNlcjoxMjQ3MTM5ODk4Njg5MDY0OTYw",
                                                                "rest_id": "1247139898689064960",
                                                                "affiliates_highlighted_label": {},
                                                                "has_graduated_access": true,
                                                                "is_blue_verified": true,
                                                                "profile_image_shape": "Circle",
                                                                "legacy": {
                                                                    "can_dm": true,
                                                                    "can_media_tag": true,
                                                                    "created_at": "Mon Apr 06 12:31:51 +0000 2020",
                                                                    "default_profile": true,
                                                                    "default_profile_image": false,
                                                                    "description": "23! She/her•Rebel•Rants•Roasts• National champ• Fighting Fascism ke jokers with comedy! All views expressed are personal!",
                                                                    "entities": {
                                                                        "description": {
                                                                            "urls": []
                                                                        },
                                                                        "url": {
                                                                            "urls": [
                                                                                {
                                                                                    "display_url": "bit.ly/Punjabinfluenc…",
                                                                                    "expanded_url": "https://bit.ly/Punjabinfluencerpolicy",
                                                                                    "url": "https://t.co/BmTXC7xxk8",
                                                                                    "indices": [
                                                                                        0,
                                                                                        23
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        }
                                                                    },
                                                                    "fast_followers_count": 0,
                                                                    "favourites_count": 4643,
                                                                    "followers_count": 123354,
                                                                    "friends_count": 462,
                                                                    "has_custom_timelines": true,
                                                                    "is_translator": false,
                                                                    "listed_count": 143,
                                                                    "location": "",
                                                                    "media_count": 573,
                                                                    "name": "Ranting gola",
                                                                    "normal_followers_count": 123354,
                                                                    "pinned_tweet_ids_str": [
                                                                        "1749761520001495480"
                                                                    ],
                                                                    "possibly_sensitive": false,
                                                                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1247139898689064960/1663663597",
                                                                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1681624657005547520/etz01rtR_normal.jpg",
                                                                    "profile_interstitial_type": "",
                                                                    "screen_name": "therantinggola",
                                                                    "statuses_count": 2790,
                                                                    "translator_type": "none",
                                                                    "url": "https://t.co/BmTXC7xxk8",
                                                                    "verified": false,
                                                                    "want_retweets": false,
                                                                    "withheld_in_countries": []
                                                                },
                                                                "professional": {
                                                                    "rest_id": "1470273065888018434",
                                                                    "professional_type": "Creator",
                                                                    "category": [
                                                                        {
                                                                            "id": 935,
                                                                            "name": "Comedian",
                                                                            "icon_name": "IconBriefcaseStroke"
                                                                        }
                                                                    ]
                                                                }
                                                            }
                                                        },
                                                        "userDisplayType": "UserDetailed"
                                                    },
                                                    "clientEventInfo": {
                                                        "component": "user_module",
                                                        "element": "user",
                                                        "details": {
                                                            "timelinesDetails": {
                                                                "controllerData": "DAACDAAFDAABDAACCgABAAAAAAAAAAAKAAJw2r3wxwqUowsAAwAAAA50aGVyYW50aW5nZ29sYQoABUlWvudQgG1KCAAGAAAAEgoAB0U42vPPbXuoAAAAAAA="
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        ],
                                        "displayType": "Vertical",
                                        "header": {
                                            "displayType": "Classic",
                                            "text": "People",
                                            "sticky": true
                                        },
                                        "footer": {
                                            "displayType": "Classic",
                                            "text": "View all",
                                            "landingUrl": {
                                                "url": "twitter://search?query=therantinggola&src=recent_search_click&type=users",
                                                "urlType": "DeepLink"
                                            }
                                        },
                                        "clientEventInfo": {
                                            "component": "user_module",
                                            "element": "module"
                                        }
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
}
'''



# Load the JSON data
loads_data = json.loads(json_text)

# Assuming user_data contains the relevant portion of your JSON data
user_data = loads_data["data"]["search_by_raw_query"]["search_timeline"]["timeline"]["instructions"][0]["entries"][0]["content"]["entryType"]

# Extracting information
date_of_post = user_data["item"]["itemContent"]["user_results"]["result"]["legacy"]["created_at"]
tweet = user_data["item"]["itemContent"]["user_results"]["result"]["legacy"]["description"]
reaction_number = user_data["item"]["itemContent"]["user_results"]["result"]["favourites_count"]
comment_number = user_data["item"]["itemContent"]["user_results"]["result"]["statuses_count"]
views = user_data["item"]["itemContent"]["user_results"]["result"]["followers_count"]

# Print or use the extracted information as needed
print("Date of Post:", date_of_post)
print("Tweet:", tweet)
print("Reaction Number:", reaction_number)
print("Comment Number:", comment_number)
print("Views:", views)
