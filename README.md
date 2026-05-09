# Vinayak Multistep Recursive Reasoning Benchmark (VMRRB)

## Version: 01

## Difficulty Level: Normal

# Results

| Rank | Model Name                  | Score  |
| ---- | --------------------------- | ------ |
| 1    | Google Gemini 3.1 Pro       | 97.30% |
| 2    | DeepSeek Pro v4             | 78.80% |
| 3    | Kimi K26 Thinking           | 77.40% |
| 4    | Anthropic Claude Sonnet 4.6 | 74.40% |
| 5    | GPT-5.4 Thinking            | 67.90% |

## Benchmark File Structure

```text
vmrrb-benchmark/
├── README.md              ← methodology, benchmark specification
├── scripts/               ← scoring and evaluation scripts
├── test_prompt/           ← prompt used for testing and question & answer sheets 
├── results/               ← detailed benchmark reports
├── raw_data_ai_response/  ← raw AI model outputs
└── Leaderboard.csv
```

---

# Overview

The **Vinayak Multistep Recursive Reasoning Benchmark (VMRRB)** is designed to evaluate advanced reasoning, recursive dependency resolution, and robustness capabilities in dynamic, noisy, and structurally challenging environments. 

The benchmark architecture is designed to scale toward extremely large recursive workloads, including theoretical configurations containing trillions of interdependent questions.

Preliminary evaluations on contemporary frontier language models show substantial performance degradation even on reduced benchmark configurations containing 1,000 recursively dependent questions.

The benchmark is specifically designed to test:

* **Recursive multistep reasoning**
* **Dependency resolution across interconnected problems**
* **Long-chain consistency**
* **Robust semantic parsing**
* **Execution efficiency under recursive workloads**
* **Reliable computation under noisy input conditions**

The benchmark intentionally relies on relatively simple arithmetic primitives. The primary difficulty emerges from recursive dependency resolution, noisy semantic parsing, execution ordering, long-chain consistency, and strict instruction-following constraints rather than advanced mathematical complexity.

The objective is not only to measure reasoning accuracy, but also to evaluate whether an AI system can maintain speed, consistency, correctness, and structural reliability simultaneously.

---

# Table of Contents

* Introduction
* Benchmark Objectives
* Benchmark Design
* Evaluation & Scoring Methods
* Dataset
* Results
* Future Work

---

# Introduction

Modern frontier AI systems demonstrate strong performance on conventional reasoning benchmarks but frequently degrade under recursive dependency resolution, noisy semantic parsing, and long-chain execution constraints.

VMRRB is designed to evaluate whether a model can maintain correctness, consistency, and structured execution while solving recursively interconnected (mathematical) tasks embedded within challenging environments.

The benchmark combines:

* Recursive dependency chains
* Arithmetic reasoning
* Semantic noise injection
* Structured parsing constraints
* Strict output formatting requirements

Each question may depend on answers from one or more previous questions. Models must correctly resolve dependency chains recursively before computing the final result.

In addition, benchmark prompts intentionally contain random irrelevant tokens and corrupted text fragments. Models are expected to recover the intended mathematical meaning while ignoring semantically meaningless content.

---

# Benchmark Objectives

Below is a structured list of the capabilities benchmark aims to evaluate:

| Main Category                          | What Is Being Tested                                                                                                             |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Multistep Recursive Reasoning          | Solving recursively dependent, interconnected problems through chained reasoning                                                 |
| Dependency & Structural Resolution     | Resolving nested references and understanding hierarchical dependency structure in correct evaluation order                      |
| Mathematical & Compositional Reasoning | Correctly combining arithmetic, symbolic substitution, parsing, memory, and recursion during computation                         |
| Robust Semantic Parsing                | Recovering intended mathematical meaning from noisy, ambiguous, corrupted, or adversarial text while ignoring irrelevant content |
| Context & Long-Chain Consistency       | Retaining intermediate results and ensuring consistency across deep reasoning chains                                             |
| Instruction & Rule Following           | Strictly adhering to procedural, execution, and output-format constraints                                                        |
| Recursive Planning & Execution         | Planning dependency resolution strategy and executing computations systematically                                                |

The benchmark is intended to stress-test reasoning systems beyond conventional single-step mathematical evaluation tasks.

---

# Benchmark Design

## Mathematical Operations

The benchmark uses a constrained set of arithmetic operations designed to isolate reasoning, dependency resolution, and semantic robustness from advanced mathematical complexity.

