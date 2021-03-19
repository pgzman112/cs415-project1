
 print("Please enter 1 to run task 1 (fibonacci and euclids algorithm)")
 print("Or enter 2 to run task 2 (Exponentiation)")
 print("Or enter 3 to run task 3(Sorting)")
 mode = input("enter your selection now: ")
 if mode == '1':
     exec(open("taskOne.py").read())
 elif mode == '2':
     exec(open("taskTwo.py").read())
 elif mode == '3':
     exec(open("taskThreeThreadTest.py").read())
 else:
     print("incorrect input run and try again")