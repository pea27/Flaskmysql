$(function() {
    $('#btnSignUp').click(function() {
 
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                var myObj = JSON.parse(response);
                $('#message').html(myObj.html);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});