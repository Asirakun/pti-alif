# author          : Alif Siky Rodhofa

# 1. Variable Declaration

variable1 = 10
variable2 = 10.5
variable3 = "sepuluh"
variable4 = True
# 2. Operators -> +, -, *, /, %, 


for baris in range(5):
    for kolom in range(5):
        print("*",end="")
    print()

print("=============")

# While interation -> Need Co
baris2 = 0
tengah = 5
while baris2 < 5 :
    kolom2 = 0
    if(baris2 % 2 == 0):
        while kolom2 < 5:
            if(kolom2 == int(round(tengah/2))):
                print("*",end="")
            else:
                print(" ",end="")
            kolom2 += 1
    else:
        while kolom2 < 5 :
            print("*",end="")
            kolom2 += 1
    print()
    baris2 += 1