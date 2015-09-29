def file_to_dict(filename):
    """opens the file and returns a dictionary of restaurants and their ratings"""

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

def printed_clearly(D):
    """Prints the contents of a dictionary in alphabetical order and includes the rating"""

    alpha_rest = sorted(D)

    for rest_name in alpha_rest:
        print "%s is rated at: %d" % (rest_name, D[rest_name])

def user_contribution():
    user_feedback = {}
    user_rest = raw_input("Please enter a restaurant: ")
    user_rating = int(raw_input("Please enter a rating for that restaurant: "))
    user_feedback[user_rest] = user_rating
    return user_feedback
    # create empty dict
    # prompt user for restaurant and rating
    # add that raw input to the dict
    # return dict


    #New function! to combine both dicts


restaurant_ratings = file_to_dict("scores.txt")

user_data = user_contribution()

def dictionary_adder(d1, d2):
    d1.update(d2)
    return d1


both = dictionary_adder(restaurant_ratings, user_data)

printed_clearly(both)

#printed_clearly(combined_restaraunt_data)

# printed_clearly(restaurant_ratings)

# printed_clearly(user_contribution())


