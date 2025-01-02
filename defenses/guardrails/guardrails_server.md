[← Back to Main](../../README.md) | [← Back to Guardrails](guardrails.md)

# 🔧 Guardrails Server Setup

## 📋 Installation Steps

### 1. Dependencies
```bash
pip install -r requirements.txt
```

### 2. Spacy Models
```bash
python -m spacy download en_core_web_trf
```

### 3. API Configuration
1. Create account at [guardrails](https://hub.guardrailsai.com/keys)
2. Setup API key

### 4. Install Required Models
```bash
guardrails hub install hub://guardrails/provenance_llm --no-install-local-models
guardrails hub install hub://guardrails/detect_pii
guardrails hub install hub://tryolabs/restricttotopic --no-install-local-models
guardrails hub install hub://guardrails/competitor_check --no-install-local-models
```

### 5. Authentication
```bash
guardrails configure
```

### 6. Server Configuration
- Create config file for hallucination detection
- Set environment variables:
  - OPENAI_API_KEY
  - GUARDRAILS_API_KEY

### 7. Launch Server
```bash
guardrails start --config config.py
```

---
**Note**: Ensure all API keys are properly configured before starting the server.

