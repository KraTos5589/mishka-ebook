#!/usr/bin/env python3
import os
from PIL import Image as PILImage
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import book_data

def get_image_flowable(image_path, max_width=6.6*inch, max_height=5.4*inch):
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

def add_page_decorations(canvas, doc):
    canvas.saveState()
    # Warm cream page background
    canvas.setFillColor(colors.HexColor('#fffdf9'))
    canvas.rect(0, 0, letter[0], letter[1], fill=1, stroke=0)

    # Decorative Publisher Border Frame
    canvas.setStrokeColor(colors.HexColor('#d4b483'))
    canvas.setLineWidth(2)
    canvas.roundRect(24, 24, letter[0] - 48, letter[1] - 48, 10, fill=0, stroke=1)

    # Top Header Accent Line
    canvas.setStrokeColor(colors.HexColor('#1b6ca8'))
    canvas.setLineWidth(1.5)
    canvas.line(42, 748, letter[0] - 42, 748)

    # Footer
    canvas.setFont('Helvetica-Bold', 9.5)
    canvas.setFillColor(colors.HexColor('#8c2d19'))
    canvas.drawString(42, 34, "The Giant Adventure  •  Written & Illustrated by Mishka Pant")
    if doc.page > 1:
        canvas.drawRightString(letter[0] - 42, 34, f"Page {doc.page - 1}")
    canvas.restoreState()

def create_pdf():
    pdf_filename = "the_giant_adventure.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=48,
        rightMargin=48,
        topMargin=52,
        bottomMargin=52
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'BookTitle',
        parent=styles['Heading1'],
        fontName='Times-Bold',
        fontSize=30,
        leading=36,
        textColor=colors.HexColor('#b71c1c'),
        alignment=1,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'BookSubtitle',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=15,
        leading=20,
        textColor=colors.HexColor('#1b6ca8'),
        alignment=1,
        spaceAfter=14
    )

    page_heading_style = ParagraphStyle(
        'PageHeading',
        parent=styles['Heading2'],
        fontName='Times-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1b6ca8'),
        alignment=1,
        spaceAfter=10
    )

    story_text_style = ParagraphStyle(
        'StoryText',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=15,
        leading=22,
        textColor=colors.HexColor('#2c3e50'),
        alignment=0,
        spaceBefore=12,
        spaceAfter=8
    )

    about_heading_style = ParagraphStyle(
        'AboutHeading',
        parent=styles['Heading3'],
        fontName='Times-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#8c2d19'),
        alignment=1,
        spaceAfter=6
    )

    about_body_style = ParagraphStyle(
        'AboutBody',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=12.5,
        leading=18,
        textColor=colors.HexColor('#3b2f2f'),
        alignment=1
    )

    story = []

    # 1. Front Cover Page
    story.append(Paragraph(book_data.BOOK_TITLE, title_style))
    story.append(Paragraph(book_data.BOOK_SUBTITLE, subtitle_style))
    cover_img = get_image_flowable(book_data.FRONT_COVER_ILLUSTRATION, max_width=6.2*inch, max_height=5.8*inch)
    if cover_img:
        story.append(cover_img)
    story.append(PageBreak())

    # 2. Story Pages 1 to 13
    for page in book_data.STORY_PAGES:
        story.append(Paragraph(page["title"], page_heading_style))
        img_flow = get_image_flowable(page["illustration_file"], max_width=6.4*inch, max_height=4.7*inch)
        if img_flow:
            story.append(img_flow)
        story.append(Spacer(1, 0.15*inch))

        # Put story text in a soft storybook box
        text_para = Paragraph(page["polished_text"], story_text_style)
        box_table = Table([[text_para]], colWidths=[6.4*inch])
        box_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fdf6e9')),
            ('BOX', (0, 0), (-1, -1), 1.5, colors.HexColor('#e2c9a0')),
            ('LEFTPADDING', (0, 0), (-1, -1), 16),
            ('RIGHTPADDING', (0, 0), (-1, -1), 16),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ]))
        story.append(box_table)
        story.append(PageBreak())

    # 3. Back Cover Page with About the Book
    story.append(Paragraph("Back Cover — About the Book", page_heading_style))
    back_img = get_image_flowable(book_data.BACK_COVER_ILLUSTRATION, max_width=5.5*inch, max_height=4.6*inch)
    if back_img:
        story.append(back_img)
    story.append(Spacer(1, 0.12*inch))

    about_content = [
        [Paragraph("About the Book", about_heading_style)],
        [Paragraph(book_data.ABOUT_THE_BOOK, about_body_style)]
    ]
    about_table = Table(about_content, colWidths=[6.4*inch])
    about_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f7ecda')),
        ('BOX', (0, 0), (-1, -1), 1.5, colors.HexColor('#c8a97e')),
        ('LEFTPADDING', (0, 0), (-1, -1), 18),
        ('RIGHTPADDING', (0, 0), (-1, -1), 18),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    story.append(about_table)

    doc.build(story, onFirstPage=add_page_decorations, onLaterPages=add_page_decorations)
    print(f"Successfully generated Publisher Edition PDF: {pdf_filename}")

if __name__ == '__main__':
    create_pdf()
