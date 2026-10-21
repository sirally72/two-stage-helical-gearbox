#!/usr/bin/env python3
"""
Two-stage helical gearbox — preliminary educational calculations.

All inputs are illustrative assumptions. This script is not a gear-rating
standard and does not validate tooth-root/contact strength, bearings, fatigue,
deflection, thermal limits, or manufacturability.
"""
from dataclasses import dataclass
from math import cos, radians, pi, tan

@dataclass(frozen=True)
class Stage:
    name: str
    pinion_teeth: int
    gear_teeth: int
    normal_module_mm: float
    helix_angle_deg: float
    normal_pressure_angle_deg: float
    face_width_mm: float

    @property
    def ratio(self) -> float:
        return self.gear_teeth / self.pinion_teeth

    @property
    def transverse_module_mm(self) -> float:
        return self.normal_module_mm / cos(radians(self.helix_angle_deg))

    @property
    def pinion_pitch_diameter_mm(self) -> float:
        return self.transverse_module_mm * self.pinion_teeth

    @property
    def gear_pitch_diameter_mm(self) -> float:
        return self.transverse_module_mm * self.gear_teeth

    @property
    def centre_distance_mm(self) -> float:
        return (self.pinion_pitch_diameter_mm + self.gear_pitch_diameter_mm) / 2

    @property
    def transverse_pressure_angle_deg(self) -> float:
        beta = radians(self.helix_angle_deg)
        alpha_n = radians(self.normal_pressure_angle_deg)
        return __import__("math").degrees(__import__("math").atan(tan(alpha_n) / cos(beta)))


def torque_nm(power_kw: float, speed_rpm: float) -> float:
    """T = 9550 * P(kW) / n(rpm)."""
    if power_kw < 0 or speed_rpm <= 0:
        raise ValueError("Power must be non-negative and speed must be positive.")
    return 9550.0 * power_kw / speed_rpm


def shaft_diameter_mm(torque_nm_value: float, allowable_shear_mpa: float = 40.0) -> float:
    """Solid circular shaft torsion-only estimate; excludes bending/keyways/fatigue."""
    if torque_nm_value < 0 or allowable_shear_mpa <= 0:
        raise ValueError("Torque must be non-negative and allowable stress positive.")
    torque_nmm = torque_nm_value * 1000.0
    return ((16.0 * torque_nmm) / (pi * allowable_shear_mpa)) ** (1.0 / 3.0)


def stage_loads(stage: Stage, torque_on_pinion_nm: float):
    """Pitch-line tangential force and approximate axial force for a helical gear."""
    d_m = stage.pinion_pitch_diameter_mm / 1000.0
    ft_n = 2.0 * torque_on_pinion_nm / d_m
    beta = radians(stage.helix_angle_deg)
    fa_n = ft_n * tan(beta)
    return ft_n, fa_n


def main():
    power_kw = 2.0
    input_rpm = 1500.0
    mesh_efficiency = 0.97  # illustrative per mesh, not a guaranteed value
    stages = [
        Stage("Stage 1", 20, 80, 2.5, 20.0, 20.0, 25.0),
        Stage("Stage 2", 20, 80, 3.0, 20.0, 20.0, 30.0),
    ]

    input_torque = torque_nm(power_kw, input_rpm)
    speed = input_rpm
    torque = input_torque
    total_ratio = 1.0

    print("TWO-STAGE HELICAL GEARBOX — PRELIMINARY EDUCATIONAL RESULTS")
    print("=" * 62)
    print(f"Input power: {power_kw:.2f} kW")
    print(f"Input speed: {input_rpm:.1f} rpm")
    print(f"Input torque: {input_torque:.2f} N·m")
    print()

    for s in stages:
        ratio = s.ratio
        ft, fa = stage_loads(s, torque)
        print(s.name)
        print(f"  Tooth ratio: {s.gear_teeth}/{s.pinion_teeth} = {ratio:.2f}:1")
        print(f"  Normal module: {s.normal_module_mm:.2f} mm")
        print(f"  Transverse module: {s.transverse_module_mm:.3f} mm")
        print(f"  Pinion pitch diameter: {s.pinion_pitch_diameter_mm:.2f} mm")
        print(f"  Gear pitch diameter: {s.gear_pitch_diameter_mm:.2f} mm")
        print(f"  Nominal centre distance: {s.centre_distance_mm:.2f} mm")
        print(f"  Face width (assumed): {s.face_width_mm:.1f} mm")
        print(f"  Tangential load at pinion pitch circle: {ft:.1f} N")
        print(f"  Approx. axial load magnitude: {fa:.1f} N")
        print(f"  Torsion-only shaft estimate at pinion torque: "
              f"{shaft_diameter_mm(torque):.1f} mm (40 MPa assumed)")
        speed /= ratio
        torque *= ratio * mesh_efficiency
        total_ratio *= ratio
        print()

    output_power_kw = power_kw * mesh_efficiency ** len(stages)
    print("OVERALL")
    print(f"  Total ratio: {total_ratio:.2f}:1")
    print(f"  Ideal kinematic output speed: {input_rpm / total_ratio:.2f} rpm")
    print(f"  Illustrative output power at assumed mesh efficiency: {output_power_kw:.3f} kW")
    print(f"  Illustrative output torque: {torque:.2f} N·m")
    print()
    print("LIMITATIONS")
    print("- These are preliminary equations and assumed values, not a certified design.")
    print("- Shaft diameter is torsion-only and must not be used as a final shaft selection.")
    print("- Gear tooth bending/contact stress and bearing life are not calculated.")
    print("- Confirm geometry, loads, material, lubrication, tolerances, and safety factors.")

if __name__ == "__main__":
    main()
