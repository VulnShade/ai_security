# 🧠 Large Language Models (LLMs)

## 📋 Table of Contents
- [Overview](#overview)
- [How LLMs Work](#-how-llms-work)
- [GPT Models](#-gpt-generative-pre-trained-transformer)
- [BERT Models](#-bert-bidirectional-encoder-representations-from-transformers)
- [Model Training](#-foundational-model-and-fine-tuned-models)
- [RAG Implementation](#-rag-retrieval-augemented-generation)

## Overview
- 🔄 Use deep learning to understand and generate human-like text
- 📚 AI systems trained on massive amounts of text data
- 💬 Process and respond to natural language inputs

---

## 🔍 How LLMs Work

### 1️⃣ Tokenizing
- Every word/character converted to numerical tokens

### 2️⃣ Embedding
- Words stored in association with other words
- Represented as vectors in high-dimensional space

### 3️⃣ Transforming
- Context-aware processing through attention mechanisms
- Next token prediction based on patterns

### 4️⃣ Generating
- Produce coherent, contextually relevant text

---

## 🔄 GPT (Generative Pre-trained Transformer)
- Based on transformer neural network architecture
- Uses self-attention mechanism for text processing
- ▶️ Forward-only processing
- ✍️ Excels at text generation

### Training Process
- **Pre-training**: Initial learning on broad text corpus
- **Fine-tuning**: Specialized training for specific tasks

---

## 📊 BERT (Bidirectional Encoder Representations from Transformers)
- Understands context bidirectionally (before and after)
- 🔄 Processes text in both directions
- 🔍 Optimized for language understanding, not generation

### Best Applications
- 📑 Text classification
- ❓ Question answering systems
- 🔎 Search and information retrieval

---

## 🏗️ Foundational Model and Fine-Tuned Models

### Pre-training
1. 🧩 Pattern Recognition - Identify linguistic structures
2. 📝 Contextual Understanding - Grasp semantic relationships
3. 💬 Response Generation - Produce coherent outputs

### Fine-tuning
- ⚙️ Weights adjusted for domain-specific knowledge
- 🔬 Specialized versions: Medical, legal, financial domains

---

## 🔄 RAG (Retrieval Augemented Generation)
- 🔍 Retrieves relevant information from sources
- 🔗 Combines retrieved context with generation capabilities

### Retrieval Sources:
- 🌐 Internet (URLs, search engines)
- 💾 Databases (Relational, Vector)
- 📄 Document repositories