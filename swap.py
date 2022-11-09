def swap_list(somelist):
    size = len(somelist)
    #even
    if (size % 2) == 0:
        print('Even')  
        pos1 = int(len(somelist)/2-1)
        pos2 = int(len(somelist)-1)
        #print(pos1,pos2)
        somelist[pos1], somelist[pos2] = somelist[pos2], somelist[pos1]
        
    #odd
    else: 
        print('Odd')
        pos1 = int(len(somelist)/2-0.5)
        pos2 = int(len(somelist)-1)
        #print(pos1,pos2)
        somelist[pos1], somelist[pos2] = somelist[pos2], somelist[pos1]
        

        
    return somelist;


#evenlist = [0,'hi',2,True]
#oddlist = [0,True,2,3,'hi']
#swap_list(evenlist)
#swap_list(oddlist)
