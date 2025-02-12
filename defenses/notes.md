## RAG Data Access Control:

### Vulnerability: User accesses data outside their role

### Defense: Meta-data filter (RBAC)
- each data set has meta data(Engineering dept vs sales)
- User token has equivalent meta data for filtering
- RAG function have metadata filter:
    - Only ingest data if filter passes

<br>


## Excessive Agency 

### Vulnerability: LLM has inappropriate access to resources/functionality
- ex: LLM has access to execute commands to shell/cli 


### Defense: Principle of least privilege
- Only give access to minimum necessary to perform required actions
- Limited access decrease scope in case of guardrail bypass
- Example: For file creation:
    - instead of shell only allow write to files
    - perform input/output validation

## Data Poisoning

### Vulnerability: Files with indirect prompt injection
- ex: resume reader app
    - resume contains prompt telling LLM person is the best candidate, to hire, etc

### Defense: Guardrails