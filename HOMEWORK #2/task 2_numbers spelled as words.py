def get_input_data(message):
    while True:
        try:
            value = input(message)
            return int(value)
        except:
            print('Please enter a numeric value')


# 1st method:
# from num2words import num2words
# print(num2words(321, to = 'cardinal', lang= 'uk'))

'''
    cardinal (default)
    ordinal
    ordinal_num
    year
    currency
'''

'''
def convert(num):
    units = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens =("", "", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    if num < 0:
        return "minus "+convert(-num)

    if num<20:
        return  units[num] 

    if num<100:

        return  tens[num // 10]  +units[int(num % 10)] 

    if num<1000:
        return units[num // 100]  +"hundred " +convert(int(num % 100))

    if num<1000000: 
        return  convert(num // 1000) + "thousand " + convert(int(num % 1000))

    if num < 1000000000:    
        return convert(num // 1000000) + "million " + convert(int(num % 1000000))

    return convert(num // 1000000000)+ "billion "+ convert(int(num % 1000000000))

print(convert(666))
'''


# Number to Words

# Main Logic
ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')

twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')

suffixes = ('', 'Thousand', 'Million', 'Billion')

def process(number, index):
    
    if number=='0':
        return 'Zero'
    
    length = len(number)
    
    if(length > 3):
        return False
    
    number = number.zfill(3)
    words = ''
 
    hdigit = int(number[0])
    tdigit = int(number[1])
    odigit = int(number[2])
    
    words += '' if number[0] == '0' else ones[hdigit]
    words += ' Hundred ' if not words == '' else ''
    
    if(tdigit > 1):
        words += tens[tdigit - 2]
        words += ' '
        words += ones[odigit]
    
    elif(tdigit == 1):
        words += twos[(int(tdigit + odigit) % 10) - 1]
        
    elif(tdigit == 0):
        words += ones[odigit]

    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '
     
    if(not len(words) == 0):    
        words += suffixes[index]
        
    return words;
    
def getWords(number):
    length = len(str(number))
    
    if length>12:
        return 'This program supports upto 12 digit numbers.'
    
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []
 
    for i in range(length - 1, -1, -3):
        words.append(process(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
        count -= 1;

    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp
    
    return final_words
# End Main Logic

# Reading number from user
number = int(input('Enter any number: '))
print('%d in words is: %s' %(number, getWords(number)))
