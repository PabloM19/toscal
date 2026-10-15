# Toscal Garden — guía de continuidad

Este directorio contiene un prototipo comercial estático en `prototype/`. No es todavía el desarrollo productivo. La prioridad es que la experiencia se sienta como un garden mediterráneo experto, amplio y cercano; nunca como un catálogo genérico.

## Estado actual del diseño

- La rama definitiva es `main`. La variante elegida por el usuario es «Donde empieza tu lado verde», con hero a todo el ancho, misma altura y sin la etiqueta superior derecha. Se mantiene la etiqueta izquierda con su punto.
- El usuario ha aprobado trasladar este estilo a todas las páginas. Las seis rutas públicas están unificadas: inicio, plantas, productos, floristería, proyectos y visita.
- Cabecera y pie comunes; menú con hovers rectangulares (radio de 2 px), a petición expresa del usuario. Mantener esta forma también en nuevos componentes.
- Mapa navegable y guía de componentes en `prototype/guia-diseno.html`, de uso interno y con `noindex`. Inventario y criterios en `MAPA_WEB.md` y `docs/GUIA_DISENO.md`.
- `prototype/site.css` y `site.js` comparten el lenguaje y la navegación accesible de la home. `hero.css` conserva su hero aprobado y `pages.css` contiene los componentes interiores. `styles.css` es la base heredada.
- `scripts/sync-layout.py` replica cabecera y pie desde la home. `scripts/check-site.py` valida rutas, anclas, imágenes y estructura básica.
- El formulario de proyectos conserva cuatro pasos, validación, navegación atrás y respuestas seleccionadas. `proyectos.js` prepara un correo; el visitante debe enviarlo desde su aplicación de correo.
- Las fotografías son propias, optimizadas en WebP con variantes responsive. No sustituir por stock.
- Las traducciones completas siguen pendientes; se ha retirado el selector que solo cambiaba el idioma visual sin traducir el contenido.

## Información de negocio confirmada

- Toscal Garden está en Camí Assagador de Cabanes, s/n, 03730 Xàbia, Alicante. Teléfono: 965 79 50 99.
- Horario usado: lunes–sábado 08:00–18:30; domingos y festivos 09:00–14:00. Verificar antes de lanzamiento.
- Valores de autoridad para home/SEO: más de 30 años, 20.000 m² de garden, 120.000 m² de producción mediterránea y premio Garden Magazine al mejor Garden de la Comunidad Valenciana 2022/23.
- Público equilibrado: particular y profesional. Idiomas prioritarios: español, inglés y neerlandés.
- Categorías actuales a preservar: plantas de exterior, plantas de interior, árboles/palmeras/ejemplares, macetas y cerámica, riego y ferretería, decoración, floristería y construcción/diseño de jardines. El sitio actual también menciona alquiler de plantas y herramientas de jardinería; confirmar alcance antes de destacarlo.

## Prioridad de conversión

La portada siempre debe ofrecer estas tres decisiones visibles y equivalentes:

1. **Quiero visitar el garden** → página con mapa, horario, teléfono, parking/accesos cuando se confirme.
2. **Busco una planta o producto** → categorías y una vía de consulta de disponibilidad por WhatsApp/llamada.
3. **Quiero crear mi jardín** → servicio de jardines, formulario corto de cualificación y contacto humano.

En desktop, mantener el mega menú con iconos y microdescripciones. En móvil, convertirlo en un acordeón accesible; no esconder categorías importantes detrás de un menú simplificado.

## Siguientes páginas a completar

1. **Plantillas de categoría SEO local**: una plantilla reusable para `/plantas-exterior-xabia/`, `/plantas-interior-xabia/`, `/palmeras-arboles-xabia/`, `/macetas-ceramica-xabia/`, `/riego-jardineria-xabia/`, `/floristeria-xabia/`.
   - H1 natural con Xàbia/Jávea solo cuando corresponda; no repetir la ciudad artificialmente.
   - Apertura útil, familias de producto, consejo experto, fotos propias, CTA a visita/WhatsApp, NAP y enlaces internos.
