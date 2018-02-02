asterix_triangle = int(raw_input("How many lines"))

def asterix_triangle(i, t=0):
    if i == 0:
        return 0
    else:
        print ' ' * ( i + 1 ) + '*' * ( t * 2 + 1 )
        return asterix_triangle( i - 1, t + 1 )