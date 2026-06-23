import json
import os
import time


from dotenv import load_dotenv
from google import genai


class GeminiTimingEngine:

    def __init__(self):

        load_dotenv()

        self.client = genai.Client(
            api_key=os.getenv(
                "GEMINI_API_KEY"
            )
        )

    def generate_timings(
        self,
        slides_file,
        transcript_file
    ):

        with open(
            slides_file,
            "r",
            encoding="utf-8"
        ) as f:

            slides = json.load(f)

        with open(
            transcript_file,
            "r",
            encoding="utf-8"
        ) as f:

            transcript = json.load(f)

        prompt = """
You are helping synchronize presentation slides with a narration.

Slides:

""" + json.dumps(slides, ensure_ascii=False, indent=2) + """

Transcript Segments:

""" + json.dumps(transcript, ensure_ascii=False, indent=2) + """

Task:

Assign every transcript segment
to exactly one slide.

Every slide must receive at least TWO transcript segments whenever possible.

Do not assign only one segment to a slide unless it is the final slide and there are no remaining segments.

Try to distribute segments naturally across slides based on topic changes.
Return ONLY valid JSON.

Format:

[
  {
    "segment_index": 0,
    "slide": 1
  },
  {
    "segment_index": 1,
    "slide": 1
  }
]

Rules:

1. Every transcript segment must be assigned.
2. Every slide must receive at least 2 transcript segments whenever possible.
3. Slides must generally progress forward.
4. Do not skip slides.
5. Avoid creating slides shorter than 4 seconds.
6. No markdown.
7. No explanations.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    
    def convert_assignments_to_timings(
        self,
        assignments_text,
        transcript_file
    ):

        import json

        cleaned = (
            assignments_text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        assignments = json.loads(
            cleaned
        )

        with open(
            transcript_file,
            "r",
            encoding="utf-8"
        ) as f:

            transcript = json.load(f)

        slide_segments = {}

        for item in assignments:

            slide = item["slide"]
            segment_index = item["segment_index"]

            slide_segments.setdefault(
                slide,
                []
            ).append(
                segment_index
            )

        timings = []

        for slide in sorted(
            slide_segments.keys()
        ):

            segment_indices = (
                slide_segments[slide]
            )

            first_segment = (
                transcript[
                    min(segment_indices)
                ]
            )

            last_segment = (
                transcript[
                    max(segment_indices)
                ]
            )

            timings.append(
                {
                    "slide": slide,
                    "start":
                        first_segment["start"],
                    "end":
                        last_segment["end"]
                }
            )

        return timings
    
    def validate_timings(
        self,
        timings,
        min_duration=4
    ):

        for timing in timings:

            duration = (
                timing["end"]
                - timing["start"]
            )

            if duration < min_duration:

                print(
                    f"WARNING: "
                    f"Slide {timing['slide']} "
                    f"is only "
                    f"{duration:.2f}s"
                )

                return False

        return True