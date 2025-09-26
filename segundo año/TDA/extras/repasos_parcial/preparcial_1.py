def greedy(array, comb):

    if comb<array[1]:
        return "No se podia"
    
    acc= 0
    i=0
    comb_temp = 0
    while i<len(array)-1:
        if comb_temp==0 or array[i+1]-array[i] > comb_temp:
            acc+=1
            comb_temp+=comb
        
        comb_temp-=array[i+1]-array[i]
        if comb_temp < 0:
            return "no se podia"
        
        i+=1
    return acc

print(greedy([0, 50, 120, 200, 320, 400, 450], 100))