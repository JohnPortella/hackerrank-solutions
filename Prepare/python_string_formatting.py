def print_formatted(number):
    # your code goes here
    len_format = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        oct_n = oct(i)[2:]
        hex_n = hex(i)[2:].upper()
        bin_n = bin(i)[2:]
        
        print(f"{str(i):>{len_format}} {oct_n:>{len_format}} {hex_n:>{len_format}} {bin_n:>{len_format}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
