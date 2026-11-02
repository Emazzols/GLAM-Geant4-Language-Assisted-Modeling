# Geant4 Allowed Primary Particles

This document defines the complete whitelist of particle names that are allowed
as primary particles in the simulation framework.

The LLM must only use particle names listed in this file.
If a particle is not listed here, it does not exist for the system.

This list is intentionally limited to stable and commonly used particles that
are valid primary particles in standard Geant4 physics lists.

---

## Photons and Leptons

| Particle | Geant4 name | Description |
|---------|-------------|-------------|
| Gamma | gamma | Electromagnetic radiation |
| Electron | e- | Standard electron |
| Positron | e+ | Antimatter electron |
| Muon minus | mu- | Charged penetrating lepton |
| Muon plus | mu+ | Antimatter muon |

---

## Hadrons

| Particle | Geant4 name | Description |
|---------|-------------|-------------|
| Proton | proton | Positively charged baryon |
| Neutron | neutron | Neutral baryon |
| Pion plus | pi+ | Light charged meson |
| Pion minus | pi- | Light charged meson |
| Kaon plus | kaon+ | Strange meson |
| Kaon minus | kaon- | Strange meson |

---

## Light Ions

| Particle | Geant4 name | Description |
|---------|-------------|-------------|
| Alpha | alpha | Helium-4 nucleus |
| Deuteron | deuteron | Hydrogen-2 nucleus |
| Triton | triton | Hydrogen-3 nucleus |
| Helium-3 | He3 | Helium-3 nucleus |

---

## Rules

- Particle names are case-sensitive.
- Only particles listed in this file are allowed.
- The LLM must never invent or modify particle names.
- If a requested particle is not listed here, the request is invalid.
- All particles listed here can be used as primary particles.
