#
# Tristan Martin
# September 2nd, 2020
# Mega-Program of different calculators made to practice
# Concepts learned in Chapter 3

import math
import random

#define pi
pi = 3.1415926

# Wrapper
def main():
    print("\nCompilation of Calculators\nPracticing Chapter 3 Concepts of Computing with Numbers\n---------------------------------------------------------------")
    print("\n1. Sphere Volume, Surface Area, Circumference")
    print("2. Cost Per Square Inch of Pizza")
    print("3. Molecular Weight of a Carbohydrate")
    print("4. Distance of a Lightning Strike")
    print("5. Konditorei Coffee Shop")
    print("6. Slope of a Line Given by Two Points")
    print("7. Gregorian Epact Calculator")
    print("8. Area of a Triangle Given Three Sides")
    print("9. Ladder Calculator")
    print("10. Sum of Natural Numbers N")
    print("11. Sum of Cube of Natural Numbers N")
    print("12. Sum of a Series of Numbers")
    print("13. Average of a Series of Numbers")
    print("14. Estimate Pi via Gregory Series")
    print("15. Fibonacci Sequence")
    print("16. Sir Isaac Newton's Square Root Estimator")
    programSelect = str(input("\nPlease select a program to run (1-16): "))
    if programSelect == "1":
        program1()
    elif programSelect == "2":
        program2()
    elif programSelect == "3":
        program3()
    elif programSelect == "4":
        program4()
    elif programSelect == "5":
        program5()
    elif programSelect == "6":
        program6()
    elif programSelect == "7":
        program8()
    elif programSelect == "8":
        program9()
    elif programSelect == "9":
        program10()
    elif programSelect == "10":
        program11()
    elif programSelect == "11":
        program12()
    elif programSelect == "12":
        program13()
    elif programSelect == "13":
        program14()
    elif programSelect == "14":
        program15()
    elif programSelect == "15":
        program16()
    elif programSelect == "16":
        program17()
    else:
        print("Input not recognized, please type 'main()' to restart")
    
# 3.1 Write a program to calculate the volume and surface area of a sphere from
# its radius, given as input. Here are some formulas that might be useful:
# V = (4/3) * pi * r ** 3
# A = 4 * pi * r ** 2

def program1():
    print("\n\n\n###### Welcome to Program 3.1 ###### Sphere Volume, Surface Area, Circumference\n---------------------------------------------------------------\nThis calculator solves the Volume, Surface Area, and Circumference\nof a Sphere given a radius.")
    sphereRadius = int(input("\nPlease enter the radius: "))
    sphereVolume = (4/3) * pi * (sphereRadius ** 3)
    sphereSurfaceArea = 4 * pi * (sphereRadius ** 2)
    sphereCircumference = 2 * pi * sphereRadius
    print("\nThe Volume of the sphere with a radius of", sphereRadius, "is         :", sphereVolume)
    print("The Surface Area of the sphere with a radius of", sphereRadius, "is   :", sphereSurfaceArea)
    print("The Circumference of the sphere with a radius of", sphereRadius, "is  :", sphereCircumference)
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog1select = str(input("Select 1 or 2: "))
    if prog1select == "1":
        program1()
    elif prog1select == "2":
        main()
    else:
        print("Input not recognized, please type 'main()' to restart")


# 3.2 Write a program that calculates the cost per square inch of a circular pizza,
# given its diameter and price.
# The formula for area is A = pi * r ** 2

def program2():
    print("\n\n\n###### Welcome to Program 3.2 ###### Cost Per Square Inch of Pizza\n---------------------------------------------------------------\nThis calculator solves the Area, and Cost Per Square Inch\nof a Pizza given a Diameter.")
    pizzaDiameter = int(input("\nWhat is the Diameter of the Pizza?: "))
    pizzaCost = int(input("What is the Price of this bad boy?: "))
    pizzaArea = pi * ( ( pizzaDiameter / 2 ) ** 2 )
    pizzaUnitCost = pizzaCost / pizzaArea
    print("\nThe Area of the Pizza is", pizzaArea, "square inches. The price per square inch is", "$" + str(round(pizzaUnitCost, 3)), "/ square inch.")
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog2select = str(input("Select 1 or 2: "))
    if prog2select == "1":
        program2()
    elif prog2select == "2":
        main()
    else:
        print("Input not recognized, please type 'main()' to restart")
        
# 3.3 Write a program that computes the molecular weight of a carbohydrate
# (in grams per mole) based on the number of hydrogen, carbon, and oxygen
# atoms in the molecule. The program should prompt the user to enter the
# number of hydrogen atoms, the number of carbon atoms, and the number
# of oxygen atoms. The program then prints the total combined molecular
# weight of all the atoms based on these individual atom weights:
# Atom   |  Weight (grams / mole)
# -------------------------------
#  H     |  1.00794
#  C     |  12.0107
#  O     |  15.9994

