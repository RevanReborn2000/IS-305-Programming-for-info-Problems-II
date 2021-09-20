#This version utilized list indexing.


_header = ['', 'Name', '', 'National Pokédex\nnumber', 'Type(s)', '', 'Evolves from', 'Evolves into', 'Notes']
bottom_header = ['Generation','English', 'Japanese', '', 'Primary', 'Secondary', '', '', '']

def combine_headers(list1, list2):
    #LengthTest
    assert len(list1) == len(list2), "Lists are different shape, they are:" + str(len(list1)) + " " + str(len(list2))
    MergedList = []
    for i in range(len(list1)):
        header = list1[i]
        botHeader = list2[i]
        if (header == '' and botHeader != '') or (header != '' and botHeader != ''):
            MergedList.append(botHeader)
        elif botHeader == '' and header != '':
            MergedList.append(header)
        else:
            MergedList.append("MissingLabel")
    return MergedList

#Function call
combine_headers(_header, bottom_header)

    
    
