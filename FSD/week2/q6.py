magnitude = float(input("Please enter the magnitude: "))
if magnitude >= 8.0:
	print("most structures fall")
elif magnitude >= 7.0:
	print("many buildings destroyed")
elif magnitude >= 6.0:
	print("many buildings considerably damaged, some collapse")
elif magnitude >= 4.5:
	print("damage to poorly constructed buildings")
else:
	print("no destructions")