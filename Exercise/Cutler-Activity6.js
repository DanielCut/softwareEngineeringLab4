var shape = "";

function sides() {
    var numSides = prompt("Enter number of sides between 3-7")
    if(numSides == 3) {
        shape = "Square";
    } else if(numSides == 4) {
        shape = "Triangle";
    } else if(numSides == 5) {
        shape = "Pentagon";
    } else if(numSides == 6) {
        shape = "Hexagon";
    } else if(numSides == 7) {
        shape = "Heptagon";
    }
    alert("Number of sides: " + numSides + "\nName of the polygon: " + shape);
    return numsides;
}

function converShape() {
    if(numSides == 3) {
        convShape = "Square";
    } else if(numSides == 4) {
        convShape = "Triangle";
    } else if(numSides == 5) {
        convShape = "Pentagon";
    } else if(numSides == 6) {
        convShape = "Hexagon";
    } else if(numSides == 7) {
        convShape = "Heptagon";
    }
}
