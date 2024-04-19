# VulnersX
VulnersX is a powerful tool for efficiently searching and analyzing software vulnerabilities. It provides comprehensive results with both SQLite database and text file outputs, ensuring flexibility and ease of use for security professionals and developers alike.

![VulnersX](https://github.com/Symbolexe/VulnersX/assets/140549630/82d52fdd-8b72-43c4-9ae7-479065736d7b)

# Features:
1. Flexible Search: Users can specify the name of the package they want to search vulnerabilities for and the date after which they want to find vulnerabilities.
2. Database Integration: The tool stores the fetched vulnerabilities in a SQLite database, allowing for easy access and management of vulnerability data.
3. Text File Output: In addition to the database, the tool also saves the search results in a text file for quick reference and sharing.
4. Detailed Reporting: Each vulnerability entry includes the CVE ID and a summary of the vulnerability, providing users with comprehensive information about the identified issues.
5. Cross-Platform Compatibility: The tool is designed to run on both Windows and Linux systems, with appropriate notifications and data storage mechanisms based on the operating system.
6. Progress Bar: During the search process, users are presented with a progress bar that visually indicates the status of the search operation.

# Installation:
- Clone the repository to your local machine.
- Ensure you have Python installed.
- Install the required dependencies using `pip install requests`.

# Usage:
- Run the script using Python: `python3 VulnersX.py`.
- Follow the on-screen prompts to enter the package name and the date for vulnerability search.
- View the search results in the database and text files.

# Pip
you can use this tool with : `pip install vulnersx`

- Example - 1
```python
from vulnersx import VulnersX

def main():
    package_name = "apache"  # Replace with the package name you want to search vulnerabilities for
    after_date = "2022-01-01"  # Replace with the date from which you want to search vulnerabilities

    print("Welcome to VulnersX Tool!")
    vst = VulnersX()
    vst.search_vulnerabilities(package_name, after_date)

if __name__ == "__main__":
    main()
```

- Example - 2
```python
from vulnersx import VulnersX

def main():
    # Define a list of packages and their corresponding after dates
    package_info = [
        {"name": "openssl", "after_date": "2022-01-01"},
        {"name": "nginx", "after_date": "2022-01-01"},
        {"name": "apache", "after_date": "2022-01-01"}
    ]

    print("Welcome to VulnersX Tool!")
    vst = VulnersX()

    for pkg_info in package_info:
        package_name = pkg_info["name"]
        after_date = pkg_info["after_date"]
        print(f"Searching vulnerabilities for {package_name} after {after_date}...")
        vulnerabilities = vst.search_vulnerabilities(package_name, after_date)
        
        if vulnerabilities:
            print(f"\033[1mFound vulnerabilities for {package_name}:\033[0m")
            for vulnerability in vulnerabilities:
                print(f"CVE ID: {vulnerability['cve_id']}")
                print(f"Summary: {vulnerability['summary']}")
                print("-" * 50)
        else:
            print(f"\033[91mNo vulnerabilities found for {package_name} after {after_date}.\033[0m")
        
        print("\n")

if __name__ == "__main__":
    main()
```
# Notes
if you use VulnersX tool, you can use this command to just extract the CVE's ID from cves.txt file.
```bash
grep -oP 'CVE-\d{4}-\d{4}' cves.txt
```
