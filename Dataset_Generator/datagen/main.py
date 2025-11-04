import typer
import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
import random
import os

app = typer.Typer()
fake = Faker()
console = Console()

# ────────────────────────────────────────────────────────────
# Header Display
# ────────────────────────────────────────────────────────────
def show_header():
    console.print("\n" + "─" * 60, style="cyan")
    console.print("[bold cyan]        DataGen CLI - Synthetic Dataset Generator[/bold cyan]")
    console.print("─" * 60, style="cyan")
    console.print("[bold yellow]Created by:[/bold yellow] Rishabh Kumar")
    console.print("[bold yellow]Version:[/bold yellow] 0.1.0")
    console.print("[bold yellow]Description:[/bold yellow] A CLI tool to generate customizable synthetic datasets")
    console.print("─" * 60, style="cyan")
    console.print("[bold white]Use 'datagen --help' to see available commands[/bold white]")
    console.print("[bold green]Tip:[/bold green] Run 'datagen generate' to create your first dataset.")
    console.print("─" * 60 + "\n", style="cyan")
    console.print("[bold yellow]License:[/bold yellow] MIT (Non-Commercial Use Only)")
    console.print("[bold yellow]Contact for commercial license:[/bold yellow] rishabh.contact.info@gmail.com\n")


# ────────────────────────────────────────────────────────────
# Available Columns (50 Options)
# ────────────────────────────────────────────────────────────
AVAILABLE_COLUMNS = {
    1: "OrderID", 2: "Date", 3: "Category", 4: "Country", 5: "CustomerName",
    6: "CustomerEmail", 7: "CustomerSegment", 8: "Quantity", 9: "Sales", 10: "Orders",
    11: "ProductName", 12: "PaymentMode", 13: "Gender", 14: "Age", 15: "City",
    16: "State", 17: "PostalCode", 18: "Region", 19: "PhoneNumber", 20: "Rating",
    21: "ReviewText", 22: "Discount", 23: "Profit", 24: "Loss", 25: "ReturnStatus",
    26: "ShippingMode", 27: "DeliveryDate", 28: "EmployeeName", 29: "Department", 30: "JobTitle",
    31: "Salary", 32: "ExperienceYears", 33: "JoinDate", 34: "LeaveDate", 35: "IP_Address",
    36: "Browser", 37: "DeviceType", 38: "LoginTime", 39: "LogoutTime", 40: "SubscriptionType",
    41: "TransactionID", 42: "CreditScore", 43: "AccountBalance", 44: "Temperature",
    45: "Humidity", 46: "WeatherCondition", 47: "Latitude", 48: "Longitude",
    49: "RandomText", 50: "BooleanFlag"
}

