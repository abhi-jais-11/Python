from datetime import datetime

def calculate_sec_diff(ts_one, ts_two):
    
    format = "%Y-%m-%d %H:%M:%S"  # Specify the timestamp format=
    time_one = datetime.strptime(ts_one, format)
    time_two = datetime.strptime(ts_two, format)
    diff = (time_two - time_one).total_seconds()
    return diff


ts_one = "2025-03-23 12:30:45"
ts_two = "2025-03-23 14:00:45"
diff_in_sec = calculate_sec_diff(ts_one, ts_two)
print(f"diff in seconds: {diff_in_sec}")