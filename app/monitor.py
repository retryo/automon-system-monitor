import psutil
import datetime

def get_system_data():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net = psutil.net_io_counters()
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "bytes_sent": net.bytes_sent,
        "bytes_recv": net.bytes_recv
    }