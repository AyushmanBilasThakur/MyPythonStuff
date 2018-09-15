def main(cd):
    destarr = []
    tickets = int(input())
    total_entry = tickets*2
    index = 0 
    ticket_data = {}
    beginwith = ''
    current = ''
    start = None
    end = ''
    sorted_arr = [] 
    while (index<total_entry):
        temp_str = input() 
        destarr.append(temp_str)
        index += 1
    
    dictionary1 = {}
    
    for src in destarr:
        if src not in dictionary1:
            dictionary1[src] = 1
        else:
            dictionary1[src] += 1
    
    i = 0
    while (i < len(destarr) - 1):
        ticket_data[destarr[i]] = destarr[i+1]
        i+=2

    for key in dictionary1.keys():
        if dictionary1[key] == 1 and start == None and key in ticket_data:
            start = key
        elif dictionary1[key] == 1 :
            end = key



   


    sorted_arr.append(start)
    current = start
    
    while (ticket_data[current] != end):
     
     for key in ticket_data:
       if key == ticket_data[current]:
           sorted_arr.append(key)
           current = key

    output = 'Case #' + str(cd) + ': '   
    for item in sorted_arr:
        output += item
        output += '-' 
        output += ticket_data[item]
        output += ' '
    
    

    

    print (output)



cases = int(input())
cd = 1 


while (cd <= cases):
    main(cd)
    cd += 1