2. **Servicios**: páginas para diseño y construcción de jardines, riego e instalación, y para profesionales si el equipo confirma alcance. Mostrar proceso, zonas atendidas y ejemplos reales.
3. **Contacto y visita**: sustituir el iframe de búsqueda genérica por el código embed definitivo que facilite el cliente. Añadir accesibilidad, aparcamiento y rutas si se confirman.
4. **Idiomas**: crear rutas reales `/en/` y `/nl/` con `hreflang`, no traducir de forma automática. Revisar español/inglés/neerlandés de manera humana.
5. **Contenido de temporada**: una biblioteca editorial corta (por ejemplo, jardín mediterráneo, riego, plantas para sol, cuidado de palmeras) que enlace a categorías y servicios. No publicar artículos de relleno.

## Producción y SEO técnico

- Reemplazar cada URL de imagen por un asset optimizado WebP/AVIF con `srcset`, `width`, `height`, `loading="lazy"` fuera del primer viewport y `alt` descriptivo.
- Mantener el logo oficial. La fuente remota puede alojarse localmente en producción si el rendimiento lo exige.
- Añadir `Organization` + `LocalBusiness`/`GardenStore` JSON-LD con datos verificados, `WebSite`, breadcrumbs y datos de horarios. No inventar perfiles sociales ni reseñas.
- Definir canonicals, sitemap XML, robots, Open Graph, favicon/manifest, redirecciones desde la web actual y medición de clic a teléfono, WhatsApp, Maps y solicitud de proyecto.
- Integrar una CMP real antes de activar analítica, píxeles o el botón “configurar cookies”; el pie actual enlaza a las políticas existentes como maqueta, no sustituye el cumplimiento legal.
- Validar contraste, foco visible, navegación por teclado, etiquetas de formulario e iframe con título. Objetivo mínimo: WCAG 2.2 AA razonable.

## Señalética física (mismo lenguaje)

Dirección: verde profundo, crema, terracota muy medida, texto editorial cálido y flechas funcionales. Debe leerse a distancia y sentirse parte del recorrido, no decoración suelta.

- Acceso: identidad + “Garden centre · Xàbia” + horarios y una orientación inmediata.
- Zonas prioritarias conforme a anotaciones recibidas: “Palmeras y árboles”, “Frutales” y “Cañizos”. En bifurcaciones: izquierda para “Frutales · Macetas · Palmeras y árboles”; recto para “Cañizos” y según ubicación “Interior”.
- Cajas: una aplicación más pequeña que ordene atención, recogida/consulta y refuerce la marca.
- Antes de arte final: medir soportes, alturas de lectura, flujos reales, materiales, normativa y condiciones de instalación. Diseño y fabricación/instalación son partidas distintas.

## Criterio de diseño

- Mucha fotografía del garden, menos bloques cromáticos planos. Cada categoría debe mostrar su propio mundo visual.
- Jerarquía serena: titulares editoriales, textos cortos y CTAs claros.
- Evitar sliders, iconos decorativos sin función, stock, frases de marketing vacías y botones repetidos.
- La foto debe apoyar la decisión: entrada para visita, pasillos/plantas para categorías, imágenes amplias para proyecto y zonas de venta para producto.

## Validación antes de presentar o publicar

- Probar las tres rutas principales en móvil y escritorio.
- Confirmar los enlaces a WhatsApp, email, número, perfiles sociales, mapa y políticas; los enlaces sociales del prototipo son placeholders hasta que se proporcionen los perfiles exactos.
- Confirmar servicios, disponibilidad, horarios, NAP, materiales de señalética y traducciones finales.
- No afirmar instalación, mantenimiento o alquiler como servicio activo sin validarlo con Toscal.
