# Day 5 - For Loop and Range
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  print(fruit + " pie")

# Exercise - average student height calculator
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
  total_height += height
print("total height = " + str(total_height))
print("number of students = " + str(len(student_heights)))
print("average height = " + str(round(total_height/len(student_heights))))

# Exercise - the highest score in a class
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
score_max = 0
for score in student_scores:
  if score > score_max:
    score_max = score
print(f"The highest score in the class is: {score_max}")

for number in range(1,10):
  print(number)

# Exercise - sum of even numbers
target = int(input())
sum = 0
for n in range(2,target+1,2):
  sum += n
print(sum)

# Exercise - FizzBuzz
for n in range(1,101):
  if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
  elif n % 3 == 0:
    print("Fizz")
  elif n % 5 == 0:
    print("Buzz")
  else:
    print(n)
