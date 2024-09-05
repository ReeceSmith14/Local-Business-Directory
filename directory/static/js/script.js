$(document).ready(function(){
    cardToggle();
    addFormValidate();

});

function cardToggle(){
    $(".toggle-button").click(function(){
        $(this).closest(".card").find(".contact-details").toggle();
    });
};

function addFormValidate() {
    $("#add-form-submit").on("click", function(event) {
        event.preventDefault(); // Prevent form submission

        let businessName = $("#business_name").val();
        let businessDescription = $("#business_description").val();
        let category = $("#category").val();
        let phone = $("#phone").val();
        let email = $("#email").val();
        let website = $("#website").val();
        let image = $("#image").val();

        // Remove any previous error messages and reset borders
        $(".error-message").remove(); // Remove all previous error messages
        $("#business_name, #business_description, #category, #phone, #email, #website, #image").css("border", "");

        let isValid = true; // Flag to check if the form is valid

        // Validate business name
        if (!businessName || businessName.length > 50) {
            $("#business_name").css("border", "2px solid red");
            $("#business_name").after("<span class='error-message' style='color: red;'>Field required, please use less than 50 characters</span>");
            isValid = false;
        } else {
            $("#business_name").css("border", "2px solid green");
        }

        // Validate business description
        if (!businessDescription || businessDescription.length > 255) {
            $("#business_description").css("border", "2px solid red");
            $("#business_description").after("<span class='error-message' style='color: red;'>Field required, please use less than 255 characters</span>");
            isValid = false;
        } else {
            $("#business_description").css("border", "2px solid green");
        }

        // Validate category (required)
        if (!category) {
            $("#category").css("border", "2px solid red");
            $("#category").after("<span class='error-message' style='color: red;'>Field required</span>");
            isValid = false;
        } else {
            $("#category").css("border", "2px solid green");
        }

        // Validate phone (must be exactly 11 characters if not empty)
        if (phone && phone.length !== 11) {
            $("#phone").css("border", "2px solid red");
            $("#phone").after("<span class='error-message' style='color: red;'>Phone number must be exactly 11 characters</span>");
            isValid = false;
        } else if (phone) {
            $("#phone").css("border", "2px solid green");
        }

        // Validate email (cannot exceed 255 characters)
        if (email && email.length > 255) {
            $("#email").css("border", "2px solid red");
            $("#email").after("<span class='error-message' style='color: red;'>Email cannot exceed 255 characters</span>");
            isValid = false;
        } else if (email) {
            $("#email").css("border", "2px solid green");
        }

        // Validate website (cannot exceed 255 characters)
        if (website && website.length > 255) {
            $("#website").css("border", "2px solid red");
            $("#website").after("<span class='error-message' style='color: red;'>Website cannot exceed 255 characters</span>");
            isValid = false;
        } else if (website) {
            $("#website").css("border", "2px solid green");
        }

        // Validate image (cannot exceed 255 characters)
        if (image && image.length > 255) {
            $("#image").css("border", "2px solid red");
            $("#image").after("<span class='error-message' style='color: red;'>Image URL cannot exceed 255 characters</span>");
            isValid = false;
        } else if (image) {
            $("#image").css("border", "2px solid green");
        }

        // Check that at least one of phone, email, or website is filled out
        if (!phone && !email && !website) {
            $("#phone, #email, #website").css("border", "2px solid red");
            $("#website").after("<span class='error-message' style='color: red;'>At least one of Number, Email, or Website must be filled out</span>");
            isValid = false;
        }

        // If all fields are valid, submit the form
        if (isValid) {
            // Show a success message
            $("#form-feedback").remove(); // Remove any previous feedback message
            $("#add-form").after("<p id='form-feedback' style='color: green;'>Form submitted successfully!</p>");

           // Reset the form fields
            $("#add-form")[0].reset();

            // reset all input borders to default
            $("#business_name, #business_description, #category, #phone, #email, #website, #image").css("border", "");
        }
    });
}


