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

## 🛡️ Project 1: Internal Security Audit & Risk Assessment (Botium Toys)

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

## 🕵️ Project 2: Incident Handler’s Journal (Multi-Case Analysis)

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

## 🐍 Projekt 3: Algorithm for file updates in Python

**Opis:** Algorytm w języku Python zaprojektowany do aktualizacji pliku tekstowego z adresami IP pracowników, którzy mają dostęp do zastrzeżonych treści w firmie medycznej. Jako analityk bezpieczeństwa przygotowałem to narzędzie, aby regularnie usuwać adresy IP z listy dozwolonych (allow list).

### 🔍 Logika i implementacja:
* **Inicjalizacja funkcji:** Algorytm definiuje funkcję `update_file`, która przyjmuje dwa parametry: nazwę pliku (`import_file`) oraz listę adresów do usunięcia (`remove_list`).
* **Bezpieczny odczyt:** Skrypt otwiera plik w trybie odczytu (`"r"`) przy użyciu instrukcji `with`, co gwarantuje automatyczne zamknięcie pliku.
* **Przetwarzanie danych:** Zawartość pliku jest konwertowana na ciąg znaków metodą `.read()`, a następnie dzielona na listę metodą `.split()`, aby umożliwić edycję poszczególnych elementów.
* **Iteracja i weryfikacja:** Pętla `for` przechodzi przez listę adresów, a instrukcja `if` sprawdza, czy dany adres znajduje się na liście adresów do usunięcia.
* **Aktualizacja zasobów:** Po usunięciu wybranych adresów metodą `.remove()`, lista jest łączona z powrotem w ciąg znaków metodą `.join()` i zapisywana do pliku w trybie zapisu (`"w"`).

### 📁 Dokumentacja i Kod:
* [**Przejdź do folderu projektu (Kod + Opis)**](Python-IP-Allow-List-Update)
* [**Pełny raport techniczny (PDF)**](Python-IP-Allow-List-Update/Algorithm for file updates in Python.pdf)
