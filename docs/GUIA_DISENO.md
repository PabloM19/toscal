# Guía de diseño · Toscal Garden

Referencia aprobada: `prototype/index.html`, hero «Donde empieza tu lado verde», fotografía a todo el ancho. Vista de componentes y mapa: `prototype/guia-diseno.html`.

## Tipografía

Escala aplicada tras la auditoría del 15/10/2026. Fuente única: `prototype/typography.css`; entrada común: `prototype/design.css`. Los archivos de composición `site.css`, `hero.css` y `pages.css` no contienen tamaños de fuente ni abreviaturas `font`.

| Token | Tamaño estándar | Uso |
|---|---|---|
| `--text-h1` | 40-98 px, fluido | Todos los H1, Fraunces 400, interlineado 1,04-1,06 |
| `--text-h2` | 36-61 px, fluido | Todos los H2, Fraunces 400, interlineado 1,08 |
| `--text-h3` | 26-28 px | Todos los H3, Fraunces 400, interlineado 1,25 |
| `--text-lead` | 18 px | Entradilla explícita, interlineado 1,6 |
| `--text-body` | 16 px | Párrafos, listas y direcciones de contenido, interlineado 1,7 |
| `--text-control` | 16 px | Botones, enlaces de acción y campos, interlineado 1,5 |
| `--text-nav` | 16 px | Menú y categorías, interlineado 1,4 |
| `--text-small` | 14 px | Ayudas, descripciones secundarias y pie, interlineado 1,6 |
| `--text-label` | 14 px | Etiquetas, progreso y rótulos del pie, interlineado 1,5 |
| `--text-meta` | 13 px | Información auxiliar, numeración y legal, interlineado 1,5 |

- DM Sans 400 para lectura y ayudas; 500 para acciones, etiquetas y navegación.
- Tamaños en rem: equivalencias anteriores con raíz estándar de 16 px. No fijar el tamaño raíz, para respetar las preferencias del lector.
- No reducir lectura, ayudas, navegación ni controles en móvil. Ningún texto visible por debajo de 13 px en configuración estándar.
- H4/H5/H6 tienen tokens de 22/18/16 px. Cifras editoriales usan `--text-stat` de 33 px; sus leyendas, `--text-small`.
- Las clases `type-*` muestran los mismos roles en la guía. Los textos anidados heredan tamaño; evitar excepciones por elemento span, small o div.
- Los párrafos del pie y notas explícitamente secundarias usan small. Los demás párrafos de contenido usan body.
- Cursiva de Fraunces para acentos cortos; conservar el mismo tamaño y peso del titular.
- No añadir `font-size`, abreviaturas `font` o estilos inline en componentes: asignar un rol en typography.css.
- La información necesaria para elegir, contactar o rellenar un formulario nunca usa meta.

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

- `prototype/design.css`: entrada CSS común con capas de cascada.
- `prototype/typography.css`: escala única de titulares y párrafos, compartida por todas las páginas.
- `prototype/styles.css`: base heredada (reset, navegación y estructura del formulario).
- `prototype/site.css` y `prototype/site.js`: lenguaje de la home, cabecera, pie, menú accesible y apariciones.
- `prototype/hero.css`: hero aprobado de la home.
- `prototype/pages.css`: componentes editoriales de las páginas interiores y la guía.
- `prototype/proyectos.js`: formulario de proyectos.
- `scripts/sync-layout.py`: replica la cabecera y el pie de inicio en las páginas interiores, respetando su contenido.

No inventar stock, reseñas, obras realizadas, servicios ni perfiles sociales. Las fotos de las ideas de jardín se presentan como imágenes del garden, no como un portfolio de obras terminadas.
