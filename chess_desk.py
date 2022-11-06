"""
10101010
01010101
10101010
01010101
10101010
01010101
10101010
01010101
"""
def check_color(coords):
    return ((coords[0] % 2) * (coords[1] % 2)) % 2

def check_equal(coord_1, coord_2):
    return check_color(coord_1) == check_color(coord_2)
a=(1,1)
b=(2,1)
print(check_color(a,b))