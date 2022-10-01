#string


score = 233
name = "Sumit"

print("Hey", name + ", My score is", score)

print("Hey %s, My score is %d" %('Amit', 245))

# concatination

myStr = "Hello World!"

print(myStr[:6] + "India")

# manuplating a string

myStr = "This is my string"

print(myStr.swapcase())
print(myStr.isdecimal())


userInput = "    Sumit    "
print(userInput.strip())

userInput = "----Sumit----"
print(userInput.strip('-'))