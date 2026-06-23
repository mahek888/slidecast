# Slidecast

Slidecast is an AI-powered video generation tool that converts presentation PDFs and narration audio into synchronized YouTube-ready videos.

The application automatically:

* Extracts slides from a PDF presentation
* Transcribes narration using Whisper
* Extracts slide content
* Aligns transcript segments to slides using Gemini
* Generates slide timings automatically
* Creates a synchronized MP4 video with narration

## Features

* PDF → Slide image extraction
* Whisper speech-to-text transcription
* AI-powered slide/audio alignment
* Automatic timing generation
* MP4 video rendering
* Streamlit-based user interface

## Workflow

```text
Presentation PDF
        +
Narration Audio
        ↓
Slide Extraction
        ↓
Audio Transcription
        ↓
AI Slide Alignment
        ↓
Timing Generation
        ↓
Video Rendering
        ↓
Final MP4 Video
```

## Installation (Windows)

### 1. Install Python

Download and install Python 3.12 from:

https://www.python.org/downloads/

During installation, ensure:

```text
✓ Add Python to PATH
```

is checked.

---

### 1. Clone the repo

```bash
clone <repourl>
cd repo
```

---

### 3. Install Dependencies

Open Command Prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

---

### 4. Create Environment File

Create a file named:

```text
.env
```

in the project root.

Add:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

### 5. Launch Application

Double-click:

```text
launch.bat
```

or run:

```bash
streamlit run app_ui.py
```

The application will open in your browser.

## Usage

1. Upload a presentation PDF.
2. Upload a narration audio file.
3. Click Generate Video.
4. Wait for processing to finish.
5. Download the generated MP4.

## Tech Stack

* Python
* Streamlit
* Google Gemini
* OpenAI Whisper
* MoviePy
* PyMuPDF

## Status

Current version is a working MVP.

Planned improvements:

* Script generation
* PPT generation
* YouTube upload integration
* Improved timing alignment
* Executable packaging
