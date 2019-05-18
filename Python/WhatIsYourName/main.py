print("Enter your name:")

name = input() 
print("Hello,", name)
print ("how are you?")
input()
print ("that is awesome",name)
print ("what is your second letter from your name ?")
letter = input()
if letter == name[1]:
 print ("correct")
else:
 print ("not this time")
lenghtOfName = len(name) #Променливата lenghtOfName е равна на големината на string-а name
reversedName = "" #Промелнивата reversedNmae е промелнива която ще се иползва като буфер
for p in range(lenghtOfName): # Правя цикъл върху броя на елементите на name
    reversedName += name[lenghtOfName - (p + 1)] # Тука сам мисли христо какво се случва :)
print("Here is you reversed name", reversedName)
    
