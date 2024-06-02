ages, cnts = 0, 0

while True:
    age = int(input())

    if age < 20 or age >= 30:
        ages /= cnts
        print("{:.2f}".format(round(ages, 1)))
        break
    else:
        ages += age
        cnts += 1