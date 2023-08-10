import re

def main(str):
  separators = r'[\s,.;]+'
  words = re.split(separators, str)
  fixed_str: str = ''
  for word in words:
    fixed_str += word.capitalize()
    fixed_str += " "
  return fixed_str[:-1]
  
# def main(str):
#   ret=""
#   first_letter=True
#   for c in str:
#     if first_letter: ret+=c.upper()
#     else: ret+=c.lower()
#     first_letter= (c in " ,.;")
#   return ret 
