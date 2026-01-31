import random
six_count=0
one_count=0
two_sixes_row=0
previous_roll=0
for i in range(1,21):
    roll=random.randint(1,6)
    print(f"roll {i} : {roll}")
    if(roll==6):
        six_count+=1
        if(previous_roll==6):
            two_sixes_row+=1
    elif(roll==1):
        one_count+=1
    previous_roll=roll
print(f"Number of times 6 come as outcome {six_count}\nNumber of times one come as outcome {one_count}\nNumber of times 6 comes twice in row {two_sixes_row}")