---
layout: default
title: Recursos Adicionales
parent: Español
nav_order: 5
permalink: /es/additional-resources/
---

<div class="language-switch"><strong>Idioma:</strong> <a href="{{ '/additional-resources/' | relative_url }}">English</a> | Español</div>

# Recursos Adicionales

Estas notas apoyan el flujo sin ser pasos del flujo en si. Uselas como contexto al planificar escaneos, diagnosticar material desvanecido o documentar decisiones de restauracion.

## Recorrido en Video: Nuke Chroma Recovery {#video-walkthrough-nuke-chroma-recovery}

El recorrido publico en YouTube es un complemento visual del repositorio. Pertenece aqui como material de apoyo: una forma rapida de ver la idea de recuperacion de croma en movimiento antes de leer el flujo paso a paso.

<figure>
  <a href="https://youtu.be/kXerjFGX9Kg" target="_blank" rel="noopener">
    <img src="{{ '/images_kebab/video_previews/color-recovery-video-preview.gif' | relative_url }}" alt="Preview animado del recorrido de Nuke chroma recovery en YouTube">
  </a>
  <figcaption>Video fuente: <a href="https://youtu.be/kXerjFGX9Kg" target="_blank" rel="noopener">Nuke Chroma Recovery: Rebuilding Faded Film Color with CopyCat</a>.</figcaption>
</figure>

## Digitalizacion: Primer Escaneo, Ultima Oportunidad {#digitization-first-scan-last-chance}

La digitalizacion es el traspaso de preservacion en el que el contenido de imagen se separa de un contenedor fisico fragil. Trata el escaneo como la base de todos los pasos posteriores de restauracion, no como una transferencia rapida ni como un grade creativo ya horneado. En materiales danados o raros, el primer escaneo puede ser tambien el unico escaneo practico: la pelicula puede no sobrevivir a manipulaciones repetidas, el presupuesto puede no permitir una segunda pasada, o el deterioro puede avanzar antes de otro intento.

<figure>
  <a href="https://fabiocolor.substack.com/p/first-scan-last-chance" target="_blank" rel="noopener">
    <img src="{{ '/images_kebab/digitization/first-scan-last-chance-hero.png' | relative_url }}" alt="Imagen hero del articulo First Scan, Last Chance">
  </a>
  <figcaption>Imagen del articulo <a href="https://fabiocolor.substack.com/p/first-scan-last-chance" target="_blank" rel="noopener">"First Scan, Last Chance"</a>: la digitalizacion como el momento en que el contenido se separa de un contenedor filmico fragil.</figcaption>
</figure>

La meta es capturar la maxima informacion recuperable en RGB y luminancia. Un buen escaneo debe preservar el rango dinamico de la pelicula, la separacion de canales de color, la variacion de densidad, el grano y la textura, para que las herramientas posteriores puedan tomar decisiones informadas. Un mal escaneo puede eliminar evidencia de forma permanente: altas luces clipeadas, sombras aplastadas, mal balance de blancos, decisiones automaticas de exposicion o clipping de canales no pueden reconstruirse de forma fiable mas adelante.

<div class="media-grid media-grid-2">
  <figure>
    <a href="https://fabiocolor.substack.com/p/first-scan-last-chance" target="_blank" rel="noopener">
      <img src="{{ '/images_kebab/digitization/first-scan-last-chance-scanner-color-controls.png' | relative_url }}" alt="Extracto del articulo sobre controles de color del escaner">
    </a>
    <figcaption>Los controles de exposicion y RGB del escaner afectan cuanta informacion util se captura antes de empezar la restauracion.</figcaption>
  </figure>
  <figure>
    <a href="https://fabiocolor.substack.com/p/first-scan-last-chance" target="_blank" rel="noopener">
      <img src="{{ '/images_kebab/digitization/first-scan-last-chance-color-systems-review.png' | relative_url }}" alt="Captura del articulo Color systems for motion picture film digitization">
    </a>
    <figcaption>Las decisiones de digitalizacion deben probarse contra el elemento filmico y la meta de preservacion, no tratarse como una ruta de color fija para todos los casos.</figcaption>
  </figure>
</div>

**Principios de escaneo:**

- Captura un sustituto digital de grado preservacion antes de hornear decisiones de restauracion.
- Evita clipping de altas luces, aplastamiento de sombras, balance de blancos automatico, reduccion de ruido fuerte, sharpening o LUTs creativos durante la captura.
- Monitorea RGB parade, waveform, histograma y clipping de canales durante la configuracion y la captura final.
- Haz una pasada preliminar de evaluacion para encontrar los extremos tonales de la secuencia, cambios de densidad, flashes de empalmes, desvanecimiento severo y cualquier ajuste del escaner que probablemente falle.
- Registra modelo de escaner, gate, optica, resolucion, profundidad de bits, codificacion de color, transformaciones, ajustes de exposicion y cualquier decision de wet-gate o limpieza.
- Preserva el escaneo crudo o master archivistico por separado de renders de restauracion, proxies de revision y grades creativos.

