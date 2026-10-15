# Toscal Garden — guía de continuidad

Este directorio contiene un prototipo comercial estático en `prototype/`. No es todavía el desarrollo productivo. La prioridad es que la experiencia se sienta como un garden mediterráneo experto, amplio y cercano; nunca como un catálogo genérico.

## Qué ya está planteado

- Home en `prototype/index.html` con cabecera contextual, menú desplegable con seis familias, hero, tres rutas de necesidad, prueba de autoridad, categorías, proyecto, mapa y pie.
- Rutas desarrolladas como muestra: `plantas.html`, `productos.html`, `floristeria.html`, `proyectos.html` y `visitanos.html`.
- Sistema visual en `prototype/styles.css`: verde profundo `#173b30`, crema `#f9f6ef`, arena, terracota y tipografías Fraunces + DM Sans.
- Interacciones pequeñas de menú e idioma en `prototype/app.js`. El selector de idioma cambia el estado visual; las traducciones completas deben ser revisadas por hablantes nativos antes de publicar.
- Fotografías reales del garden se toman de `fotos_toscal/`; no sustituirlas por stock mientras se mantenga esta propuesta.

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
