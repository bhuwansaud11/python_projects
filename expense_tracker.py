
import json, os, datetime
class Expense:
    def __init__(self,name):
        self.name = name
        self.list_of_expenses = []

    def to_dict(self):
        return {
            'Name': self.name,
            "Expenses": self.list_of_expenses
        }

    @classmethod
    def from_dict(cls,data):
        Expense = cls(data['Name'])
        Expense.list_of_expenses = data['Expenses']
        return Expense

    def add_expense(self):
        name_of_the_expense = input("Name of the expense: ")
        amount = int(input("Amount: "))
        category = input("Category: ")
        date = datetime.date.today().strftime("%d/%m/%Y")
        self.list_of_expenses.append({'Name': name_of_the_expense, 'Amount': amount, 'Category': category, 'Date': str(date)})

    def view_all(self):
        print(f"{'ID':<10} {'Name':<15} {'Amount':<10} {'Category':<15} {'Date':<10}")
        for index,list in enumerate(self.list_of_expenses,1):
            print(f"{index:<10} {list['Name']:<15} {list['Amount']:<10} {list['Category']:<15} {list['Date']:<10}")

    def view_category(self):
        found = False
        category = input("Category: ").lower()
        for index,list in enumerate(self.list_of_expenses,1):
            if list['Category'].lower() ==  category:
                print(f"{'ID':<10} {'Name':<15} {'Amount':<15} {'Category':<15} {'Date':<10}")
                print("-"*60)
                print(f"{index:<10} {list['Name']:<15} {list['Amount']:<15} {list['Category']:<15} {list['Date']:<10}")
                found = True
        if not found:
            print("No match found")

    def monthly_summary(self):
        total = 0
        month = {}
        for list in self.list_of_expenses:
            m = list['Date'].split("/")[1]
            month[m] = month.get(m,0) + list['Amount']

        for keys,values in month.items():
            print(f"You spent ${values} in {keys}")
            total+=values
        print("Total expenses: $",total)


filename = os.path.join(os.path.dirname(__file__), 'expense_tracker.json')
expense = []
def save_info():
    with open(filename,'w') as file:
        json.dump([exp.to_dict() for exp in expense],file,indent=4)
    
def load_info():
    global expense
    if os.path.exists(filename):
        with open(filename,'r') as file:
            data = json.load(file)
            expense = [Expense.from_dict(d) for d in data]

def main():
    is_running = True
    load_info()
    while is_running:
        print("-----------------------")
        print("---Expense Tracker---")
        print("-----------------------")
        print("1. Add a user")
        print("2. Add new expense to an existing user ")
        print("3. View all details")
        print("4. View details by category")
        print("5. Monthly summary")

        choice = int(input("Choose(1-5): "))
        match choice:
            case 1:
                name = input("Name of the person: ")
                expense.append(Expense(name))
                save_info()

            case 2:
                for index,exp in enumerate(expense,1):
                    print(f"{index}. {exp.name}")

                ask = int(input("Enter the SNO: "))
                if 1<=ask<=len(expense):
                    expense[ask-1].add_expense()
                    save_info()
                else:
                    print("Invalid input. Please try again.")

            case 3:
                for index,exp in enumerate(expense,1):
                    print(f"{index}. {exp.name}")

                ask = int(input("Enter the SNO: "))
                if 1<=ask<=len(expense):
                    expense[ask-1].view_all()
                else:
                    print("Invalid input. Please try again.")

            case 4:
                for index,exp in enumerate(expense,1):
                    print(f"{index}. {exp.name}")

                ask = int(input("Enter the SNO: "))
                if 1<=ask<=len(expense):
                    expense[ask-1].view_category()
                else:
                    print("Invalid input. Please try again")

            case 5:
                for index,exp in enumerate(expense,1):
                    print(f"{index}. {exp.name}")
                ask = int(input("Enter the SNO: "))
                if 1<=ask<=len(expense):
                    expense[ask-1].monthly_summary()
            
            case _:
                is_running = False
main()