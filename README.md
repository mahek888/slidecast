# Slidecast (very basic + WIP)

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

## Installation (windows)

### 1. Clone the repo

```bash
git clone https://github.com/mahek888/slidecast
cd slidecast
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create Environment File

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

### 4. Launch Application

Double-click:

```text
launch.bat
```

or run:

```bash
streamlit run app_ui.py
```

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
