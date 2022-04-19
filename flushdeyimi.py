from time import sleep
a = -1

while True:
	a = int(input("3, 2, 1 or 0 : "))
	if a == 0:
		print("Hello, world!", end='')
		sleep(5)
		print("Bye!!!")

	elif a == 1:
		print("Hello, world!", end='',flush=True)
		sleep(5)
		print("Bye!!!")

	elif a == 2:
		print("Hello, world!",flush=True)
		sleep(5)
		print("Bye!!!")

	elif a==3:
		break

		