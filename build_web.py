#!/usr/bin/env python3
import book_data

def create_web():
    toc_items = ['<li class="toc-item" data-page="1">🎨 Front Cover</li>']
    for page in book_data.STORY_PAGES:
        pnum = page["page_number"] + 1
        toc_items.append(f'<li class="toc-item" data-page="{pnum}">{page["title"]}</li>')
    toc_items.append('<li class="toc-item" data-page="15">❤️ Back Cover &amp; About the Book</li>')
    toc_html = "\n            ".join(toc_items)

    pages_html = []

    # Page 1: Front Cover
    pages_html.append(f'''
            <!-- PAGE 1: FRONT COVER -->
            <div id="page-1" class="page-content active">
                <h2 class="page-title">{book_data.BOOK_TITLE}</h2>
                <p style="text-align: center; font-size: 1.25rem; color: #1b6ca8; font-weight: bold; margin-bottom: 1rem;">
                    {book_data.BOOK_SUBTITLE}
                </p>
                <div class="image-gallery">
                    <div class="img-wrapper">
                        <img src="{book_data.FRONT_COVER_ILLUSTRATION}" alt="Front Cover Illustration">
                        <div class="img-label">Publisher Edition Front Cover</div>
                    </div>
                </div>
                <div class="original-drawings-section">
                    <div class="image-gallery">
                        <div class="img-wrapper">
                            <img src="{book_data.FRONT_COVER_ORIGINAL}" alt="Original Handmade Cover">
                            <div class="img-label">Mishka's Original Handmade Cover</div>
                        </div>
                    </div>
                </div>
            </div>''')

    # Pages 2 to 14: Story Pages 1 to 13
    for page in book_data.STORY_PAGES:
        div_id = f"page-{page['page_number'] + 1}"
        orig_imgs = "\n".join([
            f'''<div class="img-wrapper">
                    <img src="{photo}" alt="Original drawing for {page['title']}">
                    <div class="img-label">Mishka's Original Handmade Page</div>
                </div>'''
            for photo in page["original_photos"]
        ])
        pages_html.append(f'''
            <!-- {page['title'].upper()} -->
            <div id="{div_id}" class="page-content">
                <h2 class="page-title">{page['title']}</h2>
                <div class="image-gallery">
                    <div class="img-wrapper">
                        <img src="{page['illustration_file']}" alt="{page['title']} Illustration">
                        <div class="img-label">Publisher Illustration — {page['title']}</div>
                    </div>
                </div>
                <div class="story-bubble">
                    {page['polished_text']}
                </div>
                <div class="original-drawings-section">
                    <div class="image-gallery">
                        {orig_imgs}
                    </div>
                </div>
            </div>''')

    # Page 15: Back Cover & About the Book
    pages_html.append(f'''
            <!-- PAGE 15: BACK COVER -->
            <div id="page-15" class="page-content">
                <h2 class="page-title">THE END ❤️❤️❤️</h2>
                <p style="text-align: center; font-size: 1.2rem; color: #1b6ca8; font-weight: bold; margin-bottom: 1rem;">
                    Written by {book_data.BOOK_AUTHOR} &bull; Illustrated by {book_data.BOOK_AUTHOR}
                </p>
                <div class="image-gallery">
                    <div class="img-wrapper">
                        <img src="{book_data.BACK_COVER_ILLUSTRATION}" alt="Back Cover Illustration">
                        <div class="img-label">Publisher Edition Back Cover</div>
                    </div>
                </div>
                <div class="about-book-card">
                    <h3>About the Book</h3>
                    <p>{book_data.ABOUT_THE_BOOK}</p>
                </div>
                <div class="original-drawings-section">
                    <div class="image-gallery">
                        <div class="img-wrapper">
                            <img src="{book_data.BACK_COVER_ORIGINAL}" alt="Original Back Cover">
                            <div class="img-label">Mishka's Original Handmade Back Cover</div>
                        </div>
                    </div>
                </div>
            </div>''')

    all_pages_str = "\n".join(pages_html)

    html_doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{book_data.BOOK_TITLE} — Written &amp; Illustrated by {book_data.BOOK_AUTHOR}</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>

    <header>
        <div class="header-title">
            <h1>📖 {book_data.BOOK_TITLE}</h1>
            <p>{book_data.BOOK_SUBTITLE} — Publisher Edition</p>
        </div>
        <div class="header-actions">
            <button id="readAloudBtn" class="btn">🔊 Read Aloud</button>
            <button id="toggleOriginalsBtn" class="btn">🖼️ Compare Original Drawings</button>
            <button id="tocBtn" class="btn">📑 Contents</button>
            <a href="the_giant_adventure.pdf" download class="btn btn-primary">📥 Publisher PDF</a>
            <a href="the_giant_adventure.epub" download class="btn">📱 EPUB</a>
        </div>
    </header>

    <div id="tocDrawer" class="toc-drawer">
        <h3>Story Directory</h3>
        <ul class="toc-list">
            {toc_html}
        </ul>
    </div>

    <main class="main-container">
        <div class="nav-controls">
            <button id="prevBtn" class="nav-btn">◀ Previous</button>
            <span id="pageNumDisplay" class="page-indicator">Front Cover</span>
            <button id="nextBtn" class="nav-btn">Next ▶</button>
        </div>

        <div class="book-card">
            {all_pages_str}
        </div>
    </main>

    <footer>
        <p><strong>{book_data.BOOK_TITLE}</strong> &bull; Written &amp; Illustrated by {book_data.BOOK_AUTHOR} (Age 8)</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_doc)
    print("Successfully generated Publisher Edition index.html")

if __name__ == "__main__":
    create_web()
