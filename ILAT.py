





# Program for  Inverted Left-Aligned Triangle
for i in range(5):  #i indicates the number of rows and they are 5
    for j in range(5-i):  #j indicates the columns,the stars are printed based on 5-i
        print("*",end=" ")  #After prints the * and end is used to ends in the same line
    print()  #it is used to print the * in the nextline

    '''
     The Output of the above code
    * * * * *
    * * * *
    * * *
    * * 
    *
        
    '''
