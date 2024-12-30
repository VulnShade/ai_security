# LLM Vulnerabilities

## Bias & Stereotypes
- **Issue:** Chatbot gives stereotypical answers
  - **Impact:** Affects company reputation

### Causes
- Implicit bias present in foundation model
- Wrong document used to build the answer

---

## Sensitive Information Disclosure
- **Issue:** Chatbot discloses sensitive info:
  - DB hostname
  - Usernames/Passwords
  - URL of internal documents

### Causes
- Inclusion of sensitive data in documents available
- Private info in the prompt which gets leaked

---

## Service Disruption (DoS)
- **Issue:** User uses up resources:
  - Sends giant/repeated payloads
  - Prompts that generate large responses

### Causes
- Large number of requests
- Long requests
- Crafted requests

---

## Hallucinations
- **Issue:** Chatbot tells customers about company offers/info that do not exist

### Causes
- Suboptimal retrieval mechanism
- Low quality documents get misinterpreted by LLM
- LLM tendency to never contradict the user