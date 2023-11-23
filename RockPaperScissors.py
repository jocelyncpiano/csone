import random
pscore=0
cscore=0
player=0
computer=0
again="Y"
print("Welcome to rock, paper, scissors")
while(again=="Y"):
	player=int(input("Choose: 1)Rock, 2)Paper, 3)Scissors (Enter a number): "))
	computer=random.randint(1,3)
	print("Player chose", end=" ")
	if player==1:
		print("Rock.")
	elif player==2:
		print("Paper.")
	elif player==3:	
		print("Scissor.")

	print("Computer chose", end=" ")
	if computer==1:
		print("Rock.")
	elif computer==2:
		print("Paper.")
	elif computer==3:	
		print("Scissor.")

	if computer==player:
		print("Nobody wins. It is a tie.")
	if computer==1 and player==2:
		pscore+=1
		print("You, the player, wins. Player:", pscore, ", Computer:", cscore)
	if computer==1 and player==3:
		cscore+=1
		print("Computer wins. Player:", pscore, ", Computer:", cscore)
	if computer==2 and player==1:
		cscore+=1
		print("Computer wins. Player:", pscore, ", Computer:", cscore)
	if computer==2 and player==3:
		pscore+=1
		print("You, the player, wins. Player:", pscore, ", Computer:", cscore)
	if computer==3 and player==1:
		pscore+=1
		print("You, the player, wins. Player:", pscore, ", Computer:", cscore)
	if computer==3 and player==2:
		cscore+=1
		print("Computer wins. Player:", pscore, ", Computer:", cscore)
	again=input("Play again? Y/N: ")