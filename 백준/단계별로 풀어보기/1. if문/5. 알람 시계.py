hour, minuite = input().split()

hour = int(hour)
minuite = int(minuite)

if 45 <= minuite <= 59 :
    minuite = minuite - 45
    print(f"{hour} {minuite}")
elif 0 <= minuite < 45 :
    minuite = minuite + 15
    if hour == 0 :
        hour = 23
    else :
        hour = hour - 1
    print(f"{hour} {minuite}")