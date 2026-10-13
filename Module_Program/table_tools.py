#table function

# n = int(input("Enter a number of you choice :"))
# limit = int(input("Enter the limite of the table :"))
def table(n,limit=10):
    i = 1 

    while i <= limit:
        table = i*n
        print(table)

        i = i+1
    
#table(2,5)