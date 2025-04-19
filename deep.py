x = input ("what is the answer to the great question  of life , the universe, and everything? ").strip().lower()
if x == "42" :
    print("yes")
elif x == "forty two":
    print("yes")
elif x == "forty-two":
    print ("yes")
else:
    print("no")