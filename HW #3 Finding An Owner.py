# CGS 2060 – Fall Semester 2024
# CGS 2060 Homework #3 – Finding An Owner
# Linh Nguyen

def adoptDogs(dogDB, peopleDB, adoptionMatrix, numDogsToAdopt, numPeopleWhoWillAdopt):
    while len(dogDB) > 0:  # Continue until all dogs are adopted
        print(f"\n>>> There are {len(peopleDB)} adopters left")

        # Find the dog with the fewest adopters
        min_adopters = 9999  
        dog_index = -1
        for i in range(len(numPeopleWhoWillAdopt)):
            if numPeopleWhoWillAdopt[i] < min_adopters and numPeopleWhoWillAdopt[i] > 0:
                min_adopters = numPeopleWhoWillAdopt[i]
                dog_index = i
        dog_name = dogDB[dog_index][0]
        print(f">>> {dog_name} could be adopted by {min_adopters} people")
        print(f">>> {dog_name} currently has the fewest people who want to adopt it")

        # Find the adopter with the fewest dogs they are willing to adopt
        adopter_index = -1
        min_dogs = 9999
        for j in range(len(peopleDB)):
            if adoptionMatrix[j][dog_index] == 1 and numDogsToAdopt[j] < min_dogs:
                min_dogs = numDogsToAdopt[j]
                adopter_index = j
        adopter_name = peopleDB[adopter_index][0]
        print(f"\nLooking to match {dog_name} with an owner.")
        print(f"@@@ Checking to see if {adopter_name} is willing to adopt {dog_name}")
        print(f"@@@ Answer: {adoptionMatrix[adopter_index][dog_index]}")

        print(f"\n{dog_name} will be adopted by {adopter_name}")

        # Update adoptionMatrix and counts to remove dog and adopter
        print(f"+++ Removing {dog_name} from adoption matrix.")
        for row in adoptionMatrix:
            row[dog_index] = 0  # Mark the column as removed
        numPeopleWhoWillAdopt[dog_index] = 0

        print(f"+++ Removing {adopter_name} from adoption matrix.")
        for k in range(len(adoptionMatrix[0])):
            adoptionMatrix[adopter_index][k] = 0  # Mark the row as removed
        numDogsToAdopt[adopter_index] = 0

        # Remove the dog and adopter from their respective databases
        print(f"+++ Removing dog: {dogDB[dog_index]}")
        print(f"+++ Removing dog adoption count: {min_adopters}")
        print(f"+++ Removing person: {peopleDB[adopter_index]}")
        print(f"+++ Removing num dogs person will adopt: {min_dogs}")

        # Rebuild databases without the removed dog and adopter
        dogDB.pop(dog_index)
        peopleDB.pop(adopter_index)

        adoptionMatrix = [
            [adoptionMatrix[i][j] for j in range(len(adoptionMatrix[0])) if j != dog_index]
            for i in range(len(adoptionMatrix)) if i != adopter_index
        ]
        numPeopleWhoWillAdopt = [numPeopleWhoWillAdopt[j] for j in range(len(numPeopleWhoWillAdopt)) if j != dog_index]
        numDogsToAdopt = [numDogsToAdopt[i] for i in range(len(numDogsToAdopt)) if i != adopter_index]

# Main Program
dogDB = [
    ['Rover', 'M', 38, 3, 'Brown'],
    ['Missy', 'F', 35, 4, 'White'],
    ['Hank', 'M', 52, 6, 'Brindle']
]
peopleDB = [
    ['Adams', 'M', 2, 7, 'N'],
    ['Johnson', 'M', 5, 8, 'N'],
    ['Peters', 'F', 2, 8, 'N']
]

# Initialize the adoption matrix
adoptionMatrix = [
    [1, 0, 0],  # Adams can adopt Rover
    [0, 0, 1],  # Johnson can adopt Hank
    [0, 1, 0]   # Peters can adopt Missy
]

numDogsToAdopt = [2, 1, 1]  # Adams is willing to adopt 2 dogs, Johnson 1, and Peters 1
numPeopleWhoWillAdopt = [1, 1, 2]  # Rover can be adopted by 1 person, Missy by 1, Hank by 2

# Print Dog and People Info
print("\ndogInfo:")
for dog in dogDB:
    print(dog)
print("\npeopleInfo:")
for person in peopleDB:
    print(person)

# Print Adoption Matrix
print("\nAdoption Matrix:")
print("          Rover   Missy   Hank")
for i in range(len(adoptionMatrix)):
    print(f"{peopleDB[i][0]:<10} {' '.join(str(adoptionMatrix[i][j]) for j in range(len(adoptionMatrix[0])))}")

# Start the adoption process
adoptDogs(dogDB, peopleDB, adoptionMatrix, numDogsToAdopt, numPeopleWhoWillAdopt)

print("\nDone!")