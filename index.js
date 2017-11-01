'use strict';

var Sekigae = require('sekigae');
var s = new Sekigae();
var url = s.url;
var text = s.getText();

exports.helloWorld = function helloWorld(req, res) {
  s.sendPostRequest(url, text);

  res.send(s.makeMainText());
};
