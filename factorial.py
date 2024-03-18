def factorial(number):
    if number==0 or number==1:
        return 1   
    else:    
        return number * factorial(number-1)

def factorialTrainingZero(number):
    count =0
    i = 5
    while (number//1 !=0):
        count+= int(number/i)
        i = i*5
      

    fac = factorial(number)
    print(fac)
    count = 0
    while(fac%10 ==0):
        count = count +1
        number = fac/10
    return count 
if __name__ == '__main__':
    number = int(input("enter a number \n"))
    fac = factorial(number)
    print(f"the factorial is {fac}")
    print(factorialTrainingZero(number))