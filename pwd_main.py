from My_Functions import store_passwords, display,create_profile 
key = input("Enter Database Password ")
while key== "password":
    p1 = input("Enter 1 for create profile, 2 to use profile or 0 to exit ")
    if p1=="0":
        break
    elif p1 == '1':
        usname=input("Enter a username for Database ")
        create_profile(usname, key)
    elif p1 == '2':
        usname=input("Enter a username for Database ")
        p2 = input("Enter 1 to read 2 to write and 0 to exit ")
        if p2 == '1':
            display(usname, key)
            
        elif p2 == '2':
            web=input('Enter Website name ')
            user=input('Enter user name ')
            pass1=input('Enter password ')
            em_mb=input('Enter email or mobile number conncected ')
            store_passwords(usname, key, web, user, pass1, em_mb)
        elif p1=="0":
            break
        
    else:
        print('Wrong Entry')
