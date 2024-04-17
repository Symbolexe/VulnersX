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

# Notes
if you use VulnersX tool, you can use this command to just extract the CVE's ID from cves.txt file.
```bash
grep -oP 'CVE-\d{4}-\d{4}' cves.txt
```
