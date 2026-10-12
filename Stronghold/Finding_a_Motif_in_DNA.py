def Find_Motif(string: str, sub_string: str) -> list:

    '''Search through string looking for substring. If substring found, update the starting index
    for the search to start one character in from the last detected index of the substring. Repeat
    until no substring found'''
    
    index_of_substring = string.find(sub_string)
    indices = []
    if index_of_substring == -1: # If there is no substring occurance then exit
        print("NO SUBSTRING")
        return
    indices.append(index_of_substring + 1)

    while index_of_substring != -1:
        index_of_substring = string.find(sub_string, index_of_substring + 1)
        if index_of_substring != -1:
            indices.append(index_of_substring + 1)

    output_string = ' '.join(map(str, indices)) # Format output for Rosalind
    return output_string

if __name__ == '__main__':  # Code doesn't run if imported as a module

    with open("rosalind_subs.txt", 'r') as file:
        # Using context manager to open and close files automatically
        string = file.readline().strip()
        sub_string = file.readline().strip()

        print(Find_Motif(string, sub_string))