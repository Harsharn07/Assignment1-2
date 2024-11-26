import re
from collections import Counter

# Define the log file path
log_file_path = 'access.log'

def analyze_logs():
    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    # Analyzing 404 errors
    errors_404 = [line for line in logs if '404' in line]
    print(f'Total 404 Errors: {len(errors_404)}')

    # Finding the most requested pages
    pages = [re.search(r'GET (.*?) HTTP', line).group(1) for line in logs if 'GET' in line]
    page_counter = Counter(pages)
    most_requested = page_counter.most_common(5)
    print('Most Requested Pages:', most_requested)

    # Finding IPs with most requests
    ips = [line.split(' ')[0] for line in logs]
    ip_counter = Counter(ips)
    top_ips = ip_counter.most_common(5)
    print('Top IP Addresses:', top_ips)

if __name__ == "__main__":
    analyze_logs()
