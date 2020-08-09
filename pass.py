#Offcar 2020
import random
pass_input = list(input("Input: ").replace(" ",""))
output = []
for i in range(0,len(pass_input)):
    item = random.choice(pass_input) 
    output.append(item)
    pass_input.remove(item)
print("Output:",''.join(map(str, output)))
