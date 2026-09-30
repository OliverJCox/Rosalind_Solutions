import Counting_DNA_Nucleotides as cda 
# Importing my module for counting the number of times nucleotides appear in a string

def compute_GC_Content(data: str) -> tuple:

    highest_recorded_values = (0,0)
    rosalind_ID = ""

    for value in data:

        nucleotides = cda.count_nucleotides(value)      
        # Uses previous module to find how many G's and C's in current string being analysed
        g_nucleotides = int(nucleotides[2])
        c_nucleotides = int(nucleotides[1])
        gc_content = ((g_nucleotides + c_nucleotides) / len(value)) * 100 # Find percentage of G's and C's

        if gc_content > highest_recorded_values[1]:
            
            highest_recorded_values = (rosalind_ID, gc_content)

        else:
            rosalind_ID = value

    return highest_recorded_values


def read_fasta_flatfile(path):  
    # Implementing as a seperate method incase FASTA formating its used again

    data = []
    chunks = []     # Stores the chunks of data sequence, builds up as each new line is read

    with open(path) as file:

        for line in file:

            line = line.strip()     # Remove \n characters

            if line.startswith(">"):

                if chunks:      

                    '''if chunks checks if chunks is currently empty (no sequence being built).
                    The nested code executes if the list is not empty.'''                

                    data.append("".join(chunks)) 
                    # Joins the chunks of data that have been found across lines (no spaces)
                    chunks = []
                data.append(line[1:])           # Adds the label to the data list, removing the ">"

            else:
                chunks.append(line)     
                # Adds the next chunk of the data to the current datapoint being built

    if chunks:                                  # Combines chunks for last datapoint
        data.append("".join(chunks))

    return data

if __name__ == "__main__":

    '''__name == __main__ ensures that this code only runs if this program is the root. 
    It wont run if the module is imported'''

    data = read_fasta_flatfile("rosalind_gc.txt")
    
    output = compute_GC_Content(data)
    print(output[0])
    print(output[1])

