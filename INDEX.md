# SOC Report Generator - Complete Documentation Index

## 📖 Start Here

1. **[QUICKSTART.md](QUICKSTART.md)** - Get running in 30 seconds
2. **[README.md](README.md)** - Full reference documentation
3. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Architecture & features overview

---

## 🚀 Quick Commands

```bash
# Generate logs with attacks
python loggenerator.py

# Generate SOC report
python agent.py server.log

# View latest report
python view_latest_report.py

# Query the database
python query_database.py stats
python query_database.py critical
python query_database.py type LOG4SHELL
python query_database.py ip 91.240.118.44
```

---

## 📁 Project Structure

### Core Application Files
- **agent.py** (16 KB)
  - Main SOC incident report generator
  - Attack detection engine
  - Report generation with LLM
  - Database storage layer

- **loggenerator.py** (5 KB)
  - Realistic HTTP log generator
  - Simulates 4 attack types
  - Configurable event volume

- **query_database.py** (4 KB)
  - SQLite event query tool
  - Statistics & analysis
  - Forensic investigation

- **view_latest_report.py** (1 KB)
  - Quick report viewer utility

### Documentation Files
- **README.md** (8 KB) - Complete reference guide
- **QUICKSTART.md** (6 KB) - 30-second setup
- **PROJECT_SUMMARY.md** (10 KB) - Architecture & features
- **INDEX.md** (this file) - Navigation guide

### Generated Files
- **server.log** (68 KB) - HTTP access log with attacks
- **soc_events.db** (41 KB) - SQLite event database
- **SOC_REPORT_*.txt** (5 KB) - Professional incident report

---

## 🎯 Attack Types Detected

| Attack | Type | Severity | MITRE |
|--------|------|----------|-------|
| SQL Injection | SQLI | WYSOKIE | T1190 |
| Log4Shell | LOG4SHELL | KRYTYCZNE | T1190 |
| Brute Force | BRUTE_FORCE | WYSOKIE | T1110.001 |
| Scanning | SCAN | ŚREDNIE | T1595.002 |

---

## 📊 Test Data Summary

```
Total Events: 204
Attacking IPs: 3

Distribution:
• SCAN (Reconnaissance): 120 events
• BRUTE_FORCE (Admin attacks): 36 events
• SQLI (SQL Injection): 24 events
• LOG4SHELL (Critical): 24 events

Severity:
• KRYTYCZNE: 24 events
• WYSOKIE: 96 events
• ŚREDNIE: 84 events
```

---

## 🔧 Key Features

✅ **Advanced Detection** - Multi-pattern matching for accurate detection
✅ **Database Storage** - SQLite for persistent event tracking
✅ **MITRE Mapping** - Real MITRE ATT&CK framework integration
✅ **LLM Reports** - Professional insights using Ollama
✅ **Query Tools** - Forensic investigation capabilities
✅ **Timeline Analysis** - Attack flow reconstruction
✅ **Severity Scoring** - Intelligent risk assessment

---

## 📖 Documentation Roadmap

### For Quick Setup
→ Read **QUICKSTART.md** (5 min)

### For Full Understanding
→ Read **README.md** (15 min)

### For Architecture/Design
→ Read **PROJECT_SUMMARY.md** (10 min)

### For Using Tools
1. Generate logs: `python loggenerator.py`
2. Create report: `python agent.py server.log`
3. Query data: `python query_database.py <command>`

---

## 🎓 Learning Path

1. **Beginner**: Run commands, view reports
2. **Intermediate**: Modify log generation, query database
3. **Advanced**: Integrate with real logs, customize rules
4. **Expert**: Add ML detection, integrate with SIEM

---

## 💻 System Requirements

- Python 3.8+
- Ollama with llama3.1 model
- 100 MB disk space
- Windows/Linux/Mac compatible

---

## 📞 Quick Reference

### Generate Data
```bash
python loggenerator.py                    # Create test logs
```

### Create Reports
```bash
python agent.py server.log                # Single report
python agent.py /path/to/custom/log       # Custom log file
```

### View Results
```bash
python view_latest_report.py              # View latest report
python query_database.py stats            # Show statistics
python query_database.py critical         # Show critical events
python query_database.py ip <IP>          # Events from IP
python query_database.py type <TYPE>      # Events by type
```

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| LLM connection error | Ensure Ollama is running: `ollama run llama3.1` |
| No events detected | Increase log lines: edit loggenerator.py |
| Module not found | Install deps: `pip install -r requirements.txt` |
| Database locked | Close all processes and retry |

---

## 📈 Next Steps

1. **Explore**: Run all commands in QUICKSTART.md
2. **Understand**: Read full README.md
3. **Customize**: Modify attack patterns or log volume
4. **Integrate**: Connect to real server logs
5. **Extend**: Add custom detection rules

---

## 🎯 File Selection Guide

| I want to... | Read this file |
|---|---|
| Get started quickly | QUICKSTART.md |
| Understand full features | README.md |
| See what was built | PROJECT_SUMMARY.md |
| Find commands | This INDEX.md |
| Run the generator | loggenerator.py |
| Create reports | agent.py |
| Query events | query_database.py |

---

## 📊 Report Output Example

Each generated report includes:

1. **EXECUTIVE SUMMARY** - Risk level & impact
2. **TECHNICAL ANALYSIS** - Attack vectors & systems
3. **INDICATORS OF COMPROMISE** - IPs, URLs, signatures
4. **MITRE ATT&CK MAPPING** - Techniques & tactics
5. **THREAT INTELLIGENCE** - Sophistication & profile
6. **RECOMMENDATIONS** - Prioritized actions
7. **APPENDIX** - Full timeline & details

---

## 🚀 One-Liner Workflow

```bash
python loggenerator.py && python agent.py server.log && python view_latest_report.py
```

---

**Last Updated**: 2026-06-11
**Status**: ✅ Fully Functional
**Test Coverage**: 4 attack types detected, 204 events analyzed, professional report generated

For detailed usage, start with [QUICKSTART.md](QUICKSTART.md)
