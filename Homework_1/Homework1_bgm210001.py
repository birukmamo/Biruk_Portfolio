import pickle
import sys
import os
import re


# create the Person class containing the init and display method
class Person:
    def __init__(person, last, first, mi, id, phone):
        person.last = last
        person.first = first
        person.mi = mi
        person.id = id
        person.phone = phone

    def display(profile):
        print("Employee id:", profile.id, "\n\t    ", profile.first, profile.mi, profile.last)
        print("\t    ", profile.phone)

def convertFile(filepath):
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text = f.read()
    return text

def TextProcess(file):
    dict = {}
    # split the elements from the file and iterate them starting from the second line
    sentences = file.split('\n')
    for sentence in sentences[1:]:
        # get all the values for the person objet
        tokens = sentence.split(',')
        # change the lastname and first name to capital
        lastName = tokens[0][0].upper() + tokens[0][1:].lower()
        firstName = tokens[1][0].upper() + tokens[1][1:].lower()
        # change the mid to capital and if doesn't have string change to X
        mid = tokens[2].upper() if tokens[2] != '' else 'X'

        Id_person = tokens[3] # read the id from the input file

        # check if the file contain valid id else repeat until the valid one
        valid_id = re.search("[a-zA-Z]{2}[0-9]{4}", Id_person)
        while not valid_id:
            print("ID is invalid:", Id_person)
            print("ID is two letters followed by 4 digits")
            Id_person = input("Please input a valid id: ")
            valid_id = re.search("[a-zA-Z]{2}[0-9]{4}", Id_person)

        # check if the number is valid format else reapeat until the user input the valid one
        number = tokens[4]
        valid_number = re.search("([0-9]{3})-([0-9]{3})-([0-9]{4})", number)
        while not valid_number:
            print(f"Phone {number} is invalid")
            print("Enter phone number in the form 123-456-7890")
            number = input("Enter phone number: ")
            valid_number = re.search("([0-9]{3})-([0-9]{3})-([0-9]{4})", number)

        # create the person object
        person = Person(lastName, firstName, mid, Id_person, number)
        # check if the personID already exist in the dictionary
        if Id_person in dict:
            print(f"{Id_person} already exists!")
        else:
            dict[Id_person] = person
    return dict


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Invalid argument: put the file name')
    else:
        infile = sys.argv[1]
        readText = convertFile(infile)
        dict = TextProcess(readText)

        # save pickle
        pickle.dump(dict, open('dict.p', 'wb'))
        # read pickle
        dict_in = pickle.load(open('dict.p', 'rb'))
        print("Employee list:\n")
        # display the output
        for person in dict_in.values():
            person.display()
            print()