# Quick Start Guide - SOC Report Generator

## 30-Second Setup

### 1. Activate Virtual Environment
```bash
cd "f:\AI SECURITY AGENT"
.\venv\Scripts\activate
```

### 2. Generate Test Data
```bash
python loggenerator.py
```
✅ Creates: `server.log` with 300 events (85% normal, 15% attacks)

### 3. Generate SOC Report
```bash
python agent.py server.log
```
✅ Creates: `SOC_REPORT_YYYYMMDD_HHMMSS.txt` with professional analysis

### 4. View Latest Report
```bash
python view_latest_report.py
```

### 5. Query Database
```bash
# Show all statistics
python query_database.py stats

# Show critical events
python query_database.py critical

# Show events from specific IP
python query_database.py ip 91.240.118.44

# Show events by attack type
python query_database.py type LOG4SHELL
python query_database.py type SQLI
python query_database.py type BRUTE_FORCE
python query_database.py type SCAN
```

## What You Get

### Database (`soc_events.db`)
- All 204 events stored with metadata
- Queryable by IP, type, severity, timestamp

### Report (`SOC_REPORT_*.txt`)
- Executive Summary
- Technical Analysis
- MITRE ATT&CK Framework mapping
- Threat Intelligence
- Ranked Recommendations
- Full Timeline

### Attack Statistics
- **SCAN**: 120 events (59%) - Reconnaissance activity
- **BRUTE_FORCE**: 36 events (18%) - Admin panel attacks
- **SQLI**: 24 events (12%) - SQL Injection attempts
- **LOG4SHELL**: 24 events (12%) - Log4Shell/JNDI attacks

### Severity Breakdown
- **KRYTYCZNE** (Critical): 24 events - Log4Shell attempts
- **WYSOKIE** (High): 96 events - SQL Injection & Brute Force
- **ŚREDNIE** (Medium): 84 events - Scanning activity

## Key Features

✅ **Real Detection Rules** - Not just random patterns
✅ **LLM Analysis** - Professional insights using Ollama LLM
✅ **MITRE Mapping** - Real MITRE ATT&CK techniques (T1190, T1595.002, T1110.001)
✅ **Severity Scoring** - Intelligent risk assessment
✅ **SQLite Database** - Historical tracking & compliance
✅ **Queryable Results** - Forensic investigation tools

## Attacking IPs in This Test

1. **185.220.101.5** - Brute force attacker
   - Targets: `/admin/login.php`
   - Method: Password guessing
   - Status: 403 Forbidden

2. **91.240.118.44** - Exploitation attacker
   - Targets: `/shop/products` (SQLi), `/index.html` (Log4Shell)
   - Methods: SQL Injection, JNDI Injection
   - Status: 500/400 errors

3. **45.133.1.20** - Reconnaissance/Scanning
   - Targets: `/.env`, `/etc/passwd`, `/wp-admin`, `/config.php`
   - Methods: Path enumeration, config file discovery
   - Tools: Nmap, directory busters
   - Status: 404 Not Found

## Next Steps

### For More Events
```python
# Edit loggenerator.py line 4:
def generate_realistic_logs(output_file="server.log", num_lines=1000):
                                                                    ^^^^
# Increase from 300 to 1000 events
```

### For Custom Logs
```bash
# Process your own server logs
python agent.py /path/to/access.log
```

### For Real-World Use
- Integrate with actual web server logs (Apache, Nginx, IIS)
- Set up continuous monitoring
- Create alert rules from detected patterns
- Export reports for management/compliance

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Ollama connection refused" | Run `ollama run llama3.1` in another terminal |
| "No module named tabulate" | Run `pip install tabulate` |
| "No suspicious activity detected" | Increase log volume in loggenerator.py |
| "Database locked" | Close all Python processes and retry |

## File Structure

```
f:\AI SECURITY AGENT\
├── agent.py                 ← Main SOC report generator
├── loggenerator.py         ← Simulated attack log generator
├── query_database.py       ← Database query tool
├── view_latest_report.py   ← Report viewer
├── server.log              ← Generated HTTP logs
├── soc_events.db          ← SQLite event database
├── SOC_REPORT_*.txt       ← Generated reports
├── README.md              ← Full documentation
├── venv/                  ← Python environment
└── requirements           ← Dependency list
```

## Output Example

```
============================================================
SOC INCIDENT REPORT GENERATOR
============================================================

[1/6] Parsing server logs...
     ✓ Found 42 suspicious events

[2/6] Building attack map...
     ✓ Identified 3 attacking IPs

[3/6] Calculating statistics...
     ✓ Attack pattern: COORDINATED_BRUTE_FORCE

[4/6] Assessing severity...
     ✓ Severity: KRYTYCZNE (Score: 240/100)

[5/6] Mapping MITRE ATT&CK framework...
     ✓ Techniques identified

[6/6] Generating LLM-enhanced report...

✅ Report saved: SOC_REPORT_20260611_184505.txt
📊 Events stored in database: soc_events.db
```

## Database Query Examples

```bash
# Get all critical severity events
.\venv\Scripts\python.exe query_database.py critical

# Analyze specific attacker
.\venv\Scripts\python.exe query_database.py ip 91.240.118.44

# Track Log4Shell attempts
.\venv\Scripts\python.exe query_database.py type LOG4SHELL

# View summary statistics
.\venv\Scripts\python.exe query_database.py stats
```

## Report Sections Preview

Each SOC report includes:

1. **EXECUTIVE SUMMARY** - Risk level, threat description, actions
2. **TECHNICAL ANALYSIS** - Attack vectors, timeline, systems affected
3. **IOCs** - Malicious IPs, URLs, signatures
4. **MITRE ATT&CK** - Technique mapping (T1190, T1110.001, etc.)
5. **THREAT INTEL** - Sophistication level, attacker profile
6. **RECOMMENDATIONS** - Ranked by priority, actionable steps
7. **APPENDIX** - Full timeline, detailed indicators

---

**Start here**: `python loggenerator.py && python agent.py server.log && python view_latest_report.py`
