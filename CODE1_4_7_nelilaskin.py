# Code 1
# 4.7 Nelilaskin ver. 2.0

a = int(input("Anna ensimmäinen luku: "))
b = int(input("Anna toinen luku: "))


while True:
    c = input("Anna laskutoimitus (+,-,* tai /): ")

       
    if (c == "+"):
        print(str(a)+ " + " +str(b)+" = "+ str(a+b))
        break
    if (c == "-"):
        print(str(a)+ " - " +str(b)+" = "+ str(a-b))
        break
    if (c == "*"):
        print(str(a)+ " * " +str(b)+" = "+ str(a*b))
        break
    if (c == "/"):
        print(str(a)+ " / " +str(b)+" = "+ str(a/b))
        break

    else:
        print("Tuntematon komento!")


