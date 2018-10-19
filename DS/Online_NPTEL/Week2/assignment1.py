def intreverse(n):
    seperated=[char for char in str(n)]
    if seperated[0]=='-':
        return int('-'+''.join(list(reversed(seperated[1:]))))
    else:
        return int(''.join(list(reversed(seperated))))


print(intreverse(7096))
print(intreverse(-7096))