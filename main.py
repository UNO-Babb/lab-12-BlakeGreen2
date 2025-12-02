# The purpose of this lab is to see the speed of different sorting techniques.
# Use the same random seed to create the same random list of numbers for each run.
# You can change the number of elements in the arrays
# We will test 3 arrays, one that is already in order, one that is sorted in reverse order, and one that is random.

import time
import random
import os
# Your current working directory needs to see the AllSorts.py
# If you have issues you should comment out this line.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import AllSorts

def main():
    random.seed(2020) # This makes sure that the random list will be the same every time.

    numberTerms = 10000

    orderedList = []
    reversedList = []
    randomList = []

    for i in range(numberTerms):
        orderedList.append(i)
        reversedList.insert(0, i)
        randomList.append(random.randint(1, 10000))

    # List of sorting functions and their names
    sorts = [
        ("Bubble Sort", AllSorts.bubbleSort),
        ("Bubble Sort Early Exit", AllSorts.bubbleSortEarlyExit),
        ("Selection Sort", AllSorts.selectionSort),
        ("Insertion Sort", AllSorts.insertionSort),
        ("Merge Sort", AllSorts.mergeSort)
    ]

    # Run each of the sorts on all three lists
    for sortName, sortFunc in sorts:
        # Copy lists so each sort gets the same original data
        orderedCopy = orderedList[:]
        reversedCopy = reversedList[:]
        randomCopy = randomList[:]

        print("\nRunning %s..." % sortName)

        startTime = time.time()
        sortFunc(orderedCopy)
        endTime = time.time()
        print("Ordered list time: %.5f seconds" % (endTime - startTime))

        startTime = time.time()
        sortFunc(reversedCopy)
        endTime = time.time()
        print("Reversed list time: %.5f seconds" % (endTime - startTime))

        startTime = time.time()
        sortFunc(randomCopy)
        endTime = time.time()
        print("Random list time: %.5f seconds" % (endTime - startTime))

    print("\nSorting Complete")

if __name__ == '__main__':
    main()
