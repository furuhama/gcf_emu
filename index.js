'use strict';

var sekigae = require('sekigae');

exports.helloWorld = function helloWorld(req, res) {

  console.log(sekigae.my_func); // WORK
  console.log(sekigae.my_func2); // WORK
  res.send(sekigae.my_func2); // WORK
};
