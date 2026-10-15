# Resultado de la auditoría tipográfica aplicada

Aplicado el 15/10/2026 a las seis páginas públicas de Toscal y a la guía interna. Se mantienen Fraunces, DM Sans, la paleta, el hero a todo el ancho y los hovers rectangulares.

## Cambios comunes

| Función | Antes | Aplicado |
|---|---|---|
| Párrafos de lectura, listas y direcciones | 12-14 px | 16 px, interlineado 1,7 |
| Menú principal y categorías | 13-15 px | 16 px |
| Botones y enlaces de acción | 11-13 px | 16 px |
| Ayudas y descripciones secundarias | 9-11,2 px | 14 px |
| Etiquetas de formulario y consentimiento | 11 px | 14 px |
| Campos de formulario | 14 px | 16 px |
| Etiquetas sobre fotos | 7-9 px | 13 px, fondo verde para contraste estable |
| Enlaces del pie | 11 px | 14 px |
| Copyright y enlaces legales | 9 px | 13 px |

Valores equivalentes con raíz estándar de 16 px. Los tamaños se definen en rem; las media queries y el menú usan em para adaptarse también a las preferencias del navegador. Los H1/H2/H3 conservan su escala común; el mínimo de H1 en móvil pasa de 37 a 40 px.

## Página a página

- **Inicio:** accesos secundarios a 14 px, etiquetas de fotos a 13 px y acciones a 16 px. Colecciones en una columna en móvil. Cifras, textos y columnas permiten crecer.
- **Plantas:** cuerpo y listas a 16 px, consultas de tarjetas a 16 px, navegación local a 14 px y etiquetas a 13 px.
- **Productos:** misma escala para macetas, riego y decoración; textos de consulta y disponibilidad ampliados.
- **Floristería:** servicios y párrafos a 16 px, acciones a 16 px y numeración auxiliar a 13 px.
- **Crear mi jardín:** ayudas y progreso a 14 px; campos y botones a 16 px; consentimiento a 14 px sin reglas !important. Opciones en una columna en móvil y cifras con columnas que se adaptan al tamaño de letra.
- **Visítanos:** horario, teléfono, WhatsApp y FAQ a 16 px; información auxiliar y ruta a 14 px.
- **Guía:** documentación actualizada y diez muestras con nombre del token, fuente, peso, tamaño e interlineado. Los ejemplos usan los mismos roles de producción.

La guía visual está en `prototype/guia-diseno.html#tipografia`. La definición y asignación de roles está en `prototype/typography.css`. `site.css`, `hero.css` y `pages.css` se ocupan de composición, sin declaraciones font-size ni abreviaturas font.

## Contraste y carga de archivos

- Se mantienen los colores de marca. Para textos pequeños terracota se usa una variante oscura `--accent-text: #97462e` (contraste calculado superior a 4,5:1 sobre crema y fondo de sección).
- Etiquetas y dos leyendas sobre fotografía usan verde sólido con texto crema para no depender de la foto.
- Las hojas CSS importadas y el script compartido llevan una revisión en su URL para evitar reutilizar versiones anteriores retenidas por el navegador.

## Comprobaciones realizadas

- Siete páginas en 320, 390, 768 y 1440 px: **28 casos**, sin texto visible inferior a 13 px ni desbordamiento horizontal.
- Siete páginas en 390 y 1440 px con preferencia de fuente del navegador a 32 px, el doble de la base estándar: **14 casos**, sin desbordamiento horizontal. No equivale a probar todos los modos de zoom del navegador ni certifica WCAG.
- Menú desplegado en escritorio/tablet y móvil: categorías 16 px, descripciones 14 px; opción final accesible y navegación al inicio sin anclas.
- Formulario: bloqueo de paso vacío, avance por los cuatro pasos, conservación de respuestas al volver y campos dentro de pantalla a 320 px. Sin enviar datos ni activar un correo.
- Menú probado con la preferencia de texto duplicada; controles y consentimiento también aumentan proporcionalmente. Preferencias de prueba restablecidas al terminar.
- FAQ abre correctamente, preguntas a 16 px. Guía visual revisada en móvil.
- Verificador del sitio: 7 páginas, 439 referencias locales, 44 imágenes, cero errores. JavaScript y diferencias de Git comprobados.

Pruebas realizadas en el motor del navegador integrado. No sustituyen pruebas con dispositivos físicos ni una auditoría completa de contraste de todos los píxeles de las fotografías.
