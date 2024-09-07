$(document).ready(function(){
    cardToggle();
    formValidate();
    signInValidation();
    pagination();
});

function cardToggle(){
    $(".toggle-button").click(function(){
        $(this).closest(".card").find(".contact-details").toggle();
    });
};

function formValidate() {
    $(".form-submit").on("click", function(event) {
        
        $("#form-feedback").remove();

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
        if (!phone || !/^\d{11}$/.test(phone)) {
            $("#phone").css("border", "2px solid red");
            $("#phone").after("<span class='error-message' style='color: red;'>Phone number must be exactly 11 digits</span>");
            isValid = false;
        } else if (phone) {
            $("#phone").css("border", "2px solid green");
        }

        // Validate email (cannot exceed 255 characters)
        let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email pattern
        if (!email || email.length > 255 || !emailPattern.test(email)) {
            $("#email").css("border", "2px solid red");
            $("#email").after("<span class='error-message' style='color: red;'>Please enter a valid email address (must be less than 255 characters)</span>");
            isValid = false;
        } else if (email){
            $("#email").css("border", "2px solid green");
        }

        // Validate website (cannot exceed 255 characters)
        let urlPattern = /^(https?:\/\/)?[^\s/$.?#].[^\s]*$/i; // Basic URL pattern
        if (!website || (website.length > 255 || !urlPattern.test(website))) {
            $("#website").css("border", "2px solid red");
            $("#website").after("<span class='error-message' style='color: red;'>Please enter a valid URL (must be less than 255 characters)</span>");
            isValid = false;
        } else if (website) {
            $("#website").css("border", "2px solid green");
        }

        // Validate image (cannot exceed 255 characters)
        let imageUrlPattern = /^(https?:\/\/)?[^\s/$.?#].[^\s]*$/i; // Basic URL pattern for images
        if (image && (image.length > 255 || !imageUrlPattern.test(image))) {
            $("#image").css("border", "2px solid red");
            $("#image").after("<span class='error-message' style='color: red;'>Please enter a valid image URL (must be less than 255 characters)</span>");
            isValid = false;
        } else if (image) {
            $("#image").css("border", "2px solid green");
        }

         // Check that at least one of phone, email, or website is filled out
         if (!phone && !email && !website) {
            $("#phone, #email, #website").css("border", "2px solid red");
            $("#website").after("<span class='error-message' style='color: red;'>At least one of Number, Email, or Website must be filled out. </span>");
            isValid = false;
        }else{
            isValid = true;
        }

        // If all fields are valid, submit the form
        if (isValid) {

            $(".error-message").remove();
            // Show a success message
            $("#form-feedback").remove(); // Remove any previous feedback message
            $(".form").after("<p id='form-feedback' style='color: green;'>Form submitted successfully!</p>");

           // Reset the form fields
            $(".form")[0].reset();

            // reset all input borders to default
            $("#business_name, #business_description, #category, #phone, #email, #website, #image").css("border", "");
        };
        if (!isValid){
            event.preventDefault(); // Prevent form submission
        }
    });
};

function signInValidation(){
    $(".form-submit").on("click", function(event){
    let username = $("#username").val();
    let password = $("#password").val();
    
    let isValid = true; 

    // Validate username for sign in form

    if (!username){
        $("#username").css("border", "2px solid red");
        $("#username").after("<span class='error-message' style='color: red;'>Field required</span>");
        isValid = false;
    } else if (username){
        $("#username").css("border", "2px solid green");
    }
    
    // Validate password for sign in form

    if (!password){
        $("#password").css("border", "2px solid red");
        $("#password").after("<span class='error-message' style='color: red;'>Field required</span>");
        isValid = false;
    } else if (password){
        $("#password").css("border", "2px solid green");
    }

    if (!isValid){
        event.preventDefault(); 
    }else if (isValid){
        $(".error-message").remove();
            // Show a success message
            $("#form-feedback").remove(); // Remove any previous feedback message
            $(".form").after("<p id='form-feedback' style='color: green;'>Sign in successful!</p>");

           // Reset the form fields
            $(".form")[0].reset();

            // reset all input borders to default
            $("#password, #username").css("border", "");
    }
});
};

function pagination(){

    const cards = $('.card');  // All card elements
    const ul = $('.pagination');  // Pagination <ul> element

    const numberOfCards = cards.length;
    const numberOfPages = Math.ceil(numberOfCards / 10);  // Number of pages required

    // Initially show the first 10 cards and hide the rest
    cards.hide();  // Hide all cards first
    cards.slice(0, 10).show();  // Show first 10 cards

    // Create pagination links based on the number of pages
    for (let i = 1; i < numberOfPages; i++) {  // Corrected the loop to start at 0
        let newLi = `
        <li class="page-item">
            <p class="page-link">${i + 1}</a>
        </li>`;
        ul.children().last().before(newLi);
    };

    let currentPage = 1; // Start with page 1

$(".pagination").on("click", ".pagination-arrow", function(event) {
    // Check if the clicked element contains a child with the 'fa-chevron-right' class
    if ($(this).find(".fa-chevron-right").length > 0) {
        // Ensure we don't exceed the number of pages
        if (currentPage < numberOfPages) {
            // Move to the next page
            currentPage++;

            // Hide all cards
            cards.hide();

            // Show the next batch of 10 cards
            let start = (currentPage - 1) * 10;
            let end = currentPage * 10;
            cards.slice(start, end).show();
        }
    } 
    // Check if the clicked element contains a child with the 'fa-chevron-left' class
    else if ($(this).find(".fa-chevron-left").length > 0) {
        // Ensure we're not on the first page
        if (currentPage > 1) {
            // Move to the previous page
            currentPage--;

            // Hide all cards
            cards.hide();

            // Show the previous batch of 10 cards
            let start = (currentPage - 1) * 10;
            let end = currentPage * 10;
            cards.slice(start, end).show();
        }
    }
});

};
