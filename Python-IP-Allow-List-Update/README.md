# Python Automation: Algorithm for File Updates

## 🎯 Project Description
This project features a Python-based algorithm designed to update a text file containing IP addresses of employees who have access to restricted content in a healthcare company. As a security analyst, I developed this tool to regularly update the "allow list" by programmatically removing IP addresses that should no longer have access.

## 💻 Logic and Implementation
The function `update_file` takes two parameters: the name of the file and a list of IP addresses to be removed. 

### Execution Steps:
1. **Open the file:** The algorithm uses a `with` statement and the `open()` function in read mode (`"r"`) to ensure the file is handled securely.
2. **Read contents:** It uses the `.read()` method to convert the file content into a string.
3. **Convert to list:** The `.split()` method converts the string into a list for easier manipulation.
4. **Iterate and Remove:** A `for` loop iterates through the `ip_addresses` list, and an `if` condition checks if an address is in the `remove_list`. If found, it is removed using the `.remove()` method.
5. **Finalize:** The updated list is converted back into a string using `.join()` and written back to the file in write mode (`"w"`), overwriting the old content with the revised list.

## 🛠️ Tools & Methods
* **Language:** Python
* **Methods:** `open()`, `read()`, `split()`, `remove()`, `join()`, `write()`
* **Workflow:** Automated access control management

## 📁 Files in this folder
* `update_list.py` - The executable Python script.
* `Algorithm_for_file_updates_in_Python.pdf` - Detailed step-by-step technical report.
