coffee = int(input("How many coffees do you have: "))
shotAmount = []
shotTime = []
for i in range(coffee):
    shotTime.append(float(input("When do you have coffee (24hr time): ")))
    shotAmount.append(float(input("Amount of shots: ")))
shotTime.append(float(input("Bedtime (24hr time): ")))
mm = 194.22
shot = 0.095
start = 0
life = 10 + 5 * (shotAmount[0] - 1)
decay = shotAmount[0]*shot / life
for count in range(len(shotAmount)):
    start = shotAmount[0]*shot + start
    start = start - decay*(shotTime[count+1]-shotTime[count])
print(f"The amount of grams of caffeine still in your body is {start}g")
print(f"The amount of moles of caffeine still in your body is {start/mm} moles")
molecules = str(start/mm*(6*(10**23)))
print(molecules)
print(f"You have {molecules[0:6]} x 10^{molecules[len(molecules)-2:len(molecules)]} "
      f"molecules of caffeine in your body when you go to bed")
