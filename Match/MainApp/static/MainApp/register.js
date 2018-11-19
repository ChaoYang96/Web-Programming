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

    $.each($("input[type=checkbox]:checked"), function() {
      hobbies.push($(this).val());
    });

    for (var i = 0; i < hobbies.length; i++) {
      console.log(hobbies[i]);
    }

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
        'hobbies[]': hobbies
      },
      success: function(data){

        alert("You have been successfully registered!");
      }
    }

    $.ajax(ajaxReq);
  });
});
