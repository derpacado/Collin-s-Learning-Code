#  Master Budgeter
# Categories to budget: total cash, total spent, monthly spending, organize earned cash into saving vs spending vs tithings
# Structure: overview is total cash/spent


#https://github.com/derpacado/Collin-s-Learning-Code.git


#long term storage
import json
from datetime import date, datetime
current_date = date.today()
import sys

#loading history
def load_budget(file_path = "budget.json"):
    print("Loading budget:...")
    try:
        with open(file_path, "r") as f:
            print("Budget loaded successfully!!")
            return json.load(f)
    except FileNotFoundError:
        print("File not found")
    except json.JSONDecodeError:
        print("Oops! There was a problem decoding the JSON file.")

#saving new data to budget
def save_budget(budget, file_path = "budget.json"):
    with open(file_path, "w") as f:
        json.dump(budget, f, indent=2)
        print("Saved succesfully!")

#adding new data
def add_earn(d, amount, source):
    budget["earnings"].append({"date": d, "amount": amount, "source": source})
    print("Earning added successfully!")
    save_budget(budget)

def add_spend(date, amount, category):
    budget["spendings"].append({"date": date, "amount": amount, "category": category})
    print("Spending added successfully!")
    save_budget(budget)

#budget["spendings"].append

#main menu

#month information
def month_summary(budget, month, year):
    #identify month
    earnings = [e for e in budget["earnings"] if e["date"].startswith(f"{year}-{month:02d}")]
    spendings = [s for s in budget["spendings"] if s["date"].startswith(f"{year}-{month:02d}")]
   
    #calc totals
    earn_tot = sum(item["amount"] for item in earnings) if earnings != [] else 0
    spend_tot = sum(item["amount"] for item in spendings) if spendings != [] else 0
    net = earn_tot-spend_tot

    #print info
    print(f"""
Summary for the {month}/{year} month.
    Net Earned: ${net}
    Total Earned: ${earn_tot} 
    Total spent: ${spend_tot}""")

    #calc and print spending breakdown
    if spendings:  
        for spend in spendings:
            percent = (spend["amount"] / earn_tot * 100) if earn_tot > 0 else 0
            print(f"        {percent:.2f}% (${spend['amount']}) in category {spend['category']}.")
    
    #list budget numbers
    print(f"""
    Budget Numbers:
        50% Savings: ${earn_tot*0.5:.2f}
        20% Necessities: ${earn_tot*0.20:.2f}
        15% Automotive: ${earn_tot*0.15:.2f}
        10% Fun: ${earn_tot*0.10:.2f}
        10% Tithing: ${earn_tot*0.10:.2f}""")
    
#all time summary
def all_sum(budget):
    earn_tot = sum(item["amount"] for item in budget["earnings"])
    spend_tot = sum(item["amount"] for item in budget["spendings"])
    net = earn_tot-spend_tot
    print(f"""
    All Time Data
          
    Total Earned: ${earn_tot}
    Total Spent: ${spend_tot}
    Net Earned: ${net}
""")
    
def back_or_exit():
    print("""
Options
1. Back to main menu
2. Exit""")
    choice=input("Choose an option: ").strip()
    if choice=="1":
        main_menu(budget)
    elif choice=="2":
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid, try again.")
        back_or_exit()




#main menu
def main_menu(budget):
    # show summary only once per loop iteration   
    print("\n=== Main Menu ===")
    all_sum(budget)
    month_summary(budget, current_date.month, current_date.year)

    print("""
Options:
    1. View past month info
    2. Add earning
    3. Add spending
    4. Exit
""")
    while True:
        choice=input("Choose option:").strip()
        if choice=="1":
            view_past_month()
        elif choice=="2":
            add_earning()
        elif choice=="3":
            add_spending()
        elif choice=="4":
            print("Exiting...")
            sys.exit()
        else:
            print("""
Invalid response, try again.""")

#specific call for ui to view past month from terminal input
def view_past_month():
    print("\nViewing past month data.")
    month = int(input("Enter month (1–12): ").strip())
    year = int(input("Enter year (YYYY): ").strip())
    month_summary(budget, month, year)
    back_or_exit()

#specific call for ui to add earning from terminal input
def add_earning():
    print("\nAdding earning:")
    d = input("Enter date (YYYY-MM-DD): ").strip()
    amount = float(input("Enter amount: ").strip())
    source = input("Enter source: ").strip()
    add_earn(d, amount, source)
    back_or_exit()

def add_spending():
    print("\nAdding spending:")
    d = input("Enter date (YYYY-MM-DD): ").strip()
    amount = float(input("Enter amount: ").strip())
    category = input("Enter category: ").strip()
    add_spend(d, amount, category)
    back_or_exit()

 

budget = load_budget()
main_menu(budget)


# make a change - "michael jackson"