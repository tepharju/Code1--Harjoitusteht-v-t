# Code 1
# 4.8 Karkausvuosilaskin

import calendar



a = int(input("Anna vuosi: "))

if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print("Vuosi "+ str(a)+ " on karkausvuosi.")

else:
    print("Vuosi "+ str(a)+ " ei ole karkausvuosi.")

print (calendar.isleap(a)) # automate the boring stuff...