# ────────────────────────────────────────────────────────────
# Data Generation Logic
# ────────────────────────────────────────────────────────────
def generate_column(col_name, num_rows, start_date, end_date):
    data = []

    # Convert start and end date
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    for _ in range(num_rows):
        if col_name == "OrderID":
            data.append(f"ORD-{random.randint(10000, 99999)}")
        elif col_name == "Date":
            data.append(fake.date_between(start_date=start_date, end_date=end_date))
        elif col_name == "Category":
            data.append(random.choice(["Beauty", "Electronics", "Grocery", "Clothing", "Toys", "Furniture"]))
        elif col_name == "Country":
            data.append(fake.country())
        elif col_name == "CustomerName":
            data.append(fake.name())
        elif col_name == "CustomerEmail":
            data.append(fake.email())
        elif col_name == "CustomerSegment":
            data.append(random.choice(["High-Value", "Mid-Value", "Low-Value"]))
        elif col_name == "Quantity":
            data.append(random.randint(1, 10))
        elif col_name == "Sales":
            data.append(round(random.uniform(100, 5000), 2))
        elif col_name == "Orders":
            data.append(random.randint(1, 3))
        elif col_name == "ProductName":
            data.append(fake.word().capitalize())
        elif col_name == "PaymentMode":
            data.append(random.choice(["Credit Card", "Debit Card", "UPI", "PayPal", "Cash"]))
        elif col_name == "Gender":
            data.append(random.choice(["Male", "Female", "Other"]))
        elif col_name == "Age":
            data.append(random.randint(18, 70))
        elif col_name == "City":
            data.append(fake.city())
        elif col_name == "State":
            data.append(fake.state())
        elif col_name == "PostalCode":
            data.append(fake.postcode())
        elif col_name == "Region":
            data.append(random.choice(["North", "South", "East", "West"]))
        elif col_name == "PhoneNumber":
            data.append(fake.phone_number())
        elif col_name == "Rating":
            data.append(round(random.uniform(1, 5), 1))
        elif col_name == "ReviewText":
            data.append(fake.sentence())
        elif col_name == "Discount":
            data.append(round(random.uniform(0, 50), 2))
        elif col_name == "Profit":
            data.append(round(random.uniform(100, 2000), 2))
        elif col_name == "Loss":
            data.append(round(random.uniform(0, 500), 2))
        elif col_name == "ReturnStatus":
            data.append(random.choice(["Returned", "Not Returned"]))
        elif col_name == "ShippingMode":
            data.append(random.choice(["Standard", "Express", "Same-Day"]))
        elif col_name == "DeliveryDate":
            data.append(fake.date_between(start_date=start_date, end_date=end_date))
        elif col_name == "EmployeeName":
            data.append(fake.name())
        elif col_name == "Department":
            data.append(random.choice(["HR", "Finance", "Sales", "IT", "Marketing"]))
        elif col_name == "JobTitle":
            data.append(fake.job())
        elif col_name == "Salary":
            data.append(round(random.uniform(30000, 150000), 2))
        elif col_name == "ExperienceYears":
            data.append(random.randint(0, 20))
        elif col_name == "JoinDate":
            data.append(fake.date_between(start_date=start_date, end_date=end_date))
        elif col_name == "LeaveDate":
            data.append(fake.date_between(start_date=start_date, end_date=end_date))
        elif col_name == "IP_Address":
            data.append(fake.ipv4())
        elif col_name == "Browser":
            data.append(random.choice(["Chrome", "Firefox", "Edge", "Safari", "Opera"]))
        elif col_name == "DeviceType":
            data.append(random.choice(["Mobile", "Desktop", "Tablet"]))
        elif col_name == "LoginTime":
            data.append(fake.time())
        elif col_name == "LogoutTime":
            data.append(fake.time())
        elif col_name == "SubscriptionType":
            data.append(random.choice(["Free", "Basic", "Premium", "Enterprise"]))
        elif col_name == "TransactionID":
            data.append(f"TXN-{random.randint(100000, 999999)}")
        elif col_name == "CreditScore":
            data.append(random.randint(300, 850))
        elif col_name == "AccountBalance":
            data.append(round(random.uniform(1000, 100000), 2))
        elif col_name == "Temperature":
            data.append(round(random.uniform(-10, 45), 2))
        elif col_name == "Humidity":
            data.append(round(random.uniform(10, 100), 2))
        elif col_name == "WeatherCondition":
            data.append(random.choice(["Sunny", "Rainy", "Cloudy", "Stormy", "Snowy"]))
        elif col_name == "Latitude":
            data.append(round(random.uniform(-90, 90), 6))
        elif col_name == "Longitude":
            data.append(round(random.uniform(-180, 180), 6))
        elif col_name == "RandomText":
            data.append(fake.text(max_nb_chars=20))
        elif col_name == "BooleanFlag":
            data.append(random.choice([True, False]))
        else:
            data.append(None)
    return data

# ────────────────────────────────────────────────────────────
# Generate Command
# ────────────────────────────────────────────────────────────
@app.command()
def generate():
    show_header()

    console.print("[bold white]Welcome to the Data Generator CLI[/bold white]\n")

    num_rows = Prompt.ask("[bold cyan]Enter number of rows to generate[/bold cyan]", default="1000")
    start_date = Prompt.ask("[bold cyan]Enter start date (YYYY-MM-DD)[/bold cyan]", default="2020-01-01")
    end_date = Prompt.ask("[bold cyan]Enter end date (YYYY-MM-DD)[/bold cyan]", default="2024-12-31")

    console.print("\n[bold white]Available Columns:[/bold white]")
    for k, v in AVAILABLE_COLUMNS.items():
        console.print(f"[green]{k}. {v}[/green]")

    selected_cols = Prompt.ask("\n[bold cyan]Enter column numbers to include (comma-separated)[/bold cyan]")
    selected_cols = [AVAILABLE_COLUMNS[int(i.strip())] for i in selected_cols.split(",")]

    save_path = Prompt.ask("\n[bold cyan]Enter folder path to save file (e.g. ./data/)[/bold cyan]", default="./data/")
    os.makedirs(save_path, exist_ok=True)

    file_name = Prompt.ask("[bold cyan]Enter file name (without extension)[/bold cyan]", default="generated_data")
    file_type = Prompt.ask("[bold cyan]Choose file type (csv/xlsx/json)[/bold cyan]", default="csv")

    console.print("\n[bold yellow]Generating data... Please wait...[/bold yellow]")

    df = pd.DataFrame({col: generate_column(col, int(num_rows), start_date, end_date) for col in selected_cols})

    full_path = os.path.join(save_path, f"{file_name}.{file_type}")

    if file_type == "csv":
        df.to_csv(full_path, index=False)
    elif file_type == "xlsx":
        df.to_excel(full_path, index=False)
    elif file_type == "json":
        df.to_json(full_path, orient="records", lines=True)

    console.print(f"\n[bold green]Data generated successfully and saved to:[/bold green] {full_path}\n")

# ────────────────────────────────────────────────────────────
# Main Entry
# ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app()


