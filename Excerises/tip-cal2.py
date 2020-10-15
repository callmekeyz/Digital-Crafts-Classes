people = int(input("How many people are in your party?\n"))
total_bill = float (input("enter bill total\n"))
service = input("please rate your service:good,fair or bad.\n")
good = .20
fair = .15
bad = .10
if service == "good":
    print ("Tip should be 20%")
    print (good*total_bill +total_bill)
    print (good*total_bill)
    print (total_bill/people)
elif service == "fair":
    print ("Tip should be 15%")
    print (fair*total_bill +total_bill)
    print (fair*total_bill)
    print (total_bill/people)
else:
    print ("Tip should be 10%")
    print (bad*total_bill +total_bill)
    print (bad*total_bill)
    print (total_bill/people)
