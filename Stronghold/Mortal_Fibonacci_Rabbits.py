def Rabbit_Population_Mortal(no_of_months: int, time_alive: int) -> int:

    '''I have chosen to use itteration over recursion for simplicity and memory efficiency.
    O(n) time complexity and O(1) space complexity
    
    This algorithm works by creating a list where index 0 means newborn and index i means 
    month i+1. The value at each index shows how many of that type there are
    
    Time complexity: O(nm) - The loop runs n-1 times and ages[1:] and ages[:-1] both scan and
    copy a list of length n every time the loop is run.
    
    Space complexity: O(m) - ages list only ever holds m numbers at a time.'''

    # At month one there is one newborn pair, creates necessary indices based on life span
    ages = [1] + [0] * (time_alive - 1)  

    for i in range(2, no_of_months + 1):

        # Number of offspring is calculated before ages are updated so newborns aren't counted
        # until the 2nd month
        newborns = sum(ages[1:])  # Pairs aged 2+ months reproduce
        ages = [newborns] + ages[:-1]  # Age shifts right and oldest die

    return sum(ages)

             
if __name__ == "__main__":

    with open("rosalind_fibd.txt",'r') as file:

        '''Using context manager (with) for recource management and to prevent memory leaks'''

        data = file.read().strip()
        data = data.split() # Moving file data into list to assign to variables
        no_of_months =  int(data[0])
        time_alive =  int(data[1])

        population = Rabbit_Population_Mortal(no_of_months, time_alive)
        print(population)

        

