#### Fonction secondaire


def ispalindrome(p):

    s1 = p.replace(' ','').lower()
    s2 = s1[::-1]
    return p == s2 
    #i = 0
    #j = len(s) - 1
    #while i < j:
    #    while s[i] == ' ': i +=1
    #    while s[j] == ' ': j -=1
    #    if s[i].lower() != s[j].lower():
    #        return False
    ##    i += 1
    #    j -= 1
    # return True

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()