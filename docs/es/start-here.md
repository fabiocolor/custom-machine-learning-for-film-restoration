---
layout: default
title: Flujo Compartido
parent: Español
nav_order: 1
permalink: /es/start-here/
---

<div class="language-switch"><strong>Idioma:</strong> <a href="{{ '/start-here/' | relative_url }}">English</a> | Español</div>

# Flujo de Trabajo Compartido - Etapas 0-2

Esta pagina cubre todo lo que comparten ambos modos de recuperacion: exportacion desde Resolve, configuracion del proyecto en Nuke, curacion del dataset, alineacion, recorte compartido y decision de rama. Sigue esta pagina primero y despues continua en la guia de la rama elegida.

- [Recuperacion de croma](chroma-recovery.md): cuando el detalle esta intacto pero el color esta desvanecido, colapsado o desplazado.
- [Recuperacion espacial](spatial-recovery.md): cuando el color es aceptable pero el detalle, la nitidez o el grano son mas debiles que en la referencia.

![Resumen del flujo de trabajo](../images_kebab/general/full-overview-comparison.png)
*Resumen de extremo a extremo del flujo de recuperacion.*

---

## Etapa 0: Exportacion desde Resolve + Configuracion del Proyecto en Nuke

Antes de iniciar el flujo, asegurate de que el escaneo preserve la mayor cantidad posible de evidencia recuperable: evita clipping, balance de blancos automatico, grades creativos horneados e intermediarios comprimidos de baja profundidad de bits. Para el contexto de preservacion, revisa [Digitalizacion: Primer Escaneo, Ultima Oportunidad](additional-resources.md#digitization-first-scan-last-chance).

### Preparacion de Fuente y Referencia

Lo importante es si la referencia conserva mejor informacion para el problema que estas resolviendo, no si es mas nueva, mas nitida o de mayor resolucion.

![Fuente cruda antes del balance](../images_kebab/muralla-verde/muralla-verde-scan-27-35-preview.gif)
*Fuente que debe balancearse tecnicamente antes del entrenamiento.*

![Fuente balanceada para entrenamiento](../images_kebab/muralla-verde/muralla-verde-source-27-35-preview.gif)
*Placa fuente balanceada usada como input mas limpio para el flujo.*

**Preparacion de la fuente:**

- Balancea tecnicamente la fuente (neutral, no creativo).
- Elimina flicker severo, suciedad, flashes de empalmes e inestabilidad que contaminarian el entrenamiento.
- Para recuperacion de croma: degraina la fuente para entrenamiento si el grano interfiere con el aprendizaje del croma. Documenta los ajustes y conserva la placa original.
- Para recuperacion espacial: preserva la estructura de grano original; no degraines salvo que la referencia tambien este degrainada.
- Neutralizacion de dominante global: si la fuente tiene un sesgo fuerte por desvanecimiento de tintes o escaneo, aplica un prebalance neutral. Recomendado: [Faded Balancer DCTL/OFX](https://github.com/fabiocolor/Faded-Balancer-DCTL). Para contexto sobre desvanecimiento magenta y desbalance de canales, revisa [Por que los escaneos desvanecidos se vuelven magenta](additional-resources.md#why-faded-scans-turn-magenta).

| Antes (escaneo crudo desvanecido) | Despues (Faded Balancer aplicado) |
| --- | --- |
| ![Escaneo desvanecido crudo](../images_kebab/candy-candy/candy-candy-faded-balancer-raw.png) | ![Escaneo balanceado](../images_kebab/candy-candy/candy-candy-faded-balancer-finished.png) |

*Faded Balancer DCTL neutralizando desvanecimiento magenta de tintes en Resolve antes de ingresar a Nuke.*

**Preparacion de la referencia:**

- Lo bastante limpia para quitar artefactos de transferencia que podrian confundir al modelo.
- Para recuperacion de croma: suprime polvo, ruido de compresion y banding (denoise/deband/median ligero). No se recomiendan cambios de geometria ni warping temporal.
- Para recuperacion espacial: elimina solo polvo/suciedad/rayaduras. **No** apliques median ni desenfoques la referencia: preserva todo el detalle espacial (grano, nitidez, definicion de bordes). Para referencias magneticas/de video, ataca solo artefactos de compresion evidentes con herramientas que preserven el contenido de frecuencia espacial.

**Geometria/estabilizacion:** prefiere limpieza que no altere la geometria. Si debes estabilizar o reencuadrar, aplica transformaciones identicas a ambas exportaciones.

### Exportacion desde Resolve

![Preparacion de referencia en Resolve](../images_kebab/cropped/muralla-verde-reference-pre-alignment-timeline-resolve-cropped.png)
*Fuente y referencia colocadas en el mismo contenedor de Resolve.*

1. Conforma ambas fuentes en una sola timeline. Desactiva retimes, efectos y grades por clip.
2. Alinea la referencia con la fuente en Edit/Inspector (Translate/Scale/Rotate). Permite letterbox/pillarbox; conserva un encuadre estable.
3. Usa configuracion de proyecto ACES. Exporta ambas con **ODT Rec.709 2.4** a EXR: mantiene valores acotados en [0-1], que es lo que espera `CopyCat`.
4. Verifica paridad: resolucion, pixel aspect, rango/rate de fotogramas, conjunto de canales (solo RGB; omite alpha).
5. Anota cualquier offset global (scale/translate/rotate) para referencia posterior.

**Reglas:**

- Mismo rango de fotogramas, encuadre y resolucion.
- Sin grading creativo.
- Corrige entrelazado, problemas de cadencia y errores de decodificacion antes de exportar.

**Checklist de QC:**

- [ ] Dimensiones, rangos de fotogramas y pixel aspect coinciden
- [ ] Los conjuntos de canales coinciden (RGB), valores en 0-1 al leer en Nuke
- [ ] No hay retimes ni transformaciones de color accidentales

### Configuracion del Proyecto en Nuke

**Ajustes del proyecto:**

- Gestion de color: `OCIO` con `ACES 1.2` o `ACES 1.3`.
- Espacio de trabajo: `ACEScg` (scene-linear, AP1).
- Viewer process: ACES ODT que coincida con tu display (por ejemplo, `ACES 1.0 SDR-video / Rec.709 2.4`).

**Ajustes de nodos Read (Fuente y Referencia):**

- Pares de entrenamiento (desde Resolve Rec.709 2.4 ODT): `Read.colorspace = Utility - sRGB - Color Picking`.
- Masters ACES (intercambio/comp): `Read.colorspace = ACES - ACES2065-1`. Si se usan para entrenamiento, transforma a display-referred (aplica Rec.709 2.4 ODT) en vez de clipear ingenuamente.

**Verifica:**

- Alterna el Viewer entre Fuente/Referencia; confirma apariencia consistente bajo el ODT elegido.
- Confirma transformaciones de ingesta identicas en ambas ramas.

### Referencia de ACES y Gestion de Color

**Dominio de entrenamiento (recomendado):** Display-referred: exporta Rec.709 2.4 ODT, ingesta con `Utility - sRGB - Color Picking`, procesa en ACEScg y construye la verdad de referencia YCbCr con cadenas identicas. Los valores quedan naturalmente acotados; solo hace falta un clamping ligero de seguridad.

**Alternativa: dominio Log:** viable en teoria, pero significativamente mas lento y, en pruebas, inferior para fidelidad de recuperacion de croma. Usalo solo si el material lo exige.

**No recomendado: clamp lineal ingenuo de ACES:** Ingestar ACES 2065-1 y clipear a [0-1] aplasta altas luces y perjudica tanto el mapeo de croma como el espacial. Si partes de masters ACES, transforma primero a display-referred.

**Input y Target deben compartir exactamente el mismo dominio y las mismas transformaciones.** No mezcles lineal y display-referred entre ramas.

**Nodos Write (entrega):**

- Archivo: `Write.colorspace = ACES - ACES2065-1` (AP0), EXR 16-bit half (ZIP/DWAA).
- Revision/proxy: Rec.709 ODT -> ProRes/H.264. Documenta la intencion de visualizacion y el ODT.

**Interop con Resolve:**

- Proyecto ACES 1.2/1.3; exporta masters EXR ACES 2065-1 para ingesta en Nuke.
- Para entrenamiento display-referred, exporta Rec.709 2.4 ODT e ingesta con `Utility - sRGB - Color Picking`.
- Mantén identicos tamano de fotograma, PAR y canales.

---

## Etapa 1: Curacion del Dataset

Construye un pequeno conjunto de ensenanza a partir de fotogramas representativos; no metas toda la secuencia en el entrenamiento.

![Curacion del dataset](../images_kebab/cropped/dataset-curation-cropped.png)
*Construccion de ejemplos de entrenamiento pareados en Nuke.*

### Criterios de Seleccion

- **Fotogramas fuente:** luma/textura intacta, grano representativo, gate weave minimo. Evita fotogramas dominados por motion blur salvo que coincidan en la referencia.
- **Fotogramas de referencia:** mismo plano/timecode cuando exista, o un proxy bien construido. Evita compresion fuerte, subtitulos/logos incrustados y grades inestables.
- **Excluir:** pares con oclusiones unicas en un lado (flashes, marcas de empalme) que el modelo no pueda reconciliar.

### Cantidad de Pares

| Alcance | Pares | Notas |
| --- | --- | --- |
| Plano | 4-9 | Anade mas si la convergencia se estanca |
| Escena | 12-24 | |
| Secuencia | 24-64+ | Escala segun la variabilidad |

Para rangos cortos (por ejemplo, fotogramas 20-60), fija anclas en inicio/medio/medio/final.

### Cobertura

Asegura diversidad en:

- **Iluminacion:** calida/fria, dia/noche, interior/exterior
- **Sujetos:** tonos de piel, follaje/cielo, telas, neutros
- **Extremos:** sombras profundas, altas luces especulares, primarios saturados
- **Texturas** (recuperacion espacial): tela, follaje, piel, bordes, gradientes suaves

### Reglas de Emparejamiento

- **Temporal:** coincide mismo indice de fotograma/timecode. Si hay desfase de un fotograma, prefiere el fotograma con mayor solapamiento de estructura estatica.
- **Espacial:** resolucion/orientacion identicas. Overscan/crop debe ser compartido (las diferencias residuales se manejan en la Etapa 2).
- **Espacio de color:** ambos lados bajo la misma transformacion (por ejemplo, exportacion Rec.709) para que los valores permanezcan en 0-1.

### Construccion en Nuke

1. Crea un `FrameHold` por indice seleccionado en las ramas Fuente y Referencia.
2. Ensambla stacks ordenados con `AppendClip`: uno para Fuente (Input), otro para Referencia (Target).
3. Mantén un `AppendClip` de staging aguas arriba del referenciado por los nodos `PostageStamp` posteriores para reordenar con seguridad.
4. Verifica cada par con viewer wipe o `Merge (difference)`: juzga solo geometria/alineacion, no color.
5. Etiqueta los pares de forma consistente. Mantén una tabla de indices/timecodes para trazabilidad.

### Documentacion

- Registra IDs de plano, indices de pares y justificacion.
- Indica si las referencias son directas (telecine/DVD/copia) o construidas; cita las fuentes.
- Marca compromisos (compresion, paralaje residual) para revisarlos durante entrenamiento.

---

## Etapa 2: Alineacion

Alineacion precisa a nivel de pixel con recorte compartido para que las ramas solo difieran en la caracteristica prevista (color o detalle espacial).

![Flujo de alineacion](../images_kebab/cropped/alignment-cropped.png)
*Rutas de alineacion automatica y manual dentro de la plantilla.*

### Estrategia

1. Resolucion global unica con `F_Align` usando una ROI central conservadora. No iteres.
2. Evalua de inmediato con `Merge (difference)`. Si quedan bordes/geometria, cambia a `Transform` manual con keyframes.
3. Mantén un `Dissolve` para comparar rapidamente las rutas automatica/manual.

![Chequeo de alineacion con Merge (difference)](../images_kebab/general/merge-difference-alignment-check.gif)
*Merge (difference) en el viewer: geometria/bordes deberian quedar casi negros. Las diferencias visibles de color son esperadas; solo la desalineacion estructural es un problema.*

### Recorte y Manejo de Subtitulos

- Elimina bordes negros/overscan en ambas ramas; no entrenes con contenido que no sea imagen.
- Excluye subtitulos/logos quemados. Cuando sea inevitable, anima un recorte compartido.
- Aplica el **mismo recorte exacto** a Fuente y Referencia (clone/link) para que las areas de pixel correspondan.

![Ajustes del nodo Crop](../images_kebab/cropped/crop-node-settings-cropped.png)
*Recorte compartido que mantiene ambas ramas en la misma area de imagen util.*

### Construccion en Nuke

- Compara Referencia contra Fuente con Viewer wipe y `Merge (difference)`.
- Usa un `Dissolve` para alternar rutas automatica/manual. Coloca keyframes por fotograma (0 = auto, 1 = manual) tras inspeccion.
- **Ruta automatica:** `F_Align` con ROI central conservadora. Resolucion global unica (Translate/Scale/Rotate/Perspective). Sin perseguir parametros.
- **Ruta manual:** `Transform` (translate/scale/rotate) con keys segun necesidad. Juzga con `Merge (difference)`.
- **Reference Crop (ultimo paso):** agrega `Crop` en la Referencia alineada para quitar overscan/overlays transitorios. Mantenlo bypassed durante la resolucion; activalo como paso final. Guarda este nodo para clone/link en la Etapa 3. No recortes la Fuente aqui.

### Checklist de Verificacion

- [ ] `Merge (difference)` muestra solo diferencias de color/fotometricas; geometria/bordes casi negros. No apliques Grade/correccion de color aqui.
- [ ] No hay shimmer de bordes en esquinas/laterales al alternar Fuente/Referencia.
- [ ] El recorte de Referencia quita overscan/mattes sin ocultar pistas de alineacion.

**Solucion de problemas:** Gate weave/paralaje en referencias deformadas de multiples generaciones: espera que el keyframing manual con `Transform` tome tiempo.

---

## Decision de Rama - Etapa 3

Aqui el flujo diverge. El layout es compartido; la decision de rama es que canales entran en el objetivo de verdad de referencia.

![Ajustes del nodo Colorspace](../images_kebab/cropped/colorspace-node-linear-to-ycbcr-settings-cropped.png)
*Convierte ambas ramas a YCbCr antes de recombinar canales.*

![Ajustes del nodo Shuffle](../images_kebab/cropped/shuffle-node-settings-cropped.png)
*Nodo Shuffle usado para construir el objetivo de verdad de referencia.*

![Nodo CopyBBox](../images_kebab/general/copybbox-node-settings.png)
*CopyBBox asegura bbox identico entre Fuente y Ground Truth antes de conectar a CopyCat.*

| Rama | Objetivo de verdad de referencia | Continua en |
| --- | --- | --- |
| **Recuperacion de croma** | Fuente `Y` + Referencia `Cb/Cr` | [chroma-recovery.md](chroma-recovery.md) |
| **Recuperacion espacial** | Referencia `Y` + Fuente `Cb/Cr` | [spatial-recovery.md](spatial-recovery.md) |

### Reglas Despues de la Rama

- No combines recuperacion de croma y espacial en la misma construccion de objetivo.
- Valida una pasada antes de intentar la segunda.
- Entrena primero a nivel de secuencia; divide a nivel de plano solo donde falle la pasada amplia.
- Ejecuta inferencia sobre toda la fuente, no solo sobre fotogramas de entrenamiento.
- Compara contra una linea base (`MatchGrade`) para probar que el modelo hace algo especifico.

### Modos de Falla Comunes

- Entrenar con una fuente inestable (flicker, suciedad, desequilibrio severo).
- Confiar en una mala referencia solo porque tiene mayor resolucion.
- Mantener fotogramas desalineados en el dataset.
- Dejar bordes, subtitulos u overlays dentro del area de entrenamiento.
- Esperar que un solo modelo resuelva todos los planos de una secuencia dificil.
