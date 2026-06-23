import fitz
import json
import os


class SlideTextExtractor:

    def extract(self, pdf_path):

        doc = fitz.open(pdf_path)

        slides = []

        for page_num in range(len(doc)):

            page = doc[page_num]

            text = page.get_text()

            slides.append(
                {
                    "slide": page_num + 1,
                    "text": text.strip()
                }
            )

        return slides

    def save_json(
        self,
        slides,
        output_path
    ):

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                slides,
                f,
                ensure_ascii=False,
                indent=4
            )