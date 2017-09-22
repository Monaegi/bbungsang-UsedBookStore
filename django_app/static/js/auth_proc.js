
var token = localStorage.getItem('token');
console.log(token);
var test = accessPage(token);

function accessPage(token) {
  $.ajax({
    type: "GET",
    url: "http://localhost:8000/book/buy/register/",
    // dataType: 'json',
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Authorization", token);
    },
    success: function (response) {
      alert('접근 성공!');
      console.log(response);
    },
    error: function(request, status, error) {
      alert(error);
    }
  });
  // event.preventDefault();
}
