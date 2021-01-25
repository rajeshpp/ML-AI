def matched(value):
    d={}
    for val in value:
        if val=='(':
            if len(d.keys())==0:
                d[1]='('
            else:
                d[max(d.keys())+1]='('
        elif val==')':
            try:
                for k in d.keys():
                    if d[k]=='(':
                        d[k]+=')'
            except:
                return False
    for k in d.keys():
        if d[k]!='()':
            return False
    return True




print(matched("(7)(a"))
print(matched("a)*(?"))
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))