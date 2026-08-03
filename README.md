# The Giant Adventure 📖

> A digital ebook adaptation of a handmade interactive storybook written and illustrated by 8-year-old **Mishka Pant**.

![Cover Preview](photos/WhatsApp%20Image%202026-07-17%20at%204.32.18%20PM.jpeg)

---

## 🌟 About the Book

* **Author & Illustrator**: Mishka Pant (Age 8)
* **Characters**: Mishka, Mira, Billy
* **Story Summary**: A grand adventure spanning Singapore, Greenland, a Desert Island, a Space Hole, Flower Island, Chocolate Island, Treasure Island, the Centre of the Earth, Cloud Castle, a Magical World, Bangalore, and Planet Earth 2!

The original physical book features handmade **lift-the-flaps**, **pull-tabs**, and an **envelope with a secret treasure map**!

---

## 📚 Ebook Formats Included

1. **[Interactive Web Ebook (`index.html`)](./index.html)**
   * Digital **lift-the-flap**, **pull-tab**, and **envelope opening** animations.
   * **Read Aloud** speech narration support.
   * Responsive storybook reader with page navigation and Table of Contents.

2. **[EPUB Ebook (`the_giant_adventure.epub`)](./the_giant_adventure.epub)**
   * EPUB3 format compatible with Apple Books, Kindle, e-readers, and tablets.

3. **[Printable PDF Ebook (`the_giant_adventure.pdf`)](./the_giant_adventure.pdf)**
   * High-resolution picture storybook formatted with headers, custom page borders, original artwork, and clean typography.

4. **[Story Transcript (`story.md`)](./story.md)**
   * Full text transcript preserving original childhood phrasing and charm.

---

## 🛠️ How to Build / Run Locally

### Requirements
- Python 3.8+
- `Pillow`, `reportlab`, `ebooklib`

### Setup & Build
```bash
# Create virtual environment & install dependencies
python3 -m venv venv
source venv/bin/activate
pip install ebooklib Pillow reportlab

# Build EPUB
python build_epub.py

# Build PDF
python build_pdf.py

# Serve Interactive Web Ebook
python -m http.server 8080
```
Open `http://localhost:8080` in your web browser to view the interactive storybook.

---

## 📜 License
Content © Mishka Pant. Code MIT License.
