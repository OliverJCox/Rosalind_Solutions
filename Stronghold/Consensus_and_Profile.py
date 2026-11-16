from Computing_GC_Content import read_fasta_flatfile


def Get_Matrix(dna_strings: list) -> list:

    dna_strings = dna_strings[1::2] # Takes every other item
    
    return dna_strings

    
def Find_Consensus_And_Profile(dna_matrix: list) -> tuple[str, dict]:

    profile = {base: [] for base in "ACGT"} # Using dictionary comprehension to construct profile
    column = []

    for column in zip(*dna_matrix):   
        # Zip matches each of the elements in the list to the corresponding item in the next list
        # eg. (1,2,3), (A,C,G) goes to (1,A), (2,C), (3, G)
        # Zip is done lazily so information is discarded after being used, optimises memory use
        for base in "ACGT":
            profile[base].append(column.count(base))
            # Gets the number of occurrances of each nucleotide and places it in profile

    consensus_string = "".join(
        max("ACGT", key=lambda base: profile[base][i]) for i in range(len(dna_matrix[0]))
        )
    # Finds the most common letter for each column and adds it to the string
    # Finds max for each column as for i in range... is not in []

    return consensus_string, profile


if __name__ == "__main__":
    data = read_fasta_flatfile("rosalind_cons.txt")
    consensus, profile = Find_Consensus_And_Profile(Get_Matrix(data))

    print(consensus)
    for base in "ACGT":
        print(f"{base}: {' '.join(map(str, profile[base]))}")
        # Puts each number set for each base into a string form for Rosalind
