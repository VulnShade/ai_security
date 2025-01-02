[← Back to Main](../../README.md) | [← Back to Guardrails](guardrails.md)

# 🎯 Topic Restriction

## 🛠️ Custom Guardrail Implementation
```python
def detect_topics(
    text: str,
    topics: list[str],
    threshold: float = 0.8
) -> list[str]:
    result = CLASSIFIER(text, topics)
    return [topic
            for topic, score in zip(result["labels"], result["scores"])
            if score > threshold]

@register_validator(name="constrain_topic", data_type="string")
class ConstrainTopic(Validator):
    def __init__(
        self,
        banned_topics: Optional[list[str]] = ["politics"],
        threshold: float = 0.8,
        **kwargs
    ):
        self.topics = banned_topics
        self.threshold = threshold
        super().__init__(**kwargs)

    def _validate(
        self, value: str, metadata: Optional[dict[str, str]] = None
    ) -> ValidationResult:
        detected_topics = detect_topics(value, self.topics, self.threshold)
        if detected_topics:
            return FailResult(error_message="The text contains the following banned topics: "
                        f"{detected_topics}",
            )

        return PassResult()

guard = Guard(name='topic_guard').use(
    ConstrainTopic(
        banned_topics=["politics", "violence"],
        on_fail=OnFailAction.EXCEPTION,
    ),
)
```

<br>

## 📚 Using Predefined Validators
Implementation using [Restrict to Topic](https://hub.guardrailsai.com/validator/tryolabs/restricttotopic)

```python
# install('hub://tryolabs/restricttotopic')

guarded_client = OpenAI(
    base_url='http://localhost:8000/guards/topic_guard/openai/v1/'
)

guarded_rag_chatbot = RAGChatWidget(
    client=guarded_client,
    system_message=system_message,
    vector_db=vector_db,
)
```

---
**Note**: Regular review of topic restrictions helps maintain appropriate conversation boundaries.

