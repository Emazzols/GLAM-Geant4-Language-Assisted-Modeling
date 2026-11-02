# IR Structural Reference Warning

This document applies to the file:

**ir_reference_structure.json**

---

## Purpose of the Reference File

The referenced JSON file describes **all structural possibilities**
supported by the Intermediate Representation (IR).

It exists only to expose:

- available sections
- allowed fields
- possible object structures
- supported configuration patterns

It is a **structural catalogue**, not a simulation description.

---

## Critical Warning

The referenced JSON file is:

- ❌ NOT a valid IR
- ❌ NOT executable
- ❌ NOT a template
- ❌ NOT an example configuration
- ❌ NOT internally consistent by design

Fields appearing together in the reference **are not intended to coexist**
in a real simulation.

Many elements shown simultaneously are mutually exclusive.

---

## Mandatory Interpretation Rules for the LLM

When using `ir_reference_structure.json`, the LLM must understand that:

1. The file defines **what is allowed**, not **what must be generated**.
2. Only fields explicitly required by the user request may appear in the generated IR.
3. The LLM must never copy structural blocks from the reference.
4. The LLM must never attempt to complete or instantiate the reference.
5. Missing information must remain missing.
6. The reference must not influence geometry design decisions.

The reference provides **vocabulary**, not **content**.

---

## Relationship With Other Documents

The system components have distinct roles:

- `ir_translation_rules.md`  
  Defines mandatory behavioral and translation rules.

- `ir_reference_structure.json`  
  Defines structural possibilities.

- IR examples  
  Demonstrate valid causal constructions.

These documents must not be merged conceptually.

---

## Generation Principle

Valid IR generation must follow this logic:

User request  
→ apply translation rules  
→ select only necessary structures from the schema  
→ produce minimal valid IR

The reference structure must never be reproduced directly.

---

## Non-Goal

The reference file is intentionally exhaustive and abstract.

It is **not intended** to:

- represent realistic simulations
- suggest defaults
- enforce completeness
- guide optimization
- improve physical correctness

---

## Final Constraint

If uncertainty exists, the LLM must prefer:

**omitting fields rather than inventing structure.**