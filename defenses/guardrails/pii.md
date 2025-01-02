[← Back to Main](../../README.md) | [← Back to Guardrails](guardrails.md)

# 🔒 PII Protection

## Microsoft Presidio Integration
Using [Presidio](https://microsoft.github.io/presidio/) for PII detection

### 🛡️ PII Validator Implementation
```python
# Type hints
from typing import Optional, Any, Dict

# Standard imports
import time
from openai import OpenAI

# Helper functions
from helper import RAGChatWidget, SimpleVectorDB

# Presidio imports
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Guardrails imports
from guardrails import Guard, OnFailAction, install
from guardrails.validator_base import (
    FailResult,
    PassResult,
    ValidationResult,
    Validator,
    register_validator,
)

presidio_analyzer = AnalyzerEngine()
presidio_anonymizer= AnonymizerEngine()

def detect_pii(
    text: str
) -> list[str]:
    result = presidio_analyzer.analyze(
        text,
        language='en',
        entities=["PERSON", "PHONE_NUMBER"]
    )
    return [entity.entity_type for entity in result]

@register_validator(name="pii_detector", data_type="string")
class PIIDetector(Validator):
    def _validate(
        self,
        value: Any,
        metadata: Dict[str, Any] = {}
    ) -> ValidationResult:
        detected_pii = detect_pii(value)
        if detected_pii:
            return FailResult(
                error_message=f"PII detected: {', '.join(detected_pii)}",
                metadata={"detected_pii": detected_pii},
            )
        return PassResult(message="No PII detected")

guard = Guard(name='pii_guard').use(
    PIIDetector(
        on_fail=OnFailAction.EXCEPTION
    ),
)

guarded_client = OpenAI(base_url='http://localhost:8000/guards/pii_guard/openai/v1/')

guarded_rag_chatbot = RAGChatWidget(
    client=guarded_client,
    system_message=system_message,
    vector_db=vector_db,
)
```

### 🔄 Real-Time Stream Validation
```python
from guardrails.hub import DetectPII

guard = Guard().use(
    DetectPII(pii_entities=["PHONE_NUMBER", "EMAIL_ADDRESS"], on_fail="fix")
)

from IPython.display import clear_output

validated_llm_req = guard(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a chatbot."},
        {
            "role": "user",
            "content": "Write a short 2-sentence paragraph about an unnamed protagonist while interspersing some made-up 10 digit phone numbers for the protagonist.",
        },
    ],
    stream=True,
)

validated_output = ""
for chunk in validated_llm_req:
    clear_output(wait=True)
    validated_output = "".join([validated_output, chunk.validated_output])
    print(validated_output)
    time.sleep(1)
```

---
**Note**: Regular updates to PII detection patterns help maintain robust protection.