# Day 9 - Dictionaries and Nesting

# Creating a dictionary
programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function":
    "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

# Adding new items to a dictionary
programming_dictionary[
    "Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

for item in programming_dictionary:
    print(item)
    print(programming_dictionary[item])

# Exercise - Student grade calculation
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for item in student_scores:
    if student_scores[item] > 90:
        student_grades[item] = "Outstanding"
    elif student_scores[item] > 80:
        student_grades[item] = "Exceeds Expectations"
    elif student_scores[item] > 70:
        student_grades[item] = "Acceptable"
    else:
        student_grades[item] = "Fail"

print(student_grades)

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

nested_list = ["A", "B", ["C", "D"]]

travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits" : 5
    },
    "Germany": {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 3},
}

travel_log3 = [
    {
      "country" : "France",
      "cities_visited": ["Paris", "Lille", "Dijon"],
      "total_visits" : 5
    },
    {
      "country" : "Germany",
      "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
      "total_visits" : 3
    },
]

# Exercise - Travel log creation
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(country_name,visits_number,cities):
  travel_log.append({
      "country" : country_name,
      "visits" : visits_number,
      "cities" : cities,
    })

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
