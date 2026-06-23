import json


class TimingEngine:

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

        total_duration = transcript[-1]["end"]

        slide_count = len(slides)

        seconds_per_slide = (
            total_duration / slide_count
        )

        timings = []

        current_time = 0

        for slide in slides:

            timings.append(
                {
                    "slide": slide["slide"],
                    "start": round(
                        current_time,
                        2
                    ),
                    "end": round(
                        current_time +
                        seconds_per_slide,
                        2
                    )
                }
            )

            current_time += seconds_per_slide

        return timings
    
    def save_timings(
        self,
        timings,
        output_file="output/timings.json"
    ):

        import json

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                timings,
                f,
                ensure_ascii=False,
                indent=4
            )

    