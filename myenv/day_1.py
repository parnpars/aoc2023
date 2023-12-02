import re
with open('/Users/parniaparsa/Documents/aoc2023/myenv/input_day_1.txt', "r") as text_file:
    lines = text_file.read().splitlines()
    text_file.close()

values = []

for line in lines:
    digits = ''.join(filter(str.isdigit, line))
    values.append(int(str(digits[0] + digits[len(digits)-1])))
    
summa = 0
for i in range(0, len(values)):    
   summa = summa + values[i]
print(summa)
      
  

