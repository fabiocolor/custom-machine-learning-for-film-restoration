# Provenance & Metadata for ML Restoration

Practical guide to document ML-based restoration for archival transparency and reproducibility, aligned with IPTC and C2PA concepts, and integrated with DaVinci Resolve delivery.

## Why It Matters
- Declare ML processing for ethical transparency and future reproducibility.
- Track source/reference provenance and training parameters.
- Align with IPTC Digital Source Type and provenance standards.

## Required Metadata
- Digital Source Type (IPTC): `trainedAlgorithmicMedia` or `compositeWithTrainedAlgorithmicMedia`.
- ML processing declaration: tool/version, processing date.
- Source/reference provenance: element type, scan details, authorization.
- Training metadata: dataset shots/frames, steps, model size, checkpoint.
- Recovery classification: Color (Reference/Non-Reference), Spatial (technique/inputs), or Combined.

## Embed in Nuke (EXR)
Use a `ModifyMetaData` node before `Write` to add EXR keys that Resolve can read.

Python snippet (equivalent UI entries):
```python
metadata = nuke.nodes.ModifyMetaData()
metadata['metadata'].fromScript("""
  set exr/MLProcessing "CopyCat Color Recovery"
  set exr/RecoveryType "Reference-Based Color"
  set exr/FilmTitle "Film Title"
  set exr/ShotID "SHOT_001"
  set exr/TrainingDate "2025-10-10"
  set exr/ModelCheckpoint "checkpoint_60000"
  set exr/SourceElement "16mm positive print"
  set exr/ReferenceSource "PAL DVD 2003"
  set exr/ProcessingDate "2025-10-10"
  set exr/Restorationist "Your Name"
  set exr/Institution "Archive Name"
  set exr/IPTCDigitalSourceType "trainedAlgorithmicMedia"
""")
write_node = nuke.nodes.Write(); write_node.setInput(0, metadata)
```

Verify on disk:
```
exrheader your_sequence.0001.exr | grep "ML\|Recovery\|IPTC"
```

## Sidecar Files (Optional/Recommended)
Keep machine- and human-readable records alongside renders.

Example `SHOT_001_metadata.json`:
```json
{
  "film_title": "Film Title",
  "shot_id": "SHOT_001",
  "frame_range": "0001-4234",
  "ml_processing": "CopyCat Color Recovery",
  "recovery_type": "Reference-Based Color",
  "source_element": "16mm positive print",
  "reference_source": "PAL DVD 2003",
  "training_date": "2025-09-15",
  "model_checkpoint": "checkpoint_60000.ckpt",
  "processing_date": "2025-10-10",
  "restorationist": "Your Name",
  "institution": "Archive Name",
  "iptc_digital_source_type": "trainedAlgorithmicMedia",
  "nuke_script": "pipeline/04_inference_render/SHOT_001_inference.nk",
  "notes": "Output appropriate for 1970s Eastmancolor stock. Grain preserved."
}
```

Example `SHOT_001_metadata.txt`:
```
ML RESTORATION METADATA - SHOT_001
Film: Film Title | Shot: SHOT_001 (0001-4234)
ML: CopyCat Color Recovery (Reference-Based) | Date: 2025-10-10
Source: 16mm positive print | Condition: Magenta/cyan fading
Reference: PAL DVD (2003) | Provenance: Official studio release
Training: Medium, 60k steps | Checkpoint: checkpoint_60000 | Frames: 1,245,1892,3456
IPTC Digital Source Type: trainedAlgorithmicMedia
```

## Resolve Integration
1) Import EXR: Resolve reads EXR keys; check Metadata panel.
2) Map to Resolve fields: fill Description, Scene/Shot/Take, Keywords, Creator, Rights, Dates; paste custom keys (e.g., `ML_Processing`, `Recovery_Type`).
3) Batch entry: select clips → Metadata → Batch Change for common fields (film title, institution, restorationist).

## Notes on Standards
- IPTC fields communicate AI/ML classification; pair with institutional policy text in Description/Rights.
- C2PA/Content Credentials can be layered later for cryptographic provenance.

