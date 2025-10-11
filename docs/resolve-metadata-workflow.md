# DaVinci Resolve Metadata Workflow for ML-Restored Assets

## Overview

Since DaVinci Resolve is the final delivery platform for graded and mastered film assets, this guide documents how to collect metadata generated in Nuke and embed it into Resolve deliverables for archival transparency.

## The Workflow Chain

```
Nuke (ML Processing) → EXR Sequence (with metadata) → Resolve (Grading/Delivery) → Final Master (with complete metadata)
```

## Metadata Collection from Nuke

### Method 1: Embed Metadata in EXR Files (Recommended)

In your Nuke write node, embed ML workflow metadata that Resolve can read:

**In Nuke Script (Python):**
```python
# Add before your Write node
metadata = nuke.nodes.ModifyMetaData()
metadata['metadata'].fromScript("""
    set exr/MLProcessing "CopyCat Color Recovery"
    set exr/RecoveryType "Reference-Based Color"
    set exr/FilmTitle "Film Title Here"
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

# Connect to Write node
write_node = nuke.nodes.Write()
write_node.setInput(0, metadata)
```

**Or manually in Nuke UI:**
1. Create `ModifyMetaData` node before Write
2. In Properties, click `metadata` tab
3. Add key/value pairs:
   - Key: `exr/MLProcessing`, Value: `CopyCat Color Recovery`
   - Key: `exr/RecoveryType`, Value: `Reference-Based Color`
   - etc.

**Verify metadata was written:**
```bash
exrheader your_sequence.0001.exr | grep "ML\|Recovery\|IPTC"
```

### Method 2: Generate Sidecar Files Alongside EXR

Create metadata files that travel with your renders:

**Structure:**
```
renders/
├── SHOT_001/
│   ├── SHOT_001.0001.exr
│   ├── SHOT_001.0002.exr
│   ├── ...
│   ├── SHOT_001_metadata.json       # Machine-readable
│   ├── SHOT_001_metadata.txt        # Human-readable
│   └── SHOT_001_workflow.json       # Full workflow details
```

**Example SHOT_001_metadata.json:**
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

**Example SHOT_001_metadata.txt (human-readable):**
```
ML RESTORATION METADATA - SHOT_001
=====================================

Film: Film Title
Shot: SHOT_001 (frames 0001-4234)

ML PROCESSING:
- Type: CopyCat Color Recovery
- Approach: Reference-Based Color
- Processing Date: 2025-10-10

SOURCE MATERIAL:
- Element: 16mm positive print
- Scan Resolution: 4096x3072
- Condition: Severe cyan/magenta fading

REFERENCE MATERIAL:
- Source: PAL DVD (2003 release)
- Provenance: Official studio release
- Authorization: Licensed for archival use

TRAINING:
- Date: 2025-09-15
- Model: CopyCat Medium
- Checkpoint: checkpoint_60000.ckpt
- Dataset: 4 frames (1, 245, 1892, 3456)
- Steps: 60,000

QUALITY NOTES:
- Output appropriate for 1970s Eastmancolor stock
- Grain structure preserved
- No significant artifacts

RESPONSIBLE PARTY:
- Restorationist: Your Name
- Institution: Archive Name

IPTC CLASSIFICATION:
- Digital Source Type: trainedAlgorithmicMedia
```

## Importing to DaVinci Resolve

### Step 1: Import EXR Sequence with Metadata

1. **Media Pool** → Right-click → **Import Media**
2. Select your EXR sequence
3. Resolve will import with embedded EXR metadata intact

**Verify metadata imported:**
1. Right-click clip in Media Pool → **Clip Attributes**
2. Go to **Metadata** tab
3. Look for your custom `exr/*` fields

### Step 2: Map EXR Metadata to Resolve Metadata Fields

Resolve has its own metadata fields. Map your EXR metadata:

**In Resolve's Metadata Panel:**
1. Select clip in Media Pool
2. Open **Metadata** panel (Shift+Cmd+6 / Shift+Ctrl+6)
3. Manually populate standard fields:

**Standard Resolve Metadata Fields to populate:**
```
Description: Color recovery using custom supervised learning with CopyCat CNN.
             Source: 16mm positive print. Reference: PAL DVD 2003.

Scene: SHOT_001
Shot: SHOT_001
Take: 1

Keywords: ML restoration, CopyCat, color recovery, reference-based,
          trainedAlgorithmicMedia

Creator: Your Name
Creator's Job Title: Film Restorationist
Creator's Contact: your.email@institution.org

Institution: Archive Name
Project: Film Title Restoration

Copyright: © Archive Name. ML-restored content.
Rights Usage Terms: Archival use only. ML processing disclosed.

Date Created: 2025-10-10
Metadata Date: 2025-10-10

Custom Fields:
- ML_Processing: CopyCat Color Recovery
- Recovery_Type: Reference-Based Color
- Training_Date: 2025-09-15
- Model_Checkpoint: checkpoint_60000
- IPTC_Digital_Source_Type: trainedAlgorithmicMedia
```

