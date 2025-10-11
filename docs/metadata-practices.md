# ML Restoration Metadata Practices

## Overview

Following practices established by ComfyUI workflows, C2PA (Coalition for Content Provenance and Authenticity), and IPTC standards for AI-generated content, this guide documents how to embed ML workflow metadata into restored film assets for archival transparency and reproducibility.

## Why Metadata Matters for Archival Restoration

**Transparency Requirements:**
- Archival institutions need to know exactly how digital assets were created
- ML-restored assets must declare their processing history
- Future archivists need to understand and potentially reproduce the work
- Ethical requirement to disclose AI/ML interventions

**Reproducibility:**
- Complete workflow documentation enables re-processing if needed
- Model versioning allows tracking of restoration decisions over time
- Training parameters document the specific approach used

**Standards Alignment:**
- IPTC Digital Source Type: "trainedAlgorithmicMedia" or "compositeWithTrainedAlgorithmicMedia"
- IPTC AI Generation fields for documenting ML processes
- C2PA content credentials for provenance tracking

## Metadata Fields for ML-Restored Film Assets

### Required Fields

**1. Digital Source Type** (IPTC)
```
Digital Source Type: trainedAlgorithmicMedia
or
Digital Source Type: compositeWithTrainedAlgorithmicMedia
```
Use "trainedAlgorithmicMedia" for fully ML-processed output, "compositeWithTrainedAlgorithmicMedia" when ML recovery is composited with original elements.

**2. ML Processing Declaration**
```
Description: Color recovery applied using custom supervised learning with CopyCat CNN
Creator Tool: Nuke [version], CopyCat [version]
Processing Date: YYYY-MM-DD
```

**3. Source Material Provenance**
```
Source: [Film Title], [Gauge], [Element Type]
Reference Material: [Reference Source Description]
Original Scan Date: YYYY-MM-DD
Original Scan Resolution: [width]x[height]
```

### Workflow-Specific Fields

**Training Metadata:**
```
ML Model Type: Custom CNN (CopyCat)
Training Method: Supervised learning
Training Dataset: [Shot ID], frames [frame range]
Training Date: YYYY-MM-DD
Training Duration: [steps/epochs]
Model Checkpoint: [checkpoint file path/hash]
Training Parameters:
  - Model Size: [Small/Medium/Large]
  - Batch Size: [number]
  - Learning Rate: [value]
  - Total Steps: [number]
```

**Recovery Type Classification:**
```
Recovery Type: Color Recovery (Reference-Based)
or
Recovery Type: Spatial Recovery (Reference-Based)
or
Recovery Type: Combined Recovery (Spatial + Color)

Recovery Approach:
  Color: [Reference-Based/Non-Reference]
  Spatial Sources: [e.g., "35mm internegative + 16mm print"]
```

**Reference Material Documentation:**
```
Reference Source: [DVD/Telecine/Film Element/Painting/Manual]
Reference Provenance: [Detailed description of reference authenticity]
Reference Authorization: [Permission/Rights documentation]
```

**Processing Pipeline:**
```
Pipeline Stage 1: Dataset Curation - [frame count] pairs selected
Pipeline Stage 2: Alignment - [method: F_Align/manual]
Pipeline Stage 3: Training - [checkpoint used]
Pipeline Stage 4: Inference - [frame range processed]
Pipeline Stage 5: Validation - [comparison method]
```

### Optional but Recommended

**Quality Control:**
```
QC Date: YYYY-MM-DD
QC Notes: [Observations about output quality, artifacts, appropriateness]
Comparison: [Link to MatchGrade baseline or traditional method comparison]
```

**Archival Decision Context:**
```
Restoration Goal: [What problem was being addressed]
Why ML Approach: [Why traditional methods insufficient]
Limitations: [Known limitations or compromises in output]
Alternative Approaches Considered: [What else was evaluated]
```

## Implementation Methods

### Method 1: IPTC/XMP Sidecar Files

