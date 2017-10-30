'use strict';

var Sekigae = require('sekigae');
var s = new Sekigae();

exports.helloWorld = function helloWorld(req, res) {
  console.log(s.my_func); // WORK
  // console.log(Sekigae.my_func2); // WORK
  res.send(s.my_func); // NOT WORK
};
