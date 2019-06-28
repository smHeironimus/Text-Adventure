import random
import time
from PIL import Image

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
    time.sleep(3)
    print('You can see a feint light inside and hear what appears to be the rattling of bones.')
    time.sleep(3)
    print('You wonder to yourself if you should enter the castle as you have heard stories '
          'of otherworldly horrors living inside.')
    time.sleep(2)
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
    room_one_image = Image.open('images/Room 1.png')
    room_one_image.show()
    print('You enter through the large doors and see that you can only go "North" or "East" to move on.')
    user_direction = input('Which direction do you want to go? (North|East)')
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

    # room_two_image = Image.open('images/Room 2.png')
    # room_two_image.show()

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
            time.sleep(2)
            player_hp = player_hp - 1
            time.sleep(1)
            print('You swing you sword again.')
            time.sleep(2)
        elif player_damage == 1:
            damage_hit = random.randint(1, 5)
            print('Your sword connects and hits the skeleton for %s damage' % damage_hit)
            skeleton_one_hp = skeleton_one_hp - damage_hit
            time.sleep(2)
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

    # room_three_image = Image.open('images/Room 3.png')
    # room_three_image.show()

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

    # print('DEBUG -- start of function, no key only potions ' + str(player_backpack))
    # room_four_image = Image.open('images/Room 4.png')
    # room_four_image.show()

    if 'Skeleton Key' in player_backpack:
        # print('DEBUG -- Key already in bag if here ' + str(player_backpack))
        # print('What direction would you like to go now? (East|South)')
        print('You enter the room again. What direction do you want to go? (East|South)')
        user_direction = input()
        if user_direction == 'East' or user_direction == 'east':
            print('You approach the door, weapon ready because you know a fight is coming.')
            room_five()
        elif user_direction == 'South' or user_direction == 'south':
            print('You return to the previous room.')
            room_three()
        else:
            print('Please enter a valid input.')
            room_four()
    else:
        # print('DEBUG -- about to add key to bag ' + str(player_backpack))
        print('Entering the room, you notice light shining through a small window.')
        time.sleep(2)
        print('The light is illuminating a small pedestal and what appears to be a shiny skeleton key.')
        time.sleep(3)
        print('You hesitate, but take the key and add it to your pack.')
        time.sleep(2)
        print('You think to yourself how this might be important later on.')
        player_backpack.append('Skeleton Key')
        print('You currently have ' + str(player_backpack) + ' in your bag.')
        # print('DEBUG -- key has been added to the bag ' + str(player_backpack))
        print('What direction would you like to go now? (East|South)')
        user_direction = input()
        if user_direction == 'East' or user_direction == 'east':
            print('You approach the door, weapon ready because you know a fight is coming.')
            room_five()
        elif user_direction == 'South' or user_direction == 'south':
            print('You return to the previous room.')
            room_three()
        else:
            print('Please enter a valid input.')
            room_four()


def room_five():
    global skeleton_two_hp
    global player_hp
    global player_backpack

    room_five_image = Image.open('images/Room 5.png')
    room_five_image.show()

    if skeleton_two_hp >= 1:
        print('Another skeleton has appeared and threatens you.')
        time.sleep(2)
        print('Quickly dispatch your foe to move on.')
    else:
        print('The skeleton remains a pile of bones.')
        time.sleep(1)
        print('You continue on your quest. What direction do you go? (East|South)')
        user_direction = input()
        if user_direction == 'East' or user_direction == 'east':
            room_four()
        elif user_direction == 'South' or user_direction == 'south':
            room_six()
        else:
            print('Please enter a valid direction')
            room_two()

    while skeleton_two_hp > 0:
        print('The skeleton has %sHP left' % skeleton_two_hp)
        player_damage = random.randint(0, 2)
        if player_damage == 0:
            print('The skeleton dodges your attack and takes a swing at you, dealing 2 damage.')
            time.sleep(2)
            player_hp = player_hp - 2
            time.sleep(1)
            print('You swing you sword again.')
            time.sleep(2)
        elif player_damage == 1:
            damage_hit = random.randint(1, 5)
            print('Your sword connects and hits the skeleton for %s damage' % damage_hit)
            skeleton_two_hp = skeleton_two_hp - damage_hit
            time.sleep(2)
            # print('The skeleton has %sHP left' % skeleton_one_hp)
            if skeleton_two_hp <= 0:
                room_five()
        else:
            print('With a mighty swing of your sword, you slice right through the skeleton and'
                  ' send him back to the grave.')
            skeleton_two_hp = 0
            room_five()


