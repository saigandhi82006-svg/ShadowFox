justice_league=["Superman", "Batman", "WonderWoman", "Flash", "Aquaman", "Green Lantern"] 
#Number Of members in justuce league
print(f"Number of members in justice league is",len(justice_league))
print(justice_league)
#Adding new members to the list
justice_league.extend(["Batgirl","Nightwing"])
print(justice_league)
#Moving wonderwoman to the beginning of the list
justice_league[2],justice_league[0]=justice_league[0],justice_league[2]
print(justice_league)
#conflict between aquaman and flash
justice_league[2],justice_league[3]=justice_league[3],justice_league[2]
print(justice_league)
#Replacing list with new list
new_justice_league=["Cyborg", "Shazam", "Hawkgirl", "MartianManhunter", "Green Arrow"]
justice_league.clear()
justice_league.extend(new_justice_league)
print(justice_league)
#Sorting the new justice league list and declaring the leader
justice_league.sort()
print(justice_league)
print(f"Leader for this justice league is",justice_league[0])