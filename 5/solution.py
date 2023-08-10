def pad_num(num):
  formatted_num = int(num)
  if formatted_num <= 9:
    return f'0{num}'
  else:
    return num
  
def main(seconds):
  formatted_time = ''
  if seconds < 0:
    formatted_time = '-'
  abs_seconds = abs(seconds)
  hours = abs_seconds // 3600
  minutes = (abs_seconds // 60) % 60
  seconds_left = abs_seconds - (minutes * 60) - (hours * 3600)
  formatted_time += f'{hours}:{pad_num(minutes)}:{pad_num(seconds_left)}'
  return formatted_time