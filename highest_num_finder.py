#Adding function to find the highest number from a user
def get_highest_num_from_user_input():

#Getting user to input five (5) numbers
    number_1 = int(float(input("Kindly enter your first number: ")))
    number_2 = int(float(input("Kindly enter your second number: ")))
    number_3 = int(float(input("Kindly enter your third number: ")))
    number_4 = int(float(input("Kindly enter your fourth number: ")))
    number_5 = int(float(input("Kindly enter your fifth number: ")))

#Assuming that number_1 is the highest
    highest = number_1

#Find and print the highest number using only if statement
    
    if number_2 > highest:
        highest == number_2
    elif number_3 > highest:
        highest == number_3
    elif number_4 > highest:
        highest == number_4
    elif number_5 > highest:
        highest == number_5
    

#Finalize the code
    print(f"The highest number is: {highest}")

#Call the function
get_highest_num_from_user_input()