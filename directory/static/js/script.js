$(document).ready(function(){
    $(".toggle-button").click(function(){
        $(this).closest(".card").find(".contact-details").toggle();
    });

});

