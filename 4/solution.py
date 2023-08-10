import re

def main(str):

  separators = r'[\s,.;]+'
  words = re.split(separators, str)
  fixed_str: str = ''
  for word in words:
    fixed_str += word.capitalize()
    fixed_str += " "
  return fixed_str[:-1]
