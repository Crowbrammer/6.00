def textPull():

    fileName = input("Please input a filename!: ")
    while True:
        try:
            with open(fileName) as f:
                my_list = f.read().splitlines()
            f.close()
            return my_list

        except FileNotFoundError:
            fileName = input("Can't find the file... Please input a filename!: ")
            return False

# print(textPull())

answers = dict()


def askUser(sItem, rItem):
    """
    Get ask which is higher priority, the sItem, or the rItem
    """
    try:
        if answers[(sItem, rItem)] == "y":
            return True
        else:
            return False
    except KeyError:

        answers[(sItem, rItem)] = input("Is: \n\n{}\n\nhigher priority than...\n\n{}? Y/N: ".format(sItem, rItem)).lower()
        print()
        while answers[(sItem, rItem)] != "y" and answers[(sItem, rItem)] != "n":
            answers[(sItem, rItem)] = input("Is: \n\n{}\n\nhigher priority than...\n\n{}? (Please enter 'Y' or 'N'):".format(sItem, rItem)).lower()
            print()
            # print("answer:", aanswers[(sItem, rItem)])
        if answers[(sItem, rItem)] == "y":
            return True
        else: return False

def sort(wl, comparator):
    """
    Sorts the list of subjects' names in descending order
    acording to the comparator, using bisection search.
    """

    sl = []
    rl = []
    start_list_size = len(wl)

    if len(wl) == 1 or len(wl) == 0: # 1
        print("#: 1")
        return l

    if len(wl) == 2: # 2
        print("#: 2")
        if comparator(wl[0], wl[1]):
            results = [wl[0], wl[1]]
        else:
            results = [wl[1], wl[0]]
        return results

    high = len(rl)
    low = 0
    x = (high + low) / 2
    loop_num = 0

    while wl or sl:
        # "AIM: Move all items from wl to rl, sorted, in logn time"
        if wl and len(sl) == 0: # 3
            print("#: 3")
            # "AIM: If wl has items, and sl doesn't, give an item to sl for rl transfer")
            sl = [wl.pop()]

        if len(rl) == 0 and sl: # 4
            print("#: 4")
            # "AIM: If rl is empty, simply move item from sl to rl"
            rl = [sl.pop()]
            high = len(rl)
            low = 0
            loop_num += 1
            continue
        # if len(rl) == 1 and sl...
            # Needs to restart

        if x == 0: # 5
            print("#: 5")
            # "AIM: If x is at 0, simply compare sl with 1st value of rl, \
            #    then put it at [0:0] if True or [1:1] if not"
            if comparator(sl[0], rl[0]): # 6
                print("#: 6")
                rl.insert(int(x), sl.pop()) # Can I do the sl without the index?
            else:
                print("#: 6.5")
                rl.insert(int(x)+1, sl.pop())
            high = len(rl)
            low = 0

        # elif len(rl) == 2:
        #     ##### Scaffold
        #     print("AIM: Prevent incorrect sorting from the x == len(rl) -1 conditional by handling the len(rl) == 2" \
        #         "scenario.")
        #     print("ACTION: Check if it's ")
        #     print("MEASUREMENTS BEFORE ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
        #             x, high, low, wl, sl, rl, loop_num))
        #     print("ACTION IMPLEMENTING...")
        #     raw_input()
        #     ##### Actual Code
        #     if comparator(sl[0][1], rl[0][1]):
        #         rl.insert(x, sl.pop()) # Can I do the sl without the index?
        #     else:
        #         rl.insert(x+1, sl.pop())
        #     high = len(rl)
        #     low = 0
        #     ##### Scaffold
        #     print("ACTION COMPLETE.\n")
        #     print("MEASUREMENTS AFTER ACTION:\nx:{}\nhigh:{}\nlow:{}\nwl:{}\nsl:{}\nrl:{}\nloop #:{}\n".format(\
        #             x, high, low, wl, sl, rl, loop_num))
        #     raw_input()
        #     ##### End Scaffold

        elif x == len(rl) - 1 and len(rl) > 2: # 7
            print("#: 7")
            # "AIM: If x is equal to the length of the list or just before it, \
            #    either append it, or put it just before the end value"
            if comparator(sl[0], rl[int(x)]): # 8
                print("#: 8")
                rl.insert(int(x), sl.pop())
            else: # 8.5
                print("#: 8.5")
                rl.insert(int(x)+1, sl.pop())
            high = len(rl)
            low = 0
        else:
            # AIM: Do actual bisection sort here."
            if comparator(sl[0], rl[int(x)-1]) and comparator(sl[0], rl[int(x)]): # 9
                print("#: 9")
                # AIM: If it's larger than both items, cut the half of the search space.\
                #    after x away."
                high = int(x)

            elif comparator(sl[0], rl[int(x)-1]) and  comparator(sl[0], rl[int(x)]) == False: # 10
                print("#: 10")
                # AIM: If it's larger than the one above and lower than the one below, stop the program \
                #    because it's not sorting correctly"
                print("Program not sorting correctly. Exiting...")
                import sys
                sys.exit()
            elif comparator(sl[0], rl[int(x)-1]) == False and  comparator(sl[0], rl[int(x)]): # 11
                print("#: 11")
                # AIM: If less than the one above but greater than the one below, put sl between the two."
                rl.insert(int(x), sl.pop())
                high = len(rl)
                low = 0
            elif comparator(sl[0], rl[int(x)-1]) == False and  comparator(sl[0], rl[int(x)]) == False: # 12
                print("#: 12")
                # "AIM: If sl == to either the one above or below it, slap sl in the middle. Else cut the
                #    search space before x away."
                low = int(x)

        x = (high + low) / 2
        loop_num += 1
    print("# of loops required for list size {}: {}".format(start_list_size, loop_num))
    return rl

def textPush(l):
    fileName = input("Please choose a filename.")
    try:
        with open(fileName, "w") as f:
            for item in l:
                f.write("%s\n" % item)
        f.close()
        return

    except FileNotFoundError:
        input("Can't find the file...")
        with open(fileName, "w") as f:
            for item in l:
                f.write("%s\n" % item)
        f.close()
        return my_list
        return False

def main():
    textPush(sort(textPull(), askUser))

main()
# print(textPush(['1', 'b', '3', '4', '5', '6', '7', '8', '9', '10']))
# print(sort(textPull(), askUser))
