# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def get_hypothenuse(a, b):
    return math.sqrt( a**2 + b**2 )

def convert_rads_to_degrees(rad):
    return a_mbc*180/math.pi

# input
ab = int(input())
bc = int(input())
# get hypothenuse of main triangle
ac = get_hypothenuse(ab, bc)
# get sin of angle AB side
sin_a_bca = ab/ac
# median of a triangle theorem    
mc = bm = ac/2
# Relation between the sides and angles
a_mbc = math.asin( (sin_a_bca * mc) / bm )
# Output
print( f"{round( convert_rads_to_degrees(a_mbc) )}\u00b0" )