Create `.xmp` sidecar files alongside rendered sequences:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
  <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
    <rdf:Description rdf:about=""
      xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/"
      xmlns:dc="http://purl.org/dc/elements/1.1/">

      <Iptc4xmpExt:DigitalSourceType>trainedAlgorithmicMedia</Iptc4xmpExt:DigitalSourceType>

      <dc:description>Color recovery applied using custom supervised learning with CopyCat CNN.
      Film: [Title], Source: 16mm positive print, Reference: PAL DVD.
      Training: [date], [steps] steps, checkpoint: [hash].</dc:description>

      <dc:creator>
        <rdf:Seq>
          <rdf:li>[Restorationist Name]</rdf:li>
        </rdf:Seq>
      </dc:creator>

      <Iptc4xmpExt:CreatorTool>Nuke 15.1v3, CopyCat</Iptc4xmpExt:CreatorTool>

    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>
```

### Method 2: JSON Workflow Files (ComfyUI Style)

Create `[shot_id]_workflow.json` alongside renders:

```json
{
  "workflow_version": "1.0",
  "film_title": "Film Title",
  "shot_id": "SHOT_001",
  "recovery_type": "color_recovery_reference_based",
  "processing_date": "2025-10-10",

  "source_material": {
    "element": "16mm positive print",
    "scan_date": "2024-01-15",
    "scan_resolution": "4096x3072",
    "gauge": "16mm",
    "generation": "positive_print"
  },

  "reference_material": {
    "type": "DVD",
    "source": "PAL DVD Release 2003",
    "authorization": "Licensed for archival use",
    "provenance": "Official studio release, verified color grading"
  },

  "training": {
    "method": "supervised_learning",
    "model_type": "CopyCat_CNN",
    "model_size": "Medium",
    "training_date": "2025-09-15",
    "dataset_frames": [1, 245, 1892, 3456],
    "training_steps": 60000,
    "checkpoint_hash": "sha256:abc123...",
    "batch_size": 3,
    "learning_rate": 0.0001
  },

  "pipeline": {
    "stage_01_dataset_curation": {
      "frames_selected": 4,
      "selection_criteria": "beginning, middle, end + one problematic frame"
    },
    "stage_02_alignment": {
      "method": "F_Align",
      "crop_applied": "16:9 safety crop, sprocket removal"
    },
    "stage_03_training": {
      "colorspace": "Linear -> YCbCr -> Linear",
      "channels_trained": "Cb, Cr (chroma only)",
      "luma_preservation": true
    },
    "stage_04_inference": {
      "frames_processed": "1-4234",
      "output_colorspace": "ACES2065-1"
    },
    "stage_05_validation": {
      "comparison_method": "MatchGrade baseline",
      "notes": "CopyCat preserved grain better than LUT approach"
    }
  },

  "quality_control": {
    "qc_date": "2025-09-16",
    "qc_by": "Restorationist Name",
    "notes": "Output appropriate for historical period, grain structure preserved",
    "known_limitations": "Minor chroma bleeding in high-contrast edges"
  },

  "nuke_script": "pipeline/04_inference_render/SHOT_001_inference.nk",
  "render_settings": {
    "format": "EXR",
    "compression": "DWAA",
    "bit_depth": "16-bit float"
  }
}
```

### Method 3: Embedded EXR Metadata

Use Nuke's metadata node to embed directly in EXR files:

```python
# In Nuke script, add MetadataNode before Write
metadata_node = nuke.nodes.ModifyMetaData()
metadata_node['metadata'].fromScript("""
    set exr/MLProcessing "CopyCat Color Recovery"
    set exr/RecoveryType "Reference-Based Color"
    set exr/TrainingDate "2025-09-15"
    set exr/ModelCheckpoint "checkpoint_60000.ckpt"
    set exr/SourceElement "16mm positive print"
    set exr/ReferenceSource "PAL DVD 2003"
    set exr/IPTCDigitalSourceType "trainedAlgorithmicMedia"
""")
```

### Method 4: Markdown Documentation (Current Practice)

Continue using `notes/experiments.md` but with structured format:

```markdown
## SHOT_001 - Color Recovery (2025-09-15)

**Recovery Type:** Reference-Based Color Recovery

