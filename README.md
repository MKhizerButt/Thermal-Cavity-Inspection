# Thermal Cavity Inspection System

An automated **Non-Destructive Testing (NDT)** solution designed for the industrial manufacturing sector to detect, localize, and quantify insulation defects within refrigerator cabinets. By combining **Active Infrared Thermography** with advanced **digital image processing**, the system provides a robust and cost-effective alternative to conventional destructive quality assurance methods.

---

## 📌 Project Overview

During refrigerator manufacturing, liquid polyurethane foam is injected between the inner cabinet and the outer housing. The foam expands rapidly and solidifies to create an airtight thermal insulation barrier that significantly improves energy efficiency.

However, air can become trapped during the injection process, forming **cavities (air pockets)** inside the insulation walls. These defects increase heat transfer, reduce thermal performance, and negatively impact the overall efficiency of the refrigerator.

### The Core Problem

Traditional quality assurance relies on **Acceptable Quality Level (AQL)** destructive testing. Typically, approximately **2.5%** of manufactured units are physically cut open and inspected.

This approach presents several drawbacks:

* Tested units become unusable and must be discarded.
* Results from a small sample are extrapolated to the entire production batch.
* If defect rates exceed acceptable limits, large quantities of otherwise functional products may be rejected.
* Significant material waste and financial losses are incurred.

### Our NDT Solution

The Thermal Cavity Inspection System eliminates the need for destructive testing by enabling **localized inspection of individual units**.

The process uses an external thermal excitation source to introduce heat into the refrigerator cabinet. Because polyurethane foam has extremely low thermal conductivity, regions containing air cavities respond differently to thermal loading and appear as localized **hot spots** on the cabinet surface.

The software automatically:

* Detects thermal anomalies.
* Segments cavity regions.
* Draws spatial bounding boxes.
* Calculates cavity dimensions and estimated physical properties.
* Generates inspection results in real time.

---

# 🛠️ System Architecture

The system combines a custom industrial hardware platform with a computer vision-based analytical software stack.

## Hardware Specifications

### Thermal Imaging Core

* **FLIR E8 Thermal Camera**
* Infrared sensor resolution: **320 × 240**
* Thermal sensitivity: **< 0.06°C**

### Compute Processing Unit

* **Raspberry Pi 3 Model B+**
* 64-bit Quad-Core ARM Processor
* Clock Frequency: **1.4 GHz**

### Thermal Excitation Load

* Custom **1500 W Radiant Heating Array**
* Consists of:

  * 3 × 500 W Halogen Heating Rods
* Provides uniform contactless thermal stimulation

### Enclosure Assembly

Custom **Cavity Detection and Localization Box (CDLB)** featuring:

* Industrial Run Button
* Emergency Shutdown Button
* VGA Connectivity
* Power Management Interface

---

## Software Processing Pipeline

### 1. Color Space Translation

Thermal images are converted from RGB format into the **HSV (Hue, Saturation, Value)** color space to isolate thermal information while minimizing the effects of illumination variations.

### 2. Dynamic Masking Matrix

Multi-stage `cv2.inRange()` filtering is applied to segment thermal regions corresponding to elevated temperatures, particularly:

* High-saturation reds
* Bright white thermal zones

### 3. Contour Extraction

OpenCV contour tracing is used to identify and isolate the boundaries of detected hot spots.

### 4. Spatial Moments Evaluation

Image moments are computed to determine:

* Geometric centroids
* Bounding coordinates
* Cavity area
* Relative position
* Estimated depth
* Estimated volume

These measurements provide actionable manufacturing quality metrics.

---

# 🗂️ Project Structure

```text
Thermal-Cavity-Inspection/
├── .gitignore
├── README.md
├── dataset/
│   └── test_image.jpg
├── icons/
│   ├── logo.jpg
│   ├── logo_dark.jpg
│   ├── open.jpg
│   └── run.jpg
└── src/
    ├── app.py
    └── processing.py
```

### Directory Description

| File / Folder       | Description                                          |
| ------------------- | ---------------------------------------------------- |
| `.gitignore`        | Excludes temporary build artifacts and editor files  |
| `README.md`         | Project documentation                                |
| `dataset/`          | Sample thermal images for testing                    |
| `icons/`            | GUI assets and application icons                     |
| `src/app.py`        | Main Tkinter application and GUI engine              |
| `src/processing.py` | Core computer vision and thermal analysis algorithms |

---

# 💻 Installation

## Prerequisites

* Python 3.8+
* Raspberry Pi OS, Ubuntu, Windows, or macOS

## Clone Repository

```bash
git clone https://github.com/MKhizerButt/Thermal-Cavity-Inspection.git
cd Thermal-Cavity-Inspection
```

## Install Dependencies

```bash
pip install opencv-python numpy pillow
```

### Dependencies

* OpenCV
* NumPy
* Pillow
* Tkinter (included with standard Python installations)

---

# 🚀 Execution

Launch the desktop application by running:

```bash
python src/app.py
```

---

# ✨ Application Features

### 🎨 Dual Theme Engine

* Light Mode
* Dark Mode
* Dynamic switching during runtime

### 📷 Live Camera Integration

* Webcam support
* Real-time thermal image acquisition
* Direct hardware connectivity

### 🔍 Automated Cavity Detection

* Hot-spot segmentation
* Thermal anomaly localization
* Automatic cavity bounding

### 📊 Diagnostic Analysis

* Area estimation
* Coordinate extraction
* Depth estimation
* Volume estimation

### ⚡ Real-Time Processing

* Immediate inspection feedback
* Rapid defect identification
* Manufacturing-ready workflow

---

# 📬 Contact

**M. Khizer Butt**

* LinkedIn: https://linkedin.com/in/mkhizerbutt
* GitHub: https://github.com/MKhizerButt
