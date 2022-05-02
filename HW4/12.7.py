#Huy Nguyen
#PSID 1346435

def get_age():
    age = int(input())
    if 17 < age < 76:
        return age
    raise ValueError("Invalid age.")

def fat_burning_heart_rate(age):
    return (220-age) * 0.7

if __name__ == "__main__":
    try:
        age = get_age()
        fat = str(fat_burning_heart_rate(age))
        print("Fat burning heart rate for a " + str(age) + " year-old: " + fat + " bpm")
    except ValueError as i:
        print(i)
        print("Could not calculate heart rate info.\n")