caseno = int(input()) # Gets Input for no. of cases
tc = caseno #No. of total cases

def dictionary_append(name):
    each_letter_dictionary = {}
    unique_char = 0
    alreadyexist = False
    for c in name:
        if c != ' ': #Ignore whitespaces from Count
            for k in each_letter_dictionary.keys():
                if c == k:
                    alreadyexist = True
            if not alreadyexist:
                each_letter_dictionary[c] = 1
                unique_char += 1
            alreadyexist = False
    person_name_dictionary[name] = unique_char
    max = 0
    for p in person_name_dictionary.values():
        if max == 0:
            max = p
        if p > max:
            max = p
    return(max)

def final_output(integer):
    final_array = []
    for a in person_name_dictionary.keys():
        if(person_name_dictionary[a] == integer):
            final_array.append(a)
    final_array.sort()
    ctd = tc-caseno+1
    print("Case #" + str(ctd) + ": " + final_array[0])

#This IS Where the main function starts
while caseno > 0:
    i = int(input()) #Gets the input how many person to be added
    
    #Insitialization of variables
    
    persons_in_city = [] #List for no of persons in the city
    person_name_dictionary = {} #Dictionary for no. of unique charcater for each person
    
    while i > 0:
        persons_in_city.append(input()) #Append each input to person_in_city list
        i = i-1 #keep the loop running

    for person in persons_in_city:
        max_unique = dictionary_append(person)
        #Used for appending all the names with their no. of unique charcters in person_name_dictionary and returns the max_unique chars in name

    final_output(max_unique) #Gives Final name print
    
    caseno -= 1 #Decrement case no. to keep on counting