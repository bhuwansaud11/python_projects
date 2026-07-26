import json, os
class Expense:
    def __init__(self,name,amount,category,responsible_person):
        self.name = name
        self.amount = amount
        self.category = category
        self.responsible_person = responsible_person

    def to_dict(self):
        return {
            'Name': self.name,
            'Amount': self.amount,
            'Category': self.category,
            'Responsible_person': self.responsible_person
        }

    @classmethod
    def from_dict(cls,data):
        Expense = cls(data['Name'], data['Amount'], data['Category'],data['Responsible_person'])
        return Expense
class ExpenseTracker:
    def __init__(self,username: str = "guest"):
        self.expenses = []
        self.set_user(username)

    def set_user(self,username: str):
        self.username = username.strip().lower() if username.strip() else "guest"
        self.filename = f"{self.username}_expenses.json"
        self.load()
    
    def save(self):
        with open(self.filename,'w') as file:
            json.dump([exp.to_dict() for exp in self.expenses],file,indent=4)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                data = json.load(file)
                self.expenses = [Expense.from_dict(d) for d in data]
        else:
            self.expenses = []
            self.save()

    def add_expense(self):
        print(f"\n---Add new expense ({self.username.title()} Profile)---")
        name = input("Name: ")
        amount = int(input("Amount: "))
        if amount<0:
            print("Amount must be positive ")
        category = input("Category: ")
        repsonsible_person = input("Repsonsible Person: ")
        if not repsonsible_person:
            print("A responsible person must be specified")
        self.expenses.append(Expense(name,amount,category,repsonsible_person))
        self.save()
        print("Expenses saved to: ", self.username.title())

    def view_all(self):
        if not self.expenses:
            print("No expenses recorded yet under profile: ", self.username.title())
            return

        print("\n Expense Profile: ", self.username.title())
        print(f"{'ID':<10} {'Name':<10} {'Amount':<10} {'Category':<10} {'Responsible Person':<10}")
        print("-"*50)
        for index,expense in enumerate(self.expenses,1):
            print(f"{index:<10} {expense.name:<10} {expense.amount:<10} {expense.category:<10}")
        print("-"*50)
    def view_by_category(self):
        if not self.expenses:
            print("No expenses recorded yet under profile: ",self.username.title())
            return
        category = input("Category: ").strip().lower()
        print(f"{'ID':<10} {'Name':<10} {'Amount':<10} {'Category':<10} {'Responsible Person':<10}")
        print("-"*50)
        found = False
        for index,expense in enumerate(self.expenses,1):
            expense_category = str(expense.category if expense.category is not None else '')
            if category == expense_category.lower():
                print(f"{index:<10} {expense.name:<10} {expense.amount:<10} {expense.category:<10} {expense.responsible_person:<10}")
                found = True
        print("-"*50)
        if not found:
            print("No match found")
    def personal_summary(self):
        if not self.expenses:
            print("No data available to calculate summaries!")
            return
        
        summaries = {}
        for expense in self.expenses:
            person = expense.responsible_person.title()
            summaries[person] = summaries.get(person,0) + expense.amount
        print(f"\n---Spending Profile ({self.username.title()} Profile)---")
        for person, total in summaries.items():
            print(f"{person}: ${total}")

    def total_spending(self):
        return sum(expense.amount for expense in self.expenses)

def main():
    tracker = ExpenseTracker()
    is_running = True
    while is_running:
        print("-------EXPENSE TRACKER------")
        print("1. Set/switch user")
        print("2. Add expenses to the existing user")
        print("3. View all details")
        print("4. View by category")
        print("5. Personal summary")
        print("6. Total spending")
        print("7. Exit")

        choice = int(input("Choose(1-7): "))

        match choice:
            case 1:
                new_user = input("Username: (or leave blank for guest)").strip()
                tracker.set_user(new_user)
                print(f"Switched context! Active profile is now: {tracker.filename}")

            case 2:
                tracker.add_expense()

            case 3:
                tracker.view_all()

            case 4:
                tracker.view_by_category()

            case 5:
                tracker.personal_summary()

            case 6:
                total = tracker.total_spending()
                print(f"Total money spent on this profile: ${total}")

            case 7:
                print("Thanks for visiting me...")
                print("Exiting")
                is_running = False

            case _:
                print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()