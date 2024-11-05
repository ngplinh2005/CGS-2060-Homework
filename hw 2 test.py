# CGS 2060 Fall Semester 2024
#
# CGS 2060 Homework #2 Finding A Home
#
# Student Name: Linh Nguyen


# Function Name: printMatrix
# Description: This function reads prints out the adoption matrix. The dog names are used for column headers and an adopting family name is used to label each row.
#
# Input:
#    dogDB = list of lists of dog information
#    peopleDB = list of lists of people informaton
#    adoptionMatrix: the matrix that shows who is willing to adopt which dogs

def printMatrix(dogDB, peopleDB, adoptionMatrix):
    print("\nAdoption Matrix:")
    print(" " * 10, end="")
    for loop in range(0, len(dogDB)):
        print("{0:7} ".format(dogDB[loop][0]), end="")
    print()

    for loop1 in range(0, len(adoptionMatrix)):
        print("{0:8s} ".format(peopleDB[loop1][0]), end="")
        for loop2 in range(len(adoptionMatrix[0])):
            print("{0:8d}".format(adoptionMatrix[loop1][loop2]), end="")
        print()

# Function Name: getInfo
# Description: This function reads dog information in from one file and then people information in from another file and then removes "\N" and converts numbers into integers.
#
# Output:
#    dogInfo = list of lists of dog information
#    peopleInfo = list of lists of people information

def getInfo(dogInfo, peopleInfo):
    # Read dog data from DogData.txt
    file_dog_data = open("HW #2 DogData.txt", "r")
    for line in file_dog_data:
        data = line.strip().split(';')
        dogInfo.append([data[0], data[1], int(data[2]), int(data[3]), data[4]])

    # Read people data from PeopleData.txt
    file_people_data = open("HW #2 PeopleData.txt", "r")
    for line in file_people_data:
        data = line.strip().split(';')
        if len(data) == 6:
            peopleInfo.append([data[0], data[1], int(data[2]), int(data[3]), data[4], data[5]])
        else:
            peopleInfo.append([data[0], data[1], int(data[2]), int(data[3]), data[4]])

# Function Name: potentialOwners
# Description: This function matches dogs to the people who would be willing to adopt them. It creates a matrix that shows the matches. Once this has been created, the total number of potential owners for each dog is then calculated.
#
# Input
#    dogDB = list of lists of dog information
#    peopleDB = list of lists of potential adopter information
#
# Output:
#    adoptionMatrix = matrix of who is willing to adopt which dogs
#    numDogsToAdopt: count of the number of dogs each person is willing to adopt
#    numPeopleWhoWillAdopt: count of the number of people who are willing to adopt each dog

def potentialOwners(dogDB, peopleDB, adoptionMatrix, numDogsToAdopt, numPeopleWhoWillAdopt):
    for j, dog in enumerate(dogDB):
        match_counts = [0] * len(peopleDB)
        for i, person in enumerate(peopleDB):
            print(f">>> {dog[0]} is being matched to {person[0]}")
            gender_match = person[1] == dog[1]
            age_match = person[2] <= dog[3] <= person[3]
            has_dog = person[4] == 'Y'
            owns_female_dog = len(person) == 6 and person[5] == 'F'

            if gender_match:
                print(f"{dog[0]} has a gender match to {person[0]}")
            else:
                print(f"{dog[0]} is NOT a gender match to {person[0]}")
            
            if age_match:
                print(f"{dog[0]} has an age match to {person[0]}")
            else:
                print(f"{dog[0]} is NOT an age match to {person[0]}")

            match = False
            if gender_match and age_match:
                if not has_dog:
                    print(f"{person[0]} does not have a dog, {dog[0]} is a match for this family")
                    match = True
                elif not owns_female_dog:
                    print(f"{person[0]} already has a dog")
                    print(f"{person[0]} we are trying to place a {dog[1]} dog, {dog[0]} is a match for this family")
                    match = True
                else:
                    print(f"{person[0]} already has a female dog, {dog[0]} is NOT a match for this family")
            
            # Update adoption matrix and counts if match is found
            if match:
                adoptionMatrix[i][j] = 1
                numDogsToAdopt[i] += 1
                numPeopleWhoWillAdopt[j] += 1
                match_counts[i] += 1
            else:
                match_counts[i] = 0

        # Print summary for each dog
        print(f">>> done with {dog[0]}: {' '.join(map(str, match_counts))}")

# Main Program
dogDB = []
peopleDB = []
getInfo(dogDB, peopleDB)

print("dogInfo:")
print(dogDB[0])
print(dogDB[1])
print(dogDB[2])

print("\npeopleInfo:")
print(peopleDB[0])
print(peopleDB[1])
print(peopleDB[2])

# Initialize adoption matrix and counters
adoptionMatrix = [[0] * len(dogDB) for _ in range(len(peopleDB))]
numDogsToAdopt = [0] * len(peopleDB)
numPeopleWhoWillAdopt = [0] * len(dogDB)

# Determine which families could adopt which dog
potentialOwners(dogDB, peopleDB, adoptionMatrix, numDogsToAdopt, numPeopleWhoWillAdopt)

# Print adoption matrix
printMatrix(dogDB, peopleDB, adoptionMatrix)

# Print the number of dogs each family is willing to adopt
for i, person in enumerate(peopleDB):
    print(f"{person[0]} is willing to adopt {numDogsToAdopt[i]} dogs.")

# Print the number of people willing to adopt each dog
for j, dog in enumerate(dogDB):
    print(f"{dog[0]} can be adopted by {numPeopleWhoWillAdopt[j]} people.")

print("\nDone!")