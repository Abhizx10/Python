"""
All About Strings (Edabit)

Create a function that, given a string with at least 3 characters, returns a list of its:
  1. Length.
  2. First character.
  3. Last character.
  4. Middle character, if the string has an odd number of characters. Middle TWO characters, if the string has an even number of characters.
  4. Index of the second occurrence of the second character in the format "@ index #" and "not found" if the second character doesn't occur again.
"""
def all_about_strings(txt):
  result = []
  if len(txt)%2==0:
    mid = txt[len(txt)//2 -1 :len(txt)//2 +1]
  else:
    mid = txt[len(txt)//2]
  if txt[1] in txt[2:]:
    index = txt[2:].index(txt[1])
    last = "@ found "+ str(index)
  else:
    last = "not found"
  return [len(txt),txt[0],txt[-1],mid,last]
