# GLAM — Geant4 Language-Assisted Modeling

**GLAM (Geant4 Language-Assisted Modeling)** is a prototype framework that explores the use of Large Language Models (LLMs) to simplify the configuration of Geant4 simulations through natural-language instructions.

The framework translates user requests into a structured Intermediate Representation (IR), validates the generated configuration, and compiles it into Geant4-compatible C++ code using a predefined simulation backend.

The main objective is to make the configuration of Geant4 simulations more accessible while maintaining a controlled, reproducible, and structured generation process.

## Overview

Geant4 is a powerful toolkit for the simulation of particle interactions with matter. However, configuring a simulation requires knowledge of its geometry, materials, particle sources, physics processes, and scoring mechanisms.

GLAM explores an alternative approach in which users describe the desired simulation in natural language, while the framework handles the translation into a structured configuration.

Rather than allowing an LLM to generate an entire Geant4 application, GLAM constrains the generation process through an intermediate representation and a deterministic compilation pipeline.

## Architecture

The framework follows a multi-stage workflow:

```text
Natural-language request
          |
          v
     LLM API
          |
          v
 Intermediate Representation (JSON)
          |
          v
 Deterministic validation
          |
          v
   Code generation
          |
          v
 Geant4 simulation backend
          |
          v
    Simulation output
```

### 1. LLM-based generation

An external LLM is accessed through an API to translate the user's natural-language request into a structured JSON representation.

The model is instructed to follow predefined translation rules, reference information, and examples.

### 2. Intermediate Representation (IR)

The generated JSON acts as an intermediate representation between the user's request and the Geant4 implementation.

The IR describes the main components of a simulation:

- **Geometry:** volumes, primitive solids, Boolean operations, transformations, and placements.
- **Source:** particle properties, spatial distributions, positions, and emission directions.
- **Scoring:** volumes in which simulation quantities are recorded.

This representation separates the high-level simulation description from the underlying C++ implementation.

### 3. Deterministic validation

The generated IR is checked against predefined structural and semantic constraints.

The validation stage verifies that the configuration follows the expected format and that the supported simulation components are used consistently.

This step helps prevent invalid or unsupported configurations from reaching the code-generation stage.

### 4. Code generation

A deterministic compiler translates the validated IR into Geant4-compatible C++ code.

The generated code is inserted into predefined locations of an existing simulation backend, rather than replacing the entire application.

This approach preserves the existing simulation infrastructure and limits the scope of LLM-generated content.

## Features

- Natural-language interface for Geant4 simulation configuration.
- LLM-based translation into a structured JSON representation.
- Support for primitive geometries, including boxes, cylinders, spheres, and cones.
- Support for Boolean geometry operations.
- Geometry transformations and volume placement.
- Configurable particle sources, including point, disk, and spherical distributions.
- Scoring configuration for selected volumes.
- Deterministic IR validation.
- Automated generation of Geant4-compatible C++ code.
- Integration with an existing Geant4 simulation backend.
- Validation through predefined test configurations and end-to-end natural-language requests.

## Project structure

```text
GLAM/
├── backend/          # Geant4 simulation backend
├── examples/         # Reference examples and instructions
│   ├── README.md
│   ├── composed/
│   ├── geometry/
│   ├── instruction/
│   └── scoring/
├── examples_old/     # Previous examples
├── instructor.ipynb  # LLM-based IR generation
├── json_from_Gemini  # Contains the json file produced by the LLM
├── sim/              # Simulation files
├── validation_set/   # IR validation configurations
└── README.md
```

The `examples/` directory provides reference information used to guide the LLM generation process.

The `validation_set/` directory contains predefined IR configurations used to test the deterministic validation and compilation pipeline.

## Requirements

The project requires:

- Python 3
- Jupyter Notebook
- Access to a supported LLM API
- A configured Geant4 installation
- A C++ compiler compatible with the Geant4 installation
- ROOT, if required by the simulation backend

The current implementation uses Google's Gemini API for LLM-based generation.

Geant4 and its dependencies are required to compile and execute the generated simulation code.

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/GLAM.git
cd GLAM
```

### 2. Configure the LLM API

Obtain an API key from the provider and configure it in the notebook or through an environment variable.

Do not commit API keys or other credentials to the repository.

### 3. Generate a simulation configuration

Open the notebook:

```bash
jupyter notebook instructor.ipynb
```

Provide a natural-language description of the desired simulation and execute the generation workflow.

The LLM produces a JSON representation of the requested configuration.

### 4. Validate and compile the IR

The generated JSON can be passed to the validation and compilation pipeline.

The validator checks the configuration, while the compiler translates the accepted IR into the corresponding Geant4 C++ code.

### 5. Run the simulation

The generated code is integrated into the existing Geant4 backend.

The simulation can then be compiled and executed using the standard build and execution procedures of the backend.

## Validation and testing

The framework is evaluated through two complementary approaches.

**IR-based validation**

Predefined JSON configurations are used to test the deterministic validation and compilation stages independently of the LLM.

**End-to-end testing**

Natural-language requests are submitted to the LLM to evaluate the generation of IR configurations and their compatibility with the validation and compilation pipeline.

This approach allows the framework to be tested both at the individual component level and as an integrated workflow.

## Limitations

GLAM is currently a prototype and supports a limited subset of Geant4 simulation configurations.

Its main limitations include:

- The supported geometries, sources, and scoring mechanisms are restricted to the implemented IR specification.
- The quality of the generated IR depends on the LLM and the clarity of the user's request.
- The validator can detect structural and predefined semantic errors, but it cannot guarantee the physical correctness of a simulation.
- The generated code relies on an existing Geant4 backend.
- The framework does not currently support arbitrary Geant4 configurations or unrestricted C++ code generation.

The current implementation is intended as a proof of concept and a foundation for further development.

## Future work

Possible extensions include:

- Expanding the supported IR specification.
- Adding new Geant4 geometry, source, and scoring components.
- Improving validation and error reporting.
- Extending the range of supported simulation configurations.
- Developing more systematic evaluation procedures for LLM-generated IR.
- Exploring alternative LLMs and generation strategies.

## Acknowledgements

Geant4: https://geant4.web.cern.ch/

Google Gemini API: https://ai.google.dev/
