from validation import check_string,check_eamil,is_equal,check_mobile,save_to_file,find_user,valid_date
def register_to():
    first_name=check_string("pleas enter your first_name: ")

    last_name=check_string("pleas enter your last_name: ")

    email=check_eamil("pleas enter your email : ")

    password=input("pleas enter your password : ")

    confirm_password=is_equal(password,"pleas confirm your password : ")
    check_user=find_user(email,password)
    if check_user:
        print("this email and password is dublicated please try again later")
    else:
        mobile=check_mobile("please enter your mobile ")
        user_data=f'{first_name}:{last_name}:{email}:{password}:{mobile}\n'
        save_to_file(user_data)

def login_user():
    email=check_eamil("please enter your email : ")
    password=input("please enter your password : ")
    result,user=find_user(email,password)
    if result:
        print("welcome yasta")       
    else:
        print("mesh anta ya am")


print("welcome to our aplication")

cho=input("please choice regiser r or have email to login l : ")
while True:
    if  cho.__eq__('r'):
        register_to()
        break
    elif cho.__eq__('l'):
        login_user()
        break
    else:
        print("invalid choice ")