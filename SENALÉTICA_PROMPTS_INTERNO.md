# Toscal Garden — sistema de señalética y prompts de muestra

Documento interno de Green Digital. Sirve para generar propuestas visuales y montajes de venta. **No es un documento de producción ni contiene artes finales.** Antes de fabricar: visita, medidas, soportes, materiales, iluminación, normativa, flujos reales y traducciones.

## Objetivo

Construir un sistema que haga tres cosas a la vez:

1. Orientar sin esfuerzo en un garden de gran escala.
2. Reforzar a Toscal como garden mediterráneo experto, cálido y profesional.
3. Convertir los puntos de contacto (entrada, secciones, cajas y salida) en una experiencia coherente.

La muestra comercial debe enseñar **pocas piezas bien elegidas**: acceso, una direccional, un rótulo de zona, servicio y cajas. El inventario completo queda como hoja de ruta interna.

## Identidad común

### Paleta

| Uso | Color | Hex |
| --- | --- | --- |
| Fondo / estructura principal | Verde Toscal | `#173B30` |
| Fondo cálido / soporte secundario | Crema | `#F9F6EF` |
| Material / base | Arena | `#E8DDCD` |
| Acabado o llamada puntual | Terracota | `#B75B3D` |
| Texto secundario | Verde musgo | `#496355` |

### Tipografía y tono

- Titulares y nombres de sección: serif editorial cálida, de alto contraste (referencia: Fraunces / Canela / Cormorant, elegir una licenciada para producción).
- Información funcional, distancias, flechas y pictogramas: sans muy legible (referencia: DM Sans / Inter / Avenir).
- Una idea por soporte. Nombre principal muy grande; descriptor sólo si resuelve una duda.
- Español base. Las soluciones de idioma deben ser modulares: pictograma primero y, donde sea útil, sublínea EN/NL revisada por nativos.

### Lenguaje visual

- Fondo verde mate y texto crema para las piezas principales.
- Arena o crema para interiores, servicios y señal menor.
- Terracota sólo para subrayar orientación, numeración o un detalle; nunca como fondo dominante en todo el sistema.
- Flechas consistentes y geométricas. Pictogramas de trazo simple, una sola familia.
- Evitar: fotos de stock, hojas decorativas, exceso de ilustración, estética rústica de pizarra, iconos mezclados, vinilos con mucho texto o neones.

## Jerarquía y tamaños orientativos

Estos rangos se validan in situ. No producir desde aquí.

| Familia | Uso | Tamaño visual orientativo | Lectura |
| --- | --- | --- | --- |
| A. Hito de acceso | bienvenida / identidad | 180–300 cm de ancho | desde vehículo y acceso peatonal |
| B. Direccional | bifurcaciones | 80–150 cm de ancho | 5–15 m |
| C. Zona | inicio de área | 60–120 cm de ancho | 3–10 m |
| D. Servicio | baños, parking, cajas | 25–50 cm | 1–5 m |
| E. Información | horario, normas, consulta | A3–A1 / atril | lectura próxima |

**Material a proponer, no cerrar:** panel aluminio compuesto o chapa lacada mate para exterior; vinilo de corte/impresión protegido; soporte metálico verde profundo; madera sólo como acento controlado si encaja con la ubicación. Evaluar resistencia UV, riego, viento, humedad y limpieza.

## Inventario de piezas

### Prioridad 1 — para la muestra comercial

| Código | Pieza | Mensaje base | Opciones que enseñar |
| --- | --- | --- | --- |
| A01 | Bienvenida | “Bienvenidos a Toscal Garden” | marca editorial / icono botánico / foto del garden |
| B01 | Direccional de bifurcación | Izq. Frutales · Macetas · Palmeras y árboles; recto Cañizos | flechas grandes / icono por destino / franja de color |
| C01 | Zona | “Palmeras y árboles” | sólo texto / icono palmera / foto botánica acotada |
| C02 | Zona | “Frutales” | sólo texto / icono fruto / foto botánica acotada |
| D01 | Cajas / ayuda | “¿Necesitas ayuda?” | conversacional / icono pregunta / logotipo + llamada |

### Prioridad 2 — sistema a presupuestar tras validación

