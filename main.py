import random
import time

player_hp = 25
skeleton_one_hp = 10
skeleton_two_hp = 10
skeleton_three_hp = 10
large_skeleton_hp = 15
dragon_hp = 30
player_backpack = ['Health Potion', 'Health Potion', 'Health Potion']


def main():
    print('You find yourself on a quest from the King to explore this so called "abandoned" castle.')
    print('Wearing your protective plate armor and wielding your trusty long sword, '
          'you approach the large castle doors.')
    #time.sleep(2)
    print('You can see a feint light inside and hear what appears to be the rattling of bones.')
    #time.sleep(3)
    print('You wonder to yourself if you should enter the castle as you have heard stories '
          'of otherworldly horrors living inside')
    #time.sleep(2)
    start()


def start():
    print('Complete the quest the King has sent you on? (Yes|No)')
    user_confirm = input()
    if user_confirm == 'Yes' or user_confirm == 'yes':
        room_one()
    elif user_confirm == 'No'or user_confirm == 'no':
        print('You cowardly turn around and run back to your King empty handed.')
        quit()
    else:
        print('Please enter "Yes" or "No"')
        start()


def room_one():
    print('You enter through the large doors and see that you can only go "North" or "East" to move on.')
    user_direction = input('Which direction do you want to go? (North|East')
    if user_direction == 'North' or user_direction == 'north':
        room_two()
    elif user_direction == 'East' or user_direction == 'east':
        room_eight()
    else:
        print('Please enter a valid direction')
        room_one()


def room_two():
    global skeleton_one_hp
    global player_hp

    if skeleton_one_hp >= 1:
        print('A skeleton appears to blocking your progression to other rooms.')
        time.sleep(1)
        print('Quickly dispatch your foe to move on.')
    else:
        print('The skeleton remains a pile of bones.')
        time.sleep(1)
        print('You may move on. Your choices are "North" or "East" again.')
        user_direction = input()
        if user_direction == 'North' or user_direction == 'north':
            room_three()
        elif user_direction == 'East' or user_direction == 'east':
            room_seven()
        else:
            print('Please enter a valid direction')
            room_two()

    while skeleton_one_hp > 0:
        print('The skeleton has %sHP left' % skeleton_one_hp)
        player_damage = random.randint(0, 2)
        if player_damage == 0:
            print('The skeleton dodges your attack and takes a swing at you, dealing 1 damage.')
            player_hp = player_hp - 1
            time.sleep(1)
            print('You swing you sword again.')
            time.sleep(1)
        elif player_damage == 1:
            damage_hit = random.randint(1, 5)
            print('Your sword connects and hits the skeleton for %s damage' % damage_hit)
            skeleton_one_hp = skeleton_one_hp - damage_hit
            # print('The skeleton has %sHP left' % skeleton_one_hp)
            if skeleton_one_hp <= 0:
                room_two()
        else:
            print('With a mighty swing of your sword, you slice right through the skeleton and'
                  ' send him back to the grave.')
            skeleton_one_hp = 0
            room_two()


def room_three():
    global player_hp
    global player_backpack

    print('You find yourself in another dark and cold room with only a door in front of you.')
    time.sleep(1)
    print('Thankfully, the room appears to be empty. You question your choices of taking this quest.')
    time.sleep(1)
    if player_hp < 25:
        print('You notice you are wounded from the previous skeleton.')
        time.sleep(1)
        print('Would you like to drink a health potion? (Yes|No)')
        user_decision = input()
        if user_decision == 'Yes' or user_decision == 'yes':
            player_hp = 25
            # print(player_backpack)
            # print(player_hp)
            print('What direction do you want to go now? (North|South)')
            user_direction = input()
            if user_direction == 'North' or user_direction == 'north':
                print('You push the heavy door open revealing the next room.')
                room_four()
            elif user_direction == 'South' or user_direction == 'south':
                print('You turn back and return to the previous room.')
                room_two()
            else:
                print('Please enter a valid input')
                room_three()
        elif user_decision == 'No' or user_decision == 'no':
            print('Good idea, save those for later if something larger comes along.')
            print('What direction do you want to go now? (North|South)')
            user_direction = input()
            if user_direction == 'North' or user_direction == 'north':
                print('You push the heavy door open revealing the next room.')
                room_four()
            elif user_direction == 'South' or user_direction == 'south':
                print('You turn back and return to the previous room.')
                room_two()
        else:
            print('Please enter a valid input.')
            room_three()
    else:
        print('What direction do you want to go now? (North|South)')
        user_direction = input()
        if user_direction == 'North' or user_direction == 'north':
            print('You push the heavy door open revealing the next room.')
            room_four()
        elif user_direction == 'South' or user_direction == 'south':
            print('You turn back and return to the previous room.')
            room_two()
        else:
            print('Please enter a valid input')
            room_three()


def room_four():
    global player_backpack

    print('Entering the room, you notice light shining through a small window.')
    print('The light is illuminating a small pedestal and what appears to be a shiny skeleton key.')
    time.sleep(3)
    print('You hesitate, but take the key and add it to your pack.')
    print('You think to yourself how this might be important later on.')
    player_backpack.append('Skeleton Key')
    # print(player_backpack)
    print('The familiar sound of bones rattling is coming from the next room.')
    print('What direction would you like to go now? (East|South')
    user_direction = input()
    if user_direction == 'East' or user_direction == 'east':
        print('You approach the door, weapon ready because you know a fight is coming.')
        room_five()
    elif user_direction == 'South' or user_direction == 'south':
        print('You return to the previous room.')
    else:
        print('Please enter a valid input.')
        room_four()


def room_five():
    print('')


def room_six():
    print('')


def room_seven():
    print('')


def room_eight():
    print('')


def room_nine():
    print('')


def room_ten():
    print('')


def eleven():
    print('')


def room_twelve():
    print('')


def boss_room():
    print('')


#main()
#room_two()
room_three()
#room_four()
#room_five()