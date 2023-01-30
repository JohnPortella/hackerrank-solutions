# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

words = []
for _ in range(n):
    s = input()
    words.append( s[0::2] + " " + s[1::2] )

for word in words:
    print(word)
