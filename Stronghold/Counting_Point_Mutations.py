def count_point_mutations(string1 : str, string2 : str) -> int:

    if len(string1) != len(string2):
        raise ValueError("Strings must be of the same length")
    
    mutations = 0

    for i in range(len(string1)):
        # Compare each character in the strings and count the number of differences
        if string1[i] != string2[i]: 
            mutations += 1
    return mutations

if __name__ == "__main__":

    '''Using context manager to open the file and read the two strings, inceasing memory 
    efficiency and ensuring the file is properly closed after reading'''

    with open("rosalind_hamm.txt", "r") as file:
        string1 = file.readline().strip().upper()
        string2 = file.readline().strip().upper()
        print(count_point_mutations(string1, string2))