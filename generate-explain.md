# some concepts you need to know before you understand how the generate works?
- the game has been made in Array with 9 placeholder [1,2,3,4,5,6,7,8,9]
- the array is splited to 3 parts: row #1 [1,2,3] row #2 [4,5,6] row #3 [7,8,9]
- and another 3 parts: column #1 [1,4,7] column #2 [2,5,8] column #3 [3,6,9]

# how the random generate works?
- the code generate first number and it's between [1, 3]
- then it get's a random place for it in the row #1 between [0, 2]
- then it gets the first number column with another function by sending the number index in row #1 
- then it compare it to columns arrays and if it find match this will be the coulmn of the first number
- then it generate the second number and compare it to the first number if they are the same it generate another number
