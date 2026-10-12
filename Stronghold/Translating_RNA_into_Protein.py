def Translate_RNA_Into_Protein(rna_string : str) -> str:

    rna_codon_table = {     # First row blocks (U)
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

    chunks_of_rna = [rna_string[i:i+3] for i in range(0,len(rna_string), 3)]
    # Make a list containing each of the sets of 3 characters that will map to a protein letter

    protein_string = ""

    for chunk in chunks_of_rna:
        if len(rna_codon_table[chunk]) > 1: # Handles the Stop code
            break
        protein_string += rna_codon_table[chunk]

    return protein_string

if __name__ == '__main__':  # This code can be used as a module without this running

    with open("rosalind_prot.txt",'r') as file: 
        # Using context manager so that file open and close is handled propperly
        rna_string = file.read().strip().upper()

        print(Translate_RNA_Into_Protein(rna_string))
