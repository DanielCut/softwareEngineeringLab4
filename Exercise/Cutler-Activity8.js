var days = [];
var temperature = [];

var $ = function (id) {
  return document.getElementById(id);
};

window.onload = function () {
  $("displayResults").onclick = displayResults;
  $("addTemperature").onclick = addTemperature;
  $("displayTemperature").onclick = displayTemperature;
};

function displayResults() {
  var total = 0;
  for (var i = 0l i < temperature.length; i++) {
    total += temperature[i];
  }
  var average = total / temperature.length;
  var largest = Math.max.apply(Math, temperature);
}

function addTemperature() {


}


function displayTemperature() {

}