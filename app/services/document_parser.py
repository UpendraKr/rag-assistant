import fitz


class PDFParser:

    def extract_pages(
        self,
        file_path: str,
    ) -> list[dict]:

        document = fitz.open(file_path)

        pages = []

        for page_number, page in enumerate(
            document,
            start=1,
        ):
            
            text = page.get_text()

            if text.strip():

                pages.append({
                    "page": page_number,
                    "text": text,
                })

        document.close()

        return pages