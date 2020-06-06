'''
An imminent hurricane threatens the coastal town of Codeville.
If at most two people can fit in a rescue boat,
and the maximum weight limit for a given boat is k,
determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200,
the smallest number of boats required will be three.
'''
import itertools

population_weights = [100, 200, 150, 80]
MAX_WEIGHT = 200

def find_sum(population_weights, boats_num):

    #checks if the sum of 2 persons is less than MAX_WEIGHT
    for persons in itertools.combinations(population_weights, 2):
        if sum(persons) <= MAX_WEIGHT:
            #removes the checked persons
            [population_weights.remove(person) for person in persons]
            #adds 1 boat per iteration
            boats_num += 1
            return find_sum(population_weights, boats_num)

    #returns a tuple of the number of boats
    #and
    #the rest of the population that cannot be combined
    return boats_num, population_weights

def main():
    data = find_sum(population_weights, 0)
    boats = data[0]
    separate_persons = len(data[1])
    boats += separate_persons

    print(f'The min number of boats is {boats}')
    return boats

if __name__ == '__main__':
    main()
