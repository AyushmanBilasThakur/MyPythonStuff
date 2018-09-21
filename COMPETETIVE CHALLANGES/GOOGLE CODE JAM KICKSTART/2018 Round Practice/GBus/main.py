def check_in(city_no,arr_bus):
    i = 0
    ip = 0
    while (i < len(arr_bus) - 1):
        if (city_no >= arr_bus[i]) and (city_no<=arr_bus[i+1]):
            ip += 1
        i+=2
    return ip
def main(c):
    output_str = 'Case #' + str(c) + ": "
    Gbus_in = int(input())
    inp_take = Gbus_in * 2
    ini_arr = []    
    temp_str = input().split()
    i = 0 
    while(i < inp_take):
        ini_arr.append(int(temp_str[i]))
        i+=1
    no_cities = int(input())
    ctm = []
    i = 0 
    while (i < no_cities):
        tmp = int(input())
        ctm.append(tmp)
        i += 1
    i=0
    while (i < no_cities):
        is_in = check_in(ctm[i],ini_arr)
        i += 1
        output_str += str(is_in) + ' '
    print(output_str)
    input()


cases = int(input())
cd = 1

while (cd <= cases):
    main(cd)
    cd += 1