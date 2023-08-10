import re

def main(sentence):
  longest_word:str = ""
  # max_word_lenght:int = len(longest_word)
  pattern = r'\s|[,.;:\'"()\{\}]'
  sentence_into_list = re.split(pattern, sentence)

  for word in sentence_into_list:
    if len(word) > len(longest_word):
      longest_word = word
  return longest_word