def room_six():
    global skeleton_three_hp
    global player_hp
    global player_backpack

    room_six_image = Image.open('images/Room 6.png')
    room_six_image.show()

    if skeleton_three_hp >= 1:
        print('Really, another skeleton blocking my way?.')
        time.sleep(2)
        print('Quickly dispatch your foe to move on.')
    else:
        print('The skeleton remains a pile of bones.')
        time.sleep(1)
        print('You continue on your quest. What direction do you go? (North|South)')
        user_direction = input()
        if user_direction == 'North' or user_direction == 'North':
            room_five()
        elif user_direction == 'South' or user_direction == 'south':
            room_seven()
        else:
            print('Please enter a valid direction')
            room_six()

    while skeleton_three_hp > 0:
        print('The skeleton has %sHP left' % skeleton_three_hp)
        player_damage = random.randint(0, 2)
        if player_damage == 0:
            print('The skeleton dodges your attack and takes a swing at you, dealing 2 damage.')
            time.sleep(2)
            player_hp = player_hp - 2
            time.sleep(1)
            print('You swing you sword again.')
            time.sleep(2)
        elif player_damage == 1:
            damage_hit = random.randint(1, 5)
            print('Your sword connects and hits the skeleton for %s damage' % damage_hit)
            skeleton_three_hp = skeleton_three_hp - damage_hit
            time.sleep(2)
            # print('The skeleton has %sHP left' % skeleton_one_hp)
            if skeleton_two_hp <= 0:
                room_six()
        else:
            print('With a mighty swing of your sword, you slice right through the skeleton and'
                  ' send him back to the grave.')
            skeleton_three_hp = 0
            room_six()


def room_seven():
    global player_hp
    global player_backpack

    room_seven_image = Image.open('images/Room 7.png')
    room_seven_image.show()

    print('Another empty room.')
    time.sleep(1)
    if player_hp < 25:
        print('You notice you are wounded from the previous skeletons.')
        time.sleep(1)
        print('Would you like to drink a health potion? (Yes|No)')
        user_decision = input()
        if user_decision == 'Yes' or user_decision == 'yes':
            player_hp = 25
            time.sleep(2)
            print('You currently have ' + str(player_backpack) + ' in your bag.')
            # print(player_backpack)
            # print(player_hp)
            print('What direction do you want to go now? (North|South|East|West)')
            user_direction = input()
            if user_direction == 'North' or user_direction == 'north':
                print('You push the heavy door open revealing the next room.')
                room_six()
            elif user_direction == 'South' or user_direction == 'south':
                print('You turn back and return to the previous room.')
                room_eight()
            elif user_direction == 'East' or user_direction == 'east':
                print('You turn back and return to the previous room.')
                room_nine()
            elif user_direction == 'West' or user_direction == 'west':
                print('You turn back and return to the previous room.')
                room_two()
            else:
                print('Please enter a valid input')
                room_seven()
        elif user_decision == 'No' or user_decision == 'no':
            print('Good idea, save those for later if something larger comes along.')
            print('What direction do you want to go now? (North|South|East|West)')
            user_direction = input()
            if user_direction == 'North' or user_direction == 'north':
                print('You push the heavy door open revealing the next room.')
                room_six()
            elif user_direction == 'South' or user_direction == 'south':
                print('You turn back and return to the previous room.')
                room_eight()
            elif user_direction == 'East' or user_direction == 'east':
                print('You turn back and return to the previous room.')
                room_nine()
            elif user_direction == 'West' or user_direction == 'west':
                print('You turn back and return to the previous room.')
                room_two()
            else:
                print('Please enter a valid input')
                room_seven()
        else:
            print('Please enter a valid input.')
            room_seven()
    else:
        print('What direction do you want to go now? (North|South|East|West)')
        user_direction = input()
        if user_direction == 'North' or user_direction == 'north':
            print('You walk through the doorway into the previous room.')
            room_six()
        elif user_direction == 'South' or user_direction == 'south':
            print('You push the heavy door open revealing the next room.')
            room_eight()
        elif user_direction == 'East' or user_direction == 'east':
            print('You push the heavy door open revealing the a new room.')
            room_nine()
        elif user_direction == 'West' or user_direction == 'west':
            print('You push the heavy door open revealing the a previous room.')
            room_two()
        else:
            print('Please enter a valid input')
            room_seven()


