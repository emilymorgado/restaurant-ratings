def file_to_dict(filename):
# open file
    file_contents = open(filename)
    Yelp = {}
# loop through file
    for rest_line in file_contents:
        rest_line = rest_line.strip().split(":")
# feed dict Restaurant name = key, Score = value
        Yelp[rest_line[0]] = int(rest_line[1])
# return dictionary
    return Yelp
    file_contents.close() #crazy!  we have to close our variable, not the filename!


# def printed_clealy(D):
#     for rest, score in D.items():


#         print "%s is rated at: %d" %(rest, score)


def printed_clearly(D):
    alpha_rest = sorted(D)
    #sort the dictionary that gives us a list of keys
    # now we have an alphabetical list (but no values)
    for rest_name in alpha_rest:
        print "%s is rated at: %d" % (rest_name, D[rest_name])
    #loop through list
    # find each rest and query its value in dict
    # add rest and dict_value to printed message


restaurant_ratings = file_to_dict("scores.txt")

printed_clearly(restaurant_ratings)
