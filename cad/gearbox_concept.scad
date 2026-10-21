// Two-stage helical gearbox — packaging concept only
// Open with OpenSCAD. Smooth gear blanks are intentional; no gear teeth are modeled.
// Units: millimetres. Not for manufacturing or load-bearing use.

$fn = 72;

// Layout variables
wall = 8;
base_z = 0;
housing_length = 310;
housing_width = 155;
housing_height = 110;
shaft_z = 55;
stage1_cd = 125; // approximate layout centre distance
stage2_cd = 150; // approximate layout centre distance
gear1_d = 80;
pinion1_d = 24;
gear2_d = 100;
pinion2_d = 30;
gear_width1 = 25;
gear_width2 = 30;
shaft_d = 20;

module rounded_box(size=[10,10,10], r=4) {
    // Simple rounded rectangular envelope using minkowski; visual concept only.
    minkowski() {
        cube([size[0]-2*r, size[1]-2*r, size[2]-2*r], center=true);
        sphere(r=r, $fn=16);
    }
}

module shaft(x, y, z, len=70, d=shaft_d) {
    translate([x,y,z])
        rotate([90,0,0])
            cylinder(h=len, d=d, center=true);
}

module gear_blank(x, y, z, d, width) {
    // Smooth cylindrical blank used to show gear packaging; not a gear model.
    translate([x,y,z])
        rotate([90,0,0])
            cylinder(h=width, d=d, center=true);
}

module housing() {
    difference() {
        translate([housing_length/2, 0, housing_height/2])
            rounded_box([housing_length, housing_width, housing_height], 8);
        translate([housing_length/2, 0, housing_height/2 + wall])
            cube([housing_length-2*wall, housing_width-2*wall,
                  housing_height], center=true);
        // Conceptual open top to make internals visible
        translate([housing_length/2, 0, housing_height + 5])
            cube([housing_length+2, housing_width+2, 20], center=true);
    }
}

module layout() {
    // Shafts run along Y. X-Z positions are schematic for packaging review.
    x_in = 35;
    x_mid = x_in + stage1_cd;
    x_out = x_mid + stage2_cd;

    // Input and intermediate shafts
    color("silver") shaft(x_in, 0, shaft_z, 105, 18);
    color("silver") shaft(x_mid, 0, shaft_z, 105, 22);
    color("silver") shaft(x_out, 0, shaft_z, 105, 25);

    // Stage 1: small pinion at input, large gear on intermediate shaft
    color("gold") gear_blank(x_in, 0, shaft_z, pinion1_d, gear_width1);
    color("goldenrod") gear_blank(x_mid, 0, shaft_z, gear1_d, gear_width1);

    // Stage 2: small pinion on intermediate shaft, large gear on output shaft
    // Offset along Y to distinguish the two meshes in this simplified schematic.
    color("orange") gear_blank(x_mid, -25, shaft_z, pinion2_d, gear_width2);
    color("peru") gear_blank(x_out, -25, shaft_z, gear2_d, gear_width2);

    // Bearing blocks shown as simplified support collars
    for (x = [x_in, x_mid, x_out]) {
        for (y = [-42, 42]) {
            color("dimgray")
                translate([x, y, shaft_z])
                    rotate([90,0,0])
                        difference() {
                            cylinder(h=12, d=38, center=true);
                            cylinder(h=14, d=shaft_d+5, center=true);
                        }
        }
    }
}

color("lightgray", 0.25) housing();
layout();

// Add labels and dimensions in a drawing/CAD tool if using this as a portfolio concept.
// Geometry is schematic: the stage centre distances and blank diameters are not a fully
// interference-checked or standards-rated gear design.
