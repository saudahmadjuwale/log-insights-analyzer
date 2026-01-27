Log Insights Analyzer

A simple Python script to analyze log files and generate insights about errors and warnings.

Features

Counts total errors and warnings.

Groups errors and warnings by IP address.

Groups errors and warnings by message.

Identifies the peak hour for errors and warnings.

Log File Format

The script expects a log file with each line in the following format:

YYYY-MM-DD HH:MM:SS LEVEL IP_ADDRESS MESSAGE


Where:

LEVEL is either INFO, WARNING, or ERROR.

IP_ADDRESS is the source IP of the event.

MESSAGE is the event description.

Example:

2026-01-20 09:12:45 INFO 192.168.1.10 User logged in
2026-01-20 09:15:02 ERROR 192.168.1.12 Failed login
2026-01-20 09:18:33 WARNING 192.168.1.15 High memory usage

How to Use

Clone the repository or download the script.

Make sure your log file (e.g., sample.log) is in the same directory as the script.

Run the script:

python log_analyzer.py


The script will display a summary like:

Total Errors: 5 | Total Warnings: 2

Errors By IP's:
 192.168.1.12 -> 3
 192.168.1.18 -> 2

Errors By Messages:
 Failed login -> 3
 Database timeout -> 1
 Disk full -> 1

Peak error hour: 12:00

Warnings By IP's:
 192.168.1.15 -> 2

Warnings By Messages:
 High memory usage -> 1
 Disk usage at 85 percent -> 1

Peak Warnings hour: 11:00

Requirements

Python 3.x

No external libraries required (uses standard Python libraries)