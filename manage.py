#!/usr/bin/env python
import os
import sys
import time




if __name__ == '__main__':
    main()


print "Hi what is your name?"

extracted_name = raw_input(" ")
print "It's nice to meet you, " + extracted_name + \
    ". Are you interested in becoming a developer?"

winner_loser = raw_input(" ").lower()
if winner_loser == "yes" or winner_loser == "yeah" or \
   winner_loser == "yea" or winner_loser == "ye" or \
   winner_loser == "yee" or winner_loser == "duh" or \
   winner_loser == "y" or winner_loser == "okay":
    print "You have made the best decision of your life!"
    time.sleep(1)
    print "Are you up for an adventure?"

    winner = raw_input(" ").lower()
    if winner == "yes" or winner == "yeah" or winner == "ok" or\
       winner == "for sure" or winner == "duh" or winner =="y":
        print "I think you have an amazing outlook on life." 
        time.sleep(1)
        print "You will soon be rewarded you for it."
        time.sleep(.7)
        print "Would you consider moving to Thailand?"
        time.sleep(.5)
        print "... $200 a month for a 2 bedroom apartment."
        time.sleep(.6)
        print " You could start an online business there."
        print "And it'd allow you to save a ton of money! Down?"

        adventure = raw_input(" ").lower()
        if adventure == "down" or adventure == "yea" or adventure == \
           "y" or adventure == "yeah" or adventure == "duh":
            print "You are on your way my friend!"
            time.sleep(.3)
            print "You are on the road to success!"
        elif adventure == "yes":
            print "You my friend, are going places!"
            time.sleep(.4)
            print "Can't wait to see where you are in 1 year!"
        elif adventure == "ok":
            print "get more exited, your life is about the change!"
            time.sleep(.2)
            print "For the Better!"
        else:
            print "You should think about it more.."
            time.sleep(.2)
            print " Try to look at it in a positive way"
            
            
    elif winner == "yup" or winner == "maybe":
        print "Well don't get too excited.. "
        time.sleep(1)
        print "I have an idea, what about moving to Thailand?"
        time.sleep(.2)
        print "I hear it's going off for digital nomads"
        time.sleep(.1)
        print "Would you consider moving to Chaing Mai?"
        
        adventurer = raw_input(" ").lower()
        if adventurer == "yes" or adventurer == "yee" or adventurer \
           == "yeah" or adventurer == "ok" or adventurer == "yup" or \
           adventurer == "yea":
            print "You're bout to go down the rabbit hole. Good luck!"            
        else:
            print "Well maybe you're not up for awesome adventures.."
            time.sleep(.3)
            print "Good bye"
            
    elif winner == "definitely":
        print "Amazing! I think you should consider the digital nomad"
        print " lifestyle. Have you been to Thailand?"
        ans_tra = raw_input(" ").lower()
        if ans_tra == "yes" or ans_tra == "yea" or ans_tra == "yee" \
           or ans_tra == "yeah" or ans_tra == "yup" or ans_tra == "duh"\
           or ans_tra == "once" or ans_tra == "long time ago":
            print "Cool so you know its the spot to be for young "
            print "entreprenuers!"
        else:
            print " dude you should look into Chaing Mai, Thailand. "
            time.sleep(.2)
            print "The rent is cheap and tons of internet cafes."
            
    elif winner == "no" or winner == "nope" or winner == "n":
        print "Really?! Well my guess is you might have a lot of "
        print "regrets later in life and that will be unfortunate. "
        time.sleep(.2)
        print "Best of luck mate."
    else:
        print "Dude, I can't understand that,.."
        time.sleep(.1)
        print "And I'm a computer so that's usually not probable."
        
elif winner_loser == "no" or winner_loser == "n" or winner_loser == \
    "no" or winner_loser == "nope":
    print "You have the wrong attitude"
    time.sleep(.2)
    print "well what else are you going to do?!"
    dont_matter = raw_input(" ").lower()
    if dont_matter == "nothing" or dont_matter == "nada":
        print "Sounds like it..  "
        
    elif dont_matter == "something":
        print "ok smart guy..  I doubt it."
    elif dont_matter == "everything":
        print "Mr. Optimistic, where were you a few mins ago?"
    else:
        print "Well I hope you plan works out bc you missed out here"
        
