$('.stars a').on('click', function(){
    $('.stars span span.rate, .stars a').removeClass('active');
    $(this).addClass('active');
    $('.stars span').addClass('active');
    var value = $(this).attr('value');
    $('#stars_rate').val(value); // Expected to assign the value to the form attribute
});
$(document).ready(function() {
    $( "#star_rate" ).hide();
    $('label[for="stars_rate"]').hide();
});