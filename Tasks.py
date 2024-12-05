import os
import shutil
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openpyxl import Workbook
import schedule
import time

# ---------------------
# File Organizer
# ---------------------
def organize_files(directory):
    """
    Organize files in the directory by their extensions.
    """
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = filename.split('.')[-1]
            folder = os.path.join(directory, extension)
            os.makedirs(folder, exist_ok=True)
            shutil.move(file_path, os.path.join(folder, filename))
    print(f"Files in {directory} have been organized by type.")

# ---------------------
# Web Scraper
# ---------------------
def scrape_weather():
    """
    Scrape weather data from a sample website.
    """
    try:
        url = "https://www.weather.com/"  # Replace with a working weather URL
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to fetch weather data.")
            return "N/A"
        soup = BeautifulSoup(response.text, "html.parser")
        # Example: Parse weather info (replace with actual tag/class from the website)
        weather = soup.find("span", class_="CurrentConditions--tempValue--3KcTQ")
        if weather:
            weather_text = weather.text
            print(f"Scraped Weather: {weather_text}")
            return weather_text
        else:
            print("Could not extract weather details.")
            return "N/A"
    except Exception as e:
        print(f"Error scraping weather: {e}")
        return "N/A"

# ---------------------
# Email Automation
# ---------------------
def send_email(sender, recipient, subject, body, smtp_server="smtp.gmail.com", port=587):
    """
    Send an email using SMTP.
    """
    try:
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender, "your_password")  # Replace "your_password" with your actual app password
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# ---------------------
# Excel Report Generation
# ---------------------
def generate_excel_report(file_path):
    """
    Generate a sample Excel report.
    """
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Automation Report"
    sheet.append(["Task", "Status", "Timestamp"])
    sheet.append(["Organize Files", "Completed", "2024-12-04 10:00 AM"])
    sheet.append(["Weather Scraping", "Completed", "2024-12-04 10:15 AM"])
    sheet.append(["Email Sent", "Completed", "2024-12-04 10:30 AM"])
    workbook.save(file_path)
    print(f"Excel report saved at {file_path}")

# ---------------------
# Task Scheduler
# ---------------------
def scheduled_task():
    """
    A task that runs automatically at a scheduled time.
    """
    print("Running scheduled tasks...")
    organize_files("sample_directory")  # Replace with your directory
    weather = scrape_weather()
    send_email(
        sender="your_email@gmail.com",  # Replace with your email
        recipient="recipient_email@gmail.com",  # Replace with recipient email
        subject="Daily Automation Report",
        body=f"Today's weather: {weather}\nAutomation tasks completed successfully."
    )
    generate_excel_report("daily_report.xlsx")
    print("Scheduled tasks completed.")

def schedule_tasks():
    """
    Schedule daily tasks at a specific time.
    """
    schedule.every().day.at("10:00").do(scheduled_task)

    print("Task scheduler is running...")
    while True:
        schedule.run_pending()
        time.sleep(1)

# ---------------------
# Main Execution
# ---------------------
if __name__ == "__main__":
    print("Welcome to Automated Task Master!")

    # Example Tasks
    print("\n1. Organizing Files...")
    organize_files("sample_directory")  # Replace with your directory path

    print("\n2. Scraping Weather Data...")
    weather_data = scrape_weather()

    print("\n3. Sending Email...")
    send_email(
        sender="your_email@gmail.com",  # Replace with your email
        recipient="recipient_email@gmail.com",  # Replace with recipient email
        subject="Automation Report",
        body=f"Today's weather: {weather_data}\nAll tasks executed successfully."
    )

    print("\n4. Generating Excel Report...")
    generate_excel_report("automation_report.xlsx")

    print("\n5. Scheduling Tasks...")
