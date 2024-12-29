from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.colors import CMYKColor
from reportlab.graphics.shapes import Drawing, Rect
from api import menu
from my_functions import *

# Fonty a farby
pdfmetrics.registerFont(TTFont("MyriadSB", "assets/MyriadPro-Semibold.ttf"))
pdfmetrics.registerFont(TTFont("MyriadB", "assets/MyriadPro-Bold.ttf"))
pdfmetrics.registerFont(TTFont("MyriadBlck", "assets/MyriadPro-Black.ttf"))
pdfmetrics.registerFont(TTFont("MyriadBolCon", "assets/MyriadPro-BoldCond.ttf"))
pdfmetrics.registerFont(TTFont("MyriadCond", "assets/MyriadPro-Cond.ttf"))
my_black = CMYKColor(0, 0, 0, 1)  # 100% black
my_dblue = CMYKColor(0.40, 0.19, 0, 0.64)  # Dark Blue
my_white = CMYKColor(0, 0, 0, 0)  # White

# Create canvas
c = canvas.Canvas("menu.pdf", pagesize=(595, 842), enforceColorSpace="CMYK")

# Draw the background image to cover the entire page
#c.drawImage("assets/background.png", 0, 0, width=595, height=842)

def template():
    # Draw the rectangle
    c.setFillColor(my_dblue)
    c.roundRect(134, y(222), 327, 32, 6, stroke=0, fill=1)
    c.roundRect(22, y(260), 100, 22, 4, stroke=0, fill=1)
    c.roundRect(22, y(317), 135, 22, 4, stroke=0, fill=1)
    c.roundRect(22, y(451), 215, 22, 4, stroke=0, fill=1)
    c.roundRect(22, y(769), 550, 4, 1, stroke=0, fill=1)
    c.roundRect(501, y(353.7), 71, 2, 0.5, stroke=0, fill=1)
    c.roundRect(501, y(402), 71, 2, 0.5, stroke=0, fill=1)
    c.roundRect(501, y(492), 71, 2, 0.5, stroke=0, fill=1)
    c.roundRect(501, y(546.5), 71, 2, 0.5, stroke=0, fill=1)
    c.roundRect(501, y(601.5), 71, 2, 0.5, stroke=0, fill=1)
    c.roundRect(501, y(657), 71, 2, 0.5, stroke=0, fill=1)
    c.roundRect(501, y(699), 71, 2, 0.5, stroke=0, fill=1)
    # logo a nadpisy
    c.drawImage("assets/logoLUNA.png", 167, y(94), width=232.9, height=73.9)
    c.setFillColor(my_dblue)
    c.setFont("MyriadBlck", 77)
    c.drawString(50, y(172), "DENNÉ MENU", charSpace=1.7)
    c.setFillColor(my_white)
    c.setFont("MyriadB", 17)
    c.drawString(33, y(255), "POLIEVKA", charSpace=0)
    c.drawString(33, y(312), "HLAVNÉ MENU", charSpace=-0.1)
    c.drawString(33, y(446.3), "TRVALÉ MENU - MINÚTKY", charSpace=-0.1)
    
    # oznacenie jedal
    c.setFillColor(my_black)
    c.setFont("MyriadBlck", 17)
    c.drawString(129, y(254), "P1", charSpace=0)
    c.drawString(129, y(279), "P2", charSpace=0)
    c.drawString(31.5, y(341), "1.", charSpace=0)
    c.drawString(31.5, y(390), "2.", charSpace=0)
    c.drawString(31.5, y(477.5), "3.", charSpace=0)
    c.drawString(31.5, y(532), "4.", charSpace=0)
    c.drawString(31.5, y(586.5), "5.", charSpace=0)
    c.drawString(31.5, y(641), "6.", charSpace=0)
    c.drawString(31.5, y(695), "7.", charSpace=0)
    c.setFont("MyriadBolCon", 13)
    c.drawString(175, y(254), "AL:", charSpace=0)
    c.drawString(175, y(279), "AL:", charSpace=0)
    c.drawString(49.5, y(362), "AL:", charSpace=0)
    c.drawString(49.5, y(410), "AL:", charSpace=0)
    c.drawString(49.5, y(498.5), "AL:", charSpace=0)
    c.drawString(49.5, y(552.5), "AL:", charSpace=0)
    c.drawString(49.5, y(607), "AL:", charSpace=0)
    c.drawString(49.5, y(661.5), "AL:", charSpace=0)
    c.drawString(76.5, y(695), "AL:", charSpace=0)
    c.setFont("MyriadBolCon", 11)
    c.drawString(152, y(254), "0,33 l", charSpace=-0.5)
    c.drawString(152, y(279), "0,33 l", charSpace=-0.5)
    
    # spodne texty
    c.setFillColor(my_dblue)
    c.setFont("MyriadBolCon", 16)
    c.drawRightString(567, y(312), "CENA MENU S POLIEVKOU:", charSpace=0.3)
    c.setFont("MyriadB", 17)
    c.drawCentredString(298, y(756), "Palárikova ulica 89, otváracia doba 9:00-13:30", charSpace=-0.1)
    c.drawCentredString(298, y(790), "Objednávky na rozvoz prijímame na tel.  0907 048 780 do 11:00", charSpace=-0.1)
    c.setFillColor(my_black)
    c.setFont("MyriadB", 10)
    c.drawString(245, y(447), "(čas prípravy podľa vyťaženia kuchyne, obvykle do 5 min.)", charSpace=-0.2)
    c.setFont("MyriadB", 13)
    c.drawCentredString(298, y(727), "CENA POLOVIČNEJ PORCIE JE 70%. Pri niektorých jedlách nie je polovičná porcia možná.", charSpace=-0.1)
    c.setFont("MyriadCond", 8.5)
    c.drawCentredString(298, y(807), "Zoznam alergénov: 1. Obilniny obsahujúce lepok (t.j. pšenica, raž, jačmeň, ovos, špalda, kamut alebo ich hybridné odrody). 2. Kôrovce a výrobky z nich. 3. Vajcia a výrobky z nich. 4. Ryby a výrobky z nich. 5. Arašidy a výrobky z nich.", charSpace=-0.2)
    c.drawCentredString(298, y(815), "6. Sójové zrná a výrobkyz nich. 7. Mlieko a výrobky z neho.  8. Orechy, ktorými sú mandle, lieskové orechy, vlašské orechy, kešu, pekanové orechy, para orechy, pistácie, makadanové orechy a queenslandské orechy a výrobky z nich.", charSpace=-0.2)
    c.drawCentredString(298, y(823), "9. Zeler a výrobky z neho. 10. Horčica a výrobky z nej. 11. Sezamové semená a výrobky z nich. 12. Oxid siričitý a siričitany v koncentráciách vyšších ako 10 mg/kg alebo 10 mg/l. 13. Vlčí bôb a výrobky z neho. 14. Mäkkýše a výrobky z nich.", charSpace=-0.25)

