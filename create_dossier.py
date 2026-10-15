from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output' / 'pdf' / 'toscal-garden-propuesta.pdf'
PAGE_W, PAGE_H = landscape(A4)
M = 42
INK = HexColor('#12251F')
GREEN = HexColor('#193D31')
SAND = HexColor('#EEE6D9')
CREAM = HexColor('#FAF7F0')
TERRACOTTA = HexColor('#B85C3D')
MOSS = HexColor('#496352')
PHOTO_ENTRANCE = ROOT / 'fotos_toscal' / 'WhatsApp Unknown 2026-09-24 at 11.41.45' / 'WhatsApp Image 2026-09-23 at 19.02.01.jpeg'
PHOTO_AISLE = ROOT / 'fotos_toscal' / 'WhatsApp Image 2026-09-23 at 19.06.13.jpeg'
PHOTO_CASH = ROOT / 'fotos_toscal' / 'WhatsApp Unknown 2026-09-24 at 11.41.55' / 'WhatsApp Image 2026-09-23 at 18.36.19.jpeg'
PHOTO_PLANTS = ROOT / 'fotos_toscal' / 'WhatsApp Image 2026-09-23 at 19.06.57.jpeg'

def set_font(c, kind='regular', size=10):
    names = {'regular': 'Helvetica', 'bold': 'Helvetica-Bold', 'display': 'Times-Roman', 'displaybold': 'Times-Bold'}
    c.setFont(names[kind], size)

def text(c, x, y, value, size=10, color=INK, kind='regular'):
    c.setFillColor(color); set_font(c, kind, size)
    for index, line in enumerate(value.split('\n')):
        c.drawString(x, y - index * size * 1.05, line)

def wrapped(c, x, y, value, width, size=10, leading=None, color=INK, kind='regular'):
    if leading is None: leading = size * 1.38
    set_font(c, kind, size)
    words = value.split()
    line, lines = '', []
    for word in words:
        trial = (line + ' ' + word).strip()
        if stringWidth(trial, c._fontname, size) > width and line:
            lines.append(line); line = word
        else: line = trial
    if line: lines.append(line)
    c.setFillColor(color)
    for line in lines:
        c.drawString(x, y, line); y -= leading
    return y

def cover_image(c, path, x, y, w, h):
    with Image.open(path) as im:
        iw, ih = im.size
    scale = max(w / iw, h / ih)
    dw, dh = iw * scale, ih * scale
    dx, dy = x + (w-dw)/2, y + (h-dh)/2
    c.saveState(); p = c.beginPath(); p.rect(x, y, w, h); c.clipPath(p, stroke=0, fill=0)
    c.drawImage(str(path), dx, dy, dw, dh); c.restoreState()

def header(c, page, label='PROPUESTA DE CAPTACION'):
    c.setFillColor(CREAM); c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    text(c, M, PAGE_H-M+4, 'T  Toscal Garden', 10, INK, 'bold')
    text(c, PAGE_W-M-156, PAGE_H-M+4, label, 7.5, MOSS, 'bold')
    c.setStrokeColor(HexColor('#D3CBC0')); c.line(M, PAGE_H-M-8, PAGE_W-M, PAGE_H-M-8)
    text(c, M, 25, 'Green Digital  |  Concepto comercial - Septiembre 2026', 7.5, MOSS)
    text(c, PAGE_W-M-20, 25, f'{page:02d}', 8, INK, 'bold')

def pill(c, x, y, label, color=GREEN):
    c.setFillColor(color); c.roundRect(x,y, stringWidth(label,'Helvetica-Bold',7)+16,18,9,fill=1,stroke=0)
    text(c,x+8,y+6,label,7,white,'bold')

def label_panel(c, x, y, w, h, title, subtitle, dark=False):
    fill = GREEN if dark else SAND; fg = white if dark else INK
    c.setFillColor(fill); c.roundRect(x, y, w, h, 3, fill=1, stroke=0)
    text(c, x+15, y+h-24, title, 18, fg, 'displaybold')
    wrapped(c, x+15, y+h-45, subtitle, w-30, 8.5, 11.5, HexColor('#D9E0D9') if dark else MOSS)

def signal_mockup(c, path, x, y, w, h, title, sub, align='top'):
    cover_image(c, path, x, y, w, h)
    if align == 'top': ly = y+h-70
    elif align == 'middle': ly = y+h/2-25
    else: ly = y+18
    c.setFillColor(GREEN); c.roundRect(x+14,ly,w-28,51,4,fill=1,stroke=0)
    title_size = 14 if stringWidth(title, 'Times-Bold', 14) <= w-56 else 10.5
    text(c,x+28,ly+28,title,title_size,white,'displaybold')
    text(c,x+28,ly+13,sub,7.5,HexColor('#DDE5D8'),'bold')

