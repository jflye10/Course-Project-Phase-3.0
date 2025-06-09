# Joshua Flye, CIS 261, Course Project Phase 3

import os
import re

FILENAME = "employee_data.txt"

def is_valid_date(date_str):
    return re.match(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|[12]|3[01])/\d{4}$", date_str)

def append_employee_record(from_date, to_date, name, hours, rate, tax_rate):
    with open(FILENAME, "a") as f:
        record = f"{from_date}|{to_date}|{name}|{hours}|{rate}|{tax_rate}\n"
        f.write(record)

def prompt_employee_data():
    while True:
        print("\nEnter employee data:")
        from_date = input("From Date (mm/dd/yyyy): ")
        while not is_valid_date(from_date):
            print("Invalid date format. Use mm/dd/yyyy.")
            from_date = input("From Date (mm/dd/yyyy: ")

        to_date = input("To Date (mm/dd/yyyy): ")
        while not is_valid_date(to_date):
            print("Invalid date format. Use mm/dd/yyyy.")
            to_date = input("To Date (mm/dd/yyyy): ")
        
        name = input("Employee Name: ")
        hours = float(input("Hours Worked: "))
        rate = float(input("Pay Rate: "))
        tax_rate = float(input("Income Tax Rate (e.g. 0.15 for 15%): "))

        append_employee_record(from_date, to_date, name, hours, rate, tax_rate)

        another = input("Add another emploee? (y/n): ").lower()
        if another != 'y':
            break

def get_report_date():
    while True:
        date_str = input("\nEnter From Date for report (mm/dd/yyyy or 'All'): ")
        if date_str.lower() == "all" or is_valid_date(date_str):
            return date_str
        else:
            print("Invalid input. Enter 'All' or a date in mm/dd/yyyy format.")

def display_report(report_date):
    totals = {
        "employees": 0,
        "hours": 0.0,
        "tax": 0.0,
        "net_pay": 0.0
    }

    if not os.path.exists(FILENAME):
        print("No employee records found.")
        return

    print("\n--- Payroll Report ---")
    with open(FILENAME, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            from_date, to_date, name, hours, rate, tax_rate = line.split("|")
            hours = float(hours)
            rate = float(rate)
            tax_rate = float(tax_rate)
            gross_pay = hours * rate
            income_tax = gross_pay * tax_rate
            net_pay = gross_pay - income_tax

            if report_date.lower() == "all" or report_date == from_date:
                print(f"From: {from_date}, To: {to_date}, Name: {name}, "
                      f"Hours: {hours:.2f}, Rate: ${rate:.2f}, Gross: ${gross_pay:.2f}, "
                      f"Tax Rate: {tax_rate:.2%}, Tax: ${income_tax:.2f}, Net: ${net_pay:.2f}")

                totals["employees"] += 1
                totals["hours"] += hours
                totals["tax"] += income_tax
                totals["net_pay"] += net_pay
    
    print("\n--- Totals ---")
    print(f"Total Employees: {totals['employees']}")
    print(f"Total Hours: {totals['hours']:.2f}")
    print(f"Total Taxes: ${totals['tax']:.2f}")
    print(f"Total Net Pay: ${totals['net_pay']:.2f}")

def main():
    print("Employee Payroll System")
    prompt_employee_data()
    report_date = get_report_date()
    display_report(report_date)

if __name__ == "__main__":
    main()
