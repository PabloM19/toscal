# Guía de diseño · Toscal Garden

Referencia aprobada: `prototype/index.html`, hero «Donde empieza tu lado verde», fotografía a todo el ancho. Vista de componentes y mapa: `prototype/guia-diseno.html`.

## Tipografía

- **Fraunces**, peso 400: titulares editoriales, cifras y nombres de colecciones. Cursiva para una frase corta de acento.
- **DM Sans**, pesos 400–600: párrafos, navegación, botones, etiquetas y formularios.
- Héroes: 64–98 px en escritorio; 40–64 px en móvil. Titulares de sección: 37–61 px. Texto de contenido: 14–16 px, interlineado 1,7–1,85.
- Cuerpo en verde oscuro o verde grisáceo; evitar párrafos centrados o titulares enteros en mayúsculas.

## Colores

| Token | Valor | Uso |
|---|---|---|
| `--ink` | `#102820` | Texto principal |
| `--green` | `#173b30` | Acciones principales y fondos oscuros |
| `--moss` | `#496355` | Texto secundario |
| `--cream` | `#f9f6ef` | Fondo principal y texto sobre fotografía |
| `--sand` | `#e8ddcd` | Franjas y acentos cálidos |
| `--terracotta` | `#b75b3d` | Cursivas, numeración y pequeños acentos |

## Composición e imagen

- Hero fotográfico a todo el ancho, sin marco. Gradiente verde para leer el texto; nunca una placa detrás del titular.
- Contenido en una columna máxima de 1320 px, con los márgenes responsive de la home.
- Ritmo de 90–110 px entre secciones en escritorio y 56–65 px en móvil.
- Fotografías propias en WebP con `srcset`, dimensiones y carga diferida fuera del hero.
- Colecciones con foto grande y texto debajo; alternar composiciones escalonadas y bloques de imagen + texto. Contornos finos y sin sombras ornamentales.

## Botones, enlaces y formularios

- Botón rectangular con radio de 2 px; verde sobre crema y crema sobre fotografía/verde. Altura mínima 50–54 px, foco visible y flecha funcional.
- Menú superior: hover y selección rectangulares, con radio de 2 px; sin cápsulas.
- Enlace de texto subrayado o con una línea inferior fina. No usar flechas en elementos que no llevan a un destino.
- Campos con etiqueta visible, borde fino, fondo claro, tipografía sans y estado de foco explícito.
- Opciones seleccionadas con borde verde y fondo suave; foco de teclado en la opción completa.
- Formulario de proyectos en cuatro pasos: espacio, medida, plazo/presupuesto, contacto. Validación del paso antes de avanzar, navegación atrás y explicación clara del envío por correo.
- Movimiento breve y discreto, desactivado con `prefers-reduced-motion`.

## Archivos comunes

- `prototype/styles.css`: base heredada (reset, navegación y estructura del formulario).
- `prototype/site.css` y `prototype/site.js`: lenguaje de la home, cabecera, pie, menú accesible y apariciones.
- `prototype/hero.css`: hero aprobado de la home.
- `prototype/pages.css`: componentes editoriales de las páginas interiores y la guía.
- `prototype/proyectos.js`: formulario de proyectos.
- `scripts/sync-layout.py`: replica la cabecera y el pie de inicio en las páginas interiores, respetando su contenido.

No inventar stock, reseñas, obras realizadas, servicios ni perfiles sociales. Las fotos de las ideas de jardín se presentan como imágenes del garden, no como un portfolio de obras terminadas.
