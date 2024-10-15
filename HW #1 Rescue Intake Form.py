# CGS 2060 – Fall Semester 2024
#
# CGS 2060 Homework #1 – Owner Surrender Form
#
# Student Name: Linh Nguyen

# Collect Owner's basic info
print("OWNER INFORMATION: ")    
owner_firstname = input("What is the owner's first name? ")
owner_lastname = input("What is the owner's last name? ")
street = input("What is the owner's street address? ")
city = input("What is the owner's city? ")

# Collect Owner's state info
while True:
    state = input("What is the owner's state? ").upper()
    if len(state) == 2:
        break
    print("Error: State info will need to be two characters in length.")

# Collect Owner's zip code
while True:
    zip_code = int(input("What is the owner's zipcode? "))
    if zip_code > 0 and zip_code < 999999:
        break
    print("Error: Zip code should be a number between 0 and 999999.")

# Collect Owner's mobile phone number
while True:
    phone_number = input("What is the owner's mobile phone number? ")
    if len(phone_number) == 12 and phone_number[3] == "-" and phone_number[7] == "-":
        break
    print("Error: The phone number should be entered as XXX-XXX-XXXX format.")

# Collect Owner's email address
while True:
    email = input("What is the owner's email address? ")
    if "@" in email and "." in email:
        break
    print("Error: The email address needs to contain a '@' and '.'")

# Check if he/she is the legal owner
legal_owner = input("Are you the legal owner of this Boxer? (Y/N) ").upper()
if legal_owner == "N":
    explanation = input("If No, please explain. ")

# Print Owner's Information
print("OWNER INFORMATION")
print("\nOwner's Name: {0} {1}".format(owner_firstname, owner_lastname))
print("Address: {0}, {1}, {2} {3}". format(street, city, state, zip_code))
print("Mobile Phone: {0}".format(phone_number))
print("Email Address: {0}".format(email))
if legal_owner == "N":
    print("Legal Owner? No. Explanation: {0}".format(explanation))
else:
    print("Legal Owner? Yes")

# Collect Boxer's Info
# If an owner has more than one dog, loop through each dog.
number_of_dogs = int(input("How many dogs do you have? "))
for i in range(number_of_dogs):
    print("\nBOXER'S INFORMATION - Dog Number {0}".format(i+1))
    dog_name = input("What is the dog's name? ")

    # Collect Dog's gender info
    gender = input("What is the dog's gender? (Choose between a. Neutered Male, b. Intact Male, c. Spayed Famale, d. Intact Female) ")
    if gender == "a":
        dog_gender = "Neutered Male"
    elif gender == "b":
        dog_gender = "Intact Male"
    elif gender == "c":
        dog_gender = "Spayed Female"
    else:
        dog_gender = "Intact Female"

    # Collect Dog's color info
    color = input("What is the dog's color? (Choose between a. Fawn, b. Brindle, c. White (with hearing), d. White (unable to hear)) ")
    if color == "a":
        dog_color = "Fawn"
    elif color == "b":
        dog_color = "Brindle"
    elif color == "c":
        dog_color = "White (with hearing)"
    else:
        dog_color = "White (unable to hear)"

    # Collect Dog's weight and age info
    dog_weight = float(input("What is the dog's current weight? "))
    dog_age = int(input("What is the dog's current age? "))

    # Collect Dog's tail info
    tail = input("What does the dog's tail look like? (Choose between a. Docked and b. Natural (long tail)) ")
    if tail == "a":
        dog_tail = "Docked"
    else:
        dog_tail = "Natural (long tail)"

    # Collect Dog's ears info
    ears = input("What does the dog's ears look like? (Choose between a. Natural (floppy) and b. Cropped) ")
    if ears == "a":
        dog_ears = "Natural (floppy)"
    else:
        dog_ears = "Cropped"
    
    # Collect Dog's microchip info
    microchip = input("Is the Boxer microchipped? (Y/N)? ").upper()
    if microchip == "Y":
        microchip_number = input("What is the microchip number? ")
        microchip_company = input("What is the microchip company? ")

    # Print Dog's Information
    print("\nDOG INFORMATION - Dog Number {0}".format(i + 1))
    print("Name: {0}".format(dog_name))
    print("Gender: {0}".format(dog_gender))
    print("Color: {0}".format(dog_color))
    print("Weight: {0}".format(dog_weight))
    print("Age: {0}".format(dog_age))
    print("Tail: {0}".format(dog_tail))
    print("Ears: {0}".format(dog_ears))
    if microchip == "Y":
        print("Microchipped: Yes")
        print("Microchip Number: {0}".format(microchip_number))
        print("Microchip Company: {0}".format(microchip_company))
    else:
        print("Microchipped: No")

