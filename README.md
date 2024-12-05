
# Automated Task Master: Simplifying Repetitive Work with Python

## 🚀 Project Overview
This project is designed to demonstrate the power of Python in automating everyday repetitive tasks. From organizing files to web scraping, sending emails, and scheduling tasks, these scripts save time and effort by simplifying workflows.

## ✨ Features
- **File Organizer**: Automatically organizes files into folders based on file types.
- **Web Scraper**: Scrapes data (e.g., weather updates, stock prices) from websites.
- **Email Automation**: Sends bulk emails with custom messages and attachments.
- **Task Scheduler**: Automates task execution at scheduled times.
- **Excel Automation**: Reads, modifies, and generates Excel reports.

## 🛠️ Technologies and Libraries
- **Python** (3.7+)
- Libraries:
  - `os` and `shutil` for file handling
  - `requests` and `BeautifulSoup` for web scraping
  - `smtplib` and `email` for email automation
  - `schedule` for task scheduling
  - `openpyxl` for Excel operations

## 📂 Repository Structure
```
automated-task-master/
│
├── README.md                # Project description and overview
├── automated_task_master.py # Python script with all automation 
```

## ⚙️ How to Use
### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/automated-task-master.git
cd automated-task-master
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Script
```bash
python automated_task_master.py
```

### Step 4: Schedule Tasks
Uncomment the `schedule_tasks()` function in the script to enable daily scheduled tasks.

## 🌟 Outputs
### File Organizer Output
Organized files by type into folders:
```
/organized_files/
   ├── pdf/
   ├── txt/
   ├── images/
```

### Web Scraper Output
Scraped data saved as:
```
/data/weather_data.csv
```

### Email Automation Log
Successfully sent an email to the configured recipient.

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
