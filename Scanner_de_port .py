import sys
import socket

while True:
	ip= str(input("Entrer une IP: "))
	print(f"Scanne de l'IP: '{ip}' en cours...")

	try:
		for port in range(1,300):
			query= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			reply= query.connect_ex((ip, port))
			if reply == 0:
				print(f"{port} est ouvert.")
			query.close()

	except socket.error:
		print("Serveur injoignable")
		sys.exit()

	except socket.gaierror:
		print("Serveur injoignable")
		sys.exit()

	print("\n----------------------------------------------\n")
	continue