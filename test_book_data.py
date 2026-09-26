import unittest
import os

class TestBookData(unittest.TestCase):
    def test_book_metadata_and_pages(self):
        import book_data
        self.assertEqual(book_data.BOOK_TITLE, "The Giant Adventure")
        self.assertEqual(book_data.BOOK_AUTHOR, "Mishka Pant")
        self.assertTrue(len(book_data.ABOUT_THE_BOOK) > 100)
        self.assertEqual(len(book_data.STORY_PAGES), 13)
        for idx, page in enumerate(book_data.STORY_PAGES, 1):
            self.assertEqual(page["page_number"], idx)
            self.assertIn("title", page)
            self.assertIn("polished_text", page)
            self.assertIn("original_text", page)
            self.assertIn("illustration_file", page)
            self.assertIn("original_photos", page)
            self.assertTrue(len(page["polished_text"]) > 20)

    def test_story_md_contains_about_the_book(self):
        self.assertTrue(os.path.exists("story.md"))
        with open("story.md", "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("## About the Book", content)
        self.assertIn("My friends Mira, Billy, and I always go somewhere for the holidays.", content)
        self.assertIn("Where will we go next? Canada or the USA?", content)

if __name__ == "__main__":
    unittest.main()
