def calculate_bmi(weight_kg, height_meters):
    """Calculates the Body Mass Index (BMI) using one's weight and height"""
    return weight_kg / (height_meters ** 2)

def calculate_calories_burned(duration):
    """Calculates the estimated number of calories burned during an exercise,
     assuming 15 calories are burn per minute"""
    return duration * 15

def filter_overweight_people(people_data):
    """Filters overweight people based on BMI- if one's BMI is greater than or equal to 25, they are overweight"""
    overweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi >= 25:
            overweight_people.append(person)
    return overweight_people

def filter_underweight_people(people_data):
    """Filters underweight people based on BMI- if one's BMI is lower than or equal to 18.5, they are underweight"""
    underweight_people = []
    for person in people_data:
        bmi = calculate_bmi(person['weight'], person['height'])
        if bmi <= 18.5:
            underweight_people.append(person)
    return underweight_people

# Main program - calculates the BMI of all the people in the group
people_data = []
print("Enter fitness data for each person (Enter a blank name to finish): ")
while True:
    name = input("Enter person's name: ").strip()
    if not name:
        break
    weight = float(input("Enter person's weight in kilograms: "))
    height = float(input("Enter person's height in meters: "))
    duration = float(input("Enter exercise duration in minutes: "))
    person = {'name': name, 'weight': weight, 'height': height, 'duration': duration}
    people_data.append(person)
print("\nFitness Analysis:")
for person in people_data:
    bmi = calculate_bmi(person['weight'], person['height'])
    calories_burned = calculate_calories_burned(person['duration'])
    print(f"{person['name']}: BMI = {bmi:.2f}, Calories burned = {calories_burned:.2f}")
# calculates the BMI of the overweight people
overweight_people = filter_overweight_people(people_data)
print("\nOverweight people:")
if overweight_people:
    for person in overweight_people:
        bmi = calculate_bmi(person['weight'], person['height'])
        print(f"{person['name']}: BMI = {bmi:.2f}")
else:
    print('Nobody is overweight')
# calculates the BMI of the overweight people
underweight_people = filter_underweight_people(people_data)
print("\nUnderweight people:")
if underweight_people:
    for person in underweight_people:
        bmi = calculate_bmi(person['weight'], person['height'])
        print(f"{person['name']}: BMI = {bmi:.2f}")
else:
    print('Nobody is underweight')