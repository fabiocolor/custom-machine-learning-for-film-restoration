---
layout: default
title: Procedencia y Metadatos
parent: Español
nav_order: 6
permalink: /es/provenance-metadata/
---

<div class="language-switch"><strong>Idioma:</strong> <a href="{{ '/provenance-metadata/' | relative_url }}">English</a> | Español</div>

# Procedencia y Metadatos para Restauracion con ML

> **Trabajo futuro.** Este documento esboza un enfoque para documentar datos de entrenamiento de forma etica en restauracion cinematografica basada en ML. Los detalles de implementacion aun estan en desarrollo.

## Motivacion

La restauracion con ML debe ser transparente y reproducible. Declarar que se entreno, con que fuentes y con que parametros permite que futuros profesionales y archivos entiendan y auditen el trabajo.

## Principios Basicos

- **Declarar el procesamiento con ML**: etiquetar las salidas con herramienta, metodo y fecha de procesamiento.
- **Rastrear procedencia**: registrar tipos de elemento fuente/referencia, detalles de escaneo y autorizacion.
- **Registrar metadatos de entrenamiento**: planos/fotogramas del dataset, pasos, tamano del modelo y checkpoint.
- **Clasificar el tipo de recuperacion**: Color (con Referencia/sin Referencia), Espacial o Combinada.

## Enfoque Propuesto

### IPTC Digital Source Type

Etiqueta las salidas con `trainedAlgorithmicMedia` o `compositeWithTrainedAlgorithmicMedia` para comunicar que hubo procesamiento con ML.

### Metadatos EXR (Nuke)

Usa un nodo `ModifyMetaData` antes de `Write` para insertar claves de procedencia que herramientas posteriores (Resolve, sistemas de archivo) puedan leer:

```python
metadata = nuke.nodes.ModifyMetaData()
metadata['metadata'].fromScript("""
  set exr/MLProcessing "CopyCat Color Recovery"
  set exr/RecoveryType "Reference-Based Color"
  set exr/SourceElement "16mm positive print"
  set exr/ReferenceSource "PAL DVD 2003"
  set exr/ModelCheckpoint "checkpoint_60000"
  set exr/IPTCDigitalSourceType "trainedAlgorithmicMedia"
""")
```

### Archivos Sidecar

JSON legible por maquina y texto legible por personas junto a los renders. Consulta la version anterior de este documento para ver plantillas de ejemplo.

### Integracion con Resolve

Importa metadatos EXR mediante el panel Metadata de Resolve. Asignalos a Description, Scene/Shot/Take, Keywords, Creator, Rights y Dates. Usa Batch Change para campos comunes.

## Contexto de Estandares

- Los campos IPTC comunican la clasificacion AI/ML. Acompanalo con texto de politica institucional.
- C2PA / Content Credentials puede agregarse despues para procedencia criptografica.
