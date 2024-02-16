# Day 10 Ecercises - Functions with outputs
def name_format(first_name, last_name):
  """This is a description of name_format function"""  
  formatted_name = first_name.title() + " " + last_name.title()
  return formatted_name

name = name_format("aNGELA", "yu")
print(name)

# Number of days in a month prediction
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # print("Leap year")
        return True
      else:
        # print("Not leap year")
        return False
    else:
      # print("Leap year")
      return True
  else:
    # print("Not leap year")
    return False

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2:
    if is_leap(year):
      return month_days[month-1] + 1
    else:
      return month_days[month-1]
  else:
    return month_days[month-1]

year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)
