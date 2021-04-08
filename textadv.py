import random

print('Hello fellow adventurer!') 
input()
print('Welcome to the G&K adventure game, a wannabe D&D!')  
input()
player_name = str(input('But first, how shall we call you? ' ))
print('Welcome aboard', player_name) 
input()
warrior_atr = [12, 5, 4] # hp, sword attack, dagger attack
barbarian_atr = [14, 6, 3] # hp, axe attack, bow attack
goblin1_atr = [7, 3, 4] # hp, dagger attack, knife attack
goblin2_atr = [8, 4, 3] # hp, dagger attack, knife attack
player_class = str(input('You must choose your class. Press \'W\' if you wanna be a warrior or \'B\' if you wanna be a barbarian.' ))
print('Our adventure starts in a tavern.')  
input()
print('You are sitting at the corner corner table. You watch the world moving around, eating , having fun you while thinking that they don\'t know anything about you. How many times you have sacrificed so much to save this beautiful city you call home.')  
input()
print('You see a man wearing a black hood entering the tavern. He seems quite suspicious. He heads at your table and asks "are you the', player_name, ', the one that every hero talks about?".')  
input()
print('You answer "Yes, that\'s me".') 
input()
print('He then says "You know, there is a great threat that is heading to the city and we definitely need your help".')  
input()
print('"Of course i\'d be more than happy to help", you answer')  
input()
print('"There are two goblins heading here that are the biggest thiefs of the land. We know where they are hiding and we need your help.", the mysterious character says.')  
input()
print('"Of course, i am heading there right now", you say.')  
input()
print('You prepare your weapons, and go to the goblin nest, you see these two behind a fire laughing and drinking. You are 10 metres away. You wanna go closer, or no?   Answer with Y or N.')

def fight(lst):
    while warrior_atr[0] > 0 and barbarian_atr[0] > 0:
        while goblin1_atr[0] > 0 or goblin2_atr[0] > 0: 
            num = random.randint(1,6)
            print(num)
            input()
            if num % 2 == 0:
                print('You attack first!')
                first = True
            else:
                print('The goblin attacks first')
                first = False
            if first:
                if goblin1_atr[0] > 0:
                    if player_class == 'W':
                        print('You wanna use your sword or your dagger?    Answer with S or D')
                        weaponw = str(input())
                        if weaponw == 'S':
                            print('You deal', warrior_atr[1], 'damage to the goblin')
                            goblin1_atr[0] -= warrior_atr[1]
                            if goblin1_atr[0] <= 0:
                                print('You knocked out the first goblin!')
                        elif weaponw == 'D':
                            print('You deal', warrior_atr[2], 'damage to the goblin')
                            goblin1_atr[0] -= warrior_atr[2]
                            if goblin1_atr[0] <= 0:
                                print('You knocked out the first goblin!')
                    elif player_class == 'B':
                        print('You wanna use your axe or your bow?    Answer with A or B')
                        weaponb = str(input())
                        if weaponb == 'A':
                            print('You deal', barbarian_atr[1], 'damage to the goblin')
                            goblin1_atr[0] -= barbarian_atr[1]
                            if goblin1_atr[0] <= 0:
                                print('You knocked out the first goblin!')
                        elif weaponb == 'B':
                            print('You deal', barbarian_atr[2], 'damage to the goblin')
                            goblin1_atr[0] -= barbarian_atr[2]
                            if goblin1_atr[0] <= 0:
                                print('You knocked out the first goblin!')
                elif goblin2_atr[0] > 0:
                    if player_class == 'W':
                        print('You wanna use your sword or your dagger?    Answer with S or D')
                        weaponw = str(input())
                        if weaponw == 'S':
                            print('You deal', warrior_atr[1], 'damage to the goblin')
                            goblin2_atr[0] -= warrior_atr[1]
                            if goblin2_atr[0] <= 0:
                                print('You knocked out the second goblin!')
                        elif weaponw == 'D':
                            print('You deal', warrior_atr[2], 'damage to the goblin')
                            goblin2_atr[0] -= warrior_atr[2]
                            if goblin2_atr[0] <= 0:
                                print('You knocked out the second goblin!')
                    elif player_class == 'B':
                        print('You wanna use your axe or your bow?    Answer with A or B')
                        weaponb = str(input())
                        if weaponb == 'A':
                            print('You deal', barbarian_atr[1], 'damage to the goblin')
                            goblin2_atr[0] -= barbarian_atr[1]
                            if goblin2_atr[0] <= 0:
                                print('You knocked out the second goblin!')
                        elif weaponb == 'B':
                            print('You deal', barbarian_atr[2], 'damage to the goblin')
                            goblin2_atr[0] -= barbarian_atr[2]
                            if goblin2_atr[0] <= 0:
                                print('You knocked out the second goblin!')
            elif not first:
                goblinnum = random.randint(1, 2)
                if goblinnum == 1:
                    print('The first goblin attacks first!')
                    weapong = goblin1_atr[random.randint(1, 2)]
                    print('The first goblin deals', weapong, 'damage to you.')
                    if player_class == 'W':
                        warrior_atr[0] -= weapong
                    else:
                        barbarian_atr[0] -= weapong
                    if warrior_atr[0] <= 0 or barbarian_atr[0] <= 0:
                        break

                elif goblinnum == 2:
                    print('The second goblin attacks first!')
                    weapong = goblin2_atr[random.randint(1, 2)]
                    print('The second goblin deals', weapong, 'damage to you.')
                    if player_class == 'W':
                        warrior_atr[0] -= weapong
                    else:
                        barbarian_atr[0] -= weapong
                    if warrior_atr[0] <= 0 or barbarian_atr[0] <= 0:
                        break
        else:
            print('You succesfully took out the goblins. Good job hero!')
            break
    else:
        print('I\'m sorry hero but you died. We \'ll get \'em next time...')


move1 = str(input())
if move1 == 'Y':
    print('As you move closer, you step on a branch of a tree and the goblins are now aware of you, prepare for a fight!!')
    if player_class == 'W':
        fight(warrior_atr)
    elif player_class == 'B':
        fight(barbarian_atr)
elif move1 == 'N':
    print('You stay where you are, but one of the goblins is coming closer to you forr some reason. You wanna attack him, or you wanna hide?     Answer with A or H.')
    move2 = str(input())
    if move2 == 'A':
        print('Prepare for a fight!')
        if player_class == 'W':
            fight(warrior_atr)
        elif player_class == 'B':
            fight(barbarian_atr)
    else:
        print('As the goblin comes closer to you, he takes out a torch and unfortunately sees you.')
        print('Prepare for a fight!')
        if player_class == 'W':
            fight(warrior_atr)
        elif player_class == 'B':
            fight(barbarian_atr)