# CheckMate Validation Principles

> This document defines the philosophy, architecture, and long-term validation roadmap for CheckMate.
>
> The goal of CheckMate is to help Blender artists identify real project issues before rendering, exporting, or delivering a project.

---

# Validation Philosophy

## 1. Report Problems, Not Information

CheckMate reports issues that require attention, not project statistics.

## 2. Respect Normal Blender Workflows

Never flag something that is considered normal in professional Blender projects.

## 3. Every Rule Must Earn Its Place

Before adding a validation rule, ask:

> "Would an experienced Blender artist be glad CheckMate pointed this out?"

If the answer is no, the rule should not be added.

## 4. Keep Messages Human

Validation messages should clearly explain:

- What happened
- Why it matters

## 5. One Validator, One Responsibility

Each validator should focus on one specific area of Blender.

## 6. Validators Return Data, UI Displays Data

Validators never decide icons, colors, or layout.

## 7. Build Small, Expand Carefully

Start with essential checks first.
Improve validators over time.

---

# Validator Development Roadmap

## ✅ Current Version (v1)

- ✅ Camera Validator
- ✅ Light Validator
- ✅ Material Validator
- ✅ Texture Validator
- ✅ Geometry Validator
- ✅ Animation Validator

---

## ⏳ Later Versions

- ⏳ Render Validator
- ⏳ Scene Validator
- ⏳ Collection Validator
- ⏳ Modifier Validator
- ⏳ Object Validator
- ⏳ Performance Validator
- ⏳ World Validator
- ⏳ Asset Validator

---

## 🚀 Future Releases

These validators are planned after the first stable public release.

- 🚀 Rigging Validator
- 🚀 Physics Validator
- 🚀 Simulation Validator
- 🚀 Compositor Validator
- 🚀 Geometry Nodes Validator
- 🚀 Node Group Validator
- 🚀 Export Validator
- 🚀 Pipeline Validator
- 🚀 Add-on Compatibility Validator
- 🚀 Studio Standards Validator

---

# Validator Specifications

Each validator will receive its own specification before implementation.

Example:

- Camera Validator
- Light Validator
- Material Validator
- Texture Validator

Every validator will be designed, reviewed, and implemented individually.