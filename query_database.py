#!/usr/bin/env python3
"""
Database Query Tool for SOC Events
Allows querying events stored in the SQLite database
"""

import sqlite3
from tabulate import tabulate
import sys

DB_FILE = "soc_events.db"

def print_all_events():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT ip, event_type, severity, timestamp, url FROM events ORDER BY timestamp")
    rows = c.fetchall()
    conn.close()
    
    data = [dict(row) for row in rows]
    print("\n=== ALL SUSPICIOUS EVENTS ===\n")
    print(tabulate(data, headers="keys", tablefmt="grid"))

def print_events_by_ip(ip):
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM events WHERE ip = ? ORDER BY timestamp", (ip,))
    rows = c.fetchall()
    conn.close()
    
    data = [dict(row) for row in rows]
    print(f"\n=== EVENTS FROM IP: {ip} ===\n")
    print(tabulate(data, headers="keys", tablefmt="grid"))

def print_critical_events():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM events WHERE severity = 'KRYTYCZNE' ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    
    data = [dict(row) for row in rows]
    print("\n=== CRITICAL SEVERITY EVENTS ===\n")
    print(tabulate(data, headers="keys", tablefmt="grid"))

def print_events_by_type(event_type):
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM events WHERE event_type = ? ORDER BY timestamp", (event_type,))
    rows = c.fetchall()
    conn.close()
    
    data = [dict(row) for row in rows]
    print(f"\n=== EVENTS OF TYPE: {event_type} ===\n")
    print(tabulate(data, headers="keys", tablefmt="grid"))

def print_statistics():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    c.execute("SELECT COUNT(DISTINCT ip) as attacking_ips FROM events")
    ips = c.fetchone()[0]
    
    c.execute("SELECT COUNT(*) as total_events FROM events")
    events = c.fetchone()[0]
    
    c.execute("SELECT event_type, COUNT(*) as count FROM events GROUP BY event_type ORDER BY count DESC")
    types = c.fetchall()
    
    c.execute("SELECT severity, COUNT(*) as count FROM events GROUP BY severity ORDER BY count DESC")
    severity = c.fetchall()
    
    conn.close()
    
    print("\n=== DATABASE STATISTICS ===")
    print(f"Total Events: {events}")
    print(f"Unique Attacking IPs: {ips}")
    print(f"\nEvent Types:")
    for event_type, count in types:
        print(f"  - {event_type}: {count}")
    print(f"\nSeverity Distribution:")
    for sev, count in severity:
        print(f"  - {sev}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python query_database.py <command> [args]")
        print("\nCommands:")
        print("  all              - Show all events")
        print("  critical         - Show critical severity events")
        print("  ip <IP>          - Show events from specific IP")
        print("  type <TYPE>      - Show events of specific type (SQLI, LOG4SHELL, SCAN, BRUTE_FORCE)")
        print("  stats            - Show database statistics")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "all":
        print_all_events()
    elif command == "critical":
        print_critical_events()
    elif command == "ip" and len(sys.argv) > 2:
        print_events_by_ip(sys.argv[2])
    elif command == "type" and len(sys.argv) > 2:
        print_events_by_type(sys.argv[2])
    elif command == "stats":
        print_statistics()
    else:
        print("Invalid command")
