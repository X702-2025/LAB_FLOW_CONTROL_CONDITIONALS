movieName = "mission impossible"
rating: int = 3
popularity: float = 72.65

if (rating >= 4) and (rating <= 5) and (popularity > 80):
    print("Highly recommended")
elif (rating >= 3) and (rating < 4) and (popularity > 70):
    print("I recommend it, it is good")
elif (rating <= 2) and (popularity > 60):
    print("You should check it out!")
else:
    print ("Dont watch it, it is a waste of time")