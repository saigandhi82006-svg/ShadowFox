#City belongs to which country
Australia=["Sydney", "Melbourne", "Brisbane", "Perth"] 
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"] 
c=input("Enter a city name: " \
"Demo(Mumbai)")
if c in Australia:
    print(f"{c} is in Australia")
elif c in UAE:
    print(f"{c} is in UAE")
elif c in India:
    print(f"{c} is in India")
else:
    print("Invalid city")


#If given two cities are in same country or not
c1=input("Enter first city name")
c2=input("Enter second city name")
if c1 in Australia and c2 in Australia:
    print("Both cities are in Australia")
elif c1 in UAE and c2 in UAE:
    print("Both cities are in UAE")
elif c1 in India and c2 in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")