def program3():
    hWeight, cWeight, oWeight = 1.00794, 12.0107, 15.9994
    print("\n\n\n###### Welcome to Program 3.3 ###### Molecular Weight of a Carbohydrate\n---------------------------------------------------------------\nThis calculator computes the molecular weight\nof a Carbohydrate given its quantities of H, C, O.")
    carbStr = input("\nInput the Carbohydrate (Sucrose would be inputted as 'C,12,H,22,O,11') ")
    carbSplit = carbStr.split(",")
    carbonWeight = float(carbSplit[1]) * cWeight 
    hydrogenWeight = float(carbSplit[3]) * hWeight
    oxygenWeight = float(carbSplit[5]) * oWeight
    print("\n  Molecule Weight  |(grams / mole)\n-------------------+------------")
    print("Carbon   12.0107g/m|  ", round(carbonWeight, 4), "\nHydrogen 1.00794g/m|  ", round(hydrogenWeight, 4), "\nOxygen   15.9994g/m|  ", round(oxygenWeight, 4))
    print("-------------------+------------")
    print("Total weight       |", " ",carbonWeight + hydrogenWeight + oxygenWeight, "grams / mole")                                 
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog3select = str(input("Select 1 or 2: "))
    if prog3select == "1":
        program3()
    elif prog3select == "2":
        main()                    
    else:
        print("Input not recognized, please type 'main()' to restart")
        
# 3.4 Write a program that determines the distance to
# a lightning strike based on the time elapsed between
# the flash and the sound of thunder.
# Sound Velocity=1100 ft/sec, 1 mile = 5280ft

def program4():
    soundSpeed = 1100
    print("\n\n\n###### Welcome to Program 3.4 ###### Distance of a Lightning Strike\n---------------------------------------------------------------\nThis calculator approximates the Distance\nof a Lightning Strike given the delay between the flash and the sound of thunder.\n")
    lightningDelay = int(input("How many seconds (use a whole number)\nbetween the flash and the sound of thunder? "))
    lightningDistance = lightningDelay * soundSpeed
    lightningMiles = lightningDistance / 5280
    print("\nThe lightning strike is approximately", lightningDistance, "feet or", round(lightningMiles, 3), "miles away.")
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog4select = str(input("Select 1 or 2: "))
    if prog4select == "1":
        program4()
    elif prog4select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")
    
# 3.5 The Konditorei coffee shop sells coffee
# at $10.50 a pound plus the cost of shipping.
# Each order ships for $0.86 per pound + $1.50 fixed cost for overhead.
# Write a program that calculates the cost of an order.

def program5():
    orderNumber = random.randint(0,1000)
    print("\n\n\n######Welcome to Program 3.5###### Konditorei Coffee Shop\n---------------------------------------------------------------\n")
    print("╦╔═  ╔═╗  ╔╗╔  ╔╦╗  ╦  ╔╦╗  ╔═╗  ╦═╗  ╔═╗  ╦\n╠╩╗  ║ ║  ║║║   ║║  ║   ║   ║ ║  ╠╦╝  ║╣   ║\n╩ ╩  ╚═╝  ╝╚╝  ═╩╝  ╩   ╩   ╚═╝  ╩╚═  ╚═╝  ╩\n┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐  ┌─┐┬ ┬┌─┐┌─┐\n│  │ │├┤ ├┤ ├┤ ├┤   └─┐├─┤│ │├─┘            \n└─┘└─┘└  └  └─┘└─┘  └─┘┴ ┴└─┘┴ ")
    print("\n---coffee-:-$10.50-per-pound------------------------------------\n")
    orderPounds = input("How many pounds is the order?  ")
    orderExpense = (float(orderPounds) * 0.86) + 1.50
    orderRevenue = float(orderPounds) * 10.50
    orderProfit = orderRevenue - orderExpense
    print("\nOrder #",orderNumber) 
    print("-----------------+------------")
    print("Expenses         |", "$",orderExpense,)
    print("└─>>> Shipping   |", "$",float(orderPounds)*0.86)
    print("└─>>> Overhead   |", "$","1.50")
    print("Revenue          |", "$",orderRevenue,)
    print("-----------------+------------")
    print("Profit           |", "$",orderProfit,)
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog5select = str(input("Select 1 or 2: "))
    if prog5select == "1":
        program5()
    elif prog4select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")

    
