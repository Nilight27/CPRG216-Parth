print('Manna Corp. Retirement Eligibility Checker')
Age = int(input('Age: '))
YearsOfService = int(input('Years of Service: '))
Total = Age + YearsOfService

if(Age < 50):
    print('You are not eligible for retirement')
    
else:
    if(Age >= 65 or Total >= 80):
        print('You are eligible for retirement with full pension benefits') 
        exit()
    elif(Total < 80):
        print('You are eligible for retirement with discounted pension benefits')