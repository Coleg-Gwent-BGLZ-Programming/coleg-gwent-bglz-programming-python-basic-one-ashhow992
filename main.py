# main.py - Personal Data Manager

# TODO: Step 1 - Prompt the user to enter their name and age
# Hint: Use input() and store the values in variables

# TODO: Step 2 - Ask the user to enter 3 hobbies
# Hint: Use a loop to collect hobbies and store them in a list

# TODO: Step 3 - Create a dictionary to store the user's name, age, and hobbies
# Hint: Use key-value pairs to organize the data

# TODO: Step 4 - Display the user's information using formatted strings
# Hint: Use f-strings to format the output

# TODO: Step 5 - Convert the hobbies list into a set to remove duplicates
# Hint: Use the set() function

# TODO: Step 6 - Calculate the user's birth year and store it in a tuple with the current year
# Hint: Use subtraction and a tuple to store both years

# TODO: Step 7 - Create a function that takes the dictionary and returns a summary string
# Hint: Use string concatenation or f-strings inside the function

# TODO: Step 8 - Call the function and print the summary
# Hint: Pass the dictionary to the function and print the result



from datetime import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobbies = []
for i in range(3):
    hobby = input(f"Enter hobby {i+1}: ")
    hobbies.append(hobby)
user_data = {
    "name": name,
    "age": age,
    "hobbies": hobbies
}
print(f"\nName: {user_data['name']}")
print(f"Age: {user_data['age']}")
print(f"Hobbies: {', '.join(user_data['hobbies'])}")
hobby_set = set(hobbies)
print(f"Hobbies (unique): {', '.join(hobby_set)}")
current_year = datetime.now().year
birth_year = current_year - age
years = (birth_year, current_year)
print(f"Birth year: {birth_year}, Current year: {current_year}")
def create_summary(data):
    return (
        f"{data['name']} is {data['age']} years old. "
        f"They enjoy {', '.join(set(data['hobbies']))}. "
        f"They were born in {years[0]} and the current year is {years[1]}."
    )
summary = create_summary(user_data)
print("\nSummary:")
print(summary)
