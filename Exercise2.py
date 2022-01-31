John=170
Alice=172
Bob=150
print("John=170")
print("Alice=172")
print("Bob =150") 

if (John >= Alice) and (John >= Bob):
   largest = John
elif (Alice >= John) and (Alice >= Bob):
   largest = Alice
else:
   largest = Bob

print("The largest number is", largest)