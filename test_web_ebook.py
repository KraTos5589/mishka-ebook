import unittest
import os
import book_data

class TestWebEbook(unittest.TestCase):
    def test_index_html_has_publisher_illustrations_and_text(self):
        self.assertTrue(os.path.exists("index.html"))
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()

        self.assertIn(book_data.FRONT_COVER_ILLUSTRATION, html)
        self.assertIn(book_data.BACK_COVER_ILLUSTRATION, html)
        for page in book_data.STORY_PAGES:
            self.assertIn(page["illustration_file"], html)
            self.assertIn(page["polished_text"][:40], html)

        self.assertIn("About the Book", html)
        self.assertIn("What starts as a holiday flight to Singapore", html)

if __name__ == "__main__":
    unittest.main()
