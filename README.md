Two-Stage Helical Gearbox — Educational Design Portfolio
An original, preliminary engineering study of a two-stage helical gearbox using Python calculations and a parametric OpenSCAD concept model.
Status: Educational concept only — not a production-ready or safety-certified design. The calculations are first-pass sizing estimates. Gear tooth strength, fatigue, shaft deflection, bearings, keys/splines, lubrication, thermal behavior, housing stiffness, noise, and manufacturing tolerances require detailed verification before real-world use.
Design brief
Input power: 2.0 kW
Input speed: 1,500 rpm
Target reduction: 16:1
Arrangement: two reduction stages, each nominally 4:1
Stage 1 teeth: 20-tooth pinion / 80-tooth gear
Stage 2 teeth: 20-tooth pinion / 80-tooth gear
Illustrative normal modules: 2.5 mm (stage 1), 3.0 mm (stage 2)
Illustrative helix angle: 20°
Illustrative pressure angle: 20° (normal)
Illustrative face widths: 25 mm and 30 mm
These are assumed for a learning exercise, not selected from a complete load-rating standard.
Repository structure
.
├── README.md
├── requirements.txt
├── src/
│   └── gearbox_calculations.py
├── cad/
│   └── gearbox_concept.scad
└── docs/
    ├── engineering_report.md
    └── verification_checklist.md
​
Run the calculations
Python 3.10+; no third-party packages are required.
python src/gearbox_calculations.py
​
The script prints the ratio, speed, torque, pitch diameters, centre distances, approximate tangential loads, and preliminary shaft diameter estimates.
View the CAD concept
Install the free OpenSCAD application.
Open cad/gearbox_concept.scad.
Press F5 for preview or F6 for render.
Export an STL only if you need a visual reference; this model is a simplified layout concept.
The CAD script deliberately uses smooth gear blanks rather than pretending to provide validated helical tooth geometry. It is intended to communicate packaging, shaft positions, and a housing envelope—not to manufacture gears.
Suggested next improvements
Add a gear-rating calculation using an applicable standard (e.g., ISO 6336 or AGMA) and clearly state all factors.
Select bearings from manufacturer catalogues and calculate life from equivalent dynamic load.
Check shaft bending, torsion, fatigue, deflection, and critical speed.
Define keys/splines, fits, tolerances, seals, lubrication method, and housing split.
Replace smooth gear blanks with a verified gear-generation workflow and validate CAD interference.
Add drawings, a bill of materials, and a design review log.
