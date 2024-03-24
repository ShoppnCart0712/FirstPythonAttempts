#Converts a weight from Kg to lb and vice versa, and can detect if entered 
#values are not what is asked for
print("Heyo")
w = input("How heavy is it?") #weight input
x=0  #to be used in a loop
#test for number
while x == 0: 
    try:  
        w = int(w) #attempt to make str into int
        break
    except: #if str not a number, and error occurs 
        w = input("I need a number, man.") #ask and test again

u = input("(K)g or (L)b?")
while x==0:
    if u.__contains__("L") or u.__contains__("l"):
        print(str(float(w)/2.20462)+"kg") #lb to kg conversion
        break 
    elif u.__contains__("K") or u.__contains__("k"):
        print(str(float(w)*2.20462)+"lb") #kg to lb conversion
        break 
    else:
        u = input("Bro.")
