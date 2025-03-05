# Attacking LLMS

## 📋 Table of Contents
- Resources
    - [MITRE ATLAS](https://atlas.mitre.org/matrices/ATLAS)

## Reconnaissance
- What systems are used?
- What models are used?
- What algorithms are used?

### Resources
- Company journals
- Conferences
- [arxiv](https://arxiv.org/) (Cornell Archive)
- Blogs

### Defense
- Redact sensitive info/parameters
- Do not reveal training procedures or model architectures

<hr>

## LLM Plugin Compromise
> Specialized add-on tools that extend LLM's capabilities. Connect to external services.

Types:
- Email
- Github
- Python

### Risk
- Steal chats
- Exfiltrate senstive information

### Defense
- Limit which plugins are added
- Limit plugin permissions to minimum necessary

<br>
<hr>


## Attacks

### 1. [TextAttack](https://textattack.readthedocs.io/en/master/)
> Simulate scenarios where a model might fail due to adversarial inputs,
- Attack Recipes:
    - Predefined algorithms like TextFooler to create adversarial examples
- Model Wrappers:
    - Adapt any NLP model for evaluation
- Evaluation Framework
    - Detecting trends or sentiment shifts