Supported operations include:

| Operation        | Description                                     |
| ---------------- | ----------------------------------------------- |
| Addition         | Arithmetic summation                            |
| Subtraction      | Arithmetic difference                           |
| Multiplication   | Arithmetic product                              |
| Division         | Arithmetic quotient                             |
| Rounding         | Numeric rounding transformation                 |
| Floor Function   | Largest integer less than or equal to input     |
| Ceiling Function | Smallest integer greater than or equal to input |
| Modulo           | Remainder-based arithmetic operation            |

The benchmark intentionally relies on relatively simple arithmetic primitives. The primary challenge arises from recursive dependency resolution, noisy semantic parsing, long-chain consistency, and strict instruction-following constraints rather than advanced mathematical difficulty.

## Recursive Dependency Structure

Questions are recursively interconnected through dependency references.

Example:

```text
Question [10]: Compute the product of [ Answer 4 ] and 3.56
```

To solve Question 10, a model must first recursively solve Question 4 before computing the final answer.

The benchmark evaluates whether models can:

* Build dependency chains correctly
* Resolve nested references in proper order
* Preserve intermediate state across long reasoning sequences
* Maintain consistency throughout recursive execution

## Noise Injection Strategy

Benchmark prompts intentionally include random irrelevant tokens, malformed fragments, and semantically meaningless text.

Example:

```text
Determine the sum of xQAbc [ Answer 5 ] and two point three yzLm
```

Models are expected to:

* Recover the intended mathematical structure
* Ignore semantically irrelevant noise
* Preserve valid operators and dependency references
* Avoid corruption of execution flow due to adversarial text

## Output Constraints

Models must strictly follow predefined output formatting rules.

Outputs are evaluated not only for mathematical correctness, but also for:

* Correct dependency resolution
* Proper execution ordering
* Output structure compliance
* Consistency across all generated answers

---

# Evaluation & Scoring Methods

Model outputs are evaluated through end-to-end answer correctness against the benchmark ground-truth dataset.

Numerical answers are compared using configurable decimal-place tolerance matching to reduce sensitivity to insignificant floating-point formatting differences.

Current benchmark evaluations use a 1-decimal-place comparison threshold.

| Metric | Description |
|---|---|
| Accuracy | Percentage of correctly solved questions |

Because benchmark questions are recursively interconnected, recursive reasoning accuracy, dependency resolution, parsing robustness, and execution consistency are evaluated implicitly through final-answer correctness rather than through independently scored sub-metrics.

---

# Dataset

The benchmark dataset is synthetically generated and consists of recursively interconnected mathematical problems containing controlled semantic noise and dependency references.

Difficulty levels scale through:

* Dependency depth
* Recursive graph complexity
* Noise density
* Total question count
* Structural dependency length

The benchmark supports scalable configurations ranging from small evaluation subsets to extremely large recursive workloads.

---

# Results

## Result of 1000 Questions 

| Rank | Model Name                  | Score  |
| ---- | --------------------------- | ------ |
| 1    | Google Gemini 3.1 Pro       | 97.30% |
| 2    | DeepSeek Pro v4             | 78.80% |
| 3    | Kimi K26 Thinking           | 77.40% |
| 4    | Anthropic Claude Sonnet 4.6 | 74.40% |
| 5    | GPT-5.4 Thinking            | 67.90% |

Detailed benchmark reports, raw model outputs, and evaluation summaries are available in the `results/` and `raw_data_ai_response/` directories.

Leaderboard rankings are mainly maintained in:

```text
Leaderboard.csv
```

---

# Future Work

Future benchmark expansions may include:

- Larger recursive dependency graphs
- Multilingual noisy reasoning tasks
- Symbolic reasoning extensions
- Adaptive difficulty scaling
- Automated benchmark generation pipelines
- Expanded robustness evaluation methodologies

VMRRB already includes larger-scale benchmark configurations containing 10K, 100K, and 1M recursively interconnected questions. Preliminary evaluations indicate substantial performance and scalability challenges for current frontier language models on these larger recursive workloads.

Future development may involve collaboration with frontier AI research labs to evaluate large-scale recursive reasoning capabilities, scalability limits, and robustness under increasingly complex dependency structures.

The benchmark will continue evolving to evaluate increasingly complex recursive reasoning and execution capabilities in large-scale AI systems.



