
def areAlmostEqual( s1, s2):
    s = 0
    if s1==s2:
        return True
    if sorted(s1) != sorted(s2):
        return False
    elif s1 != s2:
        for i in range(len(s1)):
            if s1[i] != s2[i]:

                s += 1
            else:
                continue

    if s != 2:
        return False
    else:
        return True

