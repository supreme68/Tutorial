print("tell your name:")
name = input()
print("now tell your name backwards")
answer = input()
if answer == name[::-1]:
    print("yes")
else:
    print("no")