import json
import os

from moviepy import (
    ImageClip,
    concatenate_videoclips,
    AudioFileClip
)


class TimedVideoGenerator:

    def create_video(
        self,
        slides_folder,
        timings_file,
        audio_file,
        output_file
    ):

        with open(
            timings_file,
            "r",
            encoding="utf-8"
        ) as f:

            timings = json.load(f)

        clips = []

        for timing in timings:

            slide_num = timing["slide"]

            duration = (
                timing["end"]
                - timing["start"]
            )

            slide_path = os.path.join(
                slides_folder,
                f"slide_{slide_num}.png"
            )

            clip = (
                ImageClip(slide_path)
                .with_duration(duration)
            )

            clips.append(clip)

        video = concatenate_videoclips(clips)

        audio = AudioFileClip(
            audio_file
        )

        video = video.with_audio(audio)

        video.write_videofile(
            output_file,
            fps=24
        )