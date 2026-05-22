# Aprendizaje Automatico Personalizado para Restauracion Cinematografica

<p align="center">
  <a href="README.md">English</a> •
  <a href="docs/es/index.md">Documentacion en español</a> •
  <a href="https://github.com/fabiocolor/custom-machine-learning-for-film-restoration/releases/latest">Descargar plantillas</a>
</p>

Flujo de trabajo de restauracion basado en referencias para NukeX usando `CopyCat` e `Inference`. Entrena CNN pequenas con pares reales de fuente/referencia para recuperar croma perdido o detalle espacial en elementos filmicos degradados.

No es un plugin. Es un flujo de trabajo repetible y documentado para archivos, equipos de preservacion y profesionales de restauracion.

## Descargar las Plantillas de Nuke

Este flujo se basa en plantillas preconstruidas incluidas en este repositorio. Descarga la version mas reciente para tu version de Nuke desde la pagina de releases:

- [Descargar las ultimas plantillas de Nuke (`.nknc` y `.nkind`)](https://github.com/fabiocolor/custom-machine-learning-for-film-restoration/releases/latest)

## Modos de Recuperacion

| Modo | Usar cuando | Objetivo de verdad de referencia |
| --- | --- | --- |
| **Recuperacion de croma** | La luma/detalle esta intacta, pero el croma esta desvanecido, desplazado o colapsado | Fuente `Y` + Referencia `Cb/Cr` |
| **Recuperacion espacial** | El color es aceptable, pero el detalle/nitidez/grano esta degradado frente a la referencia | Referencia `Y` + Fuente `Cb/Cr` |

Empieza con recuperacion de croma salvo que tu problema sea claramente espacial. No combines ambos en la misma construccion de objetivo: tratalos como pasadas separadas.

## Documentacion

Sigue estas paginas en orden:

1. **[Flujo de trabajo compartido](docs/es/start-here.md)**: Etapas 0-2: exportacion desde Resolve, configuracion de Nuke, curacion del dataset, alineacion, recorte compartido y decision de rama.
2. **[Recuperacion de croma](docs/es/chroma-recovery.md)**: Desde la Etapa 3: construccion del objetivo de croma, entrenamiento, inferencia y validacion.
3. **[Recuperacion espacial](docs/es/spatial-recovery.md)**: Desde la Etapa 3: construccion del objetivo espacial, entrenamiento, inferencia y validacion.

Material de apoyo:

- [Estudios de caso](docs/es/case-studies.md)
- [Glosario](docs/es/references/terms-and-definitions.md)
- [Procedencia y metadatos](docs/es/provenance-metadata.md)

## Requisitos

- Foundry NukeX con `CopyCat` e `Inference` (GPU: Apple Silicon o NVIDIA)
- Un escaneo fuente con informacion de imagen sobreviviente
- Una referencia con mejor color o mayor detalle espacial
- Resolve (o equivalente) para prealineacion y preparacion del contenedor
- Gestion de color ACES/OCIO

## Plantillas

| Edicion | Archivo |
| --- | --- |
| Nuke Indie | `templates/COLOR_RECOVERY_TEMPLATE_INDIE.nkind` |
| Nuke Non-Commercial | `templates/COLOR_RECOVERY_TEMPLATE.nknc` |

## Licencia

Esta plantilla de flujo de trabajo se proporciona con fines educativos y de investigacion en preservacion y restauracion cinematografica.
