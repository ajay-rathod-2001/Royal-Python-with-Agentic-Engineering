while True:
	user_input = input("Enter a Command for software (start/stop/pause): ")
	match user_input:
		case "start":
			print("Software is Running.....!💥💫")
		case "stop":
			print("Software is Stop.....❌")
		case "pause":
			print("Software is Paused....⚡")
		case _:
			print("Invalid Command, Please Enter the Valid Command")

	sw_stop = input(f"Do you want to stop the programm? (yes/no)")

	if sw_stop == "yes":
		break
