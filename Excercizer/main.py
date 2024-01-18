import random
import website

def Printer(i, chars, line=[]):
    while(True):
        # pārveido char list uz veselu String un izprintē to, kā arī izdzēš char rindu  
        if(chars[i].isupper() == True):
            print("\n" + str.join("", line))
            line.clear()
        # pievieno nākamo char
        line.append(chars[i])
        i += 1

        # pārbauda vai nākamā treniņ veida paskaidrojums ir sācies
        if(chars[i+1].isnumeric() == True and (chars[i+2] == "." or chars[i+3] == ".")):
            print("\n" + str.join("", line))
            break

# izveido skaitli kas atbilst mājaslapas formatējumam
excNum = list(str(random.randint(1, 49)) + ". ")
chars = website.SiteToCharList()
i = 0

for _ in chars:
    # parbauda vai pēdējie divi char ir ". "
    if(chars[i] == " " and chars[i-1] == "."):
        # pārbauda vai cipars ir no 1-9 vai 10-50, ka ari noskaidro kas tas ir par skaitli
        if(excNum[0] == chars[i-3] and excNum[1] == chars[i-2]):
            Printer(i, chars)
            break
        elif(excNum[0] == chars[i-2] and len(excNum) == 3):
            Printer(i, chars)
            break
    i += 1