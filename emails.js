function GetEmailsFromString(input) {
  var ret = [];
  var email = /\"([^\"]+)\"\s+\<([^\>]+)\>/g

  var match;
  while (match = email.exec(input)) {
    ret.push({'name':match[1], 'email':match[2]});
  }
  return ret;
}

var str = '"Name one" <foo@domain.com>, ..., "And so on" <andsoon@gmx.net>';
var emails = GetEmailsFromString(str);