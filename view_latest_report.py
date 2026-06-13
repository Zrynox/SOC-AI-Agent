#!/usr/bin/env python3
"""
View the latest SOC report generated
"""

import os
import glob
from datetime import datetime

def view_latest_report():
    # Find all SOC_REPORT files
    report_files = glob.glob("SOC_REPORT_*.txt")
    
    if not report_files:
        print("❌ No reports found. Generate one with: python agent.py server.log")
        return
    
    # Get the most recent report
    latest_report = max(report_files, key=os.path.getctime)
    
    # Get file info
    file_stat = os.stat(latest_report)
    file_size = file_stat.st_size
    mod_time = datetime.fromtimestamp(file_stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\n{'='*80}")
    print(f"Latest Report: {latest_report}")
    print(f"Size: {file_size:,} bytes")
    print(f"Generated: {mod_time}")
    print(f"{'='*80}\n")
    
    # Read and display
    with open(latest_report, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
    
    print(f"\n{'='*80}")
    print(f"View all reports: dir SOC_REPORT_*.txt")
    print(f"Query database: python query_database.py --help")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    view_latest_report()
