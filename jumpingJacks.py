total_jumps = 0
target = 100

while total_jumps < target:
    print("\nDo 10 jumping jacks!")
    total_jumps += 10

    if total_jumps >= target:
        print("Congratulations! You completed the workout 🎉")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip == "yes" or skip == "y":
            print("You completed a total of", total_jumps, "jumping jacks.")
            break
    else:
        remaining = target - total_jumps
        print(remaining, "jumping jacks remaining.")
