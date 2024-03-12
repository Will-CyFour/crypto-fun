

def EGCD(a,b):#-> (g,x,y)
    if a == 0:
        return b,0,1
    else:
        q,r = divmod(b, a)
        g,x,y = EGCD(r,a)
        return g,y-q*x,x

def square_and_multiply(base:int, exponent:int):
    if exponent <= 2:
        return base ** exponent
    if exponent % 2 == 0:
        return square_and_multiply(base, exponent // 2) ** 2
    else:
        return base * square_and_multiply(base, exponent - 1)

print(EGCD(3,11))

print(square_and_multiply(6637,45))
print(6637 ** 45)
