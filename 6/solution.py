def main(bigstr,smallstr):

  bigstr_dict = {}

  for char in bigstr:
    if char not in bigstr_dict:
      bigstr_dict[char] = 1
    else:
      bigstr_dict[char] += 1
  
  for char in smallstr:
    if char in bigstr_dict and bigstr_dict[char] != 0:
      bigstr_dict[char] -= 1
      
    else:
      return False
  
  return True