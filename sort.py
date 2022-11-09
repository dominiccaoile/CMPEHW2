
def sort_dictionary(somedictionary):

    out_list = []
    age_list = []
    for k,v in somedictionary.items():
        out_list.append((k,v[0]))
        age_list.append(v[1])

    output = [x for _, x in sorted(zip(age_list, out_list))]
    

    return;


#d = {'a': (4082222, 32), 'b': (6502222, 42), 'c': (1200022, 22)}
#sort_dictionary(d)


#Output:{'Tom': 408, 'Mary':669,'Sara: 800'}

