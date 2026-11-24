# 🦷 CBCT Sinus AI Analyzer

A Streamlit web application that processes CBCT (Cone Beam Computed Tomography) scans of the maxillofacial region, segments the maxillary sinuses using a 3D AI model, calculates sinus volumes and anatomical measurements, and predicts gender based on sinus volume — an approach explored in forensic and anthropological research.

## Features

- **Two Input Modes:** Upload a raw DICOM folder or a pre-converted NRRD volume.
- **DICOM to NRRD Conversion:** Convert raw DICOM scan folders into NRRD format.
- **3D AI Segmentation:** Automatically segment the left and right maxillary sinuses.
- **Sinus Metrics:** Calculate individual left and right sinus volumes and other measurements.
- **Gender Prediction:** Rule-based gender estimation using total sinus volume.
- **Interactive Visualization:** Explore CBCT slices with corresponding segmentation overlays.
- **Patient Report Export:** Generate NRRD segmentation volumes, preview images, and Excel (`.xlsx`) reports containing measurements and predicted gender.

## Project Structure

```text
.
├── app.py                     # Streamlit application entry point
├── core/
│   ├── dicom_to_nrrd.py        # DICOM series → NRRD conversion
│   ├── segment.py              # 3D AI sinus segmentation
│   ├── metrics.py              # Left/right sinus measurement calculations
│   ├── visualize.py             # Slice-by-slice visualization
│   ├── export.py                # Save volumes, preview image, Excel report
│   └── gender_prediction.py    # Rule-based gender prediction
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Pratham-K-890/sinus-ai-segmentation.git
cd sinus-ai-segmentation
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

**Dependencies:** `streamlit`, `SimpleITK`, `numpy`, `scipy`, `tensorflow`, `pynrrd`, `matplotlib`.

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

1. Choose an input type — **Upload DICOM Folder** or **Upload NRRD File**.
2. Upload your CBCT scan data.
3. Click **🚀 Run AI** to perform segmentation, metric calculation, and gender prediction.
4. Review the left and right sinus measurements, predicted gender, and slice visualizations.
5. Download the generated Excel report from the **💾 Saving Patient Report** section.

## Output

Results for each processed case are saved under `results/<case_name>/`, including:

- Left and right segmented sinus volumes.
- Segmentation preview image.
- Excel (`.xlsx`) report containing anatomical measurements and predicted gender.

## Disclaimer

This tool is intended for **research and educational purposes only**. It is not a certified diagnostic or forensic tool and should not be used for clinical diagnosis, treatment, or legal decision-making.

## License

No license has been specified yet. Add a license of your choice (e.g., MIT) if you intend to share or accept contributions to this project.
