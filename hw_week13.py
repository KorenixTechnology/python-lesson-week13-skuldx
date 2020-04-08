def hw_week13(number):
    #number = input("Please input an integer:")

    try:
        while int(number) != 1:
            mod_result = int(number) % 2    
            if mod_result == 0:
                number = int(number) // 2
                print(str(number) + " ", end = " ")
       
            elif mod_result == 1:
                number = int(number) * 3 + 1
                print(str(number) + " ", end = " ")
   
    except Exception as e:
        print(e)

if __name__ == '__main__':
    hw_week13(input('Please input the positive integer: '))
