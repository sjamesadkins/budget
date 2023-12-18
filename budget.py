income = {
    "Credit Card Cash Back": 0,
    "Insurance": 0,
    "Miscellaneous": 0,
    "Music": 0,
    "Work": 0,
}

expense = {
    "Cash": 0,
    "IHG": 0,
    "Freedom": 0,
    "Sapphire": 0,
}

categories = {
    "Clothing": 0,
    "Disposable": 0,
    "Food": 0,
    "Gas": 0,
    "Health": 0,
    "Insurance": 0,
    "Internet": 0,
    "Media": 0,
    "Medical": 0,
    "Phone": 0,
    "Rent": 0,
    "Savings": 0,
    "Utility": 0,
}

def update_dictionary(amount, dictionary):
    names = list(dictionary)
    
    txt = "\nChoose expense category:\n\n"
    for item in names:
        txt += str(names.index(item) + 1) + ": " + item + "\n"

    category = input(txt + "\n") 

    dictionary[names[int(category) - 1]] += int(amount)

    output = "\nReported value is {total:.2f} dollars from {source}."
    print(output.format(total = int(amount), source = names[int(category) - 1]))
    print(dictionary)


menu = """\nSelect one of the following option numbers:

1: Add Income
2: Add Expense
3: Modify Budget Item
4. View Expense Type Totals
5. View Monthly Expenses By Expense Type
6. Add Expense Category
7. View Month By Expense Category
8. Quit

"""

waiting_for_input = True

while waiting_for_input == True:

    selection = input(menu)

    if (selection == "1"):
        amount = input("\nWhat is the income amount: ")
        update_dictionary(amount, income)

    if (selection =="2"):
        amount = input("\nWhat is the expense amount: ")
        update_dictionary(amount, expense)

    if (selection == "6"):
        amount = input("\nWhat is the expense amount: ")
        update_dictionary(amount, categories)

    if (selection == "8"):
        waiting_for_input = False

