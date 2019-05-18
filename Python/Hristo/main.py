def TellMeYourName():
    print("now tell your name backwards")
    answer = input()
    if answer == name[::-1]:
     print("yes")
    else:
     print("no")

print("tell your name:")
name = input()
print("hello", name)
print("can you imagine how smart i am if yes type: y if no: type: n.")
status = input()
if status == "y":
    print("I am happy to hear that!")
    TellMeYourName()
elif status == "n":
    print("OOOhhhh :((")
    TellMeYourName()
else:
    print("can`t understand you!")
    TellMeYourName()