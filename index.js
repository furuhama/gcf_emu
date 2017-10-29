// var sekigae = require('sekigae');

exports.helloWorld = function helloWorld(req, res) {
  var sekigae = require('sekigae');
  console.log(sekigae.my_func);

  res.send('hello,');
  res.send('12345');
};
