---
layout: default
title: Español
nav_order: 10
has_children: true
permalink: /es/
---

<div class="language-switch"><strong>Idioma:</strong> <a href="{{ '/' | relative_url }}">English</a> | Español</div>

# Aprendizaje Automatico Personalizado para Restauracion Cinematografica

Flujo de trabajo de restauracion basado en referencias para NukeX usando `CopyCat` e `Inference`. Entrena CNN pequenas con pares reales de fuente/referencia para recuperar croma perdido o detalle espacial en elementos filmicos degradados.

No es un plugin. Es un flujo de trabajo repetible y documentado para archivos, equipos de preservacion y profesionales de restauracion.

<div class="hero-buttons">
  <a href="{{ '/es/start-here/' | relative_url }}" class="btn btn-primary">Empezar</a>
  <a href="https://github.com/fabiocolor/custom-machine-learning-for-film-restoration/releases/latest" class="btn btn-primary" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);" target="_blank">📥 Descargar plantillas de Nuke</a>
  <a href="https://youtu.be/kXerjFGX9Kg" class="btn btn-outline" target="_blank">Ver recorrido en YouTube</a>
</div>

[![Ver el recorrido en YouTube](../images_kebab/video_previews/color-recovery-video-preview.gif)](https://youtu.be/kXerjFGX9Kg)
*Recorrido en video: complemento visual de este repositorio.*

![Resumen del flujo de trabajo](../images_kebab/cropped/node-graph-overview-cropped.png)
*Resumen del flujo de recuperacion.*

## Modos de Recuperacion

| Modo | Usar cuando | Objetivo de verdad de referencia |
| --- | --- | --- |
| **Recuperacion de croma** | La luma/detalle esta intacta, pero el croma esta desvanecido, desplazado o colapsado | Fuente `Y` + Referencia `Cb/Cr` |
| **Recuperacion espacial** | El color es aceptable, pero el detalle/nitidez/grano esta degradado frente a la referencia | Referencia `Y` + Fuente `Cb/Cr` |

Empieza con recuperacion de croma salvo que tu problema sea claramente espacial. No combines ambos en la misma construccion de objetivo: tratalos como pasadas separadas.

## Primeros Pasos

Sigue estas paginas en orden:

1. **[Flujo de trabajo compartido](start-here.md)**: Etapas 0-2: exportacion desde Resolve, configuracion de Nuke, curacion del dataset, alineacion, recorte compartido y decision de rama.
2. **[Recuperacion de croma](chroma-recovery.md)**: Desde la Etapa 3: construccion del objetivo de croma, entrenamiento, inferencia y validacion.
3. **[Recuperacion espacial](spatial-recovery.md)**: Desde la Etapa 3: construccion del objetivo espacial, entrenamiento, inferencia y validacion.

## Material de Apoyo

- [Recursos adicionales](additional-resources.md): Recorrido en video, principios de digitalizacion, contexto de escaneos desvanecidos y referencias tecnicas.
- [Estudios de caso](case-studies.md): Resultados reales en once proyectos.
- [Glosario](references/terms-and-definitions.md)
- [Procedencia y metadatos](provenance-metadata.md) *(futuro: documentacion etica de datos de entrenamiento)*

## Requisitos

- Foundry NukeX con `CopyCat` e `Inference` (GPU: Apple Silicon o NVIDIA)
- Un escaneo fuente con informacion de imagen sobreviviente
- Una referencia con mejor color o mayor detalle espacial
- Resolve (o equivalente) para prealineacion y preparacion del contenedor
- Gestion de color ACES/OCIO
