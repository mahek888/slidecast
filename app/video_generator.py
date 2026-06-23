import os

from moviepy import (
    ImageClip,
    concatenate_videoclips
)


class VideoGenerator:

    def create_video(
        self,
        slides_folder,
        output_file,
        duration=3
    ):

        clips = []

        slide_files = sorted(
            [
                f
                for f in os.listdir(slides_folder)
                if f.endswith(".png")
            ]
        )

        for slide in slide_files:

            path = os.path.join(
                slides_folder,
                slide
            )

            clip = (
                ImageClip(path)
                .with_duration(duration)
            )

            clips.append(clip)

        final_video = (
            concatenate_videoclips(clips)
        )

        final_video.write_videofile(
            output_file,
            fps=24
        )