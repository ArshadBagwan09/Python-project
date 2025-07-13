import csv
import pandas as pd


def tticket():
    source = input("Enter From: ")
    dest = input("Enter Destination: ")
    date = input("Enter Date: ")
    passengers = input("Enter No of Passengers: ")
    trainno = input("Enter Train No: ")

    # Save data to CSV
    with open("tickets.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([source, dest, date, passengers, trainno])

    print("✅ Ticket Saved Successfully!\n")


def view_tickets():
    try:
        with open("tickets.csv", mode="r") as file:
            reader = csv.reader(file)
            print("\n===== All Tickets =====")
            for row in reader:
                print(
                    f"From: {row[0]}, To: {row[1]}, Date: {row[2]}, Passengers: {row[3]}, Train No: {row[4]}"
                )
            print("=========================\n")
    except FileNotFoundError:
        print("❌ No tickets found.\n")


def generate_report():
    try:
        df = pd.read_csv("tickets.csv", header=None)
        df.columns = ["Source", "Destination", "Date", "Passengers", "Train No"]
        df.to_excel("tickets.xlsx", index=False)
        print("✅ Report Generated: tickets.xlsx\n")
    except FileNotFoundError:
        print("❌ No data to generate report.\n")


def menu():
    while True:
        print("===== Welcome to Ticket Generation =====")
        print("1. Take Ticket")
        print("2. View Tickets")
        print("3. Generate Report")
        print("4. Exit")
        op = input("Enter Option: ")

        if op == "1":
            tticket()
        elif op == "2":
            view_tickets()
        elif op == "3":
            generate_report()
        elif op == "4":
            print("🚪 Exiting Program. Goodbye!")
            break
        else:
            print("❌ Invalid Option. Try again.\n")


# Start program
menu()