def room_eight():
    global player_backpack

    room_eight_image = Image.open('images/Room 8.png')
    room_eight_image.show()

    print('No enemies in this room, but there are some boxes in the corner.')
    time.sleep(2)
    print('Would you like to investigate the boxes? (Yes|No)')
    user_decision = input()
    if user_decision == 'Yes' or user_decision == 'yes':
        print('You walk over to the boxes and start rummaging around.')
        time.sleep(5)
        print('Still digging, you\'re not finding much of value.')
        time.sleep(5)
        print('About to stop looking, you come across three health potions.')
        time.sleep(1)
        print('You add them to your bag.')
        print('DEBUG -- ' + str(player_backpack) + 'items in your bag')
        player_backpack.append('Health Potion')
        player_backpack.append('Health Potion')
        player_backpack.append('Health Potion')
        print('DEBUG -- ' + str(player_backpack) + 'items in your bag after "finding" them')
        print('What direction do you want to go now? (West|North)')
        user_direction = input()
        if user_direction == 'West' or user_direction == 'wests':
            room_one()
        elif user_direction == 'North' or user_direction == 'north':
            room_seven()
        else:
            print('Please enter a valid input.')
            room_eight()
    elif user_decision == 'No' or user_decision == 'no':
        print('Are you sure?')
        time.sleep(1)
        print('There might be something of value over there.')
        time.sleep(1)
        print('Oh well, I tried to help.')
        time.sleep(2)
        print('What direction do you want to go now? (West|North)')
        user_direction = input()
        if user_direction == 'West' or user_direction == 'west':
            room_one()
        elif user_direction == 'North' or user_direction == 'north':
            room_seven()
        else:
            print('Please enter a valid input.')
            room_eight()
    else:
        print('Please enter a valid input.')
        room_eight()


def room_nine():
    global player_backpack
    global player_hp

    room_nine_image = Image.open('images/Room 9.png')
    room_nine_image.show()

    print('Another empty room, feels like we are getting deeper into the castle.')
    time.sleep(1)
    if player_hp < 25:
        print('You notice you are wounded from the previous skeletons.')
        time.sleep(1)
        print('Would you like to drink a health potion? (Yes|No)')
        user_decision = input()
        if user_decision == 'Yes' or user_decision == 'yes':
            player_hp = 25
            time.sleep(2)
            print('You currently have ' + str(player_backpack) + ' in your bag.')
            # print(player_backpack)
            # print(player_hp)
            print('What direction do you want to go now? (South|West)')
            user_direction = input()
            if user_direction == 'South' or user_direction == 'south':
                print('You hear more rattling bones through the door.')
                time.sleep(1)
                print('But this time it sounds different, like it is a much larger skeleton.')
                room_ten()
            elif user_direction == 'West' or user_direction == 'west':
                print('You turn back and return to the previous room.')
                room_seven()
            else:
                print('Please enter a valid input')
                room_nine()
        elif user_decision == 'No' or user_decision == 'no':
            print('Good idea, save those for later if something larger comes along.')
            print('What direction do you want to go now? (South|West)')
            user_direction = input()
            if user_direction == 'South' or user_direction == 'south':
                print('You hear more rattling bones through the door.')
                time.sleep(1)
                print('But this time it sounds different, like it is a much larger skeleton.')
                room_ten()
            elif user_direction == 'West' or user_direction == 'west':
                print('You turn back and return to the previous room.')
                room_seven()
            else:
                print('Please enter a valid input')
                room_nine()
        else:
            print('Please enter a valid input.')
            room_nine()
    else:
        print('What direction do you want to go now? (South|West)')
        user_direction = input()
        if user_direction == 'South' or user_direction == 'south':
            print('You hear more rattling bones through the door.')
            time.sleep(1)
            print('But this time it sounds different, like it is a much larger skeleton.')
            room_ten()
        elif user_direction == 'West' or user_direction == 'west':
            print('You turn back and return to the previous room.')
            room_seven()
        else:
            print('Please enter a valid input')
            room_nine()


