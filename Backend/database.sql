CREATE DATABASE pv_system;
USE pv_system;




CREATE TABLE adverse_events (
  case_id VARCHAR(50) PRIMARY KEY,
  risk_level ENUM('LOW','MEDIUM','HIGH'),
  status VARCHAR(30),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE followup_tokens (
  token_hash VARCHAR(255) PRIMARY KEY,
  case_id VARCHAR(50),
  required_fields TEXT,
  expires_at DATETIME,
  used BOOLEAN DEFAULT FALSE
);

CREATE TABLE clinical_data (
  id INT AUTO_INCREMENT PRIMARY KEY,
  case_id VARCHAR(50),
  field_name VARCHAR(100),
  encrypted_value TEXT,
  source VARCHAR(30),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_logs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  case_id VARCHAR(50),
  action VARCHAR(100),
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);




CREATE TABLE identity_vault (
  id INT AUTO_INCREMENT PRIMARY KEY,
  case_id VARCHAR(50),
  encrypted_email TEXT,
  encrypted_phone TEXT
);
