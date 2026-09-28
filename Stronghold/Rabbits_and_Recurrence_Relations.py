def rabbit_population(no_of_months: int, offspring_per_pair: int) -> int:

    '''I have chosen to use itteration over recursion for simplicity and memory efficiency.
    O(n) time complexity and O(1) space complexity'''

    if no_of_months == 1 or no_of_months == 2:

        return 1

    previous_no_of_pairs = 1
    no_of_breedable_pairs = 1

    for no_of_months in range(3, no_of_months + 1):

        '''Fibonacci sequence calculation: F(n) = F(n-1) + offspring_per_pair * F(n-2)'''

        no_of_pairs = previous_no_of_pairs + (offspring_per_pair * no_of_breedable_pairs)
        no_of_breedable_pairs = previous_no_of_pairs
        previous_no_of_pairs = no_of_pairs

    return no_of_pairs
if __name__ == "__main__":
    with open("rosalind_fib.txt",'r') as file:

        '''Using context manager (with) for recource management and to prevent memory leaks'''

        data = file.read()
        data = data.split() # Moving file data into list to assign to variables 

        no_of_months =  int(data[0])
        offspring_per_pair =  int(data[1])

        population = rabbit_population(no_of_months,offspring_per_pair)
        print(population)

        

