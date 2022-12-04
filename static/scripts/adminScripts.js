
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

function retrieveVoters() {
  var path = "/v1/voters";
  var url = serverUrl + path;

  var xhr = new XMLHttpRequest();
  xhr.open("GET", url, false);
  xhr.send(null);
  return {status: xhr.status, body: xhr.responseText};

}
