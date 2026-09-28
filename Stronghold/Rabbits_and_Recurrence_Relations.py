def rabbit_population(no_of_months: int, offspring_per_pair: int) -> int:

    if no_of_months == 1 or no_of_months == 2:

        return 1

    previous_no_of_pairs = 1
    no_of_breedable_pairs = 1

    for no_of_months in range(3, no_of_months + 1):

        no_of_pairs = previous_no_of_pairs + (offspring_per_pair * no_of_breedable_pairs)
        no_of_breedable_pairs = previous_no_of_pairs
        previous_no_of_pairs = no_of_pairs

    return no_of_pairs

with open("rosalind_fib.txt",'r') as file:

    data = file.read()
    data = data.split()

    n =  int(data[0])
    k =  int(data[1])

    x = rabbit_population(n,k)
    print(x)

    

