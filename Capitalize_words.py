b=[]
def captialize_letters(str_1):
    a=str_1.split()
    for i in a:
        b.append((i[0].upper()+i[1:-1]+i[-1].upper()))
    c=(" ").join(b)
    return(c)
a=captialize_letters('My name is Ram')
print(a)