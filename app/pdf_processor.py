from pdf2image import convert_from_path
import os


class PDFProcessor:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def convert_to_images(self, pdf_path):
        os.makedirs(self.output_dir, exist_ok=True)

        pages = convert_from_path(pdf_path)

        for i, page in enumerate(pages):
            page.save(
                f"{self.output_dir}/slide_{i+1}.png",
                "PNG"
            )

        return len(pages)