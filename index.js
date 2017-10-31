'use strict';

var Sekigae = require('sekigae');
var s = new Sekigae();

exports.helloWorld = function helloWorld(req, res) {
  res.send(s.makeMainText());
};