else:
    print "I have no idea what you are trying to say,.."
    time.sleep(.25)
    print "Maybe try again?"
    loser = raw_input(" ").lower()
    if loser == "ok":
        print "Are you up for an adventure?"
        win = raw_input(" ").lower()

        if win == "yes" or win == "yeah" or win == "ok" or win == \
           "for sure" or win == "duh" or win =="y":
            print "I think you have an amazing outlook on life." 
            time.sleep(1)
            print "You will soon be rewarded you for it."
            time.sleep(.7)
            print "Would you consider moving to Thailand?"
            time.sleep(.5)
            print "... $200 a month for a 2 bedroom apartment."
            time.sleep(.6)
            print " You could start an online business there."
            print "And it'd allow you to save a ton of money! Down?"

        adventure = raw_input(" ").lower()
        if adventure == "down" or adventure == "yea" or adventure == \
           "y" or adventure == "yeah" or adventure == "duh":
            print "You are on your way my friend!"
            time.sleep(.3)
            print "You are on the road to success!"
        elif adventure == "yes":
            print "You my friend, are going places!"
            time.sleep(.4)
            print "Can't wait to see where you are in 1 year!"
        elif adventure == "ok":
            print "get more exited, your life is about the change!"
            time.sleep(.2)
            print "For the Better!"
        else:
            print "You should think about it more.."
            time.sleep(.2)
            print " Try to look at it in a positive way"
            
            
    elif loser == "yup" or loser == "maybe":
        print "Well don't get too excited.. "
        time.sleep(1)
        print "I have an idea, what about moving to Thailand?"
        time.sleep(.2)
        print "I hear it's going off for digital nomads"
        time.sleep(.1)
        print "Would you consider moving to Chaing Mai?"
        
        adventurer = raw_input(" ").lower()
        if adventurer == "yes" or adventurer == "yee" or adventurer \
           == "yeah" or adventurer == "ok" or adventurer == "yup" or \
           adventurer == "yea":
            print "You're bout to go down the rabbit hole. Good luck!"            
        else:
            print "Well maybe you're not up for awesome adventures.."
            time.sleep(.3)
            print "Good bye"
            
    elif loser == "definitely":
        print "Amazing! I think you should consider the digital nomad"
        print " lifestyle. Have you been to Thailand?"
        ans_ = raw_input(" ").lower()
        if ans_ == "yes" or ans_ == "yea" or ans_ == "yee" \
           or ans_ == "yeah" or ans_ == "yup" or ans_ == "duh"\
           or ans_ == "once" or ans_ == "long time ago":
            print "Cool so you know its the spot to be for young "
            print "entreprenuers!"
        else:
            print " dude you should look into Chaing Mai, Thailand. "
            time.sleep(.2)
            print "The rent is cheap and tons of internet cafes."
            
    elif loser == "no" or loser == "nope" or loser == "n":
        print "Really?! Well my guess is you might have a lot of "
        print "regrets later in life and that will be unfortunate. "
        time.sleep(.2)
        print "Best of luck mate."

        
        super_down = raw_input(" ").lower()
        if super_down == "yes" or super_down == "yea" or super_down ==\
           "yeah" or super_down == "y":
            print "Now that is what I'm talking about!"
            time.sleep(.3)
            print "Ok, so the game plan is to move to Thailand."
            print "Rent is $200 a month for 2 bedroom apartment."
            time.sleep(.2)
            print "You can learn to program while you are there."
        else:
            print "Well you can lead a camel to water "
            time.sleep(.2)
            print "but you can't make'm drink..   Good luck"
    elif loser == "yes":
        print "Well, good to see your attitude changing"
        time.sleep(.125)
        print "maybe you should re-run the program"

    elif loser == "yeah" or loser == "maybe":
        print "restart the program and be positive this time"

    else:
        print "Well aren't you a downer.."
        








