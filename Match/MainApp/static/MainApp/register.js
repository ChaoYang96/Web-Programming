$(document).ready(function() {
  $('#registerForm').submit(function() {
    var fName = $('#firstName').val();
    var lName = $('#lastName').val();
    var age = $('#age').val();
    var dob = $('#dob').val();
    var gender = $("name=['gender']").val();
    var email = $('#email').val();
    var pwd = $('#pwd').val();

    alert(pwd);

    ajaxReq = {
      url: '/newUser/',
      type: 'POST',
      dataType: 'json',
      data: {
        'fName': fName,
        'lName': lName,
        'age': age,
        'dob': dob,
        'gender': gender,
        'email': email,
        'pwd': pwd,
        //'pic': $('#profilePic').val()
      },
      success: function(data) {
        for (var i = 0; i < data.length; i++) {
          alert(data[i]);
        }
      }
      error: function() {
        alert("Something went wrong !");
      }
    }

    $.ajax(ajaxReq);
  });
});
