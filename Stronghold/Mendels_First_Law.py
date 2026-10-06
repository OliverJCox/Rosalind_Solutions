# dominant 2/6 + (0.5 * 2/6) + (2/6 * 2/6)

def Probability_of_Dominant_Allele(homozygous_dominant: int, heterozygous: int, homozygous_recessive: int) -> float:

    """Calculates the probability that two randomly selected organisms will 
    produce an offspring possessing a dominant allele.
    """
    total_population = homozygous_dominant + heterozygous + homozygous_recessive

    # Probability of picking two recessive organisms, 100% recessive
    probability_2_recessive = (homozygous_recessive / total_population) * ((homozygous_recessive - 1) / (total_population - 1)) * 1.00
    
    # Probability of picking two heterozygous organisms, 25% recessive
    probability_2_heterozygous = (heterozygous / total_population) * ((heterozygous - 1) / (total_population - 1)) * 0.25
    
    # Probability of picking one heterozygous and one recessive, 50% recessive
    # Multiplied by 2 because you can pick Aa first OR aa first
    probability_hetero_recessive = ((heterozygous / total_population) * (homozygous_recessive / (total_population - 1)) * 0.50) * 2
    
    # Total probability of producing a recessive offspring
    probability_recessive = probability_2_recessive + probability_2_heterozygous + probability_hetero_recessive
    
    return 1 - probability_recessive # Gives probability of producing a dominant offspring

if __name__ == "__main__":

    '''Using context manager to open the file and read the two strings, inceasing memory 
    efficiency and ensuring the file is properly closed after reading'''

    with open("rosalind_iprb.txt", "r") as file:
        data = file.read().strip()
        homozygous_dominant, heterozygous, homozygous_recessive = map(int, data.split())
        # Split the data from the file into three strings, convert them to integers, and assign them to the respective variables

    probability = print(Probability_of_Dominant_Allele(homozygous_dominant, heterozygous, homozygous_recessive))