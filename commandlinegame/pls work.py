print("You wake from a foggy dream.")
print("Looking around, you are in a dense forest")
print("You quickly stand and see a large, hooded figure standing before you.")
print("'Welcome, Mortal. What are you called?'")
# I wanted to set the scene before offering input
name = input ('Enter Your Name: ')
print(f"'Hail, {name}'")
start = input('Will you join me, or will you perish here? ')
if start == 'join':
    print("'Wise choice. Let us begin.'")
    setting = input('Shall we visit the shaman or the Queen first? ')
else:
    print('Your vision becomes blurry as the hooded figure runs you through with a dagger... Ending 1/ ') # ending 1
    quit()

# first branch 
if setting == 'shaman':
    print('You travel down a small road to an ancient looking hut in the meadow.The hooded figure asks you to wait outside while they enter the hut...')
    response = input('You wait impatiently outside, but all you hear is silence. Do you enter the hut or do you wait? ')
    if response == 'enter':
        print('You approach the hut and go inside. It\'s completely empty... ')
        transport = input('You see a trap door open in the back of the hut. Climb down or leave? ')
        if transport == 'climb down':
            print('You climb down a rickety old ladder into a dark tunnel.')
            response = input('As your eyes adjust, you see the hooded figure walking with a hunched old man. You follow them down the tunnel until you enter a large room.')
            response = input('The hooded figure turns to you as you enter the room and removes their hood. It\'s the Queen!')
            response = input('You listen as she tells you how the royal ruby went missing and she is searching for it. Help her or leave? ')
            if response == 'help her':
                print('You agree to help her. She thanks you, and you follow her to the opposite side of the room through a giant door.')
                print('She shows you a map where she got intel that the Redbrand gang took the ruby to one of their hideouts. Head to the first hideout or to the second one? ')
                if response == 'first':
                    print('The Queen hands you a sword and gives you a map to the first hideout. Good Luck!')
                    response = input('When you get there, you scope out the abandoned house. Do you go charging in or sneak in? ')
                    if response == 'Charge in':
                        print('You charge in with your sword held high. The guard dogs immediately run at you and leap for your throat! Ending 5/') # ending 5
                    elif response == 'sneak in':
                        print('You quietly sneak around the back and through an open door. You see the ruby sitting on a table with no one in sight...')
                        print('Grabbing the ruby, you sneak back out and return to the Queen. She gives you a plot of land, a house and 1000 gold pieces. You win! Ending 6/')  #  ending 6
               if response == 'second':
                   print('The Queen gives you a horse to ride into the countryside to the cave hideout. As you approach, you see it\'s full of goblins. Search the cave or go to second hideout?  ')        
        elif transport == 'leave':
            print('You turn around and find yourself face to face with a tiger - No where to run! Ending 2/ ') # ending 2
            quit()               
    elif response == 'wait':
        print('You wait another 10 minutes but the hooded figure still hasn\'t come ')
        transport = input('You see a tiger stalking you in the field. Run to the hut or freeze? ')
        if transport == 'run':
            print('You sprint to the hut as the tiger leaps and slam the door in its face. It snarls and starts to tear at the door. You see a trap door open. Climb down or hope for the best? ')
            if response == 'climb down':
                print('You climb down a rickety old ladder into a dark tunnel.')         
            elif response == 'hope for the best':
                print('You hunker down in the corner, and the tiger tears through the door. CHOMP! Ending 3/') # ending 3
        elif transport == 'freeze':
                print('You hunker down in the bushes, but the tiger is already on your trail. It pounces! Ending 4/') # ending 4
                quit()     
            
                
                  
    
        
        
        
# second branch (4 options)
if setting == 'General':
    print('You travel to a meadow within the forest to see a giant castle. The hooded figure tells you to wait as they approach the guards and go inside..')
    response == input('You wait impatiently as the sun starts to beat down. Do you approach the guards or do you wait?')
    if response == 'approach':
        print('You approach the guards, but they point their spears at you and tell you to stop.')
    elif response == 'wait':
        print('You find a shady spot under a tree to keep waiting')
    else:
        print('Invalid response. You lose!')
    
    
    