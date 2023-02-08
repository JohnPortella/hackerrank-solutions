# Enter your code here. Read input from STDIN. Print output to STDOUT
S = (input()).split(" ")
n,m = int(S[0]), int(S[1])

message = "WELCOME"
classic_col = "-"
graph = ".|."

middle = n // 2
for row in range(n):
    if row < middle:
        num_graph = 2*row+1
        char = graph * num_graph
    elif row == middle :
        char = message
    else:
        num_graph = 2*(middle -1) + 1 - (row - (middle+1))*2
        char = graph * num_graph
    
    num_complete = int((m - len(char))/2)
    char = classic_col*num_complete + char + classic_col*num_complete
    print(char)
