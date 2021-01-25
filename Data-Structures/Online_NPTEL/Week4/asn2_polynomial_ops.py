def poly_valid(p):
    d={}
    """Below for loop converts polynomial into dictionary as {exponent:coefficient}.
    Below for loop also returns False, if we have 2 same exponents in single polynomial"""
    for tup in p:
        if d.get(tup[1]):
            return False
        else:
            d.setdefault(tup[1],tup[0])
    """Below for loop returns False, if we have any zero cofficient.
       Also, Below for loop returns False, if we have any negative exponents """
    for k,v in d.items():
        if v==0:
            return False
        if k<0:
            return False
    return True

def del_zero_coefficient(p1,p2):
    d1, d2 = {}, {}
    keys_to_delete = []
    for tup in p1:
        d1.setdefault(tup[1],tup[0])
    for tup in p2:
        d2.setdefault(tup[1],tup[0])
    for d1_key in d1.keys():
        if d2.get(d1_key):
            if d2.get(d1_key)+d1.get(d1_key)==0:
                keys_to_delete.append(d1_key)
    for key_to_delete in keys_to_delete:
        del d1[key_to_delete],d2[key_to_delete]
    return (d1,d2)

def addpoly(p1,p2):
    final = {}
    keys_to_add = []
    if not poly_valid(p1) and not poly_valid(p2):
        return []

    d1,d2=del_zero_coefficient(p1,p2)

    for d1_key in d1.keys():
        if d2.get(d1_key):
            keys_to_add.append(d1_key)
    for common_key in keys_to_add:
        final[common_key]=d1.get(common_key)+d2.get(common_key)
    for d1_key in d1.keys():
        if d1_key in keys_to_add:
            pass
        else:
            final[d1_key]=d1[d1_key]
    for d2_key in d2.keys():
        if d2_key in keys_to_add:
            pass
        else:
            final[d2_key]=d2[d2_key]

    final_list=[(final[key],key) for key in sorted(final.keys(),reverse=True)]
    return (final_list)



def multpoly(p1,p2):
    temp={}
    if not poly_valid(p1) and not poly_valid(p2):
        return []
    for p1_item in p1:
        for p2_item in p2:
            key=p1_item[1]+p2_item[1]
            value=p1_item[0]*p2_item[0]
            if temp.get(key):
                temp[key].append(value)
            else:
                temp[key]=[value]
    for key in temp.keys():
        temp[key]=sum(temp[key])

    final=[(temp[key],key) for key in sorted(temp.keys(),reverse=True) if temp[key]!=0]

    return final


print(addpoly([(4,3),(3,0)],[(-4,3),(2,1)]))
print(addpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))
print(addpoly([(2,1)],[(-2,1)]))

print(multpoly([(4,3),(3,0)],[(-4,3),(2,1)]))
print(multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))
print(multpoly([(2,1)],[(-2,1)]))

