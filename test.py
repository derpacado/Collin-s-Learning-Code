import json

# ---------- JSON FILE HANDLING ----------

def load_budget(file_path="budget.json"):
    """Load budget data from JSON or create a new one if missing/corrupt."""
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("⚠️ No valid budget file found. Creating a new one...")
        clean_budget = {"earnings": [], "spendings": []}
        save_budget(clean_budget, file_path)
        return clean_budget


def save_budget(budget, file_path="budget.json"):
    """Save current budget data to JSON."""
    with open(file_path, "w") as f:
        json.dump(budget, f, indent=2)


# ---------- MONTHLY SUMMARY FUNCTION ----------

def month_summary(budget, month, year):
    """Display earnings, spendings, and budget breakdown for a given month."""
    # Filter by year and month
    earnings = [e for e in budget["earnings"] if e["date"].startswith(f"{year}-{month:02d}")]
    spendings = [s for s in budget["spendings"] if s["date"].startswith(f"{year}-{month:02d}")]

    # Calculate totals for that month
    earn_tot = sum(item["amount"] for item in earnings)
    spend_tot = sum(item["amount"] for item in spendings)
    net = earn_tot - spend_tot

    # Display results
    print(f"""
Summary for {year}-{month:02d}
------------------------------
Total Earned: ${earn_tot:.2f}
Total Spent:  ${spend_tot:.2f}
Net Cash:     ${net:.2f}
""")

    # Breakdown by category
    if spendings and earn_tot > 0:
        print("Spending Breakdown:")
        for spend in spendings:
            percent = spend["amount"] / earn_tot * 100
            print(f"  - {spend['category']}: ${spend['amount']:.2f} ({percent:.2f}%)")

    # Budget goal example
    print(f"""
Budget Goals (based on earnings):
  50% Savings:     ${earn_tot * 0.50:.2f}
  20% Necessities: ${earn_tot * 0.20:.2f}
  15% Automotive:  ${earn_tot * 0.15:.2f}
  10% Fun:         ${earn_tot * 0.10:.2f}
  10% Tithing:     ${earn_tot * 0.10:.2f}
""")


# ---------- MAIN PROGRAM FLOW ----------

# Load budget data
budget = load_budget()


# Display this month’s summary
month_summary(budget, month=10, year=2025)