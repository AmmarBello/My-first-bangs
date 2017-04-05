def Intro(name):
    print("Hi, "+name + " welcome to percentage Apps")

user=raw_input('What is your name ? :')
Intro(user)

while True:
      print"""
Enter "P" to convert an amount to percentage
Enter "A" to convert a percentage to amount
Enter "C" to quit the Apps
"""
      ans=raw_input(">>>")
      ans=ans.upper()
      if ans=='C':
        break
      elif ans=='P':
         try:
            TA=raw_input("Enter the total amout: ")
            TA=float(TA)
            A=raw_input("Enter the amount you want to convert in percentage: ")
            A=float(A)
            p=(A*100)/TA
            print"{} out of {} is {}%".format(A ,TA, p)
         except ValueError:
            print"Please provide a number"
            break
      
      elif ans=='A':
         try:
            A=raw_input("Enter the total amout: ")
            A=float(A)
            n=raw_input("Enter the number of percentage: ")
            n=float(n)
            if n>100:
                 print"Number of percentage can not exceed 100"
                 break
            elif n<0:
                 print"Number of percentage must be nonnegative"
                 break
            to_am=(n/100)* A
            print"{}% of {} is {}".format(n, A, to_am)
         except ValueError:
            print"Please provide a number"
            break
             
      else:
          print"Oops! the option you enter is not available"  
