from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.colors import CMYKColor
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import Drawing, Rect

 # Register font
pdfmetrics.registerFont(TTFont("MyriadSB", "assets/MyriadPro-Semibold.ttf"))
pdfmetrics.registerFont(TTFont("MyriadB", "assets/MyriadPro-Bold.ttf"))
pdfmetrics.registerFont(TTFont("MyriadBlck", "assets/MyriadPro-Black.ttf"))


my_colors = {
    "dark_blue": (40 / 100, 19 / 100, 0, 64 / 100),
    "light_blue": (30 / 100, 10 / 100, 0, 20 / 100),
}

# Create canvas with dimensions in millimeters (A4 size: 210mm x 297mm)
c = canvas.Canvas("Luna_menu.pdf", pagesize=(210 * mm, 297 * mm)) #, bottomup = 0

# Draw the background image to cover the entire page
c.drawImage("assets/background.png", 0 * mm, 0 * mm, width=210 * mm, height=297 * mm)



# Text content in an array
txt_content = ["Krko pečená na pive"]

def template():
    c.setFont("MyriadBlck", 77)
    #a = CMYKColor(40, 19, 0, 64)
    c.setFillColorCMYK(*my_colors["dark_blue"])  # Set color
    c.drawString(19.7 * mm, 234.5 * mm, "DENNÉ MENU")

    # drawing = Drawing(400, 200)
    # r1 = Rect(0, 0, 400, 200, 0, 0)
    # r1.fillColor = colors.beige
    # drawing.add(r1)

def obsah_menu(): 
    # Add new text on top of the background image
    c.setFont("MyriadSB", 19)
    c.setFillColor(CMYKColor(0, 0, 0, 100))  # Set color
    c.drawString(50 * mm, 250 * mm, txt_content[0])


    #c.showPage()
    #c.drawString(100, 700, "Krkovička pečená na pive")

    
# Call the function
template()
obsah_menu()
c.showPage()
template()
obsah_menu()

# Save the PDF
c.save()
print("AHOJ... PDF created successfully: Luna_menu.pdf")



# # Save the current state
# c.saveState()

# # Translate so that we can flip the Y-axis
# c.translate(0, 297*mm)

# # Scale with a negative factor along Y to flip it
# c.scale(1, -1)

# # Now draw the image at (0,0) in this transformed space
# # The image will appear correctly oriented on the final page
# c.drawImage("assets/background.png", 0, 0, width=210*mm, height=297*mm)

# # Restore the state to normal (so other content isn't flipped)
# c.restoreState()