while True:
    print"who are you?"
    ans=raw_input(":")
    if ans!="hamza":
       continue
    print"hi, hamza what is the password?"
    psw=raw_input(":")
    if psw=="mungadi":
       break
print"Access granted!"

with open("secretfile2.txt", 'a+') as myf:
    read=myf.read()
    hacker= raw_input(">>>")
    myf.write(hacker)
    print read
    

