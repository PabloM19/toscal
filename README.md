# Toscal Garden

Prototipo estático de la web de Toscal Garden, Xàbia.

- `prototype/`: páginas HTML, estilos, JavaScript y recursos optimizados.
- `fotos_toscal/`: fotografías y logotipos originales. Algunas páginas enlazan directamente a esta carpeta.
- Los documentos de la raíz recogen el contexto y la planificación del proyecto.

## Vista local

Desde la raíz del repositorio:

```sh
python3 -m http.server 5186 --bind 127.0.0.1
```

Abrir <http://127.0.0.1:5186/prototype/index.html>.

Los estilos e interacciones exclusivos de la portada están en `prototype/home.css` y `prototype/home.js`. Las páginas interiores conservan `prototype/styles.css` y `prototype/app.js`.

Las carpetas `tmp/`, `output/` y `.codex-review/` contienen archivos temporales o generados y quedan fuera de Git.
