def main():
    distance_in_miles = get_distance()
    kilometers = miles_to_km(distance_in_miles)
    print(f'The number of kilometer: {kilometers}')
    print('The number of yards:', miles_to_yards(distance_in_miles))
    miles_to_feets(distance_in_miles)


def get_distance():
    distance = int(input("Enter the number of miles: "))
    return distance
def miles_to_km(distance):
    return distance * 1.61

def miles_to_yards(distance):
    result = distance * 1760
    return result

def miles_to_feets(distance):
    result = distance * 5280
    print("The number of feet: " + str(result))





main()