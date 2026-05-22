---
layout: default
title: Glosario
parent: Español
nav_order: 5
permalink: /es/references/terms-and-definitions/
---

<div class="language-switch"><strong>Idioma:</strong> <a href="{{ '/references/terms-and-definitions/' | relative_url }}">English</a> | Español</div>

# Glosario

Terminos especificos de los flujos de recuperacion de croma y recuperacion espacial de este repositorio. Los nombres estandar de nodos de Nuke (`Read`, `Write`, `Merge`, `Transform`, `Crop`, etc.) no se redefinen aqui: consulta la documentacion de Foundry para esos conceptos.

### ACES 2065-1
Espacio de color lineal AP0 referido a escena para masters de archivo/intercambio. Espacio de entrega recomendado con EXR half.

### Alineacion
Registro pixel a pixel de la Referencia con la Fuente, incluido el recorte, para que las ramas solo difieran en la caracteristica prevista (color o espacial).

### Croma (Cb, Cr)
Canales de diferencia de color en YCbCr. En recuperacion de croma, provienen de la rama de Referencia.

### CopyCat
Nodo de Nuke que entrena una CNN compacta usando pares supervisados Input/Target ensamblados en el grafo de nodos.

### F_Align
Operador de alineacion de Furnace usado como primera pasada automatizada antes del refinamiento manual con `Transform`.

### Formato de pelicula
Ancho fisico de la pelicula (16mm, 35mm). Los distintos formatos tienen caracteristicas espaciales y patrones de dano propios.

### Generacion filmica
Etapa de duplicacion (negativo original, internegativo, copia positiva, duplicado). Las diferencias generacionales afectan la calidad espacial.

### Verdad de referencia (Target)
La salida deseada usada como Target durante el entrenamiento:
- **Recuperacion de croma:** Fuente Y + Referencia Cb/Cr
- **Recuperacion espacial:** Referencia Y + Fuente Cb/Cr

### Fotogramas de validacion
Pares de fotogramas excluidos del entrenamiento y usados solo para validacion.

### Inference
Nodo de Nuke que aplica un modelo `.cat` entrenado a nuevos fotogramas/secuencias.

### Internegativo
Negativo intermedio creado a partir de un elemento positivo. A menudo tiene mayor calidad espacial que las copias de distribucion.

### Luma (Y)
Canal de brillo en YCbCr. En recuperacion de croma, la luma proviene de la rama Fuente.

### MatchGrade
Nodo de Nuke para igualacion de apariencia. En estos flujos se usa como linea base opcional para comparar contra la reconstruccion aprendida.

### Procedencia
Historial registrado de fuentes, procesos y parametros que permite reproducibilidad y auditoria.

### Telecine
Transferencia a video de un elemento filmico realizada en flujos de preservacion anteriores. Puede conservar secciones mas limpias aunque tenga menor resolucion.

### Par de entrenamiento
Un unico ejemplo supervisado: Input (degradado) y Target (verdad de referencia), con contenido y alineacion identicos.

### YCbCr
Modelo de color que separa luma (Y) de croma (Cb, Cr). Se usa para construir la verdad de referencia recombinando canales de la Fuente y la Referencia.
