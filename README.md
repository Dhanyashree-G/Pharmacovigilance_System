# AI-Based Secure Pharmacovigilance Follow-Up System

## 📌 Overview
Pharmacovigilance (PV) systems often receive adverse drug reaction (ADR) reports with missing critical information such as patient age, dosage, onset date, or seriousness. Manual follow-ups are inefficient, repetitive, and face low response rates from busy doctors and hesitant patients.

This project implements an **AI-based, privacy-first pharmacovigilance follow-up system** that automatically detects missing information, collects it securely using one-time links, standardizes reactions using **MedDRA coding**, and generates **E2B(R3)-style XML** for regulatory submission.

---

## 🎯 Key Objectives
- Automatically detect missing mandatory fields in ADR reports
- Minimize user burden with zero-login, minimal follow-up forms
- Ensure GDPR, HIPAA, and ALCOA+ compliance
- Standardize adverse events using MedDRA Preferred Terms
- Generate E2B-compliant XML for regulatory reporting
- Provide a Safety Officer dashboard for monitoring and compliance

---

## 🏗️ System Architecture
<img width="1856" height="1184" alt="pharma_architecture diagram" src="https://github.com/user-attachments/assets/8747f4df-a6a3-40ea-8954-61a7cf8a9c06" />

---

## ✨ Features
- 🔐 One-time secure follow-up links (48-hour expiry)
- 🧠 AI-based missing field detection (NLP + rules)
- 🧾 Dynamic forms displaying only missing fields
- 🔑 AES-256 encryption for sensitive data
- 🧬 MedDRA Preferred Term (PT) coding
- 📄 E2B(R3)-style XML export
- 📊 Safety Officer Dashboard with RBAC
- 📜 Immutable audit logs

---

## 🛠️ Technologies Used

### Frontend
- React.js
- Tailwind CSS
- Axios

### Backend
- Python
- FastAPI
- spaCy (NLP)
- JWT (Authentication)
- Cryptography (AES-256)

### Database
- MySQL

### Standards & Compliance
- MedDRA (Medical Dictionary for Regulatory Activities)
- ICH E2B(R3)
- GDPR
- HIPAA
- ALCOA+

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- MySQL 8+

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/pharmacovigilance-followup-system.git
cd pharmacovigilance-followup-system
