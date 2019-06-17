###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limiti):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # result = []
    # totalweight = 0
    # singletrip = []
    # cowscopy = cows.copy()
    # if len(cowscopy) != 0:
    #     for cow in cows.keys():
    #         print(cow)
    #         print(cowscopy.keys())
    #         if totalweight < limit:
    #             print(max(cowscopy.values()))
    #             if cowscopy[cow] == max(cowscopy.values()):
    #                 totalweight += cowscopy[cow]
    #                 del cowscopy[cow]
    #                 singletrip.append(cow)
    #
    #         else:
    #             result.append(singletrip)
    # return result
    #
    #
    # result = []
    # totalweight = 0
    # singletrip = []
    # cowscopy = cows.copy()
    # values = []
    # for value in cowscopy.values():
    #     values.append(value)
    # while True:
    #     totalweight = 0
    #     namestaken =[]
    #     valuescopy = values.copy()
    #     # names = cowscopy.keys()
    #     while True:
    #         for cow in  cowscopy.keys():  #names:
    #             # print(cow)
    #             # print(cowscopy.keys())
    #             print(namestaken)
    #             if cow not in namestaken:
    #                 if totalweight < limit:
    #                     # print(max(cowscopy.values()))
    #                     biggest = max(valuescopy)
    #                     if cowscopy[cow] == biggest:
    #                         totalweight += cowscopy[cow]
    #                         # del cowscopy[cow]
    #                         namestaken.append(cow)
    #                         singletrip.append(cow)
    #                         valuescopy.remove(biggest)
    #                         print(singletrip)
    #                 else:
    #                     result.append(singletrip)
    #                     break
    #     if len(namestaken) == len(cows):
    #         break
    # return result
    #
    #
    # result = []
    # totalweight = 0
    # singletrip = []
    # cowscopy = cows.copy()
    # values = []
    # for value in cowscopy.values():
    #     values.append(value)
    # while True:
    #     totalweight = 0
    #     namestaken =[]
    #     valuescopy = values.copy()
    #     # names = cowscopy.keys()
    #     while True:
    #         if totalweight < limit:
    #             for cow in  cowscopy.keys():  #names:
    #                 # print(cow)
    #                 # print(cowscopy.keys())
    #                 print(namestaken)
    #                 if cow not in namestaken:
    #                     # print(max(cowscopy.values()))
    #                     biggest = max(valuescopy)
    #                     if cowscopy[cow] == biggest:
    #                         totalweight += cowscopy[cow]
    #                         namestaken.append(cow)
    #                         singletrip.append(cow)
    #                         valuescopy.remove(biggest)
    #                         print(singletrip)
    #                         break
    #         else:
    #             result.append(singletrip)
    #             break
    #     if len(namestaken) == len(cows):
    #         break
    # return result
    #
    #
    # result = []
    # totalweight = 0
    # singletrip = []
    # cowscopy = cows.copy()
    # values = []
    # for value in cowscopy.values():
    #     values.append(value)
    # while True:
    #     totalweight = 0
    #     namestaken =[]
    #     valuescopy = values.copy()
    #     # names = cowscopy.keys()
    #     while True:
    #         if totalweight < limit:
    #             for cow in  cowscopy.keys():  #names:
    #                 # print(cow)
    #                 # print(cowscopy.keys())
    #                 # print(namestaken)
    #                 if cow not in namestaken:
    #                     # print(max(cowscopy.values()))
    #                     biggest = max(valuescopy)
    #                     if cowscopy[cow] == biggest:
    #                         totalweight += cowscopy[cow]
    #                         namestaken.append(cow)
    #                         singletrip.append(cow)
    #                         valuescopy.remove(biggest)
    #                         # print(singletrip)
    #                         break
    #         else:
    #             result.append(singletrip)
    #             break
    #         if len(namestaken) == len(cows):
    #             result.append(singletrip)
    #             break
    #
    #     if len(namestaken) == len(cows):
    #         break
    # return result
    #



# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # for item in get_partitions(cows):
    #     good = True
    #     #assume this item is good
    #     for i in range(len(item)):
    #         # good = True
    #     #determine if every trip is goo
    #         if good:
    #             total = 0
    #             for j in range(len(item[i])):
    #                 total += cows[item[i][j]]
    #             if total >= limit:
    #                 good = False
    #     if good:
    #         return item
    for item in get_partitions(cows):
        good = True
        #assume this item is good

        for i in range(len(item)):
            if good:
                # good = True
                #determine if every trip is goo

                total = 0
                for j in range(len(item[i])):
                    total += cows[item[i][j]]
                if total >= limit:
                    good = False
        if good:
            return item





# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    pass


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.

[['Betsy', 'Millie', 'Florence', 'Herman', 'Lola', 'Maggie', 'Henrietta', 'Moo Moo', 'Milkshake', 'Oreo']]
[['Oreo', 'Herman', 'Maggie', 'Milkshake', 'Henrietta', 'Millie', 'Moo Moo', 'Betsy', 'Florence', 'Lola']]
[['Florence', 'Milkshake', 'Herman', 'Betsy', 'Henrietta', 'Moo Moo', 'Lola', 'Millie', 'Oreo'], ['Maggie']]
"""

cows = load_cows("ps1_cow_data.txt")
limit=40
# print(cows)
# for item in get_partitions(cows):
#     print(item)

# print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
