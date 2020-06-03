import random

print("welcome to snake, water, gun game")
a = [ "s", "w", "g"]
print('number of chance is 10')
chance = 1
y = 0
z = 0
print("s for snake, \ng for gun, \nw for water \n")
while (chance<=10):
	b = random.choice(a)
	x = input("you choce:-  ")
	if x == "s" and b == "s":
		print('draw')
	elif x == "w" and b == "w":
		print('draw')
	elif x == "g" and b == "g":
		print('draw')
	elif x == "g" and b == "s":
		print('you win')
		y = y + 1
	elif x == "g" and b == "w":
		print('you lose')
		z = z + 1
	elif x == "s" and b == "g":
		print('you lose')
		z = z + 1
	elif x == "s" and b == "w":
		print('you win')
		y = y + 1
	elif x == "w" and b == "g":
		print('you win')
		y = y + 1
	elif x == "w" and b == "s":
		print('you lose')
		z = z + 1
	else:
		print("not attempt you lose one chance")
		z = z + 1
	chance = chance + 1
	
print('you have complited you chance and', end=" ")
k = 10 - y - z
if y > z:
	print('you win😂😂😂😂😂😂😂😂😂')
elif y == z:
	print('draw🤬🤬🤬🤬🤬🤬')
else:
	print('you lose😭😭😭😭😭😭😭😭😭 ')
print(f"you win {y} times, \nloses {z} times, \ndraw {k} times")