### Step 3: Batch Metadata Entry for Multiple Shots

For multiple shots, use Resolve's batch metadata:

1. Select all clips in Media Pool
2. Right-click → **Metadata` → **Batch Change**
3. Fill common fields:
   - Film Title
   - Institution
   - Restorationist
   - IPTC Digital Source Type: trainedAlgorithmicMedia

4. For shot-specific data, use CSV import (see below)

### Step 4: CSV Metadata Import (Advanced)

Create a CSV with shot-specific metadata:

**metadata_import.csv:**
```csv
Clip Name,Scene,Description,ML_Processing,Recovery_Type,Training_Date
SHOT_001,SHOT_001,"Color recovery, 16mm print to PAL DVD reference",CopyCat Color Recovery,Reference-Based Color,2025-09-15
SHOT_002,SHOT_002,"Color recovery, 16mm print to PAL DVD reference",CopyCat Color Recovery,Reference-Based Color,2025-09-16
SHOT_003,SHOT_003,"Spatial recovery, 16mm to 35mm internegative",CopyCat Spatial Recovery,Reference-Based Spatial,2025-09-20
```

**Import in Resolve:**
1. Media Pool → Right-click → **Metadata` → **Import from CSV**
2. Select your CSV file
3. Map CSV columns to Resolve metadata fields
4. Import

## Embedding Metadata in Final Deliverables

### For IMF/DCP Delivery

**IMF (Interoperable Master Format):**
- Resolve exports IMF packages with embedded metadata
- Ensure IPTC fields are populated
- Use **Description** field for ML processing disclosure

**Steps:**
1. **Deliver** page → **Render Settings**
2. Format: **IMF**
3. In **Options** tab:
   - Enable **Include Metadata**
   - Check **IPTC Metadata**
4. Verify ML processing info in Description field

**DCP (Digital Cinema Package):**
- DCP has limited metadata support
- Use **Content Title Metadata** for basic info
- Provide separate documentation files

### For ProRes/DNxHD Delivery

**Quicktime ProRes:**
```
1. Deliver page → Format: QuickTime
2. Codec: Apple ProRes 4444 XQ (preserves metadata)
3. In Video tab:
   - Enable "Export Metadata"
   - Enable "Export IPTC"
4. Metadata will embed in QuickTime atoms
```

**Verify ProRes metadata:**
```bash
ffprobe -show_format -show_streams your_file.mov | grep TAG
```

### For EXR/TIFF Image Sequences

If delivering image sequences (archival master):

**EXR Delivery:**
1. Keep embedded metadata from Nuke intact
2. Provide sidecar JSON/TXT files
3. Include README with metadata explanation

**TIFF Delivery:**
1. Use IPTC/XMP sidecar files (TIFF metadata limited)
2. Export metadata as `.xmp` alongside each TIFF
3. Generate master metadata document

## Archival Delivery Package Structure

Complete package for archival institution:

```
FILM_TITLE_RESTORATION/
│
├── MASTERS/
│   ├── SHOT_001/
│   │   ├── SHOT_001.0001.exr (with embedded metadata)
│   │   ├── SHOT_001.0002.exr
│   │   ├── ...
│   │   ├── SHOT_001_metadata.json
│   │   └── SHOT_001_metadata.txt
│   ├── SHOT_002/
│   └── ...
│
├── GRADED/
│   ├── FILM_TITLE_graded.mov (ProRes 4444 XQ with metadata)
│   └── FILM_TITLE_graded_metadata.json
│
├── DOCUMENTATION/
│   ├── 00_README.txt (overview of all metadata)
│   ├── 01_ML_WORKFLOW_OVERVIEW.md (copied from notes/experiments.md)
│   ├── 02_TRAINING_LOGS/ (CopyCat training logs per shot)
│   ├── 03_MODEL_CHECKPOINTS/ (optional, if sharing models)
│   └── 04_NUKE_SCRIPTS/ (inference scripts per shot)
│
└── METADATA/
    ├── master_metadata.json (all shots combined)
    ├── master_metadata.csv (spreadsheet format)
    └── IPTC_XMP_sidecars/ (XMP files for each shot)
```

## Resolve Metadata Panel Custom Fields

Create custom metadata fields in Resolve for ML restoration:

**Setup Custom Fields:**
1. Resolve → **Preferences** → **User** → **Metadata**
2. Click **+** to add custom fields:

**Recommended Custom Fields:**
```
ML_Processing (Text)
Recovery_Type (Text)
Training_Date (Date)
Model_Checkpoint (Text)
Source_Element (Text)
Reference_Source (Text)
IPTC_Digital_Source_Type (Text) - always "trainedAlgorithmicMedia"
Restorationist (Text)
QC_Notes (Text)
Known_Limitations (Text)
```

These will appear in Metadata panel for easy population.

## Automation Options

### Python Script: Nuke Metadata to JSON

