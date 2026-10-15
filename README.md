# Toscal Garden

Web estática de Toscal Garden, Xàbia. La versión elegida está en `main`: hero fotográfico a todo el ancho, «Donde empieza tu lado verde» y un mismo sistema visual en todas las páginas.

## Vista local

Desde la raíz del repositorio:

```sh
python3 scripts/serve.py
```

- Web: <http://127.0.0.1:5186/prototype/index.html>
- Mapa navegable y guía visual: <http://127.0.0.1:5186/prototype/guia-diseno.html>
- Inventario de páginas y anclas: [MAPA_WEB.md](MAPA_WEB.md).
- Criterios de diseño: [docs/GUIA_DISENO.md](docs/GUIA_DISENO.md).

## Páginas y recursos

`prototype/` contiene inicio, plantas, productos, floristería, proyectos, visita y la guía interna. `fotos_toscal/` conserva las fotografías originales; `prototype/assets/` contiene los recursos optimizados.

- `site.css` y `site.js`: sistema visual compartido, cabecera, pie y navegación.
- `hero.css`: hero aprobado de la home.
- `pages.css`: componentes de las páginas interiores y de la guía.
- `proyectos.js`: formulario de cuatro pasos; prepara la solicitud en el correo del visitante.
- `guia.js`: demostración local de validación de campos.
- `styles.css`: base heredada de estilos y estructura del formulario.

Al cambiar la cabecera o el pie de `prototype/index.html`, replicar el layout con:

```sh
python3 scripts/sync-layout.py
```

Comprobar recursos, enlaces internos, anclas, imágenes y estructura básica:

```sh
python3 scripts/check-site.py
```

No requiere instalación ni build. Las carpetas `tmp/`, `output/` y `.codex-review/` contienen archivos temporales o generados y quedan fuera de Git.
