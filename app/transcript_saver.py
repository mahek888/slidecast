import json
import os


class TranscriptSaver:

    def save_full(
        self,
        result,
        output_file="output/transcript.json"
    ):

        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                result,
                f,
                ensure_ascii=False,
                indent=4
            )

    def save_segments(
        self,
        result,
        output_file="output/transcript_segments.json"
    ):

        segments = []

        for segment in result["segments"]:

            segments.append(
                {
                    "start": segment["start"],
                    "end": segment["end"],
                    "text": segment["text"]
                }
            )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                segments,
                f,
                ensure_ascii=False,
                indent=4
            )