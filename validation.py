import re
import time
from datetime import datetime, date


def check_string(message):
    while True:
        str=input(message)
        if str.isalpha():
            return str
        else:
            print("enter valid string")
def check_int(message):
    while True:
        str=input(message)
        if str.isdigit():
            return str
        else:
            print("enter valid string")

def check_eamil(message):
    regix=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    while True:
        str=input(message)
        if re.fullmatch(regix,str):
            return str
        else:
            print("enter valid email")


def is_equal(passw,message):
    while True:
        str =input(message)
        if passw == str:
            return str
        else:
            print("confirm drop please confirm your password")



def check_mobile(message):
    regix=r'^01[0125][0-9]{8}$'
    while True:
        str=input(message)
        if re.fullmatch(regix,str):
            return str
        else:
            print("enter valid phone nuber ")


def save_to_file(user_data):
    try:
        f1=open(r"C:\\Users\\vip\Desktop\Day3lab\\userdata.txt",'a')
    except Exception as e:
        print(e)
    else:
        f1.write(user_data)
        f1.close()
        print("saved to file ")

def find_user(email,password):
    try:
        f1=open(r"C:\\Users\\vip\Desktop\Day3lab\\userdata.txt",'r')
    except Exception as e:
        print(e)
    else:
        users=f1.readlines()
        for user in users:
            user_details = user.strip('\n').split(":")
            if user_details[2] == email and user_details[3] == password:
                return True,user_details[0]

        return False

def generate_id():
    return round(time.time())

def valid_date():
        dateregex = re.compile(r'\d{4}[-/]\d{2}[-/]\d{2}')
        format="%d-%m-%Y"

        while True:
            instr = input("enter your date")
            res = bool(datetime.strptime(instr, format))
            if res:
                return instr
            print("----Error --> please enter it again-----")

