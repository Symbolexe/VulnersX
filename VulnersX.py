import sys
import requests
import sqlite3
import time

class VulnersX:
    def __init__(self):
        print("Initializing VulnersX Tool...")
        # Connect to SQLite database
        self.conn = sqlite3.connect('vulnerabilities.db')
        self.cur = self.conn.cursor()
        # Create table if not exists
        self.cur.execute('''CREATE TABLE IF NOT EXISTS vulnerabilities (
                            id INTEGER PRIMARY KEY,
                            cve_id TEXT,
                            summary TEXT
                            )''')
        self.conn.commit()
    
    def search_vulnerabilities(self, package_name, after_date):
        print(f"Searching vulnerabilities for {package_name} after {after_date}...")
        try:
            url = f"https://access.redhat.com/labs/securitydataapi/cve.json?package={package_name}&after={after_date}"
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            vulnerabilities = response.json()
            total_vulnerabilities = len(vulnerabilities)
            if total_vulnerabilities > 0:
                print("\033[1mFound the following vulnerabilities:\033[0m")
                for i, vulnerability in enumerate(vulnerabilities, start=1):
                    cve_id = vulnerability.get('CVE')
                    summary = vulnerability.get('bugzilla_description')
                    # Save to database
                    self.save_to_database(cve_id, summary)
                    # Save to text file
                    self.save_to_text_file(i, cve_id, summary)
                    # Update progress bar
                    progress = i / total_vulnerabilities
                    self.update_progress_bar(progress)
                print("\n\033[1mSearch complete.\033[0m")
                print("Results saved.")
            else:
                print("\033[91m[-] No vulnerabilities found for the specified package after the specified date.\033[0m")
        except requests.RequestException as e:
            print(f"\033[91m[-] Error occurred while connecting to Red Hat Security Data API: {e}\033[0m")

    def save_to_database(self, cve_id, summary):
        try:
            self.cur.execute("INSERT INTO vulnerabilities (cve_id, summary) VALUES (?, ?)", (cve_id, summary))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"\033[91m[-] Error occurred while inserting data into the database: {e}\033[0m")

    def save_to_text_file(self, counter, cve_id, summary):
        with open('cves.txt', 'a') as f:
            f.write(f"{counter}|{cve_id}|{summary}\n")

    def update_progress_bar(self, progress):
        bar_length = 50
        filled_length = int(bar_length * progress)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f"\rProgress: [{bar}] {int(progress * 100)}%", end='', flush=True)
        time.sleep(0.1)  # Introduce a slight delay for visual effect

def main():
    if len(sys.argv) != 3:
        print("Usage: python VulnersX.py <package_name> <after_date>")
        sys.exit(1)

    package_name = sys.argv[1]
    after_date = sys.argv[2]

    print("Welcome to VulnersX Tool!")
    vst = VulnersX()
    vst.search_vulnerabilities(package_name, after_date)

if __name__ == "__main__":
    main()
