from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_pdf_with_image_bg(output_pdf, image_file):
    # Register Arial font
    pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
    
    c = canvas.Canvas(output_pdf, pagesize=(595, 842))  # A4 size in points (width, height)
    
    # Draw the background image to cover the entire page
    c.drawImage(image_file, 0, 0, width=595, height=842)

    # Add new text on top of the background image
    c.setFont("Arial", 19)
    c.setFillColorRGB(0, 0, 0)  # Black color
    c.drawString(200, 500, "This is text over the image background")

    # Save the PDF
    c.save()
    print(f"PDF created successfully: {output_pdf}")

# Call the function
create_pdf_with_image_bg("output_with_image_bg.pdf", "background.png")
