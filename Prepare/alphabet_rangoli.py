import string 

def print_rangoli(size):
    # your code goes here    
    base_line = '-'
    alpha = string.ascii_lowercase

    for index in range(0,2*n - 1):
        # create string with base_line x total columns
        row = base_line * (4 * n - 3)
        # get value i by growth and decrease
        if index < (2*n - 1) // 2:
            i = (n-1) - index
        else:
            i = index - ((2*n - 1) // 2)
        # generate the row with the letters
        for j in range(0, n - i):
            row = row[:(4*n - 3)// 2 - j*2] + alpha[j + i ] + row[(4*n - 3)// 2 - j*2+1:]
            row = row[:(4*n - 3)// 2 + j*2] + alpha[j + i ] + row[(4*n - 3)// 2 + j*2+1:]
        # print row
        print(row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