def reference_mockup(c, path, x, y, w, h, title, sub):
    cover_image(c, path, x, y, w, h)
    c.setFillColor(CREAM); c.roundRect(x+12,y+h-35,104,20,3,fill=1,stroke=0)
    text(c,x+20,y+h-28,'REFERENCIA',6.5,GREEN,'bold')
    c.setFillColor(GREEN); c.roundRect(x+12,y+12,w-24,48,3,fill=1,stroke=0)
    title_size = 13 if stringWidth(title, 'Times-Bold', 13) <= w-48 else 9.5
    text(c,x+23,y+38,title,title_size,white,'displaybold')
    text(c,x+23,y+22,sub,7.2,HexColor('#DDE5D8'),'bold')

def page_cover(c):
    c.setFillColor(GREEN); c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
    cover_image(c, PHOTO_AISLE, PAGE_W*.56,0,PAGE_W*.44,PAGE_H)
    c.setFillColor(HexColor('#193D31')); c.rect(PAGE_W*.51,0,PAGE_W*.12,PAGE_H,fill=1,stroke=0)
    text(c, M, PAGE_H-72, 'GREEN DIGITAL x TOSCAL GARDEN', 8, HexColor('#CFD8C8'), 'bold')
    text(c, M, PAGE_H-148, 'Un garden que\nse vive mejor.', 44, CREAM, 'displaybold')
    wrapped(c,M,PAGE_H-247,'Prototipo web, sistema de orientacion y hoja de ruta para convertir la visita en una experiencia de marca.',330,13,18,HexColor('#E1E5DB'))
    pill(c,M,55,'XABIA  |  PROPUESTA INICIAL',TERRACOTTA)
    text(c,M,32,'Septiembre 2026',8,HexColor('#CFD8C8'))

def page_opportunity(c):
    header(c,2,'EL PUNTO DE PARTIDA')
    text(c,M,PAGE_H-100,'El valor ya existe.\nHay que hacerlo visible.',32,INK,'displaybold')
    wrapped(c,M,PAGE_H-183,'Toscal es mucho mas que un vivero: combina garden, produccion mediterranea, producto especializado y servicio de jardines. La web actual no convierte esta escala en una razon clara para visitar, consultar o contratar.',450,11,16,MOSS)
    facts=[('+30','anos de trayectoria'),('20.000 m2','de garden'),('120.000 m2','de produccion mediterranea')]
    x=M
    for n,label in facts:
        c.setStrokeColor(HexColor('#D3CBC0')); c.rect(x,111,154,76,fill=0,stroke=1)
        text(c,x+14,153,n,21,INK,'displaybold'); text(c,x+14,132,label,7.5,MOSS,'bold'); x+=166
    label_panel(c,548,205,250,121,'La oportunidad','Pasar de una web informativa a una herramienta de visita, consulta y captacion de proyectos.',True)
    audits=[('Propuesta de valor','El tamanio, la especializacion y el premio no lideran el relato.'),('Recorrido','Categorias y servicios aparecen sin una ruta de necesidad o conversion.'),('Confianza local','Contenido y testimonios visibles con fechas antiguas; falta una prueba social actual.'),('Servicios','Proyectos de jardin y asesoramiento no reciben el peso comercial que merecen.')]
    x,y=M,82
    for title,body in audits:
        text(c,x,y+17,title,9,INK,'bold'); wrapped(c,x,y+4,body,170,7.7,10.5,MOSS); x+=192

def page_web(c):
    header(c,3,'PROTOCOLO WEB')
    text(c,M,PAGE_H-98,'Una portada que empieza\npor la necesidad del cliente.',30,INK,'displaybold')
    wrapped(c,M,PAGE_H-180,'La nueva home no pide que la persona navegue por intuicion: le ayuda a elegir entre visitar, encontrar producto o crear un jardin. Cada ruta lleva a una accion concreta.',380,11,16,MOSS)
    # browser frame
    bx,by,bw,bh=448,89,347,391
    c.setFillColor(white); c.roundRect(bx,by,bw,bh,8,fill=1,stroke=0); c.setStrokeColor(HexColor('#D3CBC0')); c.roundRect(bx,by,bw,bh,8,fill=0,stroke=1)
    c.setFillColor(GREEN); c.roundRect(bx+10,by+bh-126,bw-20,112,4,fill=1,stroke=0)
    text(c,bx+23,by+bh-31,'T  Toscal Garden',7,white,'bold'); text(c,bx+23,by+bh-73,'Tu jardin empieza',22,white,'displaybold'); text(c,bx+23,by+bh-97,'mucho antes de plantarlo.',22,white,'displaybold')
    text(c,bx+22,by+bh-150,'EMPIEZA POR AQUI',6.5,MOSS,'bold')
    cards=[('01','Visitar el garden'),('02','Encontrar producto'),('03','Crear mi jardin')]
    cy=by+bh-250
    for n,label in cards:
        c.setFillColor(SAND); c.roundRect(bx+20,cy,bw-40,42,3,fill=1,stroke=0); text(c,bx+31,cy+24,n,7,TERRACOTTA,'bold'); text(c,bx+57,cy+21,label,9,INK,'displaybold'); cy-=51
    text(c,bx+22,by+24,'ES  EN  NL       XABIA',6.5,MOSS,'bold')
    notes=[('1. Capta la intencion','Una entrada directa para quien quiere comprar, resolver una necesidad o pedir proyecto.'),('2. Refuerza la autoridad','La escala, el conocimiento y la produccion se muestran como prueba, no como texto secundario.'),('3. Facilita la visita','Horario, ubicacion, WhatsApp y la ruta al garden siempre estan a un toque.')]
    y=317
    for title,body in notes:
        text(c,M,y,title,10,INK,'bold'); wrapped(c,M,y-15,body,350,8.5,11.5,MOSS); y-=73

def page_seo(c):
    header(c,4,'ARQUITECTURA DE CAPTACION')
    text(c,M,PAGE_H-98,'SEO local que acompana\nla forma real de comprar.',30,INK,'displaybold')
    wrapped(c,M,PAGE_H-180,'La web completa se construira desde preguntas locales y necesidades concretas, con versiones en espanol, ingles y neerlandes revisadas antes de publicar.',420,11,16,MOSS)
    steps=[('01','BUSQUEDA LOCAL','Garden center en Xabia / Javea, vivero, plantas, macetas y riego.'),('02','NECESIDAD','Plantas para exterior, palmeras, frutales, ceramica, floristeria y jardin.'),('03','CONVERSION','Visita, WhatsApp, consulta de disponibilidad o solicitud de proyecto.'),('04','CONFIANZA','Fotos actuales, preguntas frecuentes, resenas recientes y casos de jardin.')]
    x=M
    for n,title,body in steps:
        c.setFillColor(SAND if n in ['01','03'] else HexColor('#D9E2D7')); c.roundRect(x,112,179,216,4,fill=1,stroke=0)
        text(c,x+17,294,n,9,TERRACOTTA,'bold'); text(c,x+17,260,title,9,INK,'bold'); wrapped(c,x+17,235,body,145,9,13,MOSS); x+=190
    text(c,M,70,'Mapa de contenidos futuro',9,INK,'bold')
    text(c,M,51,'Inicio  ->  Plantas  ->  Macetas  ->  Riego y ferreteria  ->  Floristeria  ->  Proyectos de jardin  ->  Visitanos',9,MOSS)

def page_signs(c):
    header(c,5,'SISTEMA DE ORIENTACION')
    text(c,M,PAGE_H-98,'La senaletica convierte\nel orden en experiencia.',30,INK,'displaybold')
    wrapped(c,M,PAGE_H-180,'No proponemos carteles aislados. Proponemos un sistema que ayude a orientarse, recuerde la marca y deje sitio a la belleza real de las plantas.',430,11,16,MOSS)
    reference_mockup(c,PHOTO_ENTRANCE,470,251,326,183,'ACCESO E IDENTIDAD','Pieza de bienvenida por desarrollar')
    reference_mockup(c,PHOTO_AISLE,470,62,157,170,'PALMERAS','Zona prioritaria')
    reference_mockup(c,PHOTO_PLANTS,639,62,157,170,'FRUTALES','Zona prioritaria')
    rows=[('IDENTIDAD','Verde profundo, arena y terracota: sobrio, calido, mediterraneo.'),('JERARQUIA','Nombre de zona grande; descriptor pequeño; flecha solo cuando orienta.'),('MATERIALES','Propuesta visual. La produccion se define tras medir, elegir soporte y validar exterior/interior.')]
    y=243
    for title,body in rows:
        text(c,M,y,title,8,TERRACOTTA,'bold'); wrapped(c,M,y-16,body,370,9,13,MOSS); y-=63

def page_mockups(c):
    header(c,6,'APLICACIONES EN EL GARDEN')
    text(c,M,PAGE_H-98,'Tres momentos.\nUna misma voz.',30,INK,'displaybold')
    cards=[(PHOTO_ENTRANCE,'01  ACCESO','BIENVENIDOS A TOSCAL','Tu garden en Xabia'),(PHOTO_AISLE,'02  PASILLO','PALMERAS Y ARBOLES','Plantas de exterior'),(PHOTO_CASH,'03  CAJAS','¿NECESITAS AYUDA?','Estamos aqui para ayudarte a elegir')]
    x=M
    for photo,small,title,sub in cards:
        reference_mockup(c,photo,x,159,236,238,title,sub)
        text(c,x,132,small,7.5,TERRACOTTA,'bold')
        x+=250
    wrapped(c,M,94,'El siguiente nivel del sistema contempla Cañizos, Frutales, Plantas de interior, Ceramica, Riego y Ferreteria. Las imagenes funcionan como referencias de ubicacion y tono; los artes se trabajaran despues de validar la linea elegida.',710,9,13,MOSS)

def page_direction(c):
    header(c,7,'DIRECCION DE LA PROPUESTA')
    text(c,M,PAGE_H-98,'Una identidad que se\nreconoce antes de leerse.',30,INK,'displaybold')
    wrapped(c,M,PAGE_H-180,'La muestra no busca cerrar artes finales. Busca validar una voz: amable, mediterranea, clara y suficientemente flexible para convivir con la variedad real del garden.',475,11,16,MOSS)
    principles=[('01','SE LEE EN UN GOLPE','Nombre de zona o accion principal grande. La informacion secundaria solo acompana.'),('02','ORIENTA, NO DECORA','Flechas, pictogramas y color solo aparecen cuando ayudan a decidir por donde seguir.'),('03','DEJA RESPIRAR AL GARDEN','La planta y el espacio siguen siendo protagonistas. La grafica ordena sin competir.'),('04','CRECE COMO SISTEMA','Bienvenida, zonas, servicios, cajas y salida hablan el mismo idioma visual.')]
    x=M
    for n,title,body in principles:
        c.setFillColor(SAND if n in ['01','04'] else HexColor('#D9E2D7')); c.roundRect(x,112,179,216,4,fill=1,stroke=0)
        text(c,x+17,294,n,9,TERRACOTTA,'bold'); text(c,x+17,260,title,9,INK,'bold'); wrapped(c,x+17,235,body,145,9,13,MOSS); x+=190
    text(c,M,70,'Antes de producir: validar las piezas prioritarias, medir soportes, elegir materiales y revisar ubicaciones reales.',9,INK,'bold')
    text(c,M,51,'La muestra visual se utiliza como direccion creativa; no representa una especificacion definitiva de fabricacion.',9,MOSS)

def page_next(c):
    header(c,8,'SIGUIENTE PASO')
    c.setFillColor(GREEN); c.roundRect(M,105,PAGE_W-2*M,345,6,fill=1,stroke=0)
    text(c,M+35,405,'La oportunidad no es hacer una web nueva.',10,HexColor('#D9E2D7'),'bold')
    text(c,M+35,347,'Es hacer que cada visita\nal garden empiece antes.',36,CREAM,'displaybold')
    wrapped(c,M+35,249,'Validamos esta direccion, tomamos medidas de las zonas prioritarias y convertimos el prototipo en un plan de ejecucion con calendario y presupuesto final.',478,12,17,HexColor('#DDE5D8'))
    pill(c,M+35,158,'DECISION PROPUESTA: VALIDAR DIRECCION Y FASE 1',TERRACOTTA)
    text(c,M+35,124,'Fuentes: web publica de Toscal Garden y visita/fotografias facilitadas por el equipo.',7.5,HexColor('#D9E2D7'))
    text(c,M,72,'Alcance de esta primera propuesta: prototipo comercial y direccion creativa. No constituye un desarrollo publicado ni artes finales de produccion.',8,MOSS)

def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c=canvas.Canvas(str(OUT),pagesize=landscape(A4),pageCompression=1)
    for page in [page_cover,page_opportunity,page_web,page_seo,page_signs,page_mockups,page_direction,page_next]:
        page(c); c.showPage()
    c.save()
    print(OUT)

if __name__ == '__main__': build()
