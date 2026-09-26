import unittest
import os
from PIL import Image
import book_data

class TestIllustrations(unittest.TestCase):
    def test_all_illustrations_exist_and_valid(self):
        expected_files = [
            book_data.FRONT_COVER_ILLUSTRATION,
            book_data.BACK_COVER_ILLUSTRATION,
        ] + [p["illustration_file"] for p in book_data.STORY_PAGES]

        self.assertEqual(len(expected_files), 15)
        for img_path in expected_files:
            self.assertTrue(os.path.exists(img_path), f"Missing illustration: {img_path}")
            with Image.open(img_path) as img:
                w, h = img.size
                self.assertGreater(w, 200)
                self.assertGreater(h, 200)

if __name__ == "__main__":
    unittest.main()
