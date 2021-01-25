#One of the following 10 statements generates an error. Which one? (Your answer should be a number between 1 and 10.)
x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
y = x[0:50]                    # Statement 2
z = y                          # Statement 3
w = x                          # Statement 4
x[1] = x[1] + 'd'              # Statement 5
x[1][1] = 'y'                  # Statement 6
y[2] = 4                       # Statement 7
z[0] = 0                       # Statement 8
w[4][0] = 1000                 # Statement 9
a = (x[4][1] == 4)             # Statement 10