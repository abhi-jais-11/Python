from datetime import datetime
current_date_time=datetime.now()
print(f"Date:{current_date_time.strftime("%d/%m/%Y")} And Time {current_date_time.strftime("%H:%M:%S")}")