# Enter your code here. Read input from STDIN. Print output to STDOUT
dims =  list(map(int, input().split(" ")))
n,m = dims[0], dims[1]

base_values = list(map(int, input().split(" ")))
a_values = set(map(int, input().split(" ")))
b_values = set(map(int, input().split(" ")))

if len(base_values) != n or len(a_values) != m  or len(b_values) != m:
    raise Exception("Different dimensions")

points_by_value = [1 if i in a_values else -1 if i in b_values else 0 for i in base_values]
print(sum(points_by_value))
