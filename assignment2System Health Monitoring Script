import psutil
import logging

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO)

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Check system health
def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage: {cpu_usage}%')
    if memory.percent > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage: {memory.percent}%')
    if disk.percent > DISK_THRESHOLD:
        logging.warning(f'Low Disk space: {disk.percent}%')
    logging.info('System health check completed.')

if __name__ == "__main__":
    check_system_health()
