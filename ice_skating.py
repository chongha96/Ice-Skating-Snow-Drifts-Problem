
def coord_grouping(snow_drifts, coordinates):
    #Use the coordinate tuple of each item as the key, and the x coordinate as the default value.
    #This will be used identify all unique groups of coordinates
    dict_coords = {key: key[0] for key in coordinates}

    #Breakdown of function:
    #1. Loop through each key of dict_coords.
    #2. A second loop (nested) of each key of dict_coords.
    #3. If there is a matching coordinate between the two,
    #   updates all values for keys that would be in the same grouping
    for i in dict_coords:
        for j in dict_coords:
            if i!=j:
                #If there is a common x or y in dict_coords, update both i and j's key to the common coordinate
                if i[0] == j[0] or i[1] == j[1]:
                    #updates entire dictionary with the shared coordinate if one is found
                    dict_coords = update_shared_values(dict_coords,i,j)

    #Returns the number of unique value sets minus 1 since there is no drift needed at the start
    return len(set(dict_coords.values())) - 1

def update_shared_values(dict_coords, former, new):
    #If former value (i) is different from new value (j), updates all (i) values in the dictionary
    #This ensures that the value remains as an identifier as a set of movements
    new_shared = (set(former) & set(new)).pop()
    for i in dict_coords:
        if dict_coords.get(i) != dict_coords.get(new):
            dict_coords[i] = new_shared
    return dict_coords

def main():
    #Test coordinates
    coordinates = [(1,1),(1,2)]
    snow_drifts = len(coordinates)
    length = coord_grouping(snow_drifts,coordinates)
    print(f"The length is {length} for {coordinates}")

if __name__ == "__main__":
    main()
