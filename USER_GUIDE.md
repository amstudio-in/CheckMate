# CheckMate User Guide

This guide explains how to use CheckMate v1.0.0 and understand its validation results.

---

## What is CheckMate?

CheckMate scans the current Blender project and identifies common issues that may affect rendering, exporting, or project delivery.

It also provides:

- Health Score
- Readiness Status
- Issue Summary
- Validation Results
- Recommendations

---

## Opening CheckMate

After installing and enabling CheckMate:

1. Open the **3D Viewport**.
2. Press `N` to open the Sidebar if it is hidden.
3. Select the **CheckMate** tab.

---

## Running a Scan

Click:

**Run Scan**

CheckMate will analyze the current Blender project.

After the scan finishes, the results are displayed in the CheckMate panel.

---

# Health Score

The Health Score represents the overall validation state of the project.

The score ranges from:

**0 to 100**

Errors and warnings reduce the score.

Information results do not reduce the score.

The score is intended to provide a quick overview of the project's current validation state.

---

# Readiness Status

CheckMate provides one of three readiness statuses.

### Ready

The project has no errors and has a Health Score of 90 or higher.

### Needs Review

The project has no errors, but the Health Score indicates that warnings should be reviewed.

### Not Ready

The project contains an error or has a low Health Score.

Readiness Status is a guide for reviewing the project. It does not replace the user's judgment or Blender's own rendering and export workflow.

---

# Issue Summary

The Issue Summary provides a quick count of the validation results.

It separates results into:

- Errors
- Warnings
- Information

This allows users to quickly understand what was found during the scan.

---

# Validation Results

Validation Results are grouped by severity.

## ERROR

Errors represent important issues that should normally be addressed before the project is considered ready.

### Missing Active Camera

No active camera is assigned to the current scene.

**Suggested action:** Add and assign an active camera if the project requires rendering from a scene camera.

### Missing Texture File

A file-based texture referenced by the project could not be found at its expected location.

**Suggested action:** Relink or restore the missing texture.

---

# WARNING

Warnings represent potential project problems that should be reviewed.

### Object Has No Material

A mesh object does not have any material slots.

**Suggested action:** Assign a material if the object requires one.

### Empty Material Slot

A mesh object contains a material slot without an assigned material.

**Suggested action:** Assign a material to the empty slot or remove the slot if it is not required.

### Non-Manifold Geometry

A mesh contains non-manifold geometry.

**Suggested action:** Review and fix the affected geometry if the project requires manifold topology.

### Output Path Not Configured

The render output path has not been configured.

**Suggested action:** Set the desired render output path before rendering if an explicit output location is required.

### Unapplied Rotation

A mesh object has unapplied rotation transforms.

**Suggested action:** Apply the object's rotation when appropriate for the project workflow.

### Unapplied Scale

A mesh object has unapplied scale transforms.

**Suggested action:** Apply the object's scale when appropriate for the project workflow.

---

# INFO

Information results are non-blocking observations.

They do not affect the Health Score or Readiness Status.

### Unused Material

A material datablock currently has no detected users.

This does not necessarily mean the material should be deleted. It may be intentionally kept for future use or other Blender workflows.

### Unused Image

A file-based image currently has no detected usage in the project.

This does not necessarily mean the image should be deleted. Review the image before removing it.

---

# Recommendations

CheckMate can provide recommendations for issues that can be addressed.

When multiple objects have the same issue, recommendations may be grouped together.

For example:

> Assign object transforms to 5 objects.

Expandable recommendations can be opened to view additional details.

Recommendations are intended as guidance. Users should decide whether a suggested action is appropriate for their specific Blender workflow.

---

# Expanding Results

Some validation results affect multiple objects or contain additional details.

When a result has an expand control:

1. Click the expand control.
2. Review the affected objects or details.
3. Collapse the group when finished.

The same behavior is available for grouped recommendations.

---

# Understanding Severity

CheckMate uses three severity levels:

| Severity | Meaning |
|---|---|
| **ERROR** | An important issue that should normally be addressed. |
| **WARNING** | A potential issue that should be reviewed. |
| **INFO** | Useful information that does not affect project readiness. |

---

# Blender Workflow

CheckMate is designed to complement Blender's normal workflow.

A validation result does not automatically mean that something is wrong with the artistic or technical choices in a project.

For example:

- An unused material may be intentionally stored.
- An unused image may be kept for future use.
- An unapplied transform may be intentional.
- Non-manifold geometry may be acceptable for a particular workflow.

Review the result and decide whether action is necessary.

---

# Recommended Workflow

A simple workflow for using CheckMate is:

1. Complete your Blender project.
2. Save your project.
3. Run CheckMate.
4. Review the Health Score.
5. Review Errors first.
6. Review Warnings.
7. Review Information results if cleanup is desired.
8. Follow appropriate Recommendations.
9. Run another scan after making changes.
10. Continue with rendering, exporting, or delivery when the project is ready.

---

# Version

**CheckMate v1.0.0**

---

## Author

**Muhammed**

**AM Studio**