def room_ten():
    global player_hp
    global large_skeleton_hp

    room_ten_image = Image.open('images/Room 10.png')
    room_ten_image.show()

    if large_skeleton_hp >= 1:
        print('A very large and menacing skeleton is stands in your way.')
        time.sleep(1)
        print('Take care of this big guy to move on.')
    else:
        print('The skeleton remains a large pile of bones.')
        time.sleep(1)
        print('You may move on. Your choices are "North" or "East" again.')
        user_direction = input()
        if user_direction == 'North' or user_direction == 'north':
            room_nine()
        elif user_direction == 'East' or user_direction == 'east':
            room_eleven()
        else:
            print('Please enter a valid direction')
            room_ten()

    while large_skeleton_hp > 0:
        print('The skeleton has %sHP left' % large_skeleton_hp)
        player_damage = random.randint(0, 2)
        if player_damage == 0:
            print('The skeleton dodges your attack and takes a swing at you, dealing 5 damage.')
            time.sleep(2)
            player_hp = player_hp - 5
            time.sleep(1)
            print('You swing you sword again.')
            time.sleep(2)
        elif player_damage == 1:
            damage_hit = random.randint(1, 5)
            print('Your sword connects and hits the skeleton for %s damage' % damage_hit)
            large_skeleton_hp = large_skeleton_hp - damage_hit
            time.sleep(2)
            # print('The skeleton has %sHP left' % skeleton_one_hp)
            if large_skeleton_hp <= 0:
                room_ten()
        else:
            print('With a mighty swing of your sword, you slice right through the skeleton and'
                  ' send him back to the grave.')
            large_skeleton_hp = 0
            room_ten()


def room_eleven():
    global player_hp
    global player_backpack

    room_one_image = Image.open('images/Room 11.png')
    room_one_image.show()

    if player_hp < 25:
        print('You notice you are wounded from the previous skeletons.')
        time.sleep(1)
        print('Would you like to drink a health potion? (Yes|No)')
        user_decision = input()
        if user_decision == 'Yes' or user_decision == 'yes':
            player_hp = 25
            # print(player_backpack)
            # print(player_hp)
            print('What direction do you want to go now? (North|West)')
            user_direction = input()
            if user_direction == 'North' or user_direction == 'north':
                print('You push the heavy door open revealing the next room.')
                room_twelve()
            elif user_direction == 'West' or user_direction == 'west':
                print('You turn back and return to the previous room.')
                room_ten()
            else:
                print('Please enter a valid input')
                room_eleven()
        elif user_decision == 'No' or user_decision == 'no':
            print('Are you sure?')
            time.sleep(1)
            print('This might be your last chance to heal up to 100%.')
            time.sleep(1)
            print('What direction do you want to go now? (North|West)')
            user_direction = input()
            if user_direction == 'North' or user_direction == 'north':
                print('You push the heavy door open revealing the next room.')
                room_twelve()
            elif user_direction == 'West' or user_direction == 'west':
                print('You turn back and return to the previous room.')
                room_ten()
        else:
            print('Please enter a valid input.')
            room_ten()
    else:
        print('What direction do you want to go now? (North|West)')
        user_direction = input()
        if user_direction == 'North' or user_direction == 'north':
            print('You push the heavy door open revealing the next room.')
            room_twelve()
        elif user_direction == 'West' or user_direction == 'west':
            print('You turn back and return to the previous room.')
            room_ten()
        else:
            print('Please enter a valid input')
            room_eleven()


