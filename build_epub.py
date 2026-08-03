#!/usr/bin/env python3
import os
from ebooklib import epub

def create_epub():
    book = epub.EpubBook()
    book.set_identifier('mishka-pant-the-giant-adventure-2026')
    book.set_title('The Giant Adventure')
    book.set_language('en')
    book.add_author('Mishka Pant')

    # Add custom CSS
    css_content = '''
    @namespace epub "http://www.idpf.org/2007/ops";
    body {
        font-family: 'Comic Sans MS', 'Chalkboard SE', 'Segoe Print', sans-serif;
        margin: 5%;
        text-align: center;
        background-color: #fffdf6;
        color: #2b2b2b;
    }
    h1 {
        color: #d9381e;
        font-size: 2.2em;
        margin-bottom: 0.2em;
    }
    h2 {
        color: #1b6ca8;
        font-size: 1.6em;
        margin-top: 1em;
    }
    p.story-text {
        font-size: 1.3em;
        line-height: 1.6;
        text-align: left;
        margin: 1.5em 0;
        background: #f7f9fa;
        padding: 15px;
        border-left: 5px solid #1b6ca8;
        border-radius: 6px;
    }
    .page-image {
        max-width: 95%;
        height: auto;
        border: 4px solid #ebd3b6;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        margin: 15px auto;
        display: block;
    }
    .interactive-note {
        font-style: italic;
        color: #e65100;
        font-weight: bold;
        margin: 10px 0;
    }
    .author-credit {
        font-size: 1.4em;
        color: #b71c1c;
        font-weight: bold;
    }
    '''
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=css_content)
    book.add_item(nav_css)

    # Helper to add image file to epub
    def add_image_item(file_path, image_name):
        with open(file_path, 'rb') as f:
            img_data = f.read()
        image_item = epub.EpubItem(
            uid=image_name,
            file_name=f"images/{image_name}",
            media_type="image/jpeg",
            content=img_data
        )
        book.add_item(image_item)
        return f"images/{image_name}"

    # Set cover image
    cover_src = 'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM.jpeg'
    with open(cover_src, 'rb') as f:
        book.set_cover('cover.jpg', f.read())

    # Create Cover Chapter
    cover_img_path = add_image_item(cover_src, 'cover_display.jpg')
    cover_chapter = epub.EpubHtml(title='Title Page', file_name='title_page.xhtml', lang='en')
    cover_chapter.content = f'''
    <div style="text-align: center;">
        <h1>The Giant Adventure</h1>
        <p class="author-credit">Written & Illustrated by Mishka Pant (Age 8)</p>
        <img src="{cover_img_path}" alt="Book Cover" class="page-image"/>
    </div>
    '''
    cover_chapter.add_item(nav_css)
    book.add_item(cover_chapter)

    chapters = [cover_chapter]

    # Pages data
    pages_data = [
        {
            "title": "Page 1: The Holiday Flight to Singapore",
            "text": "Me and My Friends Mira and billy always go somewhere in the holidays so this time we went to Singapore but the plane crashed in water everyone went on land excepte us we were stuck so we swam to an island I got some coconuts and Mira got some berries.",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (1).jpeg', 'page1_drawing.jpg'),
                ('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (2).jpeg', 'page1_handwritten.jpg')
            ]
        },
        {
            "title": "Page 2: Greenland Island",
            "text": "Next we went to greenland ilssand over there we saw a bear we knew that do not eat dead people so we act to be dead.",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (3).jpeg', 'page2_drawing.jpg')
            ]
        },
        {
            "title": "Page 3: Desert Island (Lift-the-Flap!)",
            "text": "Next we went to desert island in the island we saw a camel so we rode on it we even saw a volcano.",
            "note": "✨ Interactive Lift-the-Flap Page ✨",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (4).jpeg', 'page3_flap_closed.jpg'),
                ('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (5).jpeg', 'page3_flap_open.jpg')
            ]
        },
        {
            "title": "Page 4: The Space Hole",
            "text": "Then we found a hole so we went in it and we were in space! We explored new things then went back to earth.",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (6).jpeg', 'page4_drawing.jpg')
            ]
        },
        {
            "title": "Page 5: Flower Island (Pull Tab!)",
            "text": "And we found ourselves on flower island we slept there for one night.",
            "note": "✨ Interactive Pull-Tab Page ✨",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (7).jpeg', 'page5_tab_closed.jpg'),
                ('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (8).jpeg', 'page5_tab_pulled.jpg')
            ]
        },
        {
            "title": "Page 6: Chocolate Island",
            "text": "Then we swam to chocolate island over there we saw a candy house in the candy house we saw a chocolate man and a caramel women they gave us candy and they told us about treasure island.",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (9).jpeg', 'page6_drawing.jpg')
            ]
        },
        {
            "title": "Page 7: Treasure Island & Map (Open Envelope!)",
            "text": "In the morning we went to treasure island over there we found some gold coins and a map we followed were the map told us to go and.......",
            "note": "✨ Interactive Envelope & Map Page ✨",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (10).jpeg', 'page7_envelope_closed.jpg'),
                ('photos/WhatsApp Image 2026-07-17 at 4.32.19 PM.jpeg', 'page7_envelope_open.jpg')
            ]
        },
        {
            "title": "Page 8: Centre of the Earth",
            "text": "We reached to the centre of the earth over there we saw cave people, vikings, pirates, dinosauses and even dragons so we quikly hid behind some bushes and then walked away.",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (1).jpeg', 'page8_drawing.jpg')
            ]
        },
        {
            "title": "Page 9: The Cloud Castle",
            "text": "And then...... we found a cloud castle in there we did all kinds off things and then we found a rose and on that rose it showed how to go to magical world.",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (2).jpeg', 'page9_drawing.jpg')
            ]
        },
        {
            "title": "Page 10: The Magical World",
            "text": "We followed the way how to go there and we reached over there we played with gnomes, found emeralds with dwarfs, chit chated with elves, did magic with faries and even cackeled with witches",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (3).jpeg', 'page10_drawing.jpg')
            ]
        },
        {
            "title": "Page 11: Flight Home to Bangalore",
            "text": "And guss what after that we had a peaceful nap on the plane and then we reached banglore.",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (4).jpeg', 'page11_drawing.jpg')
            ]
        },
        {
            "title": "Page 12: Planet Earth 2 & Mysterious Unicorn",
            "text": "The next day we had to go to school and we didn't study in school we went to planet earth 2 over there was a meige and diffent school, shops, clothes, studys, homes, culture, language and tradition but the most meige and diffent thing of all was the mysteriouse unicorn it had a totaly new style, clothes, home, culture, tradition, language and colour! it was blue, green and yellow together! but the most sad thing of all was it had No friends so when we sad that you could be our friend we understud its language so we used to come to its home and sometimes it even came to ours.",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (5).jpeg', 'page12_handwritten.jpg'),
                ('photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (6).jpeg', 'page12_drawing.jpg')
            ]
        },
        {
            "title": "Page 13: Where to Next?",
            "text": "That night when we came home all of us wondered in there own house were will we go next canada or USA.",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (7).jpeg', 'page13_drawing.jpg')
            ]
        },
        {
            "title": "Back Cover: The End",
            "text": "THE END ❤❤❤<br/>Written by Mishka Pant<br/>Illustrated by Mishka Pant",
            "images": [
                ('photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (8).jpeg', 'back_cover.jpg')
            ]
        }
    ]

    for idx, page_info in enumerate(pages_data, 1):
        filename = f"page_{idx}.xhtml"
        chapter = epub.EpubHtml(title=page_info['title'], file_name=filename, lang='en')
        
        img_html = ""
        for img_src, img_dst in page_info['images']:
            img_rel_path = add_image_item(img_src, img_dst)
            img_html += f'<img src="{img_rel_path}" alt="{page_info["title"]}" class="page-image"/>'
        
        note_html = f'<p class="interactive-note">{page_info["note"]}</p>' if 'note' in page_info else ''
        
        chapter.content = f'''
        <div>
            <h2>{page_info['title']}</h2>
            {note_html}
            <p class="story-text">{page_info['text']}</p>
            {img_html}
        </div>
        '''
        chapter.add_item(nav_css)
        book.add_item(chapter)
        chapters.append(chapter)

    # Define Table of Contents & Spine
    book.toc = tuple(chapters)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ['nav'] + chapters

    # Write output
    output_filename = 'the_giant_adventure.epub'
    epub.write_epub(output_filename, book, {})
    print(f"Successfully generated EPUB file: {output_filename}")

if __name__ == '__main__':
    create_epub()
