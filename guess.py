# ask user to guess my favourite food

guess = input("What is my favourite food? ")

if guess == "Rice" or guess == "rice" or guess == "RICE" or guess =="rice":
    print("Yep! So amazing!")
else:
    print("Yuck! That's not it!")
    
print("Thanks for playing!")