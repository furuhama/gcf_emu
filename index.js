'use strict';

var Sekigae = require('sekigae');
var s = new Sekigae();

// exports.helloWorld = function helloWorld(req, res) {
//   console.log(s.my_func1()); // WORK
//   console.log(s.my_func2()); // WORK
//   console.log(Sekigae.my_func3) // WORK
//   res.send(s.my_func1()); // WORK
// };

exports.helloWorld = function helloWorld(req, res) {
  console.log(s.getYaml('name_list_1.yaml'));
  console.log(s.getYaml('name_list_2.yaml'));
  res.send(s.getToday(0));
};