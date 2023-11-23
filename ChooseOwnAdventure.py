print("Intro: you are hiking in Zion National Park.")
print("There are two trails that you can take, one towards Angels landing, the other that leads to a river in a narrow canyon.")
print("What do you do? \n1. Take the trail to Angel's landing \n2. Take the trail toward the river")
choice = int(input("Answer: "))

def Angels_Landing():
    print("\nSo you start walking up the switchback of the first section of the trail. You hear a slight rumble.")
    print("As you look up, several boulders have broken free of the overhanging cliff, and they are tumbling toward you.")
    print("What do you do? \n1. Scream and run away \n2. Stay put and see what happens")
    
def Boulder_Scream():
    print("\nYou run away and as you run aimlessly down the hill, you see a split in the path ahead.")
    print("One path goes left into a large crevice in the rock.") 
    print("The other goes down and right into a flat area with many shrubs and bushes. What should you do?")
    print("1. Go left. \n2. Go right.")

def Go_Right():
    print("\nThe boulders continue to roll toward you. A giant log is lying in its path, stopping the boulder.")
    print("You sigh with relief. But now you're lost and you don't know where to go. What should you do?")
    print("1. Look for shade and then wait for help. \n2. Mark the area where you're standing and then scout your surroundings.")

def Into_Shade():
    print("\nYou found a large enough shrub that you get some shade. You make attempts to scream and shout for help, but no one comes.") 
    print("There is enough water for you to last for another five hours. You wait for five hours, and as night comes, you don't know what to do. You ate all the food you brought with you.")
    print("So you stay there, and an animal finds you. You are eaten alive and the next day the search and rescue team finds your remains. The end.")

def Mark_Area():
    print("\nYou make a large pile of sticks, rocks, and dead plants. Then you start making your way around the area, carefully going in a circle around the center. ")
    print("You found the path! You excitedly make your way down the path and get into your car. Congratulations! You stayed alive.")

def Go_Left(): 
    print("\nYou make your way into the crevice. Everything immediately feels cooler and you begin to relax.")
    print("The boulders continue rolling past the crevice, but you begin to smell something strange. It smells like dead animals.")
    print("You slowly realize what you've gotten yourself into, but it's too late. A bear slowly comes out of the shadows, growling menacingly.")
    print("You back away, but the bear lunges, and all you see is a bright flash of immense pain, and then nothing.")
    print("Congratulations, you suceeded in dying. Try again next time.")

def Stay_Put():
    print("\nSurprisingly, all the boulders go past you. There are clouds gathering, but it shouldn't be a big threat. You are now wondering if you should keep going or turn back.")
    print("What do you do? \n1. Keep going \n2. Turn back")

def Keep_Going():
    print("\nSo you keep going. It starts to rain a bit, but it's no big deal.")
    print("You make it to the top, and you've reached the chain section of the trail where you must hold onto chains while there is a thousand foot drop on either side of you. ")
    print("So you start climbing the chain section, and you are enjoying the exhilarating feeling from the dizzying view in front of and below you. You make it to the end and take pictures. What a hike!")
    print("You turn around to head back, but as you are holding the chain and carefully climbing the rock, your foot slips on a loose stone. You lose your balance and your hands let go of the chain.")
    print("You have fallen off the cliff to your death. Congratulations on dying. ")

def Turn_Back(): 
    print("\nYou turn back. Well, you chose the non-dangerous path, but you still die. You were bitten by a snake and although you went to the hospital, there was nothing they could do. The end.")

def Narrow_river(): 
    print("\nYou decide to take the path to the river. There is a weather alert on your phone, saying that there is a 30 percent chance of rain.")
    print("The river can possibly flood if there is too much rain. What should you do?")
    print("1. Turn back around and decide not to hike today. \n2. Decide to keep going anyway.")

def No_Hiking():
    print("\nYou decide to turn back. You got into the car and start driving back home, but the storm catches up to you and it starts raining.") 
    print("Your car slipped on the wet pavement and you die from a giant car accident. The end.")

