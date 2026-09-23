def transcribe_dna_to_rna(dna_sequence: str) -> str:

    rna_sequence = dna_sequence.replace('T', 'U')
    # Using built-in method to replace 'T' with 'U' for speed purposes
    return rna_sequence

if __name__ == "__main__":

    '''Reading input data from file, removing whitespaces, and converting to uppercase to
    prevent errors if lowercase letters are used in the input file. Using with statement to
    esure file closes to prevent memory leaks.'''

    with open('rosalind_rna.txt', 'r') as file:
        dataset = file.read().strip().upper()

    print(transcribe_dna_to_rna(dataset))