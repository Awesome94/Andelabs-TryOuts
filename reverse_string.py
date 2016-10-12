def reverse_string(string):
  reversed_string = string[::-1]
  if len(string) == 0:
    return None
  elif reversed_string == string:
    return True
  else:
    return reversed_string