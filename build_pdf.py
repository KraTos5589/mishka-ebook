#!/usr/bin/env python3
import os
from PIL import Image as PILImage
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def get_image_flowable(image_path, max_width=6.5*inch, max_height=6.0*inch):
    if not os.path.exists(image_path):
        return None
    with PILImage.open(image_path) as img:
        w, h = img.size
    
    aspect = h / float(w)
    target_w = max_width
    target_h = target_w * aspect
    
    if target_h > max_height:
        target_h = max_height
        target_w = target_h / aspect
        
    return RLImage(image_path, width=target_w, height=target_h)

def add_header_footer(canvas, doc):
    canvas.saveState()
    # Colorful Top Border Line
    canvas.setStrokeColor(colors.HexColor('#1b6ca8'))
    canvas.setLineWidth(3)
    canvas.line(36, 756, 576, 756)
    
    # Bottom Footer
    canvas.setFont('Helvetica-Bold', 10)
    canvas.setFillColor(colors.HexColor('#d9381e'))
    canvas.drawString(36, 25, "The Giant Adventure by Mishka Pant")
    canvas.drawRightString(576, 25, f"Page {doc.page}")
    canvas.restoreState()

def create_pdf():
    pdf_filename = "the_giant_adventure.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'BookTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=28,
        leading=34,
        textColor=colors.HexColor('#d9381e'),
        alignment=1, # Center
        spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        'BookSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#1b6ca8'),
        alignment=1,
        spaceAfter=15
    )
    
    page_heading_style = ParagraphStyle(
        'PageHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1b6ca8'),
        spaceAfter=8
    )
    
    note_style = ParagraphStyle(
        'InteractiveNote',
        parent=styles['Italic'],
        fontName='Helvetica-Oblique',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#e65100'),
        spaceAfter=10
    )

    story_text_style = ParagraphStyle(
        'StoryText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=14,
        leading=20,
        textColor=colors.HexColor('#2b2b2b'),
        spaceAfter=12
    )

    story = []

    # Title / Cover Page
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("The Giant Adventure", title_style))
    story.append(Paragraph("Written & Illustrated by Mishka Pant (Age 8)", subtitle_style))
    cover_img = get_image_flowable('photos/WhatsApp Image 2026-07-17 at 4.32.18 PM.jpeg', max_height=6.2*inch)
    if cover_img:
        story.append(cover_img)
    story.append(PageBreak())

    pages_data = [
        {
            "title": "Page 1: The Holiday Flight to Singapore",
            "text": "Me and My Friends Mira and billy always go somewhere in the holidays so this time we went to Singapore but the plane crashed in water everyone went on land excepte us we were stuck so we swam to an island I got some coconuts and Mira got some berries.",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (1).jpeg',
                'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (2).jpeg'
            ]
        },
        {
            "title": "Page 2: Greenland Island",
            "text": "Next we went to greenland ilssand over there we saw a bear we knew that do not eat dead people so we act to be dead.",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (3).jpeg'
            ]
        },
        {
            "title": "Page 3: Desert Island (Lift-the-Flap!)",
            "text": "Next we went to desert island in the island we saw a camel so we rode on it we even saw a volcano.",
            "note": "✨ Interactive Lift-the-Flap Page (Flap Closed & Flap Opened) ✨",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (4).jpeg',
                'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (5).jpeg'
            ]
        },
        {
            "title": "Page 4: The Space Hole",
            "text": "Then we found a hole so we went in it and we were in space! We explored new things then went back to earth.",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (6).jpeg'
            ]
        },
        {
            "title": "Page 5: Flower Island (Pull Tab!)",
            "text": "And we found ourselves on flower island we slept there for one night.",
            "note": "✨ Interactive Pull-Tab Page (Tab Closed & Tab Pulled) ✨",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (7).jpeg',
                'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (8).jpeg'
            ]
        },
        {
            "title": "Page 6: Chocolate Island",
            "text": "Then we swam to chocolate island over there we saw a candy house in the candy house we saw a chocolate man and a caramel women they gave us candy and they told us about treasure island.",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (9).jpeg'
            ]
        },
        {
            "title": "Page 7: Treasure Island & Map (Open Envelope!)",
            "text": "In the morning we went to treasure island over there we found some gold coins and a map we followed were the map told us to go and.......",
            "note": "✨ Interactive Envelope Page (Envelope Closed & Map Revealed) ✨",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.18 PM (10).jpeg',
                'photos/WhatsApp Image 2026-07-17 at 4.32.19 PM.jpeg'
            ]
        },
        {
            "title": "Page 8: Centre of the Earth",
            "text": "We reached to the centre of the earth over there we saw cave people, vikings, pirates, dinosauses and even dragons so we quikly hid behind some bushes and then walked away.",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (1).jpeg'
            ]
        },
        {
            "title": "Page 9: The Cloud Castle",
            "text": "And then...... we found a cloud castle in there we did all kinds off things and then we found a rose and on that rose it showed how to go to magical world.",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (2).jpeg'
            ]
        },
        {
            "title": "Page 10: The Magical World",
            "text": "We followed the way how to go there and we reached over there we played with gnomes, found emeralds with dwarfs, chit chated with elves, did magic with faries and even cackeled with witches",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (3).jpeg'
            ]
        },
        {
            "title": "Page 11: Flight Home to Bangalore",
            "text": "And guss what after that we had a peaceful nap on the plane and then we reached banglore.",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (4).jpeg'
            ]
        },
        {
            "title": "Page 12: Planet Earth 2 & Mysterious Unicorn",
            "text": "The next day we had to go to school and we didn't study in school we went to planet earth 2 over there was a meige and diffent school, shops, clothes, studys, homes, culture, language and tradition but the most meige and diffent thing of all was the mysteriouse unicorn it had a totaly new style, clothes, home, culture, tradition, language and colour! it was blue, green and yellow together! but the most sad thing of all was it had No friends so when we sad that you could be our friend we understud its language so we used to come to its home and sometimes it even came to ours.",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (5).jpeg',
                'photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (6).jpeg'
            ]
        },
        {
            "title": "Page 13: Where to Next?",
            "text": "That night when we came home all of us wondered in there own house were will we go next canada or USA.",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (7).jpeg'
            ]
        },
        {
            "title": "Back Cover: The End",
            "text": "THE END ❤❤❤<br/>Written by Mishka Pant<br/>Illustrated by Mishka Pant",
            "images": [
                'photos/WhatsApp Image 2026-07-17 at 4.32.19 PM (8).jpeg'
            ]
        }
    ]

    for p in pages_data:
        story.append(Paragraph(p['title'], page_heading_style))
        if 'note' in p:
            story.append(Paragraph(p['note'], note_style))
        story.append(Paragraph(p['text'], story_text_style))
        
        # Calculate available height for images
        max_h = 4.6*inch if len(p['images']) > 1 else 5.2*inch
        max_w = 3.2*inch if len(p['images']) > 1 else 6.5*inch
        
        img_flowables = [get_image_flowable(img, max_width=max_w, max_height=max_h) for img in p['images']]
        img_flowables = [f for f in img_flowables if f is not None]
        
        if len(img_flowables) == 2:
            table = Table([img_flowables], colWidths=[3.4*inch, 3.4*inch])
            table.setStyle(TableStyle([
                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ]))
            story.append(table)
        elif len(img_flowables) == 1:
            story.append(img_flowables[0])
            
        story.append(PageBreak())

    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"Successfully generated PDF file: {pdf_filename}")

if __name__ == '__main__':
    create_pdf()