# 3.6 Two points in a plane are specified using
# the coordinates (x1,y1) and (x2,y2). Write a program that
# calculates the slope of a line through two(non-vertical) points entered by the user.
# slope = (y2 - y1) / (x2 - x1)

def program6():
    print("\n\n\n######Welcome to Program 3.6 + 3.7 ###### Slope of a Line Given by Two Points\n---------------------------------------------------------------\nThis calculator computes the Slope\nof a Line given two non-vertical coordinates XY.\n")
    coordinate1 = input("Input 1st coordinate (format using a comma between points eg. 'X,Y'): ")
    coordinate2 = input("Input 2nd coordinate: ")
    coordSplit1 = coordinate1.split(",")
    coordSplit2 = coordinate2.split(",")
    computeSlope = (int(coordSplit2[1]) - int(coordSplit1[1])) /(int(coordSplit2[0]) - int(coordSplit1[0]))
    computeDistance = math.sqrt(((int(coordSplit2[1]) - int(coordSplit1[1])) ** 2 ) + (int(coordSplit2[0]) - int(coordSplit1[0])) ** 2)
    computeB = (int(coordSplit2[1])) - (computeSlope * (int(coordSplit2[0])))
    print("\nThe Slope is", computeSlope)
    print("The Distance between the coordinates is", computeDistance)
    print("y = mx + b fit --->>>  y =", computeSlope,"x +", computeB) 
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog6select = str(input("Select 1 or 2: "))
    if prog6select == "1":
        program6()
    elif prog6select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")


# 3.8 The Gregorian epact is the number of days between January 1st and the
# previous new moon. This value is used to figure out the date of Easter.
# It is calculated by these formulas (using int arithmetic):
#
# C = year/ /100
# epact = (8 + (C/ /4)- C + ((80 + 13)/ /25) + 11(year%19))%30
#
# Write a program that prompts the user for a 4-digit year and then outputs
# the value of the epact.

