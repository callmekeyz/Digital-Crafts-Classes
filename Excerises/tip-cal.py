total = float(input("bill total"))

service = (input("level of service?"))
if (service == "Awesome" or service == "Amazing" or service == "Average"):
    tip = total *.2

elif (service =="Great" or service == "good" or service == "grand"):
    tip = total *.15
else:
    tip = total *.1
print("Tip will be %.2f"%tip)

print(f"Grand total will be ({total}+15)")
