def count_nucleotides(dna_sequence: str) -> str: # Specifying input type
                                                  # and return type for readability and reusability.

    # Using .count() as opposed to iterating as it is more efficient and cleaner.
    a = dna_sequence.count('A')
    c = dna_sequence.count('C')
    g = dna_sequence.count('G')
    t = dna_sequence.count('T')

    return f"{a} {c} {g} {t}"


if __name__ == "__main__":          

    ''' Executing the code to read the data file only if this entire script is being 
        run as the main program and not being imported as a module in another script.'''
    
    with open("rosalind_dna.txt", "r") as file: 

        ''' Using a context manager to open file, this ensures the file is closed 
        even if an error occurs and prevents memory leaks.'''

        dataset = file.read().strip().upper()  # .strip() removes any leading/trailing whitespace.
        print(count_nucleotides(dataset))
