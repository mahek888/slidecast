from PIL import Image
import os


TARGET_SIZE = (1920, 1080)


class SlideNormalizer:
    def normalize(self, slides_folder):

        for file in os.listdir(slides_folder):

            if not file.endswith(".png"):
                continue

            path = os.path.join(
                slides_folder,
                file
            )

            img = Image.open(path)

            img = img.resize(
                TARGET_SIZE,
                Image.Resampling.LANCZOS
            )

            img.save(path)