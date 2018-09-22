#IN THIS PROGRAMME THE INPUTS ARE NO. OF BALLS THE OUTPUT IS NO. OF CASES WHEN BOX A WILL HAVE MORE BALLS THAN BOX C, GIVEN THERE ARE 3 BOXES A,B & C

no_of_balls = int(input("Enter no. of balls: "))

balls_in_a = 0
balls_in_c = 0
balls_in_b = no_of_balls

total_cases = 0

while balls_in_c < no_of_balls//2 + 1 :
    
    balls_in_a = 0
    balls_in_b = no_of_balls - balls_in_c

    while balls_in_b >= 0:
        if( balls_in_a > balls_in_c):
            total_cases += 1
            # This line prints the no. of cases!
            # print(" {}  {}  {}  ".format(balls_in_a,balls_in_b,balls_in_c))
        balls_in_a += 1
        balls_in_b -= 1

    balls_in_c += 1

print(total_cases)