# CheckMate Installation Guide

This guide explains how to install CheckMate v1.0.0 in Blender.

---

## Requirements

- Blender 4.0 or newer
- CheckMate v1.0.0 ZIP package

---

## Installation

### 1. Download CheckMate

Download the CheckMate v1.0.0 ZIP package.

Do not extract the ZIP file before installing it in Blender.

---

### 2. Open Blender Preferences

Open Blender and go to:

**Edit → Preferences**

---

### 3. Open the Add-ons Section

In Preferences, select:

**Add-ons**

---

### 4. Install CheckMate

Click the dropdown arrow in the top-right corner of the Add-ons window and select:

**Install from Disk...**

Select the CheckMate ZIP file.

Then confirm the installation.

---

### 5. Enable CheckMate

After installation, search for:

**CheckMate**

Enable the CheckMate add-on using the checkbox.

---

## Opening CheckMate

After enabling the add-on:

1. Go to the **3D Viewport**.
2. Press `N` to open the Sidebar if it is hidden.
3. Select the **CheckMate** tab.

The CheckMate panel will appear in the Sidebar.

---

## Running a Scan

To scan the current Blender project:

1. Open the CheckMate panel.
2. Click **Run Scan**.
3. Wait for the scan to complete.
4. Review the Health Score.
5. Review the Readiness Status.
6. Review the Validation Results.
7. Review the Recommendations.

---

## Uninstalling CheckMate

To remove CheckMate:

1. Open **Edit → Preferences**.
2. Open **Add-ons**.
3. Search for **CheckMate**.
4. Disable the add-on.
5. Remove/uninstall CheckMate if required.

---

## Troubleshooting

### CheckMate does not appear in the Sidebar

Make sure:

- CheckMate is installed correctly.
- CheckMate is enabled in Blender Preferences.
- You are using the **3D Viewport**.
- The Sidebar is visible by pressing `N`.

### CheckMate does not appear in the Add-ons list

Make sure you selected the correct CheckMate ZIP package during installation.

Do not install an incorrectly nested or incomplete ZIP package.

### The scan shows unexpected results

Check the Blender project manually and review the corresponding Validation Result and its details.

Some project data may be intentionally unused or configured differently depending on the Blender workflow.

---

## Version

**CheckMate v1.0.0**