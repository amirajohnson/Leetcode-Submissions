'''
Prompt: 
You are given a string that represents time in the format hh:mm. 
Some of the digits are blank (represented by ?). Fill in ? such that the time 
represented by this string is the maximum possible. Maximum time: 23:59, minimum 
time: 00:00. You can assume that input string is always valid.
'''

def maximum_time(s):
    #let's first define what the max hour and max minute are
    max_hour0, max_hour1, max_minute0, max_minute1 = '2', '9', '5', '9'

    '''
    we have some rules that we need to follow:
        1. in the 0th hour index, the max we can have is two.
            in the 1st hour index, the max we can have is nine
            in the 0th minute index, the max we can have is five.
            in the 1st minute index, the max we can have is nine.
        Question: can we always assume that there is only one question mark?
                no, there can be multiple question marks in one input.
        Since strings are inmutable, we have to convert the input into a list before
        we can make any changes to it.
    '''
    #convert the string into a list
    time = []
    for character in s: #O(n)
        if character != ':' :
            time.append(character)

    #make changes to the time based on the location of the question marks
    #we will work backwards, so that we can choose whether or not to round up the hour
    if time[3] == '?': 
        time[3] = max_minute1
    if time[2] == '?':
        time[2] = max_minute0
    if time[0] == '2' and time[1] == '?':
        time[1] = '3'
    else:
        if time[1] == '?':  
            time[1] = '9'
    if time[0] == '?' and int(time[1]) < 4:
        time[0] = '2'
    elif time[0] == '?': time[0] = '1'
    
    

    res = time[0] + time[1] + ':' + time[2] + time[3]
    return res

assert(maximum_time("?4:5?") == '14:59')
assert(maximum_time("23:5?") == '23:59')
assert(maximum_time("2?:22") == '23:22')
assert(maximum_time("0?:??") == '09:59')
print("All tests passed!")

'''
Prompt:
Given a hotel which has 10 floors [0-9] and each floor has 26 rooms [A-Z]. 
You are given a sequence of rooms, where + suggests room is booked, - 
room is freed. You have to find which room is booked maximum number of times.

You may assume that the list describe a correct sequence of bookings in 
chronological order; that is, only free rooms can be booked and only booked 
rooms can be freeed. All rooms are initially free. Note that this does not 
mean that all rooms have to be free at the end. In case, 2 rooms have been booked 
the same number of times, return the lexographically smaller room.

You may assume:

N (length of input) is an integer within the range [1, 600]
each element of array A is a string consisting of three characters: "+" or "-"; 
a digit "0"-"9"; and uppercase English letter "A" - "Z"
the sequence is correct. That is every booked room was previously free and every 
freed room was previously booked.
'''


def most_booked_hotel_room(A):
    bookings = dict()
    most_bookings = 0
    most_booked_room = ''
    #we can write this function in O(n) time.
    #we can use a dictionary to keep track of the number of times a room is booked.
    #this will save on lookup time later/reduce overall runtime.
    #im not going to set each key in the dictionary before iterating because 
    #that would take too much time

    for status in A: #O(n)
        #if we see a plus sign, we are going to either add that room to the dictionary,
        #or incremement the count we already have if its added
        #as we go through the array A, we need to be adding things to the dictionary each time.
        if '+' in status:
            if status not in bookings:
                bookings[status] = 1
            else:
                bookings[status] += 1
    #at this point, we have the counts for the booked rooms available in bookings
    #at the end, we need to loop through the dictionary again, to get the max element.
    for room in bookings:
        if bookings[room] > most_bookings:
            most_bookings = bookings[room]
            most_booked_room = room
        elif bookings[room] == most_bookings:
            #+1A, the last character is the letter
            current_last_char, most_last_char = bookings[room][-1], most_booked_room[-1]
            smaller = min(ord(current_last_char), most_last_char)
            if smaller == ord(current_last_char):
                most_booked_room = room
            #we dont have to update the most_bookings count bc they were the same
    #we need to remove that initial + from the room name
    return most_booked_room[1:]

#tests
assert(most_booked_hotel_room(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]) == "1A")
print("All tests passed!")

