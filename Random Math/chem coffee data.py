moreCoffee = 'y'
shotAmount = []
shotTime = []
while moreCoffee == 'y':
    shotTime.append(int(input("When do you have coffee (24hr time): ")))
    shotAmount.append(int(input("Amount of shots: ")))
    moreCoffee = input("Is there more coffee in your day(y/n): ")
shotTime.append(int(input("Bedtime (24hr time): ")))
mm = 194.22
shot = 7
constanth = 10
start = 0
life = constanth + 5 * (shotAmount[0] - 1)
decay = shotAmount[0]*shot / life
for count in range(len(shotAmount)):
    start = shotAmount[0]*shot + start
    start = start - decay*(shotTime[count+1]-shotTime[count])
print(f"The amount of grams of caffeine still in your body is {start}g")
print(f"The amount of moles of caffeine still in your body is {start/mm} moles")