def program8():
    print("\n\n\n######Welcome to Program 3.8 ###### Gregorian Epact Calculator\n---------------------------------------------------------------\nThe Gregorian epact is the number of days between January 1st and the previous new moon. \nThis value is used to figure out the date of Easter.\n")
    epactYear = eval(input("Please enter a 4-digit year to determine the value of the epact: "))
    epactC = epactYear // 100
    epact = (8+(epactC//4) - epactC + (((8*epactC) + 13)//25) + 11*(epactYear%19))%30
    print("\nThe Gregorian epact is", epact)
    print("\n## A NOTE ##\n'This calculation is known to be inaccurate but the sentiment was\nthat it was better to celebrate Easter too late than too early.' - John Zelle \nIn the Gregorian calendar, the Epact can have any value from 1 to 30.")
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog8select = str(input("Select 1 or 2: "))
    if prog8select == "1":
        program8()
    elif prog8select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")

# 3.9 Write a program to calculate the area of a triangle given the length of its
# three sides-a, b, and c-using these formulas:
# s = (a + b + c) / 2
# A = sqrt( s ( s - a ) ( s - b ) (s - c) )

def program9():
    print("\n\n\n######Welcome to Program 3.9 ###### Area of a Triangle Given Three Sides\n---------------------------------------------------------------\nThis calculator computes the area of a Triangle\ngiven the lengths of three of its sides.\n")
    sideA = eval(input("Enter Side Length A: "))
    sideB = eval(input("Enter Side Length B: "))
    sideC = eval(input("Enter Side Length C: "))
    triangleS = float((sideA + sideB + sideC) / 2)
    triangleA = float(math.sqrt( triangleS * (( triangleS - sideA )*( triangleS - sideB )*( triangleS - sideC ))))
    print("\nThe Area of this Triangle is: ", triangleA)
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog9select = str(input("Select 1 or 2: "))
    if prog9select == "1":
        program9()
    elif prog9select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")
    
# 3.10 Write a program to determine the length of a ladder required to reach a
# given height when leaned against a house. The height and angle of the
# ladder are given as inputs. To compute length use:
# length = height / sin(angle)
# NOTE RADIANS/DEGREES

def program10():
    print("\n\n\n######Welcome to Program 3.10 ###### Ladder Calculator\n---------------------------------------------------------------\nThis calculator determines the length of a ladder\nrequired to reach a certain height given the height and angle it is leaned against the wall.\n")
    ladderHeight = eval(input("Enter the height the ladder must reach: "))
    ladderAngle = eval(input("Enter the angle of the ladder (degrees): "))
    ladderLength = ladderHeight / math.sin(math.radians(ladderAngle))
    print("\nThe Length of the Ladder will need to be", round(ladderLength, 3), "\nin order to reach a height of", ladderHeight, "at a", ladderAngle, "degree angle.")
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog10select = str(input("Select 1 or 2: "))
    if prog10select == "1":
        program10()
    elif prog10select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")
        
# 3.11 Write a program to find the sum of the first n natural numbers, where the
# value of n is provided by the user.

def program11():
    print("\n\n\n######Welcome to Program 3.11 ###### Sum of Natural Numbers N\n---------------------------------------------------------------\nThis calculator finds the sum of the first N natural numbers\n")
    sum_N = int(input("Enter N: "))
    sumSequence = range(0, sum_N+1)
    summation = 0
    for var in sumSequence:
            summation = summation + var
    print("\nThe sum of the first", sum_N, "natural numbers is:", summation)
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog11select = str(input("Select 1 or 2: "))
    if prog11select == "1":
        program11()
    elif prog11select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")   
    
# 3.12 Write a program to find the sum of the cubes of the first n natural numbers
# where the value of n is provided by the user.

def program12():
    print("\n\n\n######Welcome to Program 3.12 ###### Sum of Cube of Natural Numbers N\n---------------------------------------------------------------\nThis calculator finds the sum of the cubes of the first N natural numbers\n")
    sumcube_N = int(input("Enter N: "))
    sumcubeSequence = range(0, sumcube_N+1)
    summationCubed = 0
    for varcubed in sumcubeSequence:
        summationCubed = summationCubed + varcubed ** 3
    print("The sum of the cubes of the first", sumcube_N,"natural numbers is:", summationCubed)
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog12select = str(input("Select 1 or 2: "))
    if prog12select == "1":
        program12()
    elif prog12select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")   
    
# 3.13 Write a program to sum a series of numbers entered by the user. The
# program should first prompt the user for how many numbers are to be
# summed. The program should then prompt the user for each of the numbers
# in turn and print out a total sum after all the numbers have been
# entered. Hint: Use an input statement in the body of the loop.

def program13():
    print("\n\n\n######Welcome to Program 3.13 ###### Sum of a Series of Numbers\n---------------------------------------------------------------\nThis calculator finds the sum of a series where N is chosen by the user\nand the values of each number are chosen by the user.\n")
    sumSeries_N = int(input("Enter N of series: "))
    sumSeriesAcc = 0
    sumcount = 1
    sumSeriesSequence = range(0, sumSeries_N)
    for sumSeriesStore in sumSeriesSequence:
        sumSeriesStore = float(input("\nEnter Number " + str(sumcount) + " "))
        sumSeriesAcc = sumSeriesAcc + sumSeriesStore
        sumcount = sumcount + 1
    print("\nSum =", sumSeriesAcc)
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog13select = str(input("Select 1 or 2: "))
    if prog13select == "1":
        program13()
    elif prog13select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")      


# 3.14 Write a program that finds the average of a series of numbers entered by
# the user. As in the previous problem, the program will first ask the user
# how many numbers there are. Note: The average should always be a float,
# even if the user inputs are all ints.

def program14():
    print("\n\n\n######Welcome to Program 3.14 ###### Average of a Series of Numbers\n---------------------------------------------------------------\nThis calculator finds the average of a series where N is chosen by the user\nand the values of each number are chosen by the user.\n")
    averageSeries_N = int(input("Enter N of series: "))
    averageSeriesAcc = 0
    averagecount = 1
    averageSeriesSequence = range(0, averageSeries_N)
    for averageSeriesStore in averageSeriesSequence:
        averageSeriesStore = float(input("\nEnter Number " + str(averagecount) + " "))
        averageSeriesAcc = averageSeriesAcc + averageSeriesStore
        averagecount = averagecount + 1
    print("\nAverage =", float(averageSeriesAcc/averageSeries_N))
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog14select = str(input("Select 1 or 2: "))
    if prog14select == "1":
        program14()
    elif prog14select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")   
    
# 3.15 Write a program that approximates the value of pi by summing the terms
# of this series: 4/1- 4/3 + 4/5- 4/7 + 4/9- 4/11 + . . . The program should
# prompt the user for n, the number of terms to sum, and then output the
# sum of the first n terms of this series. Have your program subtract the
# approximation from the value of math. pi to see how accurate it is.

def program15():
    print("\n\n\n######Welcome to Program 3.15 ###### Estimate Pi via Gregory Series\n---------------------------------------------------------------\nThis calculator approximates the value of pi using the Gregory Series\nand the N of the series is chosen by the user.\n")
    print("The alternating series works as such: 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...")
    piApprox_N = int(input("\nEnter N of Pi Series : "))
    piSequence = range(1, piApprox_N)
    piAcc = 0
    piCount = 1
    for piStore in piSequence:
        piAcc = ((-1) ** (piCount + 1))/((2 * piCount) - 1) + piAcc
        piCount = piCount + 1
    print("\nThe Approximated Value of Pi of Series N =", piApprox_N, "is", piAcc * 4)
    print("This value is", (piAcc * 4) - pi, "off from the actual value of Pi.")
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog15select = str(input("Select 1 or 2: "))
    if prog15select == "1":
        program15()
    elif prog15select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")   

    
# 3.16 A Fibonacci sequence is a sequence of numbers where each successive
# number is the sum of the previous two. The classic Fibonacci sequence
# begins: 1, 1, 2, 3, 5, 8, 13, . . . . Write a program that computes the nth
# Fibonacci number where n is a value input by the user. For example, if
# n = 6, then the result is 8.

def program16():
    print("\n\n\n######Welcome to Program 3.16 ###### Fibonacci Sequence\n---------------------------------------------------------------\nThis calculator computes the Fibonacci Sequence\ngiven an N of the series.\n")
    fib_N = int(input("\nEnter N of Fibonacci Sequence: "))
    n1, n2 = 0, 1
    count = -1
    if fib_N <= 0:
       print("\nPlease enter a positive integer.")
    elif fib_N == 1:
       print("Fibonacci sequence upto",fib_N,":")
       print(n1)
    else:
       print("Fibonacci sequence:")
       while count < fib_N - 1:
           print("\n",n1)
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1
    print("\n", n1, "is the", str(fib_N) + "th", "value of the Fibonacci Sequence.")
    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog16select = str(input("Select 1 or 2: "))
    if prog16select == "1":
        program16()
    elif prog16select == "2":
        main()
    else:
        print("Input not recognized, please type 'main()' to restart")  
    
# 3.17 You have seen that the math library contains a function that computes
# the square root of numbers. In this exercise, you are to write your own
# algorithm for computing square roots. One way to solve this problem
# is to use a guess-and -check approach. You first guess what the square
# root might be, and then see how close your guess is. You can use this
# information to make another guess and continue guessing until you have
# found the square root (or a close approximation to it). One particularly
# good way of making guesses is to use Newton's method. Suppose x is the
# number we want the root of, and guess is the current guessed answer. The
# guess can be improved by using computing the next guess as:
#
# (guess + ( x / guess ) ) / 2
#
# Write a program that implements Newton's method. The program
# should prompt the user for the value to find the square root of (x) and
# the number of times to improve the guess. Starting with a guess value
# of x/2, your program should loop the specified number of times applying
# Newton's method and report the final value of guess. You should also
# subtract your estimate from the value of math. sqrt (x) to show how close
# it is.

def program17():
    print("\n\n\n######Welcome to Program 3.17 ###### Sir Isaac Newton's Square Root Estimator\n---------------------------------------------------------------\nSir Isaac Newton has a method for approximating the Square Root of any Number.\n\nHe will take any number you give him and make his first guess by dividing it by two.\nThen he will add his first guess to your number divided by his first guess,\nand then divide that by two to get his next guess.\nHe will then apply the same formula to his guesses as many times as you will allow him\nuntil he has approximated a square root of your number\n---------------------------------------------------------------\n")
    userRoot = input("Enter a number for Sir Isaac Newton to guess the Square Root of: ")
    realRoot = math.sqrt(float(userRoot))
    guessN = int(input("How many guesses can Sir Newton make? "))
    guessSequence = range(0, guessN)
    startGuess = float(userRoot) / 2
    for guess in guessSequence:
        startGuess = (startGuess + (float(userRoot) / startGuess)) / 2
    print("\nSir Isaac Newton supposes the square root of", userRoot, "to be", startGuess)
    print("\nIf Sir Newton had access to a state-of-the-art calculator, he would have gotten", realRoot)
    if startGuess % realRoot == 0:
        print("\nWow! Isaac was spot on, who needs a calculator!")
    elif startGuess % realRoot < 1:
        print("\nIsaac was really close! He was off by", str(float(startGuess) - float(realRoot)) + ".","Maybe let him try a little more.")
    else:
        print("\nSir Newton was off by", str(float(startGuess) - float(realRoot)) + ".","\nI suppose if you gave him some more guesses he would have been a little closer!")

    print("\n######\n\n1. Run the calculator again\n2. Return to the main menu\n")
    prog17select = str(input("Select 1 or 2: "))
    if prog17select == "1":
        program17()
    elif prog17select == "2":
        main() 
    else:
        print("Input not recognized, please type 'main()' to restart")  
