from asyncio.windows_events import NULL
from re import S

digits = []

def binary(num):
    global bin
    bin = ''
    def logic(num):
        try:
            strNum = str(num)
            if not '.' in strNum:
                if num > 0:
                    x = False if num%2 == 0 else True 
                    bin = str(int(x)) + bin 
                    binary(num//2)
                elif num < 0:
                    negative = abs(num)
                    bin += '-'
                    x = False if negative%2 == 0 else True 
                    bin = str(int(x)) + bin
                    binary(negative//2)
            else:
                integer, decimal = strNum.split('.')
                bin = binary(int(integer)) + '.' + binary(int(decimal))
        except:
            print("wrong input type, please enter a number")


    if num == 0:
        return 0
    else:
        logic(num)
        return bin


print(binary(1))
print('F')
