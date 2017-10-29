// var sekigae = require('sekigae');

exports.helloWorld = function helloWorld(req, res) {
  var sekigae = require('sekigae');
  console.log(sekigae.my_func2);
  res.send(sekigae.my_func2);
};
