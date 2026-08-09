# CheckMate

A Blender add-on for validating Blender projects before rendering, exporting, or delivery.

CheckMate scans the current Blender project, identifies common issues, calculates a project health score, and provides recommendations to help users review their project before the final render or export.

---

## About

CheckMate is designed to help Blender artists identify common project issues before rendering, exporting, or sharing their work.

It provides a simple validation workflow directly inside Blender, with results organized by severity:

- **ERROR** — Important issues that should be addressed.
- **WARNING** — Potential issues that should be reviewed.
- **INFO** — Useful project information that does not affect the health score.

CheckMate is designed to complement normal Blender workflows rather than enforce a specific way of working.

---

## Features

### Project Health

- Project Health Score
- Project Readiness Status
- Issue Summary

### Validation

#### Errors

- Missing Active Camera
- Missing Texture File

#### Warnings

- Object Has No Material
- Empty Material Slot
- Non-Manifold Geometry
- Output Path Not Configured
- Unapplied Rotation
- Unapplied Scale

#### Information

- Unused Material
- Unused Image

### Recommendations

CheckMate provides recommendations for issues that can be addressed and groups repeated recommendations when multiple objects are affected.

### Validation Results

- Severity-based validation results
- Grouped results
- Expandable result details
- Expandable recommendations

---

## Requirements

- Blender 4.0 or newer

---

## Installation

See [INSTALLATION.md](INSTALLATION.md) for installation instructions.

---

## User Guide

See [USER_GUIDE.md](USER_GUIDE.md) for information about using CheckMate and understanding its validation results.

---

## Usage

After installing and enabling CheckMate:

1. Open a Blender project.
2. Open the **3D Viewport**.
3. Open the Sidebar by pressing `N` if it is hidden.
4. Select the **CheckMate** tab.
5. Click **Run Scan**.
6. Review the Health Score and Readiness Status.
7. Review the Validation Results.
8. Expand grouped results to view additional details.
9. Review the Recommendations and address issues where appropriate.

---

## Version

**CheckMate v1.0.0**

---

## Project Status

CheckMate Version 1 is the first release of the project.

The initial release focuses on providing a reliable foundation for Blender project validation with a simple and understandable workflow.

Future releases may introduce additional validation rules and workflow improvements based on user needs and testing.

---

## Development

CheckMate follows a modular architecture designed for maintainability and future expansion.

The project was developed through an iterative workflow:

1. Design
2. Implement
3. Test
4. Optimize
5. Release

---

## Repository

This repository contains the source code and documentation for CheckMate.

---

## Author

**Muhammed**

AM Studio

---

© 2026 AM Studio. All rights reserved.