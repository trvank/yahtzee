# Copyright (c) 2014 Thomas Van Klaveren
# Build a single player Yahtzee game GUI

from tkinter import *
from random import randrange
from functions import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        #set initial dice to all blank
        self.dice_results = [0] * 5
        #set remaining rolls to 3
        self.rem_roll = 3
        #set mult_yahtzee to 0 (will increment if a second yahtzee is rolled)
        self.mult_yahtzee = 0
        #set turn to 0, will increment after each "sumbmit"
        self.turn = 0
        #set check to 0, will increment if more than one radio button is 
        #cliked in a turn.  if check > 0, the score will revert to previous
        #score and re-evaluate new selceted score card item
        self.check = 0

        #import dice images
        self.dice0 = PhotoImage(file =\
             '/home/vthomas/Desktop/Python/Classwork/yahtzee/0.png')
        self.dice1 = PhotoImage(file =\
             '/home/vthomas/Desktop/Python/Classwork/yahtzee/1.png')
        self.dice2 = PhotoImage(file =\
             '/home/vthomas/Desktop/Python/Classwork/yahtzee/2.png')
        self.dice3 = PhotoImage(file =\
             '/home/vthomas/Desktop/Python/Classwork/yahtzee/3.png')
        self.dice4 = PhotoImage(file =\
             '/home/vthomas/Desktop/Python/Classwork/yahtzee/4.png')
        self.dice5 = PhotoImage(file =\
             '/home/vthomas/Desktop/Python/Classwork/yahtzee/5.png')
        self.dice6 = PhotoImage(file =\
             '/home/vthomas/Desktop/Python/Classwork/yahtzee/6.png')

        #points dictionary to keep track of points for each score card item
        #each score card item initialized to 0
        self.points = {"ones": 0, "twos": 0, "threes": 0, "fours": 0,\
             "fives": 0, "sixes": 0, "bonus": 0, "total1": 0, "three_kind": 0,\
             "four_kind": 0, "full_house": 0, "sm_straight": 0,\
             "lg_straight": 0, "chance": 0, "yahtzee": 0, "yahtzee_bonus": 0,\
             "total2": 0, "total_score": 0}

        #initialize widgets through function
        self.create_widgets()

    def create_widgets(self):
        #dice start out as blanc dice image at start of each turn
        self.die1 = Label(self, image = self.dice0)
        self.die1.grid(row = 0, column = 0)
        self.die2 = Label(self, image = self.dice0)
        self.die2.grid(row = 0, column = 1)
        self.die3 = Label(self, image = self.dice0)
        self.die3.grid(row = 0, column = 2)
        self.die4 = Label(self, image = self.dice0)
        self.die4.grid(row = 0, column = 3)
        self.die5 = Label(self, image = self.dice0)
        self.die5.grid(row = 0, column = 4)

        # each hold button corresponds to a die and, when selected,
        # will prevent that die from being rolled in the turn
        self.held1 = BooleanVar()
        self.hold1 = Checkbutton(self, text = "Hold", variable = self.held1)
        self.hold1.grid(row = 1, column = 0)
        self.held2 = BooleanVar()
        self.hold2 = Checkbutton(self, text = "Hold", variable = self.held2)
        self.hold2.grid(row = 1, column = 1)
        self.held3 = BooleanVar()
        self.hold3 = Checkbutton(self, text = "Hold", variable = self.held3)
        self.hold3.grid(row = 1, column = 2)
        self.held4 = BooleanVar()
        self.hold4 = Checkbutton(self, text = "Hold", variable = self.held4)
        self.hold4.grid(row = 1, column = 3)
        self.held5 = BooleanVar()
        self.hold5 = Checkbutton(self, text = "Hold", variable = self.held5)
        self.hold5.grid(row = 1, column = 4)

        # Roll button can be pressed 3 times per turn.  When pressed, the
        # dice will call the roll dice function and return a random dice value.
        # If hold pressed, that dice will remain at its current dice value
        # until turn ends
        self.roll = Button(self, text = "Roll (" + str(self.rem_roll) + ")",\
                           command = self.roll_dice)
        self.roll.grid(row = 2, column = 2)

        # Create the Score Card as radiobuttons and value label
        # so that the user can select the options and see point values
        # before submitting
        self.card = StringVar()
        self.card.set(None)
        
        # Label boxes for the point values
        #First side of the score card
        self.ones_val = Label(self, text = str(self.points["ones"]))
        self.ones_val.grid(row = 3, column = 1)

        self.twos_val = Label(self, text = str(self.points["twos"]))
        self.twos_val.grid(row = 4, column = 1)

        self.threes_val = Label(self, text = str(self.points["threes"]))
        self.threes_val.grid(row = 5, column = 1)

        self.fours_val = Label(self, text = str(self.points["fours"])) 
        self.fours_val.grid(row = 6, column = 1)

        self.fives_val = Label(self, text = str(self.points["fives"]))
        self.fives_val.grid(row = 7, column = 1)

        self.sixes_val = Label(self, text = str(self.points["sixes"]))
        self.sixes_val.grid(row = 8, column = 1)

        self.bonus_val = Label(self, text =\
             str(self.points["bonus"]), font = "bold")
        self.bonus_val.grid(row = 9, column = 1)

        self.total1_val = Label(self, text =\
             str(self.points["total1"]), font = "bold")
        self.total1_val.grid(row = 10, column = 1)
       
        # second half of score card
        self.three_kind_val = Label(self, text = str(self.points["three_kind"]))
        self.three_kind_val.grid(row = 3, column = 4)

        self.four_kind_val = Label(self, text = str(self.points["four_kind"]))
        self.four_kind_val.grid(row = 4, column = 4)

        self.full_house_val = Label(self, text = str(self.points["full_house"]))
        self.full_house_val.grid(row = 5, column = 4)

        self.sm_straight_val = Label(self,\
             text = str(self.points["sm_straight"]))
        self.sm_straight_val.grid(row = 6, column = 4)

        self.lg_straight_val = Label(self,\
             text = str(self.points["lg_straight"]))
        self.lg_straight_val.grid(row = 7, column = 4)

        self.yahtzee_val = Label(self, text = str(self.points["yahtzee"]))
        self.yahtzee_val.grid(row = 8, column = 4)
  
        self.chance_val = Label(self, text = str(self.points["chance"]))
        self.chance_val.grid(row = 9, column = 4)

        self.yahtzee_bonus_val = Label(self, text =\
             str(self.points["yahtzee_bonus"]), font = "bold")
        self.yahtzee_bonus_val.grid(row = 10, column = 4)
 
        self.total2_val = Label(self, text = str(self.points["total2"]), \
             font = "bold")
        self.total2_val.grid(row = 11, column = 4)
        
        #Radiobuttons call the give_val function to show the impact of the
        #selected item on the score
        #First side of the score card
        self.ones = Radiobutton(self, text = "1s", variable = self.card,\
                    value = "ones", command = self.give_val)
        self.ones.grid(row = 3, column = 0)

        self.twos = Radiobutton(self, text = "2s", variable = self.card,\
                    value = "twos", command = self.give_val)
        self.twos.grid(row = 4, column = 0)

        self.threes = Radiobutton(self, text = "3s", variable = self.card,\
                    value = "threes", command = self.give_val)
        self.threes.grid(row = 5, column = 0)

        self.fours = Radiobutton(self, text = "4s", variable = self.card,\
                    value = "fours", command = self.give_val)
        self.fours.grid(row = 6, column = 0)

        self.fives = Radiobutton(self, text = "5s", variable = self.card,\
                    value = "fives", command = self.give_val)
        self.fives.grid(row = 7, column = 0)

        self.sixes = Radiobutton(self, text = "6s", variable = self.card,\
                    value = "sixes", command = self.give_val)
        self.sixes.grid(row = 8, column = 0)

        self.bonus = Label(self, text = "Bonus", font = "bold")
        self.bonus.grid(row = 9, column = 0)

        self.total1 = Label(self, text = "Total", font = "bold")
        self.total1.grid(row = 10, column = 0)
       
        # second half of score card
        self.three_kind = Radiobutton(self, text = "3 of a Kind",\
           variable = self.card, value = "three kind", command = self.give_val)
        self.three_kind.grid(row = 3, column = 3)

        self.four_kind = Radiobutton(self, text = "4 of a Kind",\
           variable = self.card, value = "four kind", command = self.give_val)
        self.four_kind.grid(row = 4, column = 3)

        self.full_house = Radiobutton(self, text = "Full House",\
           variable = self.card, value = "full house", command = self.give_val)
        self.full_house.grid(row = 5, column = 3)

        self.sm_straight = Radiobutton(self, text = "Sm Straight",\
           variable = self.card, value = "sm straight", command = self.give_val)
        self.sm_straight.grid(row = 6, column = 3)

        self.lg_straight = Radiobutton(self, text = "Lg Straight",\
           variable = self.card, value = "lg straight", command = self.give_val)
        self.lg_straight.grid(row = 7, column = 3)

        self.yahtzee = Radiobutton(self, text = "YAHTZEE",\
           variable = self.card, value = "yahtzee", command = self.give_val)
        self.yahtzee.grid(row = 8, column = 3)
  
        self.chance = Radiobutton(self, text = "Chance",\
           variable = self.card, value = "chance", command = self.give_val)
        self.chance.grid(row = 9, column = 3)

        #Yahtzee bonus label - not selectable score card item, auto-calc
        self.yahtzee_bonus = Label(self, text = "YAHTZEE Bonus", font = "bold")
        self.yahtzee_bonus.grid(row = 10, column = 3)
 
        #total for 2nd half of score card - not selectable, auto-calc
        self.total2 = Label(self, text = "Total", font = "bold")
        self.total2.grid(row = 11, column = 3)

        #final score, not selectable item, auto calc
        self.final_score = Label(self, text = "Score: "\
             + str(self.points["total_score"]), font = \
             "Helvetica 18 bold italic")
        self.final_score.grid(row = 13, column = 2, columnspan = 3, sticky = W)

        # Submit button will call the submit command which will finalize the
        # user selected score card item and begin the next turn.  Enabled
        # after score card item is selected
        self.submit = Button(self, text = "Submit",\
            command = self.submit_command, state = "disabled")
        self.submit.grid(row = 12, column = 2)

    # Roll dice command from the Roll button
    def roll_dice(self):
        # update remaining rolls for the turn on roll button
        self.rem_roll -= 1
        self.roll.configure(text = "Roll (" + str(self.rem_roll)+ ")")
        
        # disable the roll button if no more rolls in the turn
        if self.rem_roll == 0:
            self.roll.configure(state = "disabled")

        # update the dice values thorugh the check_hold function
        self.check_hold(self.die1, self.held1, 0, self.dice_results)
        self.check_hold(self.die2, self.held2, 1, self.dice_results)
        self.check_hold(self.die3, self.held3, 2, self.dice_results)
        self.check_hold(self.die4, self.held4, 3, self.dice_results)
        self.check_hold(self.die5, self.held5, 4, self.dice_results)

        #determine if special instances of Bonus Yahtzee

        #determine if all dice are same value
        dice_vals = same_val_check(self.dice_results)

        # if additional Yahtzee, inc mult_yahtzee and assign scores
        if dice_vals[0] == 5 and self.mult_yahtzee < 1 and\
           self.points["yahtzee"] == 50:
            self.mult_yahtzee += 1
            self.points["yahtzee_bonus"] += 100
            self.points["total2"] += 100
            self.points["total_score"] += 100
            self.yahtzee_bonus_val.configure(text =\
                 self.points["yahtzee_bonus"])
            self.total2_val.configure(text = self.points["total2"])
            self.final_score.configure(text = self.points["total_score"])

        # if user rolls on a Yahtzee bonus and gets another Yahtzee on the
        # same turn, no additional Yahtzee bonus added to score - just
        # the original yahtzee bonus for the turn
        elif dice_vals[0] == 5 and self.mult_yahtzee > 0 and\
             self.points["yahtzee"] == 50:
            self.mult_yahtzee += 1

        # if user rolls on a Yahtzee bonus and does not get another 
        # Yahtzee, the Yahtzee bonus is lost (subtract from score/total)
        # decrease mult_yahtzee 
        elif dice_vals[0] != 5 and self.mult_yahtzee > 0 and\
             self.points["yahtzee"] == 50:
            self.mult_yahtzee -= 1
            self.points["yahtzee_bonus"] -= 100
            self.points["total2"] -= 100
            self.points["total_score"] -= 100
            self.yahtzee_bonus_val.configure(text =\
                 self.points["yahtzee_bonus"])
            self.total2_val.configure(text = self.points["total2"])
            self.final_score.configure(text = self.points["total_score"])


    # Check hold value and update dice (in roll_dice)
    def check_hold(self, die, held, position, dice_list):
        #verify that the die is not held
        if not held.get():
            #if not held, get a random dice value and assign to that die
            dice_list[position] = randrange(1,7)
            #based on the die value, update the image of the dice
            if dice_list[position] == 1:
                die.configure(image = self.dice1)
            elif dice_list[position] == 2:
                die.configure(image = self.dice2)
            elif dice_list[position] == 3:
                die.configure(image = self.dice3)
            elif dice_list[position] == 4:
                die.configure(image = self.dice4)
            elif dice_list[position] == 5:
                die.configure(image = self.dice5)
            elif dice_list[position] == 6:
                die.configure(image = self.dice6)


    # updates score cared points temporarily when a score card item is selected
    def give_val(self):
        #make a copy of the current points dictionary
        points2 = self.points.copy()

        #set val to zero (val is the points that will be added to score card)
        val = 0

        #dice total calls the dice sum function which adds total dice value
        dice_total = dice_sum(self.dice_results)

        #dice vals calls the same_val_check function which returns a list of
        #number of same values
        dice_vals = same_val_check(self.dice_results)

        #create a list to iterate over when calculating and returning points
        nums = [["ones", 1, self.ones_val], ["twos", 2, self.twos_val],\
               ["threes", 3, self.threes_val], ["fours", 4, self.fours_val],\
                ["fives", 5, self.fives_val], ["sixes", 6, self.sixes_val]]

        #create a list to itereate over when reverting temp points back to 
        #previous values.  Only utilized when a new score card item
        #is selected in the same turn.
        point_vals = [["ones", self.ones_val], ["twos", self.twos_val],\
             ["threes", self.threes_val], ["fours", self.fours_val],\
             ["fives", self.fives_val], ["sixes", self.sixes_val],\
             ["bonus", self.bonus_val], ["total1", self.total1_val], \
             ["three_kind", self.three_kind_val],\
             ["four_kind", self.four_kind_val],\
             ["full_house", self.full_house_val],\
             ["sm_straight", self.sm_straight_val],\
             ["lg_straight", self.lg_straight_val],\
             ["yahtzee", self.yahtzee_val], ["chance", self.chance_val],\
             ["yahtzee_bonus", self.yahtzee_bonus_val],\
             ["total2", self.total2_val], ["total_score", self.final_score]]

        #if this is not the first score card item selected in this turn,
        #revert the score back to previous finalized score in points dictionary
        if self.check > 0:
            for e in point_vals:
                e[1].configure(text = self.points[e[0]])

        #if the score card item selected is a number, iterate over nums list
        #to see which number is selected
        for e in range(len(nums)):
            if self.card.get() == nums[e][0]:
                #for the number selected, iterate over the dice and assign
                #the point value for the number to val
                for i in self.dice_results:
                    if i == nums[e][1]:
                        val += 1 * nums[e][1]
                #assign val to the copied points dictionary for the item
                points2[nums[e][0]] = val
                #increase the temp total1 by val
                points2["total1"] += val
                #increase the temp end score by val
                points2["total_score"] += val
                #update the label for the item, total, and score for user
                nums[e][2].configure(text = points2[nums[e][0]])
                self.total1_val.configure(text = points2["total1"])
                self.final_score.configure(text\
                     = "Score: " + str(points2["total_score"]))
                #increment check value so that if user selects a different
                #score card item, the points will revert to prior values
                self.check += 1

        #if user selects three of a kind
        if self.card.get() == "three kind":
            #and if the dice has at least 3 of the same dice value,
            #assign the sum of the dice to val
            for i in range(3,6):
                if i in dice_vals:
                    val = dice_total
            #update temporary points dictionary for 3 of a kind, total2, score
            points2["three_kind"] = val
            points2["total2"] += val
            points2["total_score"] += val
            #update the points label to show user points impact
            self.three_kind_val.configure(text = points2["three_kind"])
            self.total2_val.configure(text = points2["total2"])
            self.final_score.configure(text\
                 = "Score: " + str(points2["total_score"]))
            #update check value for revert
            self.check +=1

        #if user selects four of a kind
        elif self.card.get() == "four kind":
            #and if the dice has at least 4 of same dice value,
            #assign the sum of dice to val
            for i in range(4,6):
                if i in dice_vals:
                    val = dice_total
            #update temp points dictionary for 4 of a kind, total2 and score
            points2["four_kind"] = val
            points2["total2"] += val
            points2["total_score"] += val
            #update the points label to show user points impact
            self.four_kind_val.configure(text = points2["four_kind"])
            self.total2_val.configure(text = points2["total2"])
            self.final_score.configure(text\
                 = "Score: " + str(points2["total_score"]))
            #increment check value for revert
            self.check +=1

        #if user selects full house
        elif self.card.get() == "full house":
            #and if dice values are either full house or bonus yahtzee,
            #assign point value 25 to val
            if 3 in dice_vals and 2 in dice_vals:
                val = 25
            elif 5 in dice_vals and 0 not in self.dice_results and\
            points2["yahtzee"] == 50:
                val = 25
            #update temp dictionary for full house, total2, and score
            points2["full_house"] = val
            points2["total2"] += val
            points2["total_score"] += val
            #update labels to show user point impact
            self.full_house_val.configure(text = points2["full_house"])
            self.total2_val.configure(text = points2["total2"])
            self.final_score.configure(text =\
                 "Score: " + str(points2["total_score"]))
            #increment check value for revert
            self.check += 1

        #if user selects small straight
        elif self.card.get() == "sm straight":
            #and if 4 incrementing dice values are rolled (or bonus yahtzee)
            #assign point value 30 to val
            for i in range(1,7):
                if i in self.dice_results and i+1 in self.dice_results\
                   and i+2 in self.dice_results and i+3 in self.dice_results:
                    val = 30
                elif 5 in dice_vals and 0 not in self.dice_results and\
                points2["yahtzee"] == 50:
                    val = 30
            #update temp dictionary points for sm staraight, total2, and score
            points2["sm_straight"] = val
            points2["total2"] += val
            points2["total_score"] += val
            #update sm staraight, total and score labels to show user points
            self.sm_straight_val.configure(text = points2["sm_straight"])
            self.total2_val.configure(text = points2["total2"])
            self.final_score.configure(text\
                 = "Score: " + str(points2["total_score"]))
            #increment check value for revert
            self.check += 1

        #if user selects large straight
        elif self.card.get() == "lg straight":
            #and if all dice increment by 1 (or bonus yahtzee)
            #assign point value 40 to val
            for i in range(1,7):
                if i in self.dice_results and i+1 in self.dice_results\
                and i+2 in self.dice_results and i+3 in self.dice_results\
                and i+4 in self.dice_results:
                    val = 40
                elif 5 in dice_vals and 0 not in self.dice_results and\
                points2["yahtzee"] == 50:
                    val = 40
            #update temp dictionary for lg straight, total2 and score
            points2["lg_straight"] = val
            points2["total2"] += val
            points2["total_score"] += val
            #update label to show user points for lg straight, total, score
            self.lg_straight_val.configure(text = points2["lg_straight"])
            self.total2_val.configure(text = points2["total2"])
            self.final_score.configure(text\
                 = "Score: " + str(points2["total_score"]))
            #increment check value for revert
            self.check += 1

        #if user selects chance
        elif self.card.get() == "chance":
            #assign sum of dice to val
            val = dice_total
            #update temp dictionary for chance, total2, and score
            points2["chance"] = val
            points2["total2"] += val
            points2["total_score"] += val
            #update labels to show user points for chance, total, score
            self.chance_val.configure(text = points2["chance"])
            self.total2_val.configure(text = points2["total2"])
            self.final_score.configure(text\
                 = "Score: " + str(points2["total_score"]))
            #increment check value for revert
            self.check += 1

        #if user selects yahtzee
        elif self.card.get() == "yahtzee":
            #and if all 5 dice are the same value
            #assign point value 50 to val
            if 5 in dice_vals and 0 not in self.dice_results:
                val = 50
            #update temp dictionary for yahtzee, total2, and score
            points2["yahtzee"] = val
            points2["total2"] += val
            points2["total_score"] += val
            #update lables to show user points for yahtzee, total2, and score
            self.yahtzee_val.configure(text = points2["yahtzee"])
            self.total2_val.configure(text = points2["total2"])
            self.final_score.configure(text\
                 = "Score: " + str(points2["total_score"]))
            #increment check value for revert
            self.check += 1

        #claculate Bonus
        #if bonus has not yet been acheived
        if self.points["bonus"] != 35:
            #and if the total of points for total1 is 63 or more
            if points2["ones"] + points2["twos"] + points2["threes"]\
               + points2["fours"] + points2["fives"] + points2["sixes"] > 62:
                #increment bonus, total1, and score by 35 in temp dictionary
                points2["bonus"] = 35
                points2["total1"] += 35
                points2["total_score"] += 35
                #update label to show user got bonus for bonus, total, score
                self.bonus_val.configure(text = points2["bonus"])
                self.total1_val.configure(text = points2["total1"])
                self.final_score.configure(text\
                     = "Score: " + str(points2["total_score"]))

        #enable the submit button to allow user to finalize score for turn
        self.submit.configure(state = "normal")

        #return points2 dictionary so that this function can be called to
        #make the score permenant and advance to next turn
        return points2
 
    def submit_command(self):
        #make a copy of the points dictionary obtained by user selecting 
        #score card item
        points3 = self.give_val()

        #assign points3 to points dictionary making the selection permenant
        self.points = points3

        #create a list to iterate over (will be used to disable radiobutton)
        point_vals = [["ones", self.ones], ["twos", self.twos],\
             ["threes", self.threes], ["fours", self.fours],\
             ["fives", self.fives], ["sixes", self.sixes],\
             ["three kind", self.three_kind],\
             ["four kind", self.four_kind],\
             ["full house", self.full_house],\
             ["sm straight", self.sm_straight],\
             ["lg straight", self.lg_straight],\
             ["yahtzee", self.yahtzee],\
             ["chance", self.chance]]

        #iterate over point_vals list to disable the radio button selected for 
        #the current turn
        for e in point_vals:
            if self.card.get() == e[0]:
                e[1].configure(state = "disable")

        #increment the turn by one
        self.turn += 1

        #disable the submit button until new radiobutton selected
        self.submit.configure(state = "disable")

        #if there are more turns left...
        if self.turn < 13:
            #reset dice values to 0 and the dice images to blank dice
            self.dice_results = [0] * 5
            self.die1.configure(image = self.dice0)
            self.die2.configure(image = self.dice0)
            self.die3.configure(image = self.dice0)
            self.die4.configure(image = self.dice0)
            self.die5.configure(image = self.dice0)
            #set the score card selection to none (de-select radiobutton)
            self.card.set(None)
            #reset mult_yahtzee checker to 0 
            self.mult_yahtzee = 0
            #reset check to 0
            self.check = 0
            #uncheck all hold checkboxes
            self.held1.set(False)
            self.held2.set(False)            
            self.held3.set(False)
            self.held4.set(False)
            self.held5.set(False)
            #reset remaing rolls for the turn to 3 and update rolls button
            self.rem_roll = 3
            self.roll.configure(state = "normal", text = "Rolls (" +\
              str(self.rem_roll) + ")")

        
#main
root = Tk()
root.title("YAHTZEE")
app = Application(root)
root.mainloop()
