import json
from datetime import datetime

def generate_report():
    report_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "success"
    }
    
    with open("report.json", "w") as file:
        json.dump(report_data, file)