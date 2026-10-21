# Preliminary Engineering Report: Two-Stage Helical Gearbox

## 1. Purpose and scope

This report documents an educational, preliminary concept for a two-stage helical gearbox. The goal is to demonstrate a repeatable calculation workflow, basic gear geometry relationships, and a simple parametric CAD packaging concept. It is not a production design, certified design, or manufacturing drawing package.

## 2. Design requirements and assumptions

| Parameter | Assumed value |
|---|---:|
| Input power | 2.0 kW |
| Input speed | 1,500 rpm |
| Stage 1 tooth counts | 20 / 80 |
| Stage 2 tooth counts | 20 / 80 |
| Overall nominal ratio | 16:1 |
| Normal pressure angle | 20° |
| Helix angle magnitude | 20° |
| Stage 1 normal module | 2.5 mm |
| Stage 2 normal module | 3.0 mm |
| Stage 1 face width | 25 mm |
| Stage 2 face width | 30 mm |
| Illustrative mesh efficiency | 97% per stage |
| Illustrative allowable shaft shear stress | 40 MPa |

The helix hands and orientations, materials, heat treatment, duty cycle, service factor, shock loading, reliability target, lubrication, and design life have not been specified. The assumptions are for demonstrating calculations only.

## 3. Kinematic ratio and speed

For each stage, the nominal ratio is the driven gear tooth count divided by the driving pinion tooth count:

`i = z_gear / z_pinion = 80 / 20 = 4`

For two stages:

`i_total = 4 × 4 = 16`

Ignoring slip (gear pairs are positive drives), the nominal output speed is:

`n_out = 1500 / 16 = 93.75 rpm`

This is a kinematic result based on the chosen tooth counts.

## 4. Torque and power estimate

Input torque is estimated from:

`T (N·m) = 9550 × P (kW) / n (rpm)`

For 2.0 kW at 1,500 rpm, input torque is approximately 12.73 N·m.

If 97% efficiency is assumed for each mesh, estimated output power is:

`P_out = 2.0 × 0.97² ≈ 1.882 kW`

Estimated output torque is then approximately:

`T_out = 9550 × P_out / 93.75 ≈ 191.8 N·m`

This efficiency is illustrative. Actual efficiency depends on tooth geometry, alignment, surface finish, lubricant, seals, bearings, and operating conditions. The Python script calculates output torque by propagating stage torque and efficiency; use its printed result as the authoritative script output for this repository.

## 5. Preliminary geometry

For a helical gear, the transverse module is related to normal module by:

`m_t = m_n / cos(β)`

Pitch diameter is estimated from:

`d = m_t × z`

The nominal centre distance for a pair is:

`a = (d_pinion + d_gear) / 2`

Using the selected module and helix angle gives approximate centre distances near 127.8 mm for stage 1 and 153.4 mm for stage 2. The CAD file uses rounded schematic layout dimensions and is not automatically guaranteed to match the calculated values. A future revision should link the CAD layout parameters directly to the calculation outputs.

## 6. Preliminary loads

Tangential force at the pinion pitch circle is estimated from:

`F_t = 2T / d_pinion`

For an idealized helical mesh, axial-force magnitude can be approximated as:

`F_a ≈ F_t × tan(β)`

These are simplified loads. A complete gear analysis also resolves radial forces and checks the effects of load distribution, dynamic factors, alignment, and tooth geometry. Direction depends on rotation and helix hand, neither of which is fully specified here.

## 7. Shaft estimate limitations

The Python script includes a solid circular shaft diameter estimate based on torsion only:

`d = [16T / (π τ_allow)]^(1/3)`

This omits bending from gear forces, stress concentrations, keyways, fatigue, deflection limits, bearing spans, and critical speed. It is a learning calculation, not a final shaft size recommendation.

## 8. CAD concept

`cad/gearbox_concept.scad` provides a simplified packaging illustration with a housing envelope, shafts, bearing-support placeholders, and smooth cylindrical gear blanks. The blanks intentionally do not model helical teeth. This avoids suggesting that the model is suitable for gear manufacture or strength validation. The CAD layout is schematic and should be checked and revised before being used for dimensional claims.

## 9. Verification required before practical use

1. Define duty cycle, operating hours, shock/service factors, and required life.
2. Select materials, heat treatment, quality grade, and lubrication.
3. Rate tooth-root bending and flank contact stress using an applicable recognized method such as ISO 6336 or AGMA, with suitable factors and documented inputs.
4. Calculate radial and axial loads and select bearings from manufacturer data; verify life and static capacity.
5. Check shaft combined stress, fatigue, deflection, and critical speed.
6. Design keys/splines, shoulders, fits, seals, fasteners, housing split, and assembly access.
7. Verify interference, backlash, contact pattern, alignment, thermal behavior, lubrication, and noise.
8. Produce dimensioned drawings and obtain a competent engineering review before any fabrication or operation.

## 10. Conclusion

This project demonstrates a structured starting point for a gearbox portfolio: assumptions are explicit, the core calculations are repeatable in Python, and the CAD file provides a visual packaging concept. The next meaningful step is to verify each subsystem and update the report with traceable results rather than treating the current concept as production-ready.
