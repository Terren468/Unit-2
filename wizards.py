def wizards (N,start, duels):
    owner=start 
    num_owner= 1
    for i in range (N):
        if duels [i][1]== owner:
            owner = duels[i][0]
            num_owner += 1 
    print(owner, num_owner)
wizards ( 3, "A", ["BA", "CB", "DA"])