def obsah_menu(jedlo, p): 
    # den a datum          
    c.setFillColor(my_white)
    c.setFont("MyriadB", 27)
    c.drawCentredString(298, y(215), jedlo[p][0].upper() + " " + jedlo[p][1], charSpace=-0.1)
    # polievky
    c.setFillColor(my_black)
    c.setFont("MyriadSB", 20) 
    c.drawString(216, y(254), jedlo[p][2], charSpace=-0.5)
    c.drawString(216, y(279), jedlo[p][6], charSpace=-0.5)
    # menu
    c.drawString(110, y(341), pol(jedlo[p][10], 1), charSpace=-0.25)
    c.drawString(110, y(364), pol(jedlo[p][10], 2), charSpace=-0.25)
    c.drawString(110, y(390), pol(jedlo[p][14], 1), charSpace=-0.25)
    c.drawString(110, y(413), pol(jedlo[p][14], 2), charSpace=-0.25)
    # minutky
    c.drawString(110, y(477.5), pol(jedlo[5][1], 1), charSpace=-0.25)
    c.drawString(110, y(500.5), pol(jedlo[5][1], 2), charSpace=-0.25)
    c.drawString(110, y(532), pol(jedlo[5][9], 1), charSpace=-0.25)
    c.drawString(110, y(555), pol(jedlo[5][9], 2), charSpace=-0.25)
    c.drawString(110, y(586.5), pol(jedlo[5][13], 1), charSpace=-0.25)
    c.drawString(110, y(609.5), pol(jedlo[5][13], 2), charSpace=-0.25)
    c.drawString(110, y(641), pol(jedlo[5][17], 1), charSpace=-0.25)
    c.drawString(110, y(664), pol(jedlo[5][17], 2), charSpace=-0.25)
    c.drawString(110, y(695), jedlo[5][21], charSpace=-0.25)
    # gramaz
    c.setFont("MyriadBolCon", 14)
    c.drawString(49.5, y(341), jedlo[p][12], charSpace=0)
    c.drawString(49.5, y(390), jedlo[p][16], charSpace=-0)
    c.drawString(49.5, y(477.5), jedlo[5][3], charSpace=-0)
    c.drawString(49.5, y(532), jedlo[5][11], charSpace=-0)
    c.drawString(49.5, y(586.5), jedlo[5][15], charSpace=-0)
    c.drawString(49.5, y(641), jedlo[5][19], charSpace=-0)
    c.drawString(49.5, y(695), jedlo[5][23], charSpace=-0)
    # alergeny
    c.setFont("MyriadBolCon", 12)
    c.drawString(192, y(254), jedlo[p][3], charSpace=-0.5)
    c.drawString(192, y(279), jedlo[p][7], charSpace=-0.5)
    c.drawString(66.5, y(362), jedlo[p][11], charSpace=-0.5)
    c.drawString(66.5, y(410), jedlo[p][15], charSpace=-0.5)
    c.drawString(66.5, y(498.5), jedlo[5][2], charSpace=-0.5)
    c.drawString(66.5, y(552.5), jedlo[5][10], charSpace=-0.5)
    c.drawString(66.5, y(607), jedlo[5][14], charSpace=-0.5)
    c.drawString(66.5, y(661.5), jedlo[5][18], charSpace=-0.5)
    c.drawString(91.5, y(695), jedlo[5][22], charSpace=-0.5)
    # ceny
    c.setFont("MyriadBlck", 18)
    c.drawRightString(567, y(344.5), jedlo[p][13], charSpace=0)
    c.drawRightString(567, y(393), jedlo[p][17], charSpace=0)
    c.drawRightString(567, y(483.5), jedlo[5][4], charSpace=0)
    c.drawRightString(567, y(537.5), jedlo[5][12], charSpace=0)
    c.drawRightString(567, y(592.5), jedlo[5][16], charSpace=0)
    c.drawRightString(567, y(648), jedlo[5][20], charSpace=0)
    c.drawRightString(567, y(690.5), jedlo[5][24], charSpace=0)
    
def vykresli_strany():
    for i in range(5):
        template()
        obsah_menu(menu, i)
        if i != 4:
            c.showPage()

vykresli_strany()
#! obrazky bez lepku - ak nebude 1 v alergenoch tak obrazok?
#! minúty časov ako horný index
#! bravčový a kurací
#! exe subor?

# Save the PDF
c.save()
print("AHOJ... PDF created successfully: menu.pdf")