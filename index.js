'use strict';

var sekigae = require('sekigae');
var my_val = 'hey, siri';
console.log(sekigae.my_func2); // DOES NOT WORK

exports.helloWorld = function helloWorld(req, res) {
  console.log(sekigae.my_func2); // DOES NOT WORK
  res.send(my_val); // WORK
};
