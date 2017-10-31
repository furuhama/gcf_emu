'use strict';

var Sekigae = require('sekigae');
var s = new Sekigae();

exports.helloWorld = function helloWorld(req, res) {
  if (s.checkHoliday()) {
    res.send('It is holiday!!');
  } else {
    var memberList = s.getYaml(s.yamlName);
    var randomArray = s.getRandomArray(15);

    res.send(s.setMemberDeskHash(memberList, randomArray));
  };
};
