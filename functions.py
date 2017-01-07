# Copyright (c) 2014 Thomas Van Klaveren
# create the function for Yahtzee game.  This will evaluate dice and 
# determine the points eligible for the score card item selected


#function checks the values of dice and returns a list containing the numbers
#of same valued dice (ie dice 6,2,6,6,2 would return [3,2])
def same_val_check(dice_list):
    d = {}
    l = []
    for i in dice_list:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in d:
        if d[i] not in l:
            l.append(d[i])
    return l

#function adds sum of dice values and returns that value
def dice_sum(dice_list):
    x = 0
    for i in dice_list:
        x += i
    return x



# tried to write this function as a module to import into my main file,
# however, tkinter needed this to be in the class where it was called from
# the radiobutton command 
"""
def give_val(dice_results, score_card, dictionary, item):
    val = 0    
    dice_vals = same_val_check(dice_results)
    if score_card.get() == "ones":
        for i in dice_results:
            if i == 1:
                val += 1
        dictionary["ones"] = val
        dictionary["total1"] += val
        dictionary["total_score"] += val
        item.configure(text = dictionary["ones"])
    elif score_card.get() == "twos":
        for i in dice_results:
            if i == 2:
                val += 1
        dictionary["twos"] = val
        dictionary["total1"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "threes":
        for i in dice_results:
            if i == 3:
                val += 1
        dictionary["threes"] = val
        dictionary["total1"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "fours":
        for i in dice_results:
            if i == 4:
                val += 1
        dictionary["fours"] = val
        dictionary["total1"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "fives":
        for i in dice_results:
            if i == 5:
                val += 1
        dictionary["fives"] = val
        dictionary["total1"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "sixes":
        for i in dice_results:
            if i == 6:
                val += 1
        dictionary["sixes"] = val
        dictionary["total1"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "three kind":
        for i in range(3,6):
            if i in dice_vals:
                val = dice_sum(dice_list)
                break 
        dictionary["three_kind"] = val
        dictionary["total2"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "four kind":
        for i in range(4,6):
            if i in dice_vals:
                val = dice_sum(dice_list)
                break 
        dictionary["four_kind"] = val
        dictionary["total2"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "full house":
        if 3 in dice_vals and 2 in dice_vals:
            val = 25
        elif 5 in dice_vals:
            val = 25        
        dictionary["full_house"] = val
        dictionary["total2"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "sm straight":
        for i in range(1,7):
            if [i, i+1, i+2, i+3] <= sort(dice_results):
                val = 30
            elif 5 in dice_vals:
                val = 30        
        dictionary["sm_straight"] = val
        dictionary["total2"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "lg straight":
        for i in range(1,7):
            if [i, i+1, i+2, i+3, i+4] <= sort(dice_results):
                val = 40
            elif 5 in dice_vals:
                val = 40        
        dictionary["lg_straight"] = val
        dictionary["total2"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "chance":
        val = dice_sum(dice_listi)
        dictionary["chance"] = val
        dictionary["total2"] += val
        dictionary["total_score"] += val
    elif score_card.get() == "yahtzee":
        dice_vals = same_val_check(dice_results)
        if 5 in dice_vals:
            val = 50            
        dictionary["yahtzee"] = val
        dictionary["total2"] += val
        dictionary["total_score"] += val

    if dictionary["ones"] + dictionary["twos"] + dictionary["threes"] + \
      dictionary["fours"] + dictionary["fives"] + dictionary["sixes"] > 62:
        dictionary["bonus"] = 35
        dictionary["total1"] += 35
"""













