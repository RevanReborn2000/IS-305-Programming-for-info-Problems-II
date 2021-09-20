_header = ['', 'Name', '', 'National Pokédex\nnumber', 'Type(s)', '', 'Evolves from', 'Evolves into', 'Notes']
bottom_header = ['Generation','English', 'Japanese', '', 'Primary', 'Secondary', '', '', '']

def combine_headers(list1, list2):
    #LengthTest
    assert len(list1) == len(list2), "Lists are different shape, they are:" + str(len(list1)) + " " + str(len(list2))
    pairs = list(zip(list1,list2))
    MergedList = []
    for pair in pairs:
        header = pair[0]
        botHeader = pair[1]
        if (header == '' and botHeader != '') or (header != '' and botHeader != ''):
            MergedList.append(botHeader)
        elif botHeader == '' and header != '':
            MergedList.append(header)
        else:
            MergedList.append("MissingLabel")
    return MergedList

#Function call
combine_headers(_header, bottom_header)

    
    