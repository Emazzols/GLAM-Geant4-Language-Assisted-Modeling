# LLM → IR Translation Rules (Normative)

This document defines **mandatory rules** for translating natural language user requests into the fixed Intermediate Representation (IR).

These rules are **binding**.  
They are not suggestions, examples, or best practices.

The LLM acts **only** as a translator from user intent to IR.  
It must not infer, optimize, correct, or complete the simulation.

---

## 1. General Principles

- The IR schema is **frozen** and **non-negotiable**.
- Only fields explicitly defined in the IR are allowed.
- No implicit assumptions are permitted.
- If information is missing, it must remain missing.
- The LLM must not attempt to make examples executable or self-consistent.
- The LLM must not introduce logic not explicitly requested by the user.

The LLM is **not** a physicist, CAD engine, or Geant4 expert.  
It is a deterministic translator.

---

## 2. Geometry Translation Rules

### 2.1 Size and Dimensions

- All primitives use **half-length conventions** where applicable.
- If the user specifies:
  - **side / length / width / height** → divide by 2 for `half_*` fields
  - **radius** → use as-is (never divide)
  - **diameter** → divide by 2 to obtain radius
- The LLM must never store full lengths where half-lengths are required.

Examples:
- “cube with side 10 cm” → `half_size = 5 cm`
- “cylinder height 4 cm” → `half_height = 2 cm`

---

### 2.2 Reference Frame and Positioning

- All positions are **absolute**, **center-to-center**, and expressed explicitly.
- No alignment, contact, or attachment is implicit.
- Phrases like:
  - “on top of”
  - “attached to”
  - “touching”
  - “resting on”
  
  **do not imply any automatic offset or correction**.

The LLM must always translate positions into explicit coordinates.

---

### 2.3 Placement Rules

- Every placement must explicitly specify:
  - `child`
  - `mother`
  - `position`
- The LLM must never infer the mother volume.
- No placement may be invented for convenience.

#### `place` vs `stacked`

- If the user describes:
  - layers
  - stacks
  - repeated elements along one axis
  - regularly spaced copies

  then **`PlaceStacked` must be used**.

- It is **forbidden** to replace a stacking logic with multiple equivalent `place` entries.

---

### 2.4 Rotations

- Rotations must be specified **only if explicitly requested or strictly necessary**.
- The LLM must not introduce rotations “for correctness” or “for realism”.
- No default or implicit rotations are allowed.

---

### 2.5 Boolean Solids

- Boolean solids form a **DAG** (no cycles).
- The LLM must not reorder or restructure boolean operations.
- No boolean operation may be introduced unless explicitly described.
- If a geometry can be expressed with a primitive, boolean operations must not be used.

---

## 3. Source Translation Rules

### 3.1 General Constraints

- `position` is **always mandatory**.
- Source configuration is performed **only** via IR fields.
- No additional source logic may be introduced.

---

### 3.2 Source Types

- `point`, `disk`, `sphere` are mutually exclusive.
- “Extended source” implies `disk` or `sphere`, never `point`.

---

### 3.3 Directionality

- For **all** source types::
  - **exactly one** of `direction` or `isotropic` must be present.
- Both cannot appear together.
- Neither may be omitted.

---

### 3.4 Direction Vectors

- Direction vectors may be arbitrary in the IR.
- **Normalization must NOT be performed in the IR**.
- Normalization is handled exclusively during compilation.

---

### 3.5 Energy

- Energy must always be expressed as `{ value, unit }`.
- No implicit units are allowed.
- Monoenergetic sources use `SetMonoEnergy` exclusively.

---

## 4. Scoring Rules

- Scoring is a **list of volume names only**.
- The LLM must verify that scored volumes exist.
- No additional scoring logic is allowed.
- The LLM must not suggest or add “useful” scoring volumes.

---

## 5. Prohibited Behaviors (Hard Constraints)

The LLM must **never**:

- infer missing geometry
- infer parent volumes
- add support or containment volumes
- adjust positions to avoid overlaps
- add rotations for convenience
- normalize direction vectors in the IR
- add scoring volumes
- introduce new IR fields
- repair or complete incomplete examples
- merge or simplify causal examples

Violating any of the above breaks the system contract.

---

## 6. Causal Example Integrity

Examples are part of a **causal dataset**.

- An example may intentionally:
  - modify only one section
  - rely on implicit stable context
  - be incomplete
- This is **intentional and correct**.

The LLM must preserve:
- one-change-at-a-time causality
- clarity of cause → effect
- minimal variation

The LLM must not “clean up” or “improve” examples.

---

## 7. Role of This Document

This file is:
- a **normative contract**
- equivalent in authority to canonical IR examples
- stable by design

It is **not**:
- a tutorial
- a Geant4 explanation
- a justification of design choices

The LLM must follow these rules **exactly**.
