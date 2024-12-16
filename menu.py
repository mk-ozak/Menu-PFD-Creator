from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus.flowables import Flowable

# Custom Flowable for blue rectangle
class BlueRectangle(Flowable):
    def __init__(self, width, height):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        self.canv.setFillColor(colors.blue)
        self.canv.rect(0, 0, self.width, self.height, fill=1)

# Custom Flowable for blue line
class BlueLine(Flowable):
    def __init__(self, width, height):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def draw(self):
        self.canv.setFillColor(colors.blue)
        self.canv.rect(0, 0, self.width, self.height, fill=1)

# Create the PDF
pdf_file = "recreated_menu.pdf"

# Document setup
doc = SimpleDocTemplate(pdf_file, pagesize=A4, leftMargin=50, rightMargin=50, topMargin=30, bottomMargin=30)

# Styles
styles = getSampleStyleSheet()
style_title = ParagraphStyle("title", parent=styles["Heading1"], alignment=1, fontSize=18, spaceAfter=10)
style_subtitle = ParagraphStyle("subtitle", parent=styles["Heading2"], alignment=1, fontSize=14, spaceAfter=10)
style_menu = ParagraphStyle("menu", parent=styles["BodyText"], spaceBefore=5, spaceAfter=5)
style_bold = ParagraphStyle("bold", parent=styles["BodyText"], fontName="Helvetica-Bold")
style_note = ParagraphStyle("note", parent=styles["BodyText"], fontSize=8, textColor=colors.gray)

# Content container
content = []

# Title
content.append(Paragraph("DENNÉ MENU", style_title))
content.append(Paragraph("PONDELOK 16.12.2024", style_subtitle))
content.append(Spacer(1, 0.2*inch))

# Restaurant Info
restaurant_info = [
    [Paragraph("Palárikova ulica 89, otváracia doba 9:00-13:30", style_menu)],
    [Paragraph("Objednávky na rozvoz prijímame na tel. 0907 048 780 do 11:00", style_menu)]
]
table_info = Table(restaurant_info)
content.append(table_info)
content.append(Spacer(1, 0.2*inch))

# Add Blue Rectangle
content.append(BlueRectangle(100, 100))
content.append(Spacer(1, 0.2*inch))

# Soup and Main Dishes
content.append(Paragraph("POLIEVKA", style_bold))
soups = [
    [Paragraph("Kapustnica so zemiakmi", style_menu)],
    [Paragraph("Držžková XXL s pečivom", style_menu)],
    [Paragraph("P2: Vývar s rezancami/cestovinou", style_menu)],
]
content.append(Table(soups, colWidths=400))
content.append(Spacer(1, 0.2*inch))

# Add Blue Line
content.append(BlueLine(100, 3))
content.append(Spacer(1, 0.2*inch))

# Main Menu
content.append(Paragraph("HLAVNÉ MENU", style_bold))
main_menu = [
    [Paragraph("1. Vyprážaný hermelín, varené zemiaky, tatárska omáčka, zelenina", style_menu), "6,40 €"],
    [Paragraph("2. Vyprážaný syr, hranolky, tatárska omáčka, zelenina", style_menu), "6,40 €"],
    [Paragraph("3. Vyprážaný rezeň (bravčový alebo kurací), zemiakový šalát", style_menu), "7,50 €"],
    [Paragraph("4. Kuracie prsia na Ajvari, dusená ryža, zelenina", style_menu), "5,50 €"],
    [Paragraph("5. Panenka obalená v prošute, steaková omáčka, hranolkové dukáty, zelenina", style_menu), "7,50 €"],
    [Paragraph("6. Tortilla plnená gyros kuracím mäsom, syrom a zeleninou, dresing, ½ hranolky", style_menu), "8,20 €"]
]
table_menu = Table(main_menu, colWidths=[400, 70])
table_menu.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 0.5, colors.gray),
    ('ALIGN', (1, 0), (1, -1), 'CENTER'),
]))
content.append(table_menu)
content.append(Spacer(1, 0.3*inch))

# Allergen List
content.append(Paragraph("Zoznam alergénov", style_bold))
allergen_text = (
    "1. Obilniny obsahujúce lepok (pšenica, raž, jačmeň, ovos). 2. Kôrovce. 3. Vajcia. 4. Ryby. 5. Arašidy."
    " 6. Sója. 7. Mlieko. 8. Orechy (mandle, vlašské orechy). 9. Zeler. 10. Horčica. 11. Sezam."
    " 12. Oxid siričitý. 13. Vlčí bôb. 14. Mäkkýše."
)
content.append(Paragraph(allergen_text, style_note))

# Build the document
doc.build(content)
print(f"PDF '{pdf_file}' has been created successfully!")
