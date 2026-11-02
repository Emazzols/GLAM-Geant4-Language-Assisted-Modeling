# Examples

This directory contains **canonical, minimal, non-executable examples** describing how to control Geant4 simulations through the project’s **high-level, LLM-facing interface**.

These examples are **not** Geant4 tutorials.  
They do **not** aim to be complete simulation setups.  
They exist to demonstrate how to *express physical intent* using the system’s **controlled language**, not how Geant4 works internally.

---

## Purpose

The goals of this directory are:

- Provide **reference scenarios** for common experimental setups
- Serve as **causal ground truth** for Retrieval-Augmented Generation (RAG)
- Teach the **cause–effect relationship** between configuration choices and physical outcomes
- Define the **conceptual vocabulary** understood by the system

Every example encodes **what is being simulated**, never *how* it is implemented.

---

## What an Example Is

Each example:

- Describes a simulation **only through the supported interface**
- Is intended to be translated into a **structured Intermediate Representation (IR)**
- Does **not** assume completeness or executability on its own
- Has a **single, clear physical meaning**

An example is a *statement of intent*, not a runnable program.

---

## Intermediate Representation (IR)

All user intent in this project is ultimately expressed through a **strict, validated Intermediate Representation (IR)**.

Key properties of the IR:

- Fully structured (JSON / dict–like)
- Deterministic and machine-verifiable
- Expresses **geometry**, **source**, and **scoring** separately
- Contains **no free-form code**
- Is the *only* input accepted by the Geant4 compilation pipeline

Examples in this directory are written to be **unambiguously mappable** to the IR, even when they intentionally describe only a subset of it (e.g. geometry-only or source-only scenarios).

---

## Directory Structure

Each example follows the same structure:

```
exXX_example_name/
├── description.md
├── config.py
└── expected_output.md
```

### `description.md`

Explains:
- The physical scenario being simulated
- The goal of the setup
- The intended effect of the configuration

No implementation details.  
No Geant4 concepts.

---

### `config.py`

Contains **only declarative configuration calls** related to the experimental setup:

- `configure_geometry`
- `configure_source`
- `configure_scoring` (if applicable)

Important constraints:

- Examples may configure **only part** of the simulation
- Missing sections are intentional and must **not** be inferred
- No control flow, no helpers, no logic
- No direct or indirect Geant4 code

This file exists to express **intent**, not to run a simulation end-to-end.

---

### `expected_output.md`

Describes **qualitative physical expectations**, such as:

- Where energy deposition is expected
- Which volumes should record hits
- What would clearly indicate a broken or incorrect configuration

No numerical validation.  
No performance claims.

---

## Design Constraints (Strict)

All examples **must** obey the following rules:

- No backend modifications
- No Geant4 project changes
- No assumptions outside the documented interface
- No hidden defaults
- No example-specific hacks

If a scenario requires special handling, it does **not** belong here.

---

## Intended Audience

This directory is written for:

- Users defining simulations via natural language or notebooks
- Developers working on the IR validator and compiler
- Large Language Models using RAG to reason about simulations

The examples define **what is expressible**, **what is meaningful**, and **what is allowed**.

---

## Philosophy

Geant4 is an internal engine.  
The IR is the contract.  
The examples describe **experiments**, not software.

If an example looks like Geant4 code, it is wrong.
