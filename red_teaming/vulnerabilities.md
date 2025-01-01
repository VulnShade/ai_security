[← Back to Main](../../README.md) | [← Back to Red Team Guide](redteam.md)

# 🛡️ LLM Vulnerabilities

## 🎭 Bias & Stereotypes
### Impact
> ⚠️ **Company Reputation Damage** through stereotypical responses

### Root Causes
📌 Two primary factors:
- Implicit bias present in foundation model
- Wrong document used to build the answer

---

## 🔐 Sensitive Information Disclosure
### Impact
> ⚠️ **Data Leakage** of critical information

### Types of Leaks
🚨 Common exposures include:
- Database hostnames
- Credentials (usernames/passwords)
- Internal documentation URLs

### Root Causes
📌 Key vulnerabilities:
- Sensitive data included in training documents
- Private information embedded in prompts

---

## 🚫 Service Disruption (DoS)
### Impact
> ⚠️ **Resource Exhaustion** through malicious requests

### Attack Vectors
🚨 Common methods:
- Giant/repeated payload submissions
- Prompts generating large responses

### Root Causes
📌 Primary factors:
- Excessive request volume
- Resource-intensive requests
- Specially crafted attack patterns

---

## 💫 Hallucinations
### Impact
> ⚠️ **Misinformation** through false content generation

### Root Causes
📌 Key factors:
- Suboptimal retrieval mechanisms
- Poor quality document interpretation
- Model's tendency to avoid contradiction

---
**Note**: Understanding these vulnerabilities is crucial for implementing effective security measures.