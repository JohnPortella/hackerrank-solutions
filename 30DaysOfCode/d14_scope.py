class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        maximumDifference = 0
        for index, value in enumerate(self.__elements):
            for index_2 in range(index+1, len(self.__elements)):
                v_abs = abs(value - self.__elements[index_2])
                maximumDifference = max(maximumDifference, v_abs)                        
        self.maximumDifference = maximumDifference            
    
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
