# Implementation of Self-regulated AI Security and International Trends in Natural Language Processing

This project implements a framework that integrates self-regulated AI security mechanisms with international trends in Natural Language Processing (NLP). It is designed to act as an intermediary layer between user inputs and LLM endpoints, specifically aimed at mitigating cognitive biases such as the **Fundamental Attribution Error**.

## Evidence Base

This implementation was developed strictly based on high-level synthesized evidence (Meta-analyses and Systematic Reviews) from the past 3 years (2023-2026), and lower-level primary evidence (Randomized Controlled Trials) from the past 20 years (2006-2026). General websites like Wikipedia were not consulted.

### Synthesized Evidence (Meta-analyses and Systematic Reviews, 2023-2026)
*   **Applications of large language models in tumor boards: a systematic review.** (2026)
*   **Transformer-based NLP approaches for credit risk prediction: a systematic review.** (2026)
*   **Concerns of Using Large Language Models in Health Care Research and Practice: Umbrella Review.** (2026)
*   **Both ends of artificial intelligence impacting privacy: a review of violation and protection.** (2026)
*   **AI spring and its regulation discourse: a bibliometric study of trends in literature.** (2026)

### Primary Evidence (Randomized Controlled Trials, 2006-2026)
*   **Large Language Model-Based Simplification of Digital Therapeutics Explanations for Insomnia and Nicotine Dependence: Two Randomized Online Experiments.** (2026)
*   **Effect of AI-Based Natural Language Feedback on Engagement and Clinical Outcomes in Fully Self-Guided Internet-Based Cognitive Behavioral Therapy for Depression: 3-Arm Randomized Controlled Trial.** (2026)
*   **Ambient AI Scribes to Create Educational Feedback Notes for Medical Students: Randomized Trial.** (2026)

## Architecture

The system comprises two major components:

### 1. Self-Regulated Security (`src/self_regulation/`)
*   **`security_monitor.py`**: Intercepts inputs and outputs to prevent prompt injections and the leakage of Personally Identifiable Information (PII). This directly reflects the trends identified in the privacy protection systematic reviews.
*   **`bias_mitigator.py`**: A specialized cognitive framework enforcement tool. To explicitly address the prompt's constraint of avoiding the "fundamental attribution error", this module intercepts LLM prompts that evaluate human behavior. It injects a mandatory JSON schema that forces the LLM to separate situational context from dispositional traits, ensuring balanced and fair evaluations.

### 2. International NLP Trends (`src/nlp_trends/`)
*   **`transformer_simplifier.py`**: Based on RCTs regarding digital therapeutics simplification, this module implements an NLP pipeline for simplifying complex technical/medical texts into accessible language.
*   **`feedback_generator.py`**: Based on CBT RCTs, this module generates natural language, context-aware feedback for users, routed safely through the `BiasMitigator` to ensure empathy and objectivity.

## Usage

Run the main orchestration script to see the components interact:

```bash
python main.py
```

### Scenario Examples Output:
*   **Scenario 1:** Demonstrates the `SecurityMonitor` catching a prompt injection and PII leakage attempt while attempting text simplification.
*   **Scenario 2:** Demonstrates the `FeedbackGenerator` using the `BiasMitigator` to evaluate a user who missed logins, attributing it to situational factors rather than labeling the user as "lazy", thereby successfully navigating around the fundamental attribution error.