**Source Material:**
- Element: 16mm positive print
- Scan: 2024-01-15, 4096x3072
- Condition: Severe cyan/magenta fading

**Reference Material:**
- Type: PAL DVD (2003 release)
- Provenance: Official studio release, verified color grading
- Authorization: Licensed for archival use

**Training Parameters:**
- Model: CopyCat Medium
- Dataset: 4 frames (1, 245, 1892, 3456)
- Steps: 60,000
- Date: 2025-09-15
- Checkpoint: `pipeline/03_copycat_training/SHOT_001/session_001/checkpoint_60000.ckpt`

**Pipeline:**
1. Dataset Curation: 4 representative frames selected
2. Alignment: F_Align, 16:9 crop + sprocket removal
3. Training: YCbCr chroma-only, luma preserved
4. Inference: Frames 1-4234
5. Validation: Compared to MatchGrade LUT baseline

**QC Notes:**
- Output historically appropriate for 1970s Eastmancolor stock
- Grain structure preserved better than traditional LUT approach
- Minor chroma bleeding in high-contrast edges (acceptable for archival)
- Approved for archival delivery

**Files:**
- Workflow: `pipeline/SHOT_001_workflow.json`
- Nuke Script: `pipeline/04_inference_render/SHOT_001_inference.nk`
- Training Log: `pipeline/03_copycat_training/SHOT_001/training.log`
```

## Best Practices

1. **Choose Appropriate Method for Your Institution:**
   - XMP sidecars: Industry standard, widely supported
   - JSON workflows: Developer-friendly, ComfyUI style
   - EXR metadata: Embedded in files, travels with assets
   - Markdown: Human-readable, Git-tracked, current practice

2. **Combine Multiple Methods:**
   - Use markdown for working notes
   - Export to XMP/JSON for final delivery
   - Embed critical info in EXR metadata

3. **Version Control:**
   - Track `notes/experiments.md` in Git
   - Include workflow JSON files in repository
   - Hash model checkpoints for verification

4. **Minimal Required Set:**
   At minimum, document:
   - Recovery type (color/spatial, reference/non-reference)
   - Source element description
   - Reference material provenance
   - Training date and checkpoint
   - Processing date
   - Restorationist/institution

5. **Archival Delivery Package:**
   Include:
   - Rendered sequences (EXR with embedded metadata)
   - XMP sidecar files
   - Workflow JSON
   - Complete `notes/experiments.md` excerpt for this shot
   - Model checkpoint file (if sharing)
   - Nuke script (optional)

## IPTC Standards Reference

Following IPTC's draft specification for AI-generated content metadata:

**New IPTC Fields (2024):**
- `Digital Source Type`: Classify as trained algorithmic media
- `AI Generation Tool`: Document ML framework/tool
- `AI Generation Prompt`: Not applicable for supervised learning restoration
- `AI Training Data`: Document reference material provenance
- `AI Disclosure`: Declare ML intervention for transparency

**Implementation Status:**
- ✅ Digital Source Type: Can implement now
- ✅ Custom fields via XMP: Can implement now
- ⏳ Full IPTC AI fields: Awaiting final specification

## C2PA Integration (Future)

Content Credentials (C2PA) for cryptographic provenance:
- Digital signatures verify workflow authenticity
- Chain of custody from scan to ML processing to delivery
- Tamper-evident metadata
- **Status:** Emerging standard, monitor for adoption in archival sector

## Related Documentation

- [CopyCat SOP](copycat_sop.md) - Current QC & Logging practices
- [Color Recovery Workflow](chroma-recovery.md) - Recovery methodology
- [Spatial Recovery Workflow](spatial-recovery.md) - Spatial recovery approach
- IPTC Standard: https://iptc.org/news/draft-for-public-comment-new-photo-metadata-fields-for-ai-generated-content/
- C2PA: https://c2pa.org/

## Contributing

As metadata standards for ML-restored archival materials evolve, this documentation should be updated. Consider:
- Archival institution requirements
- Emerging standards (IPTC, C2PA)
- Industry practices
- Legal/ethical disclosure requirements
