'use strict';

var Sekigae = require('sekigae');
var s = new Sekigae();

var request = require('request');
var options = {
  url: 'YOUR-URL-HERE',
  method: 'POST',
  headers: { 'Content-Type' : 'application/json' },
  json: true,
  body: { 'text' : 'konichiwa' }
};

exports.helloWorld = function helloWorld(req, res) {
  request(options, function(error, response, body) {
    if (!error && response.statusCode == 200) {
      console.log(body.name);
    } else {
      console.log('error: ' + response.statusCode)
    };
  });

  console.log(process.env.SLACK_URL);

  res.send(s.makeMainText());
};
