def orangecap(d):
    temp_d={}
    for key,value in d.items():
        for k,v in d[key].items():
            if temp_d.get(k):
                temp_d[k]+=v
            else:
                temp_d.setdefault(k,v)

    inverse = [(value, key) for key, value in temp_d.items()]
    key_to_return=max(inverse)[1]
    return(key_to_return,temp_d[key_to_return])


print(orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}}))

print(orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'ashwin':59, 'Pujara':42}}))
