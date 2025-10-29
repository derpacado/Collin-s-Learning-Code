#  Master Budgeter
# Categories to budget: total cash, total spent, monthly spending, organize earned cash into saving vs spending vs tithings
# Structure: overview is total cash/spent


#https://github.com/derpacado/Collin-s-Learning-Code.git


#long term storage
import json
from datetime import date, datetime
current_date = date.today()

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

budget = load_budget()

#main menu
def main_menu():
    while True:
        print(f"Main Menu")
        all_sum(budget)
        month_summary(budget, current_date.month, current_date.year)

        print(f""" Options:
            1. View past month info
            2. Add earning
            3. Add spending
            4. Exit
            """)
        valid = ["1", "2", "3", "4"]
        choice = ""
        while choice not in valid:
            choice = input()
        if choice == "2":
            print("Choose date (yyyy-mm-dd):")
            d=input()
            #d = datetime.strptime(d, "%Y-%m-%d").date()
            print("Choose amount:")
            amount=int(input())
            print("Choose source:")
            source=input()
            add_earn(d, amount, source)
        if choice == "4":
            break

main_menu()


# make a change - "michael jackson"