def Keep_Going_River():
    print("\nYou start wading in the water along with many other people who are taking the same route. The clouds are darkening, but there is no trouble yet.")
    print("You continue to walk and wade downstream, and you notice that the water is very slowly rising. You wonder if it is from the storm. Do you continue?")
    print("1. No, I should turn back. \n2. Yes, I'll just keep going")

def Turn_Back_River():
    print("\nYou decide to turn back. You got into the car and start driving back home, but the storm catches up to you and it starts raining.") 
    print("Your car slipped on the wet pavement and you die from a giant car accident. The end.")

def Keep_Going_Downstream():
    print("\nYou keep going. It starts to rain and the waters are continuing to rise. You can't turn back because the waters are now too high and there is a strong current. ")
    print("Many other people are screaming and being swept away. You have strong legs, but you can't hold on much longer. Then you spot a rock that is higher than the river. But ahead, there is also a large sand bar.")
    print("What do you do? \n1. Climb the rock \n2. Get to the sand bar")

def Climb_Rock():
    print("\nYou climb the rock and the waters continue to rise. The storm worsens. Thunder shakes the ground and lightning streaks across the sky.")
    print("The people below are struggling to stay afloat, and you don't know if you can hold out much longer. The waters are about to reach the rock where you stand.")
    print("You see a giant log floating towards you. Do you use the log to stay afloat or do you stay on the rock?")
    print("1. Climb on the log \n2. Stay on the rock")

def Log_Float():
    print("\nYou climb on the log and you float downstream. You don't know where you're going to go, but you know that at least you'll stay afloat.")
    print("The storm then begins to lighten. You continue to float downstream, and you find a hill that leads upward. You get off your log and find other campers stranded on the hill.")
    print("You join them and wait together for help. When the rangers find you, you are taken back. ")
    print("Congratulations, you survived!")

def Stay_Rock():
    print("\nYou stay on the rock, but the waters still rise. So you try to climb higher on the steep slope, but it's too slippery.")
    print("You slip into the water. You try to swim but the current is too strong.")
    print("So you die from drowning. Too bad so sad :()")

def Sand_bar():
    print("\nYou go to the sand bar, and the waters continue to rise. The storm worsens. Thunder shakes the ground and lightning streaks across the sky. The waters begin to creep up the sand bar until the water is up to your neck.")
    print("You are swept downstream and you hit a boulder. White light flashes across your vision and then blackness.")
    print("You died because your skull cracked. The end. ") 

if choice==1:
    Angels_Landing()
    choice_angels_landing = int(input("Answer: "))
    if choice_angels_landing==1:
        Boulder_Scream()
        choice_boulder = int(input("Answer: "))
        if choice_boulder==1:
            Go_Left()
        if choice_boulder==2:
            Go_Right()
            choice_go_right = int(input("Answer: "))
            if choice_go_right==1:
                Into_Shade()
            if choice_go_right==2:
                Mark_Area()
    if choice_angels_landing==2:
        Stay_Put()
        choice_stay_put = int(input("Answer: "))
        if choice_stay_put==1:
            Keep_Going()
        if choice_stay_put==2:
            Turn_Back()
if choice==2:
    Narrow_river()
    choice_river = int(input("Answer: "))
    if choice_river==1:
        No_Hiking()
    if choice_river==2:
        Keep_Going_River()
        choice_keep_going_river = int(input("Answer: "))
        if choice_keep_going_river==1:
            Turn_Back_River()
        if choice_keep_going_river==2:
            Keep_Going_Downstream()
            choice_downstream = int(input("Answer: "))
            if choice_downstream==1:
                Climb_Rock()
                choice_climb_rock = int(input("Answer: "))
                if choice_climb_rock==1:
                    Log_Float()
                if choice_climb_rock==2:
                    Stay_Rock()
            elif choice_downstream==2:
                Sand_bar()
