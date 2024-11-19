import csv

def add_student(first_name, last_name, reg_no):
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name, reg_no])


def search_student(first_name, reg_no):
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == reg_no:
                print(f'First_Name: {row[0]} Last_Name: {row[1]} Reg_No: {row[2]}')
                return


def delete_student(first_name):
    rows = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    data = []
    for row in rows:
        if row[0] != first_name:
            data.append(row)

    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for val in data:
            writer.writerow(val)


def main():
    while True:
        print("1.Add Student")
        print("2.Search for a Student")
        print("3.Delete a Student")
        print("4.Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            first_name = input("Enter Student First_Name: ").capitalize()
            last_name = input("Enter Student Last_Name: ").capitalize()
            reg_no = input("Enter Student Reg_No: ").capitalize()

            add_student(first_name, last_name, reg_no)
            return

        elif choice == '2':
            first_name = input("Enter Student First_Name: ").capitalize()
            reg_no = input("Enter Reg_No.: ").capitalize()
            search_student(first_name, reg_no)
            return

        elif choice == '3':
            first_name = input("Enter Srudent First_name to delete: ").capitalize()
            delete_student(first_name)
            return

        elif choice == '4':
            print("Exiting................")
            break
        else:
            print("Invalid choices please try again")


if __name__ == "__main__":
    main()
