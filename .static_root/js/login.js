
$("#loginForm").submit(function(event){
  var username = $("input#username").val();
  var password = $("input#password").val();

  logIn(username, password);
})

function logIn(username, password) {
  console.log(username);
  var token = '';
  $.ajax({
    type: "POST",
    url: "http://localhost:8000/member/api/login/",
    data: {'username': username, 'password': password, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
    dataType: "json",
    success: function (response) {
      console.log(response);
      token = response.token;
      localStorage.setItem('token', token);
      $("#result").html(token);
      // location.href='http://localhost:8000/book/main/';
    },
    error: function(request, status, error) {
      $("#result").html(error);
    }
  });
  // event.preventDefault();
}
