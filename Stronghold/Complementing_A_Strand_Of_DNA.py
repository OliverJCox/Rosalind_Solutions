def complement_dna(dna_sequence: str) -> str:

    reversed_sequence = dna_sequence[::-1]

    '''Nothing assigned to start and stop in the slice, step set to -1 reverses the string.'''

    translation_table = str.maketrans('ATCG', 'TAGC')
    reversed_sequence = reversed_sequence.translate(translation_table)

    '''maketrans builds a translation table and is faster than creating and using a dictionary.
    translate then switches the characters in the string based on the translation table.'''

    return reversed_sequence

if __name__ == "__main__":

    '''Reading input data from file, removing whitespaces, and converting to uppercase to
    prevent errors if lowercase letters are used in the input file. Using with statement to
    esure file closes to prevent memory leaks.'''

    with open('rosalind_revc.txt', 'r') as file:
        dataset = file.read().strip().upper()

    print(complement_dna(dataset))