| Código | Pieza | Mensaje base |
| --- | --- | --- |
| A02 | Salida | “Gracias por visitarnos” / “Hasta pronto” |
| B02 | Direccional interior | Recto: Interior; recto: Cañizos; izquierda según cruce real |
| C03 | Zona | Cañizos |
| C04 | Zona | Plantas de interior |
| C05 | Zona | Cerámica y macetas |
| C06 | Zona | Riego y ferretería |
| C07 | Zona | Floristería y decoración |
| D02 | Servicio | Baños |
| D03 | Servicio | Parking |
| D04 | Servicio | Punto de información / proyectos de jardín |
| D05 | Servicio | Carga profesional / recogida, sólo si flujo real lo requiere |
| E01 | Horario y contacto | Horario, teléfono, QR a Maps/WhatsApp |

## Prompts: carteles aislados

### Reglas comunes para todos los prompts

Usar siempre este bloque al final:

> premium Mediterranean garden centre wayfinding system, deep matte forest green #173B30, warm cream #F9F6EF, sand #E8DDCD, restrained terracotta #B75B3D accent, elegant high-contrast editorial serif paired with a clean geometric sans, minimal pictograms in one consistent line style, real retail signage proportions, no rustic chalkboard, no stock leaves, no gradients, no neon, no clutter, front elevation, production-minded layout, **no AI-generated readable text**; leave exact text areas clean for later typesetting in Canva

En la imagen generada, el texto se trata como composición/placeholder. El texto final se monta después en Canva para que sea correcto, legible y consistente.

### A01 — bienvenida / acceso

**Opción A · Marca editorial**

> front elevation of a large freestanding entrance monument sign for Toscal Garden, 240 cm wide, deep matte forest green rectangular panel on slender dark metal posts, generous cream area reserved for the authentic Toscal Garden logo, large editorial welcome heading placeholder, very small location and opening-hours placeholder below, no photograph, calm premium Mediterranean garden centre identity. [Añadir bloque común]

**Opción B · Icono botánico**

> front elevation of an entrance sign for a premium Mediterranean garden centre, 240 cm wide, warm cream panel with a deep forest green vertical band, one elegant simple palm-and-leaf line pictogram in terracotta, logo safe area, large welcome text placeholder, subtle directional arrow toward entrance, sophisticated and clear, no photograph. [Añadir bloque común]

**Opción C · Ventana fotográfica**

> front elevation of a premium garden centre entrance sign, 240 cm wide, deep forest green frame and cream typography zones, one narrow cropped photographic window showing real Mediterranean foliage texture only, logo safe area and welcome headline placeholder, highly restrained composition, no fake readable words. [Añadir bloque común]

### A02 — salida / despedida

**Opción A · Conversacional**

> front elevation of a compact exit sign for a Mediterranean garden centre, deep matte forest green panel, cream farewell headline placeholder, small terracotta arrow pointing toward exit, authentic logo safe area at bottom, warm and understated, designed to be read from a moving car. [Añadir bloque común]

**Opción B · Logo protagonista**

> front elevation of an exit monument sign, warm cream background, oversized deep green authentic logo safe area, small farewell placeholder, single line leaf icon in terracotta, refined minimal brand sign. [Añadir bloque común]

**Opción C · Foto recortada**

> front elevation of a slim landscape exit sign, dark green lower panel with cream farewell placeholder and arrow, upper strip with a cropped real photograph of lush garden foliage, quiet premium retail identity. [Añadir bloque común]

### B01 — direccional de bifurcación

Texto a componer después: `← Frutales · Macetas · Palmeras y árboles` / `Cañizos →`.

**Opción A · Flechas protagonistas**

> front elevation of a two-direction outdoor wayfinding sign for a premium Mediterranean garden centre, two stacked deep forest green blades on a slender dark metal post, oversized cream directional arrows, clear large destination text placeholders, tiny terracotta section numbers, functional, extremely legible, no logos except a small safe area. [Añadir bloque común]

**Opción B · Pictograma por destino**

> front elevation of a garden centre crossroads wayfinding sign, warm cream base panels with deep green text zones, a simple fruit icon, pot icon, tree icon and cane texture icon aligned to destinations, large arrows, controlled terracotta accent, visual hierarchy designed for a real outdoor retail environment. [Añadir bloque común]

**Opción C · Código cromático**

> front elevation of a minimal outdoor directional sign, one large deep forest green panel split by thin sand and terracotta bands that assign a quiet category code, wide cream arrow areas and clean type placeholders, no illustration, elegant contemporary garden centre wayfinding. [Añadir bloque común]

### C01 / C02 / C03 — rótulos de zona

Aplicar a: Palmeras y árboles, Frutales, Cañizos. Cambiar icono y una foto sólo si se elige la opción C.

**Opción A · Nombre puro**

> front elevation of a 100 cm wide rectangular zone marker sign for a Mediterranean garden centre, deep matte forest green background, one very large cream category name placeholder, small category number in terracotta, no image, no icon, elegant editorial serif typography layout. [Añadir bloque común]

**Opción B · Icono funcional**

> front elevation of a zone marker sign for a premium garden centre, warm cream background, large deep green category name placeholder, a single simple line pictogram at left [palm tree / fruit / bamboo cane], narrow terracotta rule, clear professional wayfinding. [Añadir bloque común]

**Opción C · Foto botánica acotada**

> front elevation of a garden centre zone sign, deep green typographic field plus one narrow vertical photographic crop of [palm fronds / citrus fruit / cane texture], cream category name placeholder, no generic stock scene, editorial and restrained. [Añadir bloque común]

### C04–C07 — zonas comerciales

Aplicar las mismas tres opciones a: Plantas de interior, Cerámica y macetas, Riego y ferretería, Floristería y decoración. Iconos permitidos: hoja interior, maceta, gota/herramienta, flor. Para estas cuatro categorías se recomienda que la opción de foto, si se usa, sea una textura mínima; no un cartel-catalogo.

### D01 — cajas / ayuda

Texto final: `¿Necesitas ayuda?` / `Pregúntanos. Estamos aquí.`

**Opción A · Conversación directa**

> front elevation of a small counter-top or wall sign for the checkout area of a premium garden centre, deep forest green base, large warm cream help-message placeholder, small terracotta question mark pictogram, subtle logo safe area, friendly but not playful. [Añadir bloque común]

**Opción B · Icono de atención**

> front elevation of a checkout assistance sign, warm cream background, one large clean line icon of a speech bubble and leaf, deep green text placeholder, terracotta accent line, calm hospitality design. [Añadir bloque común]

**Opción C · Marca como firma**

> front elevation of a small checkout sign, dark green panel, authentic logo safe area is dominant, short cream help-message placeholder below, no illustration, quiet premium wayfinding. [Añadir bloque común]

### D02 — baños

**Opción A · Pictograma estándar**

> front elevation of a compact restroom directional sign for a premium garden centre, warm cream square plaque, deep green universal restroom pictogram, small terracotta directional arrow, no wording, accessible and extremely clear. [Añadir bloque común]

**Opción B · Bilingüe modular**

> front elevation of a small garden centre restroom sign, deep forest green background, cream universal restroom pictogram and a blank small bilingual text area below, subtle terracotta dot, elegant wayfinding. [Añadir bloque común]

**Opción C · Colgante interior**

> front elevation of a hanging double-sided restroom sign for a refined garden centre, dark green edge, warm cream face, simple deep green pictogram, clean metal suspension, no fake text. [Añadir bloque común]

### D03 — parking

**Opción A · Vehículo + P**

> front elevation of a compact outdoor parking direction sign, deep forest green panel, large cream P and simple car pictogram, terracotta arrow, blank distance placeholder, real garden centre wayfinding proportions. [Añadir bloque común]

**Opción B · Profesional / carga**

> front elevation of a modular outdoor parking sign family for a garden centre, one panel for visitor parking and one panel for professional loading, same deep green and cream identity, simple vehicle and box icons, no readable generated text. [Añadir bloque común]

**Opción C · Tótem**

> front elevation of a slim vertical parking totem for a Mediterranean garden centre, cream structure with green top cap, large P pictogram, directional arrow and logo safe area, understated terracotta accent. [Añadir bloque común]

### D04 — información / proyectos de jardín

**Opción A · Servicio editorial**

> front elevation of a small service sign in a premium garden centre, deep forest green background, cream heading placeholder for garden project advice, fine terracotta rule, a discreet landscape-plan icon, logo safe area. [Añadir bloque común]

**Opción B · Icono de conversación**

> front elevation of a garden project consultation sign, warm cream panel, deep green dialogue-and-garden line pictogram, strong heading placeholder, small call-to-action placeholder, serene retail hospitality identity. [Añadir bloque común]

**Opción C · QR / cita**

> front elevation of a compact project-information plaque, deep green frame, cream blank QR-code safe zone, heading and short CTA placeholders, no generated QR code, designed for later Canva production. [Añadir bloque común]

## Prompts de montaje con IA sobre fotos reales

Estos prompts se usan **con la foto real como imagen de referencia**. El objetivo es enseñar la escala y la intención, no simular una instalación aprobada. Añadir en cada pedido: “preserve the exact architecture, plant placement, shadows, people and camera angle; edit only the described sign”.

### M01 — acceso / bienvenida

**Foto sugerida:** `fotos_toscal/WhatsApp Unknown 2026-09-24 at 11.41.45/WhatsApp Image 2026-09-23 at 19.02.01.jpeg`

> Edit this real Toscal Garden entrance photograph. Add one plausible freestanding deep matte forest-green welcome monument sign at the entrance edge, correctly scaled and naturally grounded, cream logo-safe area and text placeholders only, subtle terracotta accent. Preserve the exact building, plants, shadows, driveway and camera angle. Do not alter any architecture or make readable AI text.

### M02 — pasillo / palmeras y árboles

**Foto sugerida:** `fotos_toscal/WhatsApp Image 2026-09-23 at 19.06.13.jpeg`

> Edit this real garden-centre aisle photograph. Add one elegant hanging or post-mounted zone marker for “Palmeras y árboles” in the established Toscal wayfinding system: deep green, cream blank typography field, one simple palm pictogram, small terracotta detail. It must look naturally installed and legible at a distance. Preserve plants, aisles, roof, light and all existing objects exactly; no fake readable text.

### M03 — cruce / direccional

**Foto sugerida:** la fotografía de cruce o pasillo donde se vean varias direcciones; si no existe, usar la de acceso como prueba conceptual.

> Edit this real Toscal Garden photograph by adding a realistic two-blade directional sign on a dark metal post at the visible decision point. Use deep forest green blades, large cream arrows and blank destination text zones. Keep the scene photorealistic, structurally plausible and understated. Do not alter layout, foliage, architecture, shadows or people; do not generate readable words.

### M04 — cajas / ayuda

**Foto sugerida:** `fotos_toscal/WhatsApp Unknown 2026-09-24 at 11.41.55/WhatsApp Image 2026-09-23 at 18.36.19.jpeg`

> Edit this real checkout photograph. Add a small refined deep-green counter or wall sign near the service point, with a cream help-message placeholder, small terracotta question-mark icon and logo-safe area. It should feel useful and naturally integrated, not oversized branding. Preserve the counter, products, lighting, people and all camera details exactly; no readable AI text.

### M05 — parking / baños

Usar la foto real correspondiente cuando esté disponible. Si se hace un montaje sin foto exacta, no presentarlo al cliente como ubicación aprobada: etiquetar “aplicación conceptual”.

> Edit this real location photograph by adding a compact wayfinding plaque for [parking / restrooms] in the established Toscal system. Use universal pictogram first, deep forest green and warm cream, terracotta arrow only if direction is needed. Preserve all original scene details, scale and lighting. No generated text.

## Flujo de trabajo recomendado

1. Generar **tres carteles aislados** para A01, B01 y C01 con las variantes de arriba.
2. Elegir una de las tres direcciones, no mezclar estilos.
3. Generar cuatro montajes: acceso, pasillo, direccional y cajas.
4. Presentar como “dirección creativa y aplicaciones conceptuales”.
5. Tras aprobación: medir, definir familia final, producir arte vectorial y montar en Canva/Illustrator con texto real y logotipo oficial.

## Reglas de presentación al cliente

- No poner precios en el dossier de dirección creativa.
- No llamar “cartel final” a ninguna imagen IA.
- Etiquetar los montajes como `Aplicación conceptual` y los carteles como `Muestra de dirección`.
- Mostrar las tres variantes por familia en páginas separadas o como tira comparativa; no saturar una sola diapositiva.
- Llevar a la reunión sólo 4–6 imágenes de muestra, no el inventario completo. El inventario sirve para demostrar que el sistema tiene recorrido.
