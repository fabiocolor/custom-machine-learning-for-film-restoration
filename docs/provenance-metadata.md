---
layout: default
title: Provenance & Metadata
nav_order: 7
---

<div class="language-switch"><strong>Language:</strong> English | <a href="{{ '/es/provenance-metadata/' | relative_url }}">Español</a></div>

# Provenance and Metadata for ML Restoration

> **Future work.** This document outlines an approach to ethical training data documentation for ML-based film restoration. Implementation details are still being developed.

## Motivation

ML restoration should be transparent and reproducible. Declaring what was trained, on what sources, with what parameters allows future practitioners and archives to understand and audit the work.

## Core Principles

- **Declare ML processing** — tag outputs with tool, method, and processing date.
- **Track provenance** — record source/reference element types, scan details, and authorization.
- **Record training metadata** — dataset shots/frames, steps, model size, checkpoint.
- **Classify recovery type** — Color (Reference/Non-Reference), Spatial, or Combined.

## Proposed Approach

### IPTC Digital Source Type

Tag outputs with `trainedAlgorithmicMedia` or `compositeWithTrainedAlgorithmicMedia` to communicate that ML processing was involved.

### EXR Metadata (Nuke)

Use a `ModifyMetaData` node before `Write` to embed provenance keys that downstream tools (Resolve, archival systems) can read:

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

### Sidecar Files

Machine-readable JSON and human-readable text alongside renders. See the previous version of this document for example templates.

### Resolve Integration

Import EXR metadata via Resolve's Metadata panel. Map to Description, Scene/Shot/Take, Keywords, Creator, Rights, Dates. Use Batch Change for common fields.

## Standards Context

- IPTC fields communicate AI/ML classification. Pair with institutional policy text.
- C2PA / Content Credentials can be layered later for cryptographic provenance.
