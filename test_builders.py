import unittest
import os
import zipfile
import book_data
import build_epub
import build_pdf

class TestBuilders(unittest.TestCase):
    def test_epub_contains_publisher_illustrations_and_text(self):
        build_epub.create_epub()
        self.assertTrue(os.path.exists("the_giant_adventure.epub"))
        with zipfile.ZipFile("the_giant_adventure.epub", "r") as zf:
            names = zf.namelist()
            self.assertIn("EPUB/images/cover_illustration.png", names)
            self.assertIn("EPUB/images/back_cover_illustration.png", names)
            for page in book_data.STORY_PAGES:
                fname = os.path.basename(page["illustration_file"])
                self.assertIn(f"EPUB/images/{fname}", names)
            back_cover_html = zf.read("EPUB/back_cover.xhtml").decode("utf-8")
            self.assertIn("About the Book", back_cover_html)
            self.assertIn("What starts as a holiday flight to Singapore", back_cover_html)

    def test_pdf_builds_cleanly(self):
        build_pdf.create_pdf()
        self.assertTrue(os.path.exists("the_giant_adventure.pdf"))
        self.assertGreater(os.path.getsize("the_giant_adventure.pdf"), 1_000_000)

if __name__ == "__main__":
    unittest.main()
