chemistry=int(input("Enter Chemistry score:"))
biology=int(input("Enter Biology score:"))
physics=int(input("Enter Physics score:"))
math=int(input("Enter Math score:"))
english=int(input("Enter English score:"))
kiswahili=int(input("Enter Kiswahili score:"))
history=int(input("Enter History score:"))
score=(chemistry+biology+physics+math+english+kiswahili+history)/7
if (score>=0 and score <=39):
   print("You Failed")
elif (score>=40 and score <=49):
   print("Your have a D")
elif (score>=50 and score <=59):
   print("Your have a C")      
elif (score>=60 and score <=69):
   print("Your have a B")
elif (score>=70 and score <=100):
   print("Your have an A") 
else:
    print("Error")        