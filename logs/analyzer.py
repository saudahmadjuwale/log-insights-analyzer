from collections import defaultdict

error_count = 0
errors_by_ip = defaultdict(int)
errors_by_message = defaultdict(int)
errors_by_hour = defaultdict(int)

def read_log_file(filepath):
    with open(filepath,"r") as file:
        return file.readlines()

def parse_log_line(line):
    parts = line.strip().split(" ",4)
    
    if len(parts) < 5:
        return None
    
    date,time,level,ip,message = parts
    return date,time,level,ip,message

def process_error(date,time,ip,message):
    global error_count
    error_count += 1
    errors_by_ip[ip] += 1
    errors_by_message[message] += 1

    hour = time.split(":")[0]
    errors_by_hour[hour] += 1

def print_summary():
    print("\n Log Analysis Summary\n")
    print(f"Total Errors: {error_count}\n")

    print("Errors By IP's:\n")
    for ip , count in errors_by_ip.items():
        print(f" {ip} -> {count}")
    print("\n Errors By Messages:\n")
    for message, count in errors_by_message.items():
        print(f" {message} -> {count}")
    
    if errors_by_hour:
        peak_hour = max(errors_by_hour,key = errors_by_hour.get)
        print(f"\n Peakest error hour: {peak_hour}:00")

def main():
    log_files = "sample.log"
    lines = read_log_file(log_files)

    for line in lines:
        parsed = parse_log_line(line)
        if not parsed:
            continue
        date, time, level, ip, message = parsed 
        
        if level == "ERROR":
            process_error(date, time, ip, message)
    
    print_summary()

if __name__ == "__main__":
    main()
