# PulseFit Studio Booking System

A menu-driven Python program to manage classes, bookings, members, payments, and maintenance for PulseFit Studio. Built without OOP or external libraries, using text files for data storage.

## Project Structure

```
pulsefit/
│
├── main.py          # Role menu + all role menus/functions
├── log.py           # Functions for writing to the activity log
│
└── data/
    ├── classes.txt
    ├── members.txt
    ├── bookings.txt
    ├── payments.txt
    └── maintenance.txt
```

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/nyareth/pulsefit.git 
   cd pulsefit 
   ```
2. Run the program:
   ```
   python main.py
   ```

## How to Contribute

We're all working on the same files, so follow these steps every time so we don't overwrite each other's work.

### 1. Before you start coding, pull the latest version
```bash
git pull
```
This makes sure you have everyone else's latest changes before you add your own.

### 2. Make your changes
Add your functions to `main.py` (or `log.py` if it's logging-related), under the correct section comment (e.g. `# ADMIN FUNCTIONS`).

## Ground Rules

- **Don't reformat other people's code without alerting them** — it creates unnecessary merge conflicts.
- **Test your function before pushing** — make sure `main.py` still runs.
- **Ask before deleting anything** in `data/` — those files hold everyone's test data.

## Data Files

Format for each file (comma-separated, one record per line) — **to be finalized as a team before writing functions**:


| File | Schema |
|---|---|
| `classes.txt` | `class_id|class_name|instructor|date|time|capacity|status|fee` |
| `members.txt` | `member_id|name|phone|email|membership|date_joined` |
| `bookings.txt` | `booking_id|member_id|class_id|booking_date|reschedule_date|reschedule_time|status|record_status` |
| `payments.txt` | `payment_id|member_id|payment_type|description|amount|payment_date|status` |
| `maintenance.txt` | `maintenance_id|equipment|type|description|date|status` |
| `activity_log.txt` | `timestamp|action` |
