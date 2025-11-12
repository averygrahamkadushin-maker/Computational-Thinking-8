Lebron_points = 0 
J_points = 0

Answer = input("would you reather meet A.) M.J , or B) Lebron" )
if Answer == "A":
    Lebron_points += 1
elif Answer == "B":
    J_points += 1

Answer = input("are u a) scorer, or B) a passer" )
if Answer == "A":
    J_points += 1
elif Answer == "B":
    Lebron_points += 1

Answer = input("in your  free time would you rather A Play basketball , or B) just chill")
if Answer  == "A" :
    J_points += 1 
elif Answer == "B":
    Lebron_points += 1

Answer = input("Finally do u even like basketball A ) Yes , or B) no")
if Answer == "A":
    J_points += 1
elif Answer == "B":
    Lebron_points += 1

Answer + input("if u like jordans better than lebrons A)Yes, or B) dont")
if Answer == "A":
    J_points += 1
elif Answer == "B":
    Lebron_points += 1

print ("good job answering my questions")

if Lebron_points > J_points:
    print ("you are a lebron person")
if J_points > Lebron_points:
    Print ("you are a j person")


Print ("thanks for doing this and you are great ")