import requests

cookies = {
    'affDomainCookie': 'l.facebook.com',
    'route': 'inhouseweb03',
    '__cf_bm': 'MO0JDac2oc_2ZzeQxn_st2B1bUhRUxhNQJ2859E5DkM-1716481093-1.0.1.1-Ae0mwDfuBsl2PxhkEsv4sgOfLYDYDK.72hR0dqk8NLdtBDVs.6JwhpeTKeY19_O81TEMHkV1ZslpcPVHYxge2Q',
    '__cflb': '0H28vL6Y888Vk48NA1FXMtoe3v4DkBRvhCV3P8bVcjv',
    '_cfuvid': '8gbmbS8G8rbBN5C.Oj1WsNrg1ykPz7.48QK5Wdn90_0-1716481093749-0.0.1.1-604800000',
    '_gid': 'GA1.2.1764208353.1716481097',
    '_gat_gtag_UA_202237783_1': '1',
    'intercom-id-vds47pw2': '59997fc3-1843-4def-af0e-4d70e985b2b3',
    'intercom-device-id-vds47pw2': '9820482c-5e52-41e0-9a05-02ca8999cd1d',
    'JSESSIONID': '5C212FE1D9A6F3AB2F946C12EC7DD3CA',
    '_ga_ZCD016JDV9': 'GS1.1.1716481097.1.1.1716481130.0.0.0',
    '_ga': 'GA1.2.1564922539.1716481096',
    'intercom-session-vds47pw2': 'clRheHlkNHpsSkx5bGZQNXN2UHZMM1FFMEFFOWQvWFJlZkhWNkRwWGFUdTNEVTBWOWJhQmtOSzJNLzdSSitLTy0tUGljejlOcC82YVUzS2FBZEN0VlNGQT09--06d7dc96286aaff644f09e007480697368fee1bc',
    '_ga_P74FL3Z3ZY': 'GS1.1.1716481096.1.1.1716481138.0.0.0',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8,bn;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'affDomainCookie=l.facebook.com; route=inhouseweb03; __cf_bm=MO0JDac2oc_2ZzeQxn_st2B1bUhRUxhNQJ2859E5DkM-1716481093-1.0.1.1-Ae0mwDfuBsl2PxhkEsv4sgOfLYDYDK.72hR0dqk8NLdtBDVs.6JwhpeTKeY19_O81TEMHkV1ZslpcPVHYxge2Q; __cflb=0H28vL6Y888Vk48NA1FXMtoe3v4DkBRvhCV3P8bVcjv; _cfuvid=8gbmbS8G8rbBN5C.Oj1WsNrg1ykPz7.48QK5Wdn90_0-1716481093749-0.0.1.1-604800000; _gid=GA1.2.1764208353.1716481097; _gat_gtag_UA_202237783_1=1; intercom-id-vds47pw2=59997fc3-1843-4def-af0e-4d70e985b2b3; intercom-device-id-vds47pw2=9820482c-5e52-41e0-9a05-02ca8999cd1d; JSESSIONID=5C212FE1D9A6F3AB2F946C12EC7DD3CA; _ga_ZCD016JDV9=GS1.1.1716481097.1.1.1716481130.0.0.0; _ga=GA1.2.1564922539.1716481096; intercom-session-vds47pw2=clRheHlkNHpsSkx5bGZQNXN2UHZMM1FFMEFFOWQvWFJlZkhWNkRwWGFUdTNEVTBWOWJhQmtOSzJNLzdSSitLTy0tUGljejlOcC82YVUzS2FBZEN0VlNGQT09--06d7dc96286aaff644f09e007480697368fee1bc; _ga_P74FL3Z3ZY=GS1.1.1716481096.1.1.1716481138.0.0.0',
    'dnt': '1',
    'origin': 'https://www.jeetbuzz.com',
    'priority': 'u=1, i',
    'referer': 'https://www.jeetbuzz.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'userId': 'sujon329',
    'password': 'Sum0091qeqer',
    'fingerprint': '4169419518',
    'fingerprint2': '0920ed136f238abe0621e3b73994b24e',
    'fingerprintCanvas': '4047878472',
    'fingerprintActiveX': 'a2b1b79fc3cd8418c57a84b5070ad0fb',
    'fingerprintResolution': '727168705',
    'isBioLogin': 'false',
    'fingerprint4': 'b2e6c2b7f1e4048787130f27a65c8c29',
    'browserHash': '1d434fc0d389376e673efa563b30a243',
    'deviceHash': 'fd3afa997471c2196bccaf1f25216963',
}

response = requests.post('https://www.jeetbuzz.com/guest/login', cookies=cookies, headers=headers, data=data).text
print(response)