import os
import json

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from app.whisper_processor import WhisperProcessor
from app.pdf_processor import PDFProcessor
from app.slide_normalizer import SlideNormalizer
from app.video_generator import VideoGenerator
from app.slide_text_extractor import SlideTextExtractor
from app.transcript_saver import TranscriptSaver
from app.timing_engine import TimingEngine
from app.gemini_timing_engine import GeminiTimingEngine
from app.timed_video_generator import TimedVideoGenerator


def run_pipeline():

    PDF_PATH = "input/sample.pdf"

    pdf = PDFProcessor("output/slides")
    pdf.convert_to_images(PDF_PATH)

    normalizer = SlideNormalizer()
    normalizer.normalize("output/slides")

    processor = WhisperProcessor()

    result = processor.transcribe(
        "input/narration.mp3"
    )

    saver = TranscriptSaver()

    saver.save_full(result)
    saver.save_segments(result)

    extractor = SlideTextExtractor()

    slides = extractor.extract(
        "input/sample.pdf"
    )

    extractor.save_json(
        slides,
        "output/slides.json"
    )

    engine = TimingEngine()

    timings = engine.generate_timings(
        "output/slides.json",
        "output/transcript_segments.json"
    )

    engine.save_timings(
        timings
    )


    gemini_engine = GeminiTimingEngine()

    if os.path.exists(
        "output/gemini_timings.json"
    ):

        print(
            "Using cached Gemini timings."
        )

        with open(
            "output/gemini_timings.json",
            "r",
            encoding="utf-8"
        ) as f:

            timings = json.load(f)

    else:

        assignments = (
            gemini_engine.generate_timings(
                "output/slides.json",
                "output/transcript_segments.json"
            )
        )

        timings = (
            gemini_engine
            .convert_assignments_to_timings(
                assignments,
                "output/transcript_segments.json"
            )
        )

        valid = (
            gemini_engine.validate_timings(
                timings
            )
        )

        if not valid:

            raise Exception(
                "Bad timing distribution."
            )

        with open(
            "output/gemini_timings.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                timings,
                f,
                ensure_ascii=False,
                indent=4
            )


    generator = TimedVideoGenerator()

    generator.create_video(
        slides_folder="output/slides",
        timings_file=
            "output/gemini_timings.json",
        audio_file=
            "input/narration.mp3",
        output_file=
            "output/final_video.mp4"
    )

    return "output/final_video.mp4"
