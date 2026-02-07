import re

def password_strength(password):

  letter = re.search("[a-zA-Z]", password)
  digit = re.search("\d", password) 
  special = re.search("[@#$_!]", password)

  length = len(password)

  score = 0

  if length > 6:
    score += 1
  if length > 8:
    score += 1 
  if length > 10: 
    score += 1

  if letter and digit:
    score += 1
  if letter and special:
    score += 1

  if digit and special:
    score += 1

  if letter and digit and special:
    score += 1

  if length > 12:
    score += 1

  print("Password Strength: ", end="")

  if score < 1:
    print("Very Weak")
  elif score >= 1 and score < 3:
    print("Weak")
  elif score >= 3 and score < 5: 
    print("Good")
  else:
    print("Strong")

  return score

password = input("Enter password: ")

password_strength(password)