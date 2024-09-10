$(document).ready(function(){
    cardToggle();
    formValidate();
    pagination();
});

function cardToggle(){
    $(".toggle-button").click(function(){
        $(this).closest(".card").find(".contact-details").toggle();
    });
};

function formValidate() {
    $("#add-form .form-submit, #edit-form .form-submit").on("click", function(event) {
        $("#form-feedback").remove();

        // Collect form values
        let businessName = $("#add-business-name, #edit-business-name").val();
        let businessDescription = $("#add-business-description, #edit-business-description").val();
        let category = $("#add-category, #edit-category").val();
        let phone = $("#add-phone, #edit-phone").val();
        let email = $("#add-email, #edit-email").val();
        let website = $("#add-website, #edit-website").val();
        let image = $("#add-image, #edit-image").val();

        // Remove any previous error messages and reset borders
        $(".error-message").remove(); // Remove all previous error messages
        $("#add-business-name, #edit-business-name, #add-business-description, #edit-business-description, #add-category, #edit-category, #add-phone, #edit-phone, #add-email, #edit-email, #add-website, #edit-website, #add-image, #edit-image").css("border", "");

        let isValid = true; // Flag to check if the form is valid

        // Validate business name
        if (!businessName || businessName.length > 50) {
            $("#add-business-name, #edit-business-name").css("border", "2px solid red");
            $("#add-business-name, #edit-business-name").after("<span class='error-message' style='color: red;'>Field required, please use less than 50 characters</span>");
            isValid = false;
        } else {
            $("#add-business-name, #edit-business-name").css("border", "2px solid green");
        }

        // Validate business description
        if (!businessDescription || businessDescription.length > 255) {
            $("#add-business-description, #edit-business-description").css("border", "2px solid red");
            $("#add-business-description, #edit-business-description").after("<span class='error-message' style='color: red;'>Field required, please use less than 255 characters</span>");
            isValid = false;
        } else {
            $("#add-business-description, #edit-business-description").css("border", "2px solid green");
        }

        // Validate category (required)
        if (!category) {
            $("#add-category, #edit-category").css("border", "2px solid red");
            $("#add-category, #edit-category").after("<span class='error-message' style='color: red;'>Field required</span>");
            isValid = false;
        } else {
            $("#add-category, #edit-category").css("border", "2px solid green");
        }

        // Check that at least one of phone, email, or website is filled out and valid
if (!phone && !email && !website) {
    $("#add-phone, #edit-phone, #add-email, #edit-email, #add-website, #edit-website").css("border", "2px solid red");
    $("#add-website, #edit-website").after("<span class='error-message' style='color: red;'>You need to provide at least one of the following: Number, Email, or Website must be filled out.</span>");
    isValid = false;
} else {
    // Validate phone (must be exactly 11 digits if provided)
    if (phone && !/^\d{11}$/.test(phone)) {
        $("#add-phone, #edit-phone").css("border", "2px solid red");
        $("#add-phone, #edit-phone").after("<span class='error-message' style='color: red;'>Phone number must be exactly 11 digits.</span>");
        isValid = false;
    } else {
        $("#add-phone, #edit-phone").css("border", "2px solid green");
    }

    // Validate email (basic email pattern)
    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email && (!emailPattern.test(email) || email.length > 255)) {
        $("#add-email, #edit-email").css("border", "2px solid red");
        $("#add-email, #edit-email").after("<span class='error-message' style='color: red;'>Please enter a valid email (less than 255 characters).</span>");
        isValid = false;
    } else {
        $("#add-email, #edit-email").css("border", "2px solid green");
    }

    // Validate website (must be a valid URL if provided)
    let urlPattern = /^(https?:\/\/)?[^\s/$.?#].[^\s]*$/i;
    if (website && (website.length > 255 || !urlPattern.test(website))) {
        $("#add-website, #edit-website").css("border", "2px solid red");
        $("#add-website, #edit-website").after("<span class='error-message' style='color: red;'>Please enter a valid website URL (less than 255 characters).</span>");
        isValid = false;
    } else {
        $("#add-website, #edit-website").css("border", "2px solid green");
    }
}
        // Validate image (cannot exceed 255 characters)
        let imageUrlPattern = /^(https?:\/\/)?[^\s/$.?#].[^\s]*$/i; // Basic URL pattern for images
        if (image && (image.length > 255 || !imageUrlPattern.test(image))) {
            $("#add-image, #edit-image").css("border", "2px solid red");
            $("#add-image, #edit-image").after("<span class='error-message' style='color: red;'>Please enter a valid image URL (must be less than 255 characters)</span>");
            isValid = false;
        } else if(image) {
            $("#add-image, #edit-image").css("border", "2px solid green");
        } else{
            $("#add-image, #edit-image").css("border", "");
        }

        // If all fields are valid, submit the form
        if (isValid) {
            $(".error-message").remove();
            

            // Reset the form fields
            $(".form")[0].reset();

            // Reset all input borders to default
            $("#add-business-name, #edit-business-name, #add-business-description, #edit-business-description, #add-category, #edit-category, #add-phone, #edit-phone, #add-email, #edit-email, #add-website, #edit-website, #add-image, #edit-image").css("border", "");
        }

        // Prevent form submission if invalid
        if (!isValid) {
            event.preventDefault(); // Prevent form submission
        }
    });
}



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