def room_twelve():
    global player_backpack

    room_twelve_image = Image.open('images/Room 12.png')
    room_twelve_image.show()

    print('The door is locked.')
    if 'Skeleton key' in player_backpack:
        print('This must be the door that is unlocked by the key I found earlier.')
        time.sleep(1)
        print('You insert the key into the lock.')
        time.sleep(2)
        print('As the door unlocks, the key crumbles in your hands.')
        player_backpack.remove('Skeleton Key')
        # print('DEBUG -- ' + str(player_backpack) + ' after removing key')
        print('What direction do you want to go now? (North|South)')
        user_direction = input()
        if user_direction == 'North' or user_direction == 'north':
            print('This is it, the final fight of the castle.')
            boss_room()
        elif user_direction == 'South' or user_direction == 'south':
            print('Why are you turning around? Aren\'t yuou ready for the final fight?')
            room_eleven()
    else:
        print('The door appears to be locked.')
        time.sleep(1)
        print('I must\'ve missed a room from earlier with a key.')
        # print('HINT: It is in one of the earlier rooms.')
        print('What direction do you want to go now? (South)')
        user_direction = input()
        if user_direction == 'South' or user_direction == 'south':
            print('I better find that key.')
            room_eleven()
        elif user_direction == 'North' or user_direction == 'north':
            print('The door is still locked, I really need that key.')
            room_twelve()
        else:
            print('Please enter a valid input.')
            room_twelve()


def boss_room():
    global player_hp
    global dragon_hp

    room_thirteen_image = Image.open('images/Room 13.png')
    room_thirteen_image.show()

    if dragon_hp >= 1:
        print('This is it, the final foe of your quest.')
        time.sleep(1)
        print('Be careful of this mighty beast.')
    else:
        print('The dragon remains dead on the floor.')
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

    while dragon_hp > 0:
        print('The skeleton has %sHP left' % dragon_hp)
        player_damage = random.randint(0, 2)
        if player_damage == 0:
            print('The mighty dragon swiftly dodges your attack and swipes at you with '
                  'his massive claws, dealing 8 damage to you.')
            time.sleep(2)
            player_hp = player_hp - 8
            time.sleep(1)
            print('You swing you sword again.')
            time.sleep(2)
        elif player_damage == 1:
            damage_hit = random.randint(1, 5)
            print('Your sword connects and hits the dragon for %s damage' % damage_hit)
            dragon_hp = dragon_hp - damage_hit
            time.sleep(2)
            # print('The dragon has %sHP left' % dragon_hp)
            if dragon_hp <= 0:
                congrats()
        else:
            print('Masterfully dodging the dragon\'s attacks, you managed to get up close '
                  'and thrust your sword into its chest, slaying the mighty beast.')
            dragon_hp = 0
            congrats()


def congrats():
    print('Congratulations! You have successfully made your way through the castle.')
    time.sleep(3)
    print('You return to the King with the dragon\'s head as proof of completing your quest.')
    time.sleep(3)
    print('They shall sing songs of how valiantly you fought for ages to come.')
    time.sleep(5)
    print('Would you like to play again? (Yes|No)')
    user_decision = input()
    if user_decision == 'Yes' or user_decision == 'yes':
        start()
    elif user_decision == 'No' or user_decision == 'no':
        print('Thank you for playing.')
        time.sleep(2)
        quit()
    else:
        print('Please enter a valid input.')
        congrats()


# def test():
#     global player_backpack
#
#     print(player_backpack)
#     if 'Skeleton Key' in player_backpack:
#         print('key already in backpack')
#         test()
#     else:
#         print([player_backpack])
#         print('adding key to backpack')
#         player_backpack.append('Skeleton Key')
#         print(player_backpack)
#         test()

