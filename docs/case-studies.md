# Case Studies

Real-world applications of custom machine learning-based film restoration, demonstrating both **color recovery** and **spatial recovery** workflows using supervised learning with CNNs in Nuke's CopyCat. Each case study includes project details, specific ML techniques used, challenges encountered, and results.

## Color Recovery Projects

### Reference-Based Recovery
Using DVDs, telecines, or other verifiable color-accurate sources:

### [Candy Candy Opening - 16mm](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies/candy-candy-opening.md)
Reference-based color recovery using PAL DVD source. Demonstrates chromogenic film dye fading correction while preserving 16mm grain structure.

### [Friends](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies/friends-chroma-recovery.md)
Reference-based color recovery using telecine source for film project restoration.

### [Frontier Experience](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies/frontier-experience-chroma-recovery.md)
Reference-based color recovery using video transfer reference.

### [Muralla Verde](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies/muralla-verde-chroma-recovery.md)
Trailer project demonstrating reference-based color restoration.

### Non-Reference Recovery
Inferring color from paintings, photographs, or manually created references:

### [Rebelión de Tapadas](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies/rebelion-de-tapadas-chroma-recovery.md)
Non-reference color recovery using colonial-era paintings by Pancho Fierro and Johann Moritz Rugendas. Historical archival material requiring period-accurate color reconstruction.

### [Ben](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies/ben-chroma-recovery.md)
Non-reference color recovery using manually created references in Photoshop.

---

## Spatial Recovery Projects

Example techniques for recovering spatial features (many more approaches possible):

### [Mission Kill - Gauge Recovery](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies/missionkill-combined-recovery.md)
**Technique: Gauge Recovery + Color Recovery**. Transfers spatial characteristics from 35mm internegative to 16mm positive print, combined with color restoration. Demonstrates comprehensive recovery using multiple ML techniques.

### [Knights of the Trail](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies/knights-trail-spatial-recovery.md)
Spatial reconstruction using multiple nitrate print sources. Demonstrates overlapping content technique for detail recovery.

### [El Tinterillo](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/docs/case-studies/tinterillo-spatial-recovery.md)
**Technique: Analog Video Reference Recovery**. Two-step telecine-based recovery process: trains on less-damaged telecine sections, then applies to full 16mm scan for comprehensive spatial reconstruction.

---

## Contributing Case Studies

Each case study should include:
- Source material details (format, condition, challenges)
- Workflow version and any variations from the standard template
- Demo video (YouTube unlisted or similar)
- Results and lessons learned
- Technical notes specific to that project
- Complete process documentation showing all workflow stages

---

[← Back to Main README](https://github.com/fabiocolor/nuke-chroma-recovery-template/blob/main/README.md)
