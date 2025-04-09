from flat import Bill, Flatmate
from reports import PdfReport
import os

amount = float(input("Please enter the bill amount: "))
period = input("What is the bill period? E.g. December 2021: ")
name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house? "))
name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

os.chdir('files')
pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=the_bill)