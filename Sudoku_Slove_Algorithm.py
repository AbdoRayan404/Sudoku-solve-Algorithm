import random
import time

def column_translate(number):
    #the columns in the 3x3 grid
    column_1 = [1,4,7]
    column_2 = [2,5,8]
    column_3 = [3,6,9]

    #it gives u the row of the number u send as input to the function
    if number in column_1:
        return '1'
    elif number in column_2:
        return '2'
    elif number in column_3:
        return '3'
    else: pass

def Generate(grid):
    f_num = random.randint(1, 3) #first random number
    rf_row = random.randint(0, 2) #this gets a random place in the first row
    grid.pop(rf_row) #deletes 0 from the array
    grid.insert(rf_row, f_num) #then replace it with number
    first_column = column_translate(rf_row+1) #sends row and the placeholder number to column_translate function and get the column number as input
    #
    s_num = random.randint(1, 3) #second random number
    while s_num == f_num: #checks if the second number same as first number
        s_num = random.randint(1, 3) #and if it so it will generate new second number until it become uniqe
    rs_row = random.randint(3, 5) #random second row it get random place holder from row 2
    second_column = column_translate(rs_row+1) #get u the column that ur second number has been use it
    while second_column == first_column: #checks if the second column is the same as first ccolumn
        rs_row = random.randint(3, 5) #and if it so it will generate another random numbers until it become in other column
        second_column = column_translate(rs_row+1)
    grid.pop(rs_row) #deletes 0 from the array
    grid.insert(rs_row, s_num) #then replace it with second number
    #
    t_num = random.randint(1, 3)
    while t_num == s_num or t_num == f_num:
        t_num = random.randint(1, 3)
    rt_row = random.randint(6, 8)
    third_column = column_translate(rt_row+1)
    while third_column == second_column or third_column == first_column:
        rt_row = random.randint(6, 8)
        third_column = column_translate(rt_row+1)
    grid.pop(rt_row)
    grid.insert(rt_row, t_num)
    grid_print(grid, 3)

def grid_print(grid, recursion):
    #this function use recursion to print the 3x3 grid
    global first_time_run
    if recursion <= 0:
        if first_time_run == True:
            print('The Algorithm will Solve it now...')
            first_time_run = False
        else: print('------------')
        time.sleep(0.5)
        solve(grid)
    else:
        global grid_print_outside_var
        i = 0
        while i < len(grid)/3:
            temp = grid[grid_print_outside_var]
            temp = str(temp)
            temp = temp + ' '
            print(temp, end='')
            grid_print_outside_var += 1
            i += 1
        print(' ')
        grid_print(grid, recursion-1)
#solve Algorithm doun!!!

def row_column(placeholder):
    row_1 = [1,2,3]
    row_2 = [4,5,6]
    row_3 = [7,8,9]
    column_1 = [1,4,7]
    column_2 = [2,5,8]
    column_3 = [3,6,9]
    row = '0'
    column = '0'
    #row finder
    if placeholder in row_1:
        row = '1'
    if placeholder in row_2:
        row = '2'
    if placeholder in row_3:
        row = '3'
    #column finder
    if placeholder in column_1:
        column = '1'
    if placeholder in column_2:
        column = '2'
    if placeholder in column_3:
        column = '3'

    return row, column


def solve(grid):
    rows = []
    columns = []
    row_1 = [0,1,2]
    row_2 = [3,4,5]
    row_3 = [6,7,8]
    column_1 = [0,3,6]
    column_2 = [1,4,7]
    column_3 = [2,5,8]
    solves = []
    i = 0
    while i < len(grid):
        if 0 in grid:
            if grid[i] == 0:
                solves.append(i)
                x,y = row_column(i+1)
                rows.append(x)
                columns.append(y)
        else:
            print('Done')
            exit()
        i += 1
    #print('rows:',rows)
    #print('columns:',columns)
    #check the frist row and column
    search_array = []
    search = 0
    search_compare = 2
    while search < search_compare:
        if len(rows) == 1:
            search_compare = 1
        if rows[search] == '1':
            j = 0
            while j < len(row_1):
                r_1 = grid[row_1[j]]
                #print('row', r_1)
                if r_1 != 0:
                    search_array.append(r_1)
                j += 1

        if columns[search] == '1':
            c = 0
            while c < len(column_1):
                c_1 = grid[column_1[c]]
                #print('column', c_1)
                if c_1 != 0:
                    search_array.append(c_1)
                c += 1
        #
        if rows[search] == '2':
            j_2 = 0
            while j_2 < len(row_2):
                r_2 = grid[row_2[j_2]]
                #print('row',r_2)
                if r_2 != 0:
                    search_array.append(r_2)
                j_2 += 1

        if columns[search] == '2':
            c_2 = 0
            while c_2 < len(column_2):
                cl_2 = grid[column_2[c_2]]
                #print('column',cl_2)
                if cl_2 != 0:
                    search_array.append(cl_2)
                c_2 += 1
            #print('end of tiger tiger')
        #
        if rows[search] == '3':
            j_3 = 0
            while j_3 < len(row_3):
                r_3 = grid[row_3[j_3]]
                #print('row',r_3)
                if r_3 != 0:
                    search_array.append(r_3)
                j_3 += 1

        if columns[search] == '3':
            c_3 = 0
            while c_3 < len(column_3):
                cl_3 = grid[column_3[c_3]]
                #print('column',cl_3)
                if cl_3 != 0:
                    search_array.append(cl_3)
                c_3 += 1
        search += 1
    runed_before = False
    sol = 0
    fix = 0
    arr = [1,2,3]
    while fix < 1:
        while sol < len(search_array)/3:
            if runed_before == False:
                num_1 = search_array[sol]
                runed_before = True
            elif runed_before == True:
                num_2 = search_array[sol]
            sol += 1
        if num_1 in arr:
            temp = arr.index(num_1)
            arr.pop(temp)
        if num_2 in arr:
            temp_2 = arr.index(num_2)
            arr.pop(temp_2)
        #print(arr)
        fix += 1
    now = arr[0]
    new_grid = grid
    solvee = solves[0]
    new_grid.pop(solvee)
    new_grid.insert(solvee, now)
    global grid_print_outside_var
    grid_print_outside_var = 0
    grid_print(new_grid, 3)


#               1 2 3 4 5 6 7 8 9
grid_numbers = [0,0,0,0,0,0,0,0,0]
grid_print_outside_var = 0
while_loop_fix = 0
first_time_run = True
Generate(grid_numbers)