| Riesgo durante la digitalizacion | Por que importa despues |
| --- | --- |
| Altas luces o canales clipeados | Elimina informacion de imagen permanentemente y debilita recuperacion de color, deflicker, eliminacion de polvo y grading. |
| Punto blanco incorrecto | Agrega una relacion falsa de color que las herramientas de restauracion pueden aprender o amplificar. |
| Decisiones automaticas del escaner | Pueden variar plano a plano, causando flicker artificial, densidad inestable o balance de canales inconsistente. |
| Grade creativo horneado | Reduce la evidencia disponible para restauracion futura o interpretaciones alternativas. |
| Baja profundidad de bits / formato de entrega comprimido | Reduce informacion sutil de densidad y croma necesaria para restauracion, especialmente en material desvanecido. |

Para material historico o deteriorado, prefiere un escaneo conservador de alta profundidad de bits que mantenga intacta la informacion capturada por el sistema; despues toma decisiones de restauracion en un pipeline de post controlado. Flujos ADX, Cineon, lineales, ACES y display-referred pueden ser utiles en el contexto correcto, pero deben probarse contra el elemento filmico especifico en vez de asumirse como correctos. Para el flujo de recuperacion de croma de este repositorio, la regla clave es la continuidad: sea cual sea el camino de escaneo y transformacion elegido, Fuente y Referencia deben llegar al entrenamiento con transformaciones coincidentes y documentadas.

Digitalizacion, restauracion y remasterizacion estan relacionadas, pero no son lo mismo. La digitalizacion captura la pelicula analogica como datos. La restauracion aborda danos o perdidas introducidas por el contenedor fisico. La remasterizacion puede adaptar la obra a un nuevo display, estreno o publico. Manten visibles esos limites en los metadatos para que futuros usuarios sepan que decisiones vienen del objeto, del proceso de restauracion o del master de entrega.