```python
# nuke_metadata_export.py
import nuke
import json
from datetime import datetime

def export_metadata():
    """Export Nuke metadata to JSON for Resolve import"""

    write_node = nuke.selectedNode()
    if write_node.Class() != 'Write':
        print("Select a Write node")
        return

    # Collect metadata
    metadata = {
        "film_title": nuke.root()['project_name'].value(),
        "shot_id": nuke.root().name().split('/')[-1].replace('.nk', ''),
        "processing_date": datetime.now().strftime("%Y-%m-%d"),
        "nuke_version": nuke.NUKE_VERSION_STRING,
        "nuke_script": nuke.root().name(),
        "frame_range": f"{nuke.root().firstFrame()}-{nuke.root().lastFrame()}",
        "output_path": write_node['file'].value(),
    }

    # Add custom metadata from ModifyMetaData node if exists
    metadata_node = write_node.input(0)
    if metadata_node and metadata_node.Class() == 'ModifyMetaData':
        # Extract exr/* metadata fields
        meta_dict = metadata_node['metadata'].value()
        for key, value in meta_dict.items():
            if key.startswith('exr/'):
                clean_key = key.replace('exr/', '')
                metadata[clean_key] = value

    # Export to JSON
    output_file = write_node['file'].value().replace('.%04d.exr', '_metadata.json')
    with open(output_file, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"Metadata exported to: {output_file}")

# Run in Nuke Script Editor
export_metadata()
```

### Python Script: Generate Resolve CSV from Nuke Metadata

```python
# generate_resolve_csv.py
import json
import csv
import glob
import os

def generate_resolve_csv(metadata_dir, output_csv):
    """Generate CSV from JSON metadata files for Resolve import"""

    json_files = glob.glob(os.path.join(metadata_dir, "*_metadata.json"))

    # CSV headers (map to Resolve fields)
    headers = [
        'Clip Name', 'Scene', 'Description', 'Keywords',
        'ML_Processing', 'Recovery_Type', 'Training_Date',
        'Source_Element', 'Reference_Source', 'IPTC_Digital_Source_Type'
    ]

    rows = []

    for json_file in json_files:
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Build description
        description = f"{data.get('MLProcessing', 'ML Processing')}. "
        description += f"Source: {data.get('SourceElement', 'N/A')}. "
        description += f"Reference: {data.get('ReferenceSource', 'N/A')}."

        row = {
            'Clip Name': data.get('shot_id', ''),
            'Scene': data.get('shot_id', ''),
            'Description': description,
            'Keywords': 'ML restoration, CopyCat, trainedAlgorithmicMedia',
            'ML_Processing': data.get('MLProcessing', ''),
            'Recovery_Type': data.get('RecoveryType', ''),
            'Training_Date': data.get('TrainingDate', ''),
            'Source_Element': data.get('SourceElement', ''),
            'Reference_Source': data.get('ReferenceSource', ''),
            'IPTC_Digital_Source_Type': 'trainedAlgorithmicMedia'
        }
        rows.append(row)

    # Write CSV
    with open(output_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Resolve CSV generated: {output_csv}")
    print(f"Processed {len(rows)} shots")

# Usage
generate_resolve_csv('renders/', 'resolve_metadata_import.csv')
```

## Best Practices

1. **Embed Early, Embed Often:**
   - Add metadata in Nuke before rendering
   - Keep JSON sidecars alongside EXR sequences
   - Don't rely on manual entry in Resolve alone

2. **Standardize Terminology:**
   - Use consistent field names across all shots
   - Always use "trainedAlgorithmicMedia" for IPTC classification
   - Document your metadata schema

3. **Version Control:**
   - Track metadata JSON files in Git
   - Include in repository alongside nuke scripts

4. **Test Metadata Pipeline:**
   - Render test frame with metadata
   - Import to Resolve and verify fields appear
   - Adjust before processing full sequences

5. **Archival Package Checklist:**
   - ✅ EXR masters with embedded metadata
   - ✅ JSON sidecar files for each shot
   - ✅ Human-readable TXT summaries
   - ✅ Graded ProRes with metadata
   - ✅ Complete documentation package
   - ✅ Training logs and model checkpoints
   - ✅ Master metadata CSV

## Related Documentation

- [Metadata Practices](metadata-practices.md) - Complete metadata standards guide
- [CopyCat SOP](copycat_sop.md) - Workflow and QC practices
- [Color Recovery](chroma-recovery.md) - Recovery methodology
- [Spatial Recovery](spatial-recovery.md) - Spatial recovery approach

## Troubleshooting

**Resolve doesn't show EXR metadata:**
- Check EXR was written with metadata (`exrheader` to verify)
- Ensure metadata keys start with `exr/` prefix
- Try reimporting clip

**Custom fields not appearing:**
- Create custom metadata fields in Resolve Preferences first
- Restart Resolve after creating custom fields

**CSV import doesn't match clips:**
- Ensure "Clip Name" in CSV exactly matches clip name in Media Pool
- Check for extra spaces or different file extensions
