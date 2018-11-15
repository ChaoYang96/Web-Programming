$(document).ready(function() {
  $('#register').click(function(e) {
    e.preventDefault();

    var hobbies = [];

    var fName = $('#firstName').val();
    var lName = $('#lastName').val();
    var age = $('#age').val();
    var dob = $('#dob').val();
    var gender = $('input[type=radio]:checked').val();
    var email = $('#email').val();
    var pwd = $('#pwd').val();
    var pic = $('#profilePic').val();

    $.each($("input[name='hobby']:checked"), function() {
      hobbies.push($(this).val());

    ajaxReq = {
      url: '/newUser/',
      type: 'POST',
      dataType: 'json',
      data: { 'fName': fName,
              'lName': lName,
              'age': age,
              'dob': dob,
              'gender': gender,
              'email': email,
              'pwd': pwd,
              'pic': pic
            },
      success: function(data) {
        alert("User profile created !");
      }
      error: function() {
        alert("Something went wrong during the process !");
      }
    }
    });
  });
});