Articulo e imagenes fuente: [First Scan, Last Chance: The Critical Role of Digitization in Preserving Film Heritage](https://fabiocolor.substack.com/p/first-scan-last-chance).

## Por que los escaneos desvanecidos se vuelven magenta {#why-faded-scans-turn-magenta}

La pelicula color registra la imagen mediante capas de tintes sustractivos. Cuando la densidad que sobrevive no queda equilibrada, el escaneo ya no conserva informacion RGB pareja. Un fallo comun es la dominante rosada/magenta: las densidades cian y amarilla se debilitan frente al tinte restante, asi que rojo y azul dominan y el canal verde pierde separacion cromatica util.

Para este flujo, lo importante es practico mas que estetico: la imagen magenta todavia suele conservar luma, textura y grano utilizables, pero sus canales de croma estan sesgados, comprimidos o parcialmente clipeados. Un prebalance neutral entrega a `CopyCat` una distribucion de entrada mas limpia antes de introducir el croma de la referencia.

<div class="media-grid media-grid-2">
  <figure>
    <img src="{{ '/images_kebab/resolve-dctl/faded-film-resolve-dctl-strong-red-compress-before.png' | relative_url }}" alt="Escaneo desvanecido de accion real con sesgo fuerte rojo/magenta">
    <figcaption>Escaneo desvanecido con sesgo fuerte rojo/magenta.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/images_kebab/resolve-dctl/faded-film-resolve-dctl-strong-red-compress-after.png' | relative_url }}" alt="Escaneo de accion real despues de rebalance tecnico">
    <figcaption>Compresion/rebalance tecnico del rojo para preparar un input mas limpio antes del entrenamiento ML.</figcaption>
  </figure>
</div>

<figure>
  <img src="{{ '/images_kebab/candy-candy/candy-candy-resolve-dctl-parade-scope-faded-film.png' | relative_url }}" alt="Scope de parade en Resolve mostrando desbalance de canales en pelicula desvanecida">
  <figcaption>Scope parade de Resolve y controles de Faded Balancer mostrando desbalance de canales en pelicula desvanecida. La meta es un prebalance tecnico, no un grade creativo final.</figcaption>
</figure>

<div class="media-grid media-grid-2">
  <figure>
    <img src="{{ '/images_kebab/candy-candy/candy-candy-resolve-dctl-before-correction-faded.png' | relative_url }}" alt="Escaneo desvanecido de Candy Candy antes de correccion DCTL">
    <figcaption>Escaneo de animacion desvanecido antes de correccion especifica por canal.</figcaption>
  </figure>
  <figure>
    <img src="{{ '/images_kebab/candy-candy/candy-candy-resolve-dctl-after-correction-red-channel.png' | relative_url }}" alt="Vista diagnostica de correccion del canal rojo en Candy Candy">
    <figcaption>Vista diagnostica/correccion del canal rojo usada para aislar y controlar un componente dominante.</figcaption>
  </figure>
</div>

### Datos Tecnicos Para La Investigacion

**Que esta fallando:** En materiales cromogenicos, la imagen final se forma por la superposicion de nubes de tinte cian, magenta y amarillo en capas de gelatina. Estos tintes organicos no envejecen al mismo ritmo. Cuando la densidad cian y amarilla se desvanece mas rapido que la magenta, el balance visual se desplaza hacia rosado, morado o magenta. La guia de inspeccion de NARA describe este diagnostico directamente: una pelicula magenta ha sufrido desvanecimiento de color porque las capas de tinte cian y amarillo se han debilitado, dejando dominante el magenta. La NFPF describe el mismo patron en peliculas modernas de color: cambios quimicos espontaneos en los tintes de imagen, a menudo con una dominante purpura causada por el desvanecimiento rapido de los tintes cian y amarillo.

**Por que ocurrio:** La causa raiz no es un mal escaneo ni un mal grade, aunque cualquiera de los dos puede hacer mas visible el sintoma. Es deterioro quimico acumulado: ruptura de enlaces moleculares en los tintes de imagen, estabilidad desigual de los tintes, calor, humedad, exposicion a luz, tiempo e historial de almacenamiento. Graphics Atlas senala que el desvanecimiento de tintes cromogenicos puede ocurrir tanto por exposicion a luz como durante almacenamiento en oscuridad; el desvanecimiento del tinte cian en almacenamiento oscuro puede dejar la imagen globalmente magenta. Stocks y copias cromogenicas antiguas, especialmente materiales de mediados de siglo anteriores a mejoras posteriores de estabilidad, son mas vulnerables que los stocks modernos.

**Por que el grading ordinario es limitado:** Un grade RGB puede rebalancear canales de forma global, pero no puede recrear croma ausente o comprimido en relaciones de canal contaminadas. Investigaciones recientes de digital unfading plantean esto como un problema de reconstruccion limitado por la informacion residual de tintes, la calidad del escaneo y las referencias disponibles. Los casos severos necesitan inferencia informada: referencias directas, referencias construidas, analisis espectral/de densidad, color de memoria documentado o aprendizaje supervisado.

**Datos que conviene capturar antes de restaurar:**

| Dato | Por que ayuda |
| --- | --- |
| Stock, generacion y fecha aproximada | Establece riesgo de estabilidad de tintes y proceso cromogenico probable. |
| Historial de almacenamiento | Calor, humedad y luz ayudan a explicar velocidad y patron de desvanecimiento. |
| Inspeccion fisica | Separa desvanecimiento de tintes de sindrome de vinagre, suciedad, encogimiento, moho, dano mecanico o problemas de emulsion. |
| Scopes RGB parade / histogramas | Muestran compresion, clipping y separacion de canales antes y despues del prebalance. |
| Dmin/Dmax o parches neutros cuando existan | Miden perdida de densidad y contaminacion de altas luces/sombras. |
| Comparacion con referencia | DVD, telecine, copia alternativa, artwork o referencia construida separan evidencia de decisiones subjetivas. |
| Registro de transformaciones | Documenta ajustes de escaner, ODT, espacio de color, prebalance, limpieza y decisiones de clamp antes de CopyCat. |

**Como tratarlo en este flujo:** Primero estabiliza el riesgo de preservacion: almacenamiento frio/seco, inspeccion, limpieza y digitalizacion antes de que avance el deterioro. Luego aplica un prebalance tecnico, no creativo, para reducir el sesgo extremo y dar a Nuke una placa fuente mas util. En recuperacion de croma, `CopyCat` no reemplaza toda la imagen: preserva luma/detalle de la fuente y aprende a reconstruir Cb/Cr desde una referencia alineada o construida. Si un canal esta sesgado pero todavia contiene informacion, el prebalance puede recuperar mucho. Si el croma realmente se perdio, la restauracion depende de evidencia externa y debe documentarse como interpretacion.

**Referencias tecnicas:**

- [National Archives - Motion Picture Film Condition Assessment](https://www.archives.gov/preservation/formats/motion-picture-film-condition-assessment.html)
- [National Film Preservation Foundation - Color Dye Fading](https://www.filmpreservation.org/preservation-basics/color-dye-fading)
- [Graphics Atlas - Chromogenic deterioration](https://new.graphicsatlas.org/chromogenic/object-view)
- [Heritage, 2023 - Digital Unfading of Chromogenic Film Informed by Its Spectral Densities](https://www.mdpi.com/2571-9408/6/4/181)
- [National Film Preservation Foundation - The Film Preservation Guide](https://www.filmpreservation.org/userfiles/image/PDFs/fpg.pdf)
