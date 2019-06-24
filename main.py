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
    user_direction = input('Which direction do you want to go?')
    if user_direction == 'North' or user_direction == 'north':
        room_two()
    elif user_direction == 'East' or user_direction == 'east':
        room_eight()
    else:
        print('Please enter a valid direction')
        room_one()


def room_two():
    global skeleton_one_hp
    # skeleton_alive = True

    if skeleton_one_hp >= 1:
        print('A skeleton appears to blocking your progression to other rooms.')
        time.sleep(1)
        print('Quickly dispatch your foe to move onto the next room.')
        time.sleep(1)
    else:
        print('The skeleton from earlier is still dead, good.')
        time.sleep(1)
        print('You may move on. Your choices are "North" or "East" again.')
        user_direction = input()
        if user_direction == 'North' or user_direction == 'north':
            room_three()
        elif user_direction == 'East' or user_direction == 'east':
            room_seven()
        else:
            print('Please enter a valid direction')
            room_one()

    while skeleton_one_hp > 0:
        print('The skeleton has %sHP left' % skeleton_one_hp)
        damage = random.randint(0, 2)
        if damage == 0:
            print('The skeleton dodges your attack.')
            time.sleep(1)
            print('You swing you sword again.')
            time.sleep(1)
        elif damage == 1:
            damage_hit = random.randint(1, 5)
            print('Your sword connects and hits the skeleton for %s damage' % damage_hit)
            skeleton_one_hp = skeleton_one_hp - damage_hit
            print('The skeleton has %sHP left' % skeleton_one_hp)
            if skeleton_one_hp <= 0:
                room_two()
        else:
            print('In one mighty swing of your sword, you slice right through the skeleton and'
                  ' send him back to the grave.')
            skeleton_one_hp = 0
            room_two()


def room_three():
    print('Room 3')


def room_four():
    damage = random.randint(0, 2)
    print(damage)


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
room_two()