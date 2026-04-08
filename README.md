# Cybersecurity Portfolio - Hubert Dulko

This repository contains professional documentation and case studies developed during my cybersecurity training and independent research.

---

## 🎯 Overview
This portfolio showcases a series of cybersecurity projects completed as part of the **Google Cybersecurity Professional Certificate**. These activities demonstrate practical experience in:

* **Risk Management & Compliance** (NIST CSF, GDPR, SOC2).
* **Incident Response & Digital Forensics.**
* **Security Auditing & Technical Documentation.**
* **Threat Analysis** (Ransomware, IDOR, Phishing).

---
## 🛡️ Project 1: Vulnerability Assessment & Risk Management (NIST SP 800-30)

**Description:** A professional risk assessment of a mission-critical MySQL database server hosting sensitive PII and financial records for a global e-commerce organization. This project demonstrates the ability to translate technical vulnerabilities into business risks using the **NIST SP 800-30 Rev. 1** framework.

### 🔍 Key Analysis & Methodology:
* **Business-Centric Approach:** Evaluated risks based on the **CIA Triad** (Confidentiality, Integrity, Availability), focusing on the potential impact of data breaches on business continuity and regulatory compliance.
* **Risk Identification:** Identified and categorized threat sources (e.g., competitors, hackers) and threat events (exfiltration, data alteration) targeting the organization's primary digital assets.
* **Qualitative Risk Scoring:** Developed a risk profile by calculating the likelihood and severity of various attack scenarios to prioritize remediation efforts.

### 🛠️ Remediation & Security Strategy:
Proposed a multi-layered security plan to reduce the attack surface:
* **Identity & Access Management (IAM):** Implementation of MFA, RBAC, and strict AAA protocols.
* **Network Hardening:** Transitioning to TLS encryption and implementing IP allow-listing to secure remote connections.
* **Strategic Oversight:** Aligned technical security controls with organizational goals to mitigate legal and financial consequences.

### 📁 Documentation:
* [**Full Vulnerability Assessment Report (PDF)**](./Vulnerability_Assessment_Report_Hubert_Dulko.pdf)

---

## 🛡️ Project 2: Internal Security Audit & Risk Assessment (Botium Toys)

**Scenario:** Conducted a comprehensive security audit for a rapidly growing e-commerce company to identify vulnerabilities and ensure regulatory compliance.

### 🔍 Key Audit Areas:
* **Asset Management:** Cataloged a full inventory of hardware (desktops, laptops, smartphones), software, and legacy systems requiring manual monitoring. 
* **Risk Assessment:** Evaluated the initial security posture, identifying a Baseline Risk Score of 8/10 due to critical gaps in existing controls.
* **Compliance Evaluation:** Assessed the organization's adherence to **NIST CSF**, **GDPR**, **PCI DSS**, and **SOC2** frameworks. 
* **Technical Findings:** Discovered high-risk issues including lack of encryption for credit card data, absence of IDS, and missing disaster recovery plans. 

### 💡 Strategic Recommendations:
* Implementation of the **Least Privilege** principle and separation of duties. 
* Deployment of **AES-256 encryption** for sensitive data at rest and in transit. 
* Establishing a **Disaster Recovery Plan** and regular backup restoration procedures. 
* Standardization of security policies using the **ISO/IEC 27001** framework. 

### 📁 Project Documentation:
* [View Full Audit Report (PDF)](Internal_Security_Audit_&_Risk_Assessment_Report_Hubert_Dulko.pdf)

---

## 🕵️ Project 3: Incident Handler’s Journal (Multi-Case Analysis)

**Objective:** Document and analyze real-world security incidents using the 5 W's framework and forensic tools to develop actionable remediation strategies.

### 🔍 Key Investigations:
* **Incident #001 (Ransomware):** Documented a healthcare-targeted ransomware attack, identifying the phishing vector and business impact.
* **Incident #002 (Phishing/Malware):** Conducted forensic analysis of a malicious attachment (`bfsvc.exe`) using **VirusTotal**, resulting in threat escalation and blocklisting recommendations.
* **Incident #003 (Web Data Breach):** Performed a technical root cause analysis of an **IDOR (Insecure Direct Object Reference)** vulnerability that led to the exposure of 50,000 customer records.

### 🛠️ Skills & Tools:
* **Methodologies:** 5 W’s Framework, Root Cause Analysis (RCA), Incident Response Lifecycle.
* **Technical Tools:** SIEM (Log Analysis), Web Server Logs, VirusTotal.
* **Documentation:** Professional Incident Journaling and Remediation Planning.

### 📁 Project Documentation:
* [View Full Incident Journal (PDF)](Incident_Handler's_Journal_Hubert_Dulko.pdf)

---

## 🐍 Project 4: Algorithm for File Updates in Python

**Description:** A Python-based algorithm designed to update a text file containing employee IP addresses authorized to access restricted content in a healthcare company. As a security analyst, I developed this tool to regularly update the "allow list" by programmatically removing IP addresses that no longer require access.

### 🔍 Logic and Implementation:
* **Function Initialization:** The algorithm defines the `update_file` function, which accepts two parameters: the filename (`import_file`) and a list of addresses to be removed (`remove_list`).
* **Secure File Handling:** The script opens the file in read mode (`"r"`) using the `with` statement, ensuring the file is automatically and securely closed after processing.
* **Data Processing:** File content is converted into a string using the `.read()` method and then parsed into a list via `.split()` to enable manipulation of individual elements.
* **Iteration and Verification:** A `for` loop iterates through the IP address list, while an `if` statement checks if each address is present in the removal list.
* **Resource Update:** After removing the specified addresses using the `.remove()` method, the list is converted back into a string using `.join()` and written to the file in write mode (`"w"`).

### 📁 Documentation and Code:
* [**View Project Folder (Code & README)**](./Python-IP-Allow-List-Update/)
* [**Full Technical Report (PDF)**](./Python-IP-Allow-List-Update/Algorithm_for_file_updates_in_Python.pdf)

---


