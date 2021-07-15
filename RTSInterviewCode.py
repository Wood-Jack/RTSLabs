



#
#
#
# Programmer:    Woodrow Jackson
#
#
# Description: Answering Given Interview Questions in python
# 1) Print the number of integers in an array that are above
# the given input and the number that are below, e.g. for the array [1, 5, 2, 1, 10]
# with input 6, print “above: 1, below: 4”.
#
# 2) Rotate the characters in a string by a given
# input and have the overflow appear at the beginning, e.g. “MyString” rotated by 2 is “ngMyStri”.
#
#3) If you could change 1 thing about your favorite framework/language/platform (pick one), what would it be?
#

from array import *

# Question 1a) created a Function that will take in a given
# array and give the index that is above and below of a number
# inputted that will be used to answer question 1
def checkAboveAndBelow(arr, val):

    for i in arr:
        if val >= i:
            x = arr.index(i) +1

        if val <= i:
            y = arr.index(i)

    print("Above:" , x ,"Below:", y)




#Creating an array for numbers provided using the example given to me
def main():

    #Question 1b) using the example given to output the correct index of
    # an array if its above or below a number
    numbers = array('i',[1,5,2,1,10])
    print("numbers in given array example")
    for i in range(5):
        print(numbers[i])
    x = int(input("Enter number to compare"))

    print(checkAboveAndBelow(numbers,x))


    #Question 1c) Advance Example of taking array creating size of an array and taking elements of an array
    # Which then prints the array of numbers inputted goes off example 1 giving the
    # number if it is above or below a certain index
    numberArray= array('i',[])
    sizeOfArray = int(input("Enter size of array"))
    print("Enter Elements of an array")

    for i in range(sizeOfArray):
        n= int(input())
        numberArray.append(n)
        print(i)

    numCompare = int(input("Enter number to compare"))

    print(checkAboveAndBelow(numberArray, numCompare))

# Question 2 :Rotate the characters in a string by a given input and
# have the overflow appear at the beginning, e.g. “MyString” rotated by 2 is “ngMyStri”.

    print("Instructions: DO NOT SPACE it will cause words to space EX. Hello to be o Hell ")
    print("If space is choosen is greater than the number space for the word then word will not change \n")

    # takes in the word
    word = input("Please enter a word to be reverse ", )


    print()
    print(word)

    # Asks for user input for to create spacing
    wordRotate = int(input("Please enter the number of spaces you would like to rotate the word"))

    # Explanation colon use: A colon used on the left side of the index will display everything
    # before the particular index as an output.a colon used on the right side will display
    # everything after index as an output.
    word = word[-wordRotate:] + word[:-wordRotate]

    print(word)

    """
    Question 3)  If you could change 1 thing about your favorite framework/language/platform (pick one), what would it be?
    
    Answer: If I could change 1 thing it would be in python and it would be its speed. Unlike other programming language
    python is interpreted line by line. Say if you have a big project then you might not want to consider using python.
    Because of it slowness. Other programming languages like C++ and Java are faster than python because they instantly 
    are complied or execute at once. If their was way to make python faster I would because it would could be used in many other
    applications as well. 
    """

main()


