"""
Automatically updates MySoft Cleanup Sheet
"""

from mysoft import login, get_tickets
from excel import update_tickets

def main():
    username = ""
    password = ""
    login(username, password)
    mysoft_tickets = get_tickets()

    for ticket in mysoft_tickets.keys():
        print("WO: " + ticket + " | " + "CA: " + mysoft_tickets[ticket])
    print(len(mysoft_tickets))

    update_tickets(mysoft_tickets, mysoft_tickets.keys())

if __name__ == "__main__":
    main()
