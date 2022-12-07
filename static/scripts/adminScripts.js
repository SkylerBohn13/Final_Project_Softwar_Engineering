
const serverUrl='http://127.0.0.1:5000';


function postLogin(username, password) {
  console.log(username + " " + password);
  var path = "/v1/login";
  var url = serverUrl + path;
  var xhr = new XMLHttpRequest();
  xhr.open("POST", url, false);
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhr.send("username=" + username + "&password=" + password);

  console.log(xhr.getAllResponseHeaders());
  return {status: xhr.status, body: xhr.responseText};
}

function postVoter(fname, lname, address) {
  var path = "/v1/admin/voters";
  var url = serverUrl + path;
  var body = JSON.stringify({first_name: fname, last_name: lname, address: address})
  console.log(body)
  var xhr = new XMLHttpRequest();
  xhr.open("POST", url, false);
  xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.send(body);

  var resp = xhr.response;
  var respStatus = xhr.status;
  var respBody = resp.details;
  console.log("jkfsdkjhfkdhs");
  console.log(xhr.responseText);
  return xhr.responseText;
}

function postVote(id, president, vice_president, senator, representative) {
  var path = "/v1/admin/votes";
  var url = serverUrl + path;
  var body = JSON.stringify({voter_id: id, president: president, vice_president: vice_president, senator: senator, representative: representative})
  var xhr = new XMLHttpRequest();
  xhr.open("POST", url, false);
  xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.send(body);
  console.log(xhr.getAllResponseHeaders());
  return {status: xhr.status, body: xhr.responseText};
}

function fillCandidates(){
  setCandidates("Bugs", "Bunny", "president");
  setCandidates("Marvin", "Martian", "president");
  setCandidates("Elmer", "Fudd", "vice-president");
  setCandidates("Porky", "Pig", "vice-president");
  setCandidates("Yosemite", "sam", "senator");
  setCandidates("Pepe", "Le Pew", "senator");
  setCandidates("Tweety", "Bird", "representative");
  setCandidates("Daffy", "Duck", "representative");
  
}

function setCandidates(fname, lname, position){
  var path = "/v1/admin/candidates";
  var url = serverUrl + path;
  var body = JSON.stringify({first_name: fname, last_name: lname, position: position});
  var xhr = new XMLHttpRequest();
  xhr.open("POST", url, false);
  xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.send(body);
  console.log(xhr.getAllResponseHeaders());
  return {status: xhr.status, body: xhr.responseText};
}

function retrieveVoters() {
  var path = "/v1/admin/voters";
  var url = serverUrl + path;

  var xhr = new XMLHttpRequest();
  xhr.open("GET", url, false);
  xhr.send(null);
  return {status: xhr.status, body: xhr.responseText};

}

function retrieveCandidates() {
  var path = "/v1/admin/candidates";
  var url = serverUrl + path;

  var xhr = new XMLHttpRequest();
  xhr.open("GET", url, false);
  xhr.send(null);
  return {status: xhr.status, body: xhr.responseText};
}

function retrieveVotes() {
   var path = "/v1/admin/votes";
   var url = serverUrl + path;

   var xhr = new XMLHttpRequest();
   xhr.open("GET", url, false);
   xhr.send(null);
   return {status: xhr.status, body: xhr.responseText};

 }

 function setCookie(name,value,days) {
  var expires = "";
  if (days) {
      var date = new Date();
      date.setTime(date.getTime() + (days*24*60*60*1000));
      expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for(var i=0;i < ca.length;i++) {
      var c = ca[i];
      while (c.charAt(0)==' ') c = c.substring(1,c.length);
      if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
  }
  return null;
}
function eraseCookie(name) {   
  document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}
