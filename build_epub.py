#!/usr/bin/env python3
import os
from ebooklib import epub
import book_data

def create_epub():
    book = epub.EpubBook()
    book.set_identifier('mishka-pant-the-giant-adventure-publisher-2026')
    book.set_title(book_data.BOOK_TITLE)
    book.set_language('en')
    book.add_author(book_data.BOOK_AUTHOR)

    css_content = '''
    @namespace epub "http://www.idpf.org/2007/ops";
    body {
        font-family: Georgia, 'Palatino Linotype', 'Book Antiqua', serif;
        margin: 5%;
        text-align: center;
        background-color: #fffdf8;
        color: #2c3e50;
    }
    h1 {
        color: #d9381e;
        font-size: 2.3em;
        margin-bottom: 0.2em;
    }
    h2 {
        color: #1b6ca8;
        font-size: 1.6em;
        margin-top: 0.8em;
        margin-bottom: 0.5em;
    }
    p.story-text {
        font-size: 1.35em;
        line-height: 1.75;
        text-align: left;
        margin: 1.2em auto;
        background: #fdf9f0;
        padding: 18px 22px;
        border-left: 5px solid #d9381e;
        border-radius: 8px;
    }
    .page-image {
        max-width: 96%;
        height: auto;
        border: 4px solid #ebd3b6;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        margin: 12px auto;
        display: block;
    }
    .author-credit {
        font-size: 1.3em;
        color: #1b6ca8;
        font-weight: bold;
        margin-bottom: 1em;
    }
    .about-box {
        background: #f5ebd6;
        border: 2px solid #c8a97e;
        border-radius: 12px;
        padding: 20px;
        margin: 20px auto;
        text-align: left;
    }
    .about-box h3 {
        color: #8c2d19;
        text-align: center;
        margin-top: 0;
    }
    '''
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=css_content)
    book.add_item(nav_css)

    def add_image_item(file_path):
        image_name = os.path.basename(file_path)
        media_type = "image/png" if image_name.endswith(".png") else "image/jpeg"
        with open(file_path, 'rb') as f:
            img_data = f.read()
        image_item = epub.EpubItem(
            uid=image_name.replace('.', '_'),
            file_name=f"images/{image_name}",
            media_type=media_type,
            content=img_data
        )
        book.add_item(image_item)
        return f"images/{image_name}"

    # Set EPUB cover metadata
    with open(book_data.FRONT_COVER_ILLUSTRATION, 'rb') as f:
        book.set_cover('cover.png', f.read())

    # Title / Front Cover Chapter
    cover_rel = add_image_item(book_data.FRONT_COVER_ILLUSTRATION)
    cover_chapter = epub.EpubHtml(title='Front Cover', file_name='title_page.xhtml', lang='en')
    cover_chapter.content = f'''
    <div style="text-align: center;">
        <h1>{book_data.BOOK_TITLE}</h1>
        <p class="author-credit">{book_data.BOOK_SUBTITLE}</p>
        <img src="{cover_rel}" alt="Front Cover Illustration" class="page-image"/>
    </div>
    '''
    cover_chapter.add_item(nav_css)
    book.add_item(cover_chapter)
    chapters = [cover_chapter]

    # Story Pages 1 to 13
    for page in book_data.STORY_PAGES:
        idx = page["page_number"]
        filename = f"page_{idx}.xhtml"
        chapter = epub.EpubHtml(title=page["title"], file_name=filename, lang='en')
        img_rel = add_image_item(page["illustration_file"])

        chapter.content = f'''
        <div>
            <h2>{page["title"]}</h2>
            <img src="{img_rel}" alt="{page["title"]}" class="page-image"/>
            <p class="story-text">{page["polished_text"]}</p>
        </div>
        '''
        chapter.add_item(nav_css)
        book.add_item(chapter)
        chapters.append(chapter)

    # Back Cover with About the Book
    back_cover_rel = add_image_item(book_data.BACK_COVER_ILLUSTRATION)
    back_chapter = epub.EpubHtml(title='Back Cover & About the Book', file_name='back_cover.xhtml', lang='en')
    back_chapter.content = f'''
    <div>
        <h2>THE END ❤️❤️❤️</h2>
        <p class="author-credit">Written by {book_data.BOOK_AUTHOR} &bull; Illustrated by {book_data.BOOK_AUTHOR}</p>
        <img src="{back_cover_rel}" alt="Back Cover Illustration" class="page-image"/>
        <div class="about-box">
            <h3>About the Book</h3>
            <p class="story-text" style="border:none; background:transparent; padding:0; margin:0;">
                {book_data.ABOUT_THE_BOOK}
            </p>
        </div>
    </div>
    '''
    back_chapter.add_item(nav_css)
    book.add_item(back_chapter)
    chapters.append(back_chapter)

    book.toc = tuple(chapters)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ['nav'] + chapters

    output_filename = 'the_giant_adventure.epub'
    epub.write_epub(output_filename, book, {})
    print(f"Successfully generated Publisher Edition EPUB: {output_filename}")

if __name__ == '__main__':
    create_epub()
