import streamlit as st
import os

from pipeline import run_pipeline

st.set_page_config(
    page_title="VideoForge",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Hide Streamlit UI */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Background */
.stApp {
    background:
    radial-gradient(circle at 20% 20%, rgba(255,255,255,0.7), transparent 30%),
    radial-gradient(circle at 80% 30%, rgba(220,220,220,0.4), transparent 35%),
    radial-gradient(circle at 50% 80%, rgba(255,255,255,0.6), transparent 40%),
    #F8F5EE;
}

/* Floating Stars */
.star {
    position: fixed;
    color: rgba(180,180,180,0.25);
    font-size: 20px;
    z-index: 0;
    animation: float 8s ease-in-out infinite;
}

.star1 { top: 10%; left: 12%; animation-delay: 0s; }
.star2 { top: 20%; right: 15%; animation-delay: 1s; }
.star3 { top: 65%; left: 8%; animation-delay: 2s; }
.star4 { top: 80%; right: 12%; animation-delay: 3s; }
.star5 { top: 45%; right: 5%; animation-delay: 4s; }
.star6 { top: 35%; left: 5%; animation-delay: 5s; }

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-18px); }
    100% { transform: translateY(0px); }
}

/* Hero */
.hero-title {
    text-align: center;
    font-size: 4rem;
    font-weight: 800;
    color: #2F2F2F;
    margin-top: 40px;
    letter-spacing: -2px;
}

.hero-subtitle {
    text-align: center;
    font-size: 1.2rem;
    color: #666666;
    margin-bottom: 50px;
}

/* Glass Card */
.glass-card {
    max-width: 850px;
    margin: auto;
    padding: 40px;

    background: rgba(255,255,255,0.22);

    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);

    border-radius: 32px;

    border: 1px solid rgba(255,255,255,0.4);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.08),
        inset 0 1px 0 rgba(255,255,255,0.5);
}

/* Section Labels */
.section-title {
    font-size: 1rem;
    font-weight: 600;
    color: #777;
    margin-top: 15px;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Button */
.stButton > button {

    width: 100%;
    height: 65px;

    border-radius: 20px;

    border: none;

    background:
    linear-gradient(
        135deg,
        #FFFFFF,
        #E8E3DA
    );

    color: #222;

    font-size: 18px;
    font-weight: 700;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);

    transition: all 0.3s ease;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.10);
}

/* File Uploaders */
[data-testid="stFileUploader"] {

    background:
        rgba(255,255,255,0.35);

    border-radius: 20px;

    padding: 15px;

    border:
        1px solid rgba(255,255,255,0.45);
}

/* Status Box */
.status-box {

    margin-top: 25px;

    background:
        rgba(255,255,255,0.25);

    padding: 18px;

    border-radius: 18px;

    color: #555;
}

</style>

<div class="star star1">✦</div>
<div class="star star2">✦</div>
<div class="star star3">✦</div>
<div class="star star4">✦</div>
<div class="star star5">✦</div>
<div class="star star6">✦</div>

""", unsafe_allow_html=True)

st.markdown(
    '<div class="hero-title">VideoForge</div>',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div class="hero-subtitle">
        Turn presentations and narration into fully synced YouTube videos.
    </div>
    ''',
    unsafe_allow_html=True
)



st.markdown(
    '<div class="section-title">Step 1 · Presentation</div>',
    unsafe_allow_html=True
)

pdf_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"],
    label_visibility="collapsed"
)

st.markdown(
    '<div class="section-title">Step 2 · Narration</div>',
    unsafe_allow_html=True
)

audio_file = st.file_uploader(
    "Upload MP3 / WAV",
    type=["mp3", "wav", "m4a"],
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

generate = st.button(
    "Generate Video"
)

st.markdown(
    """
    <div class="status-box">
    ● Waiting for files...
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

if generate:

    if pdf_file is None:

        st.error(
            "Please upload a PDF."
        )

    elif audio_file is None:

        st.error(
            "Please upload narration audio."
        )

    else:

        os.makedirs(
            "input",
            exist_ok=True
        )

        with open(
            "input/sample.pdf",
            "wb"
        ) as f:

            f.write(
                pdf_file.getbuffer()
            )

        with open(
            "input/narration.mp3",
            "wb"
        ) as f:

            f.write(
                audio_file.getbuffer()
            )

        status = st.empty()

        progress = st.progress(0)

        status.info(
            "Extracting slides..."
        )

        progress.progress(10)

        video_path = run_pipeline()

        progress.progress(100)

        status.success(
            "Video generated successfully!"
        )

        with open(
            video_path,
            "rb"
        ) as video_file:

            st.download_button(
                label="⬇ Download Video",
                data=video_file,
                file_name="final_video.mp4",
                mime="video/mp4"
            )
