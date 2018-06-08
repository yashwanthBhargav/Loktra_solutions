
def rev(res,h):
    letters = "acdegilmnoprstuw"
    temp=""
    for i in range(h):
        temp=temp+letters[res%37]
        print res%37
        res=res/37
        print h
    return temp[::-1]

print rev(680131659347,7)