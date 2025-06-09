import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
import markdown2

def export_to_pdf(memo_content: str) -> bytes:
    """
    Convert the memo markdown content to a PDF file using reportlab.
    """
    # Convert markdown to HTML
    html_content = markdown2.markdown(memo_content)
    
    # Create a buffer for the PDF
    buffer = io.BytesIO()
    
    # Create the PDF document
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Create styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=HexColor('#2c3e50')
    ))
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        leading=14
    ))
    
    # Create the story (content)
    story = []
    
    # Add title
    story.append(Paragraph("VC Investment Memo", styles['CustomTitle']))
    story.append(Spacer(1, 12))
    
    # Split content into paragraphs and add them
    paragraphs = html_content.split('\n')
    for para in paragraphs:
        if para.strip():
            if para.startswith('# '):
                # Handle main headers
                story.append(Paragraph(para[2:], styles['Heading1']))
            elif para.startswith('## '):
                # Handle subheaders
                story.append(Paragraph(para[3:], styles['Heading2']))
            else:
                # Handle regular paragraphs
                story.append(Paragraph(para, styles['CustomBody']))
            story.append(Spacer(1, 6))
    
    # Build the PDF
    doc.build(story)
    
    # Get the value from the buffer
    pdf_content = buffer.getvalue()
    buffer.close()
    
    return pdf_content