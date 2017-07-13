#This is a survey that will ask you questions about your lifestyle, and suggest possible mental health outcome

print()
print("Welcome to Screening Test for future dementia");
print()

s = input("How many times have you smoke marijuana in the past 2 months?")
try:
    f = float(s)
except ValueError:
    print("Sorry,", s, "is not a number.")
    f = 50
    print("I'll assume you wanted to type ", f, ".", sep = "")

s = input("Have many times have you been drunk in the past 2 months?")
try:
    g = float(s)
except ValueError:
    print("Sorry,", s, "is not a number.")
    g = 40
    print("I'll assume you wanted to type ", g, " and please don't ask me why.", sep = "")

s = input("How many times have you been exercising in the last 2 months?")
try:
    h = float(s)
except ValueError:
    print("Sorry,", s, "is not a number.")
    h = 1
    print("I'll assume you wanted to type ", h, ".\n", sep = "")
    
sum = f + g 
if sum >= 20 and h < 8:
	print("OMG ", sum, " times, you man have to take it easy. You need to reduce your smoking and drinking if you want to keep your cognitive abilities. And you need to hit the gym please.", sep = "")
if sum >= 20 and h >= 8:
	print("Man you have to take it easy on the bad stuff, ok it's great that you work out a lot BUT you still need to act healthy.");
if sum < 20 and h < 8:
	print("Ok,", sum , ",if this is closer to 0 and 10 you are in a good range for no future dementia , if closer to 20 be careful.")
	print(" About the gym, it would be good for you to hit it sometimes.")
if sum < 20 and h >= 8:
	print("Bravo on the work out! You are on the right track to keep all your cognitive functions!")

print()
print("Thank you for using and good luck :)")
