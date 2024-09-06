$(document).ready(function(){
    cardToggle();
    addFormValidate();
    editFormValidate();
    pagination();
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
        };
    });
};

function editFormValidate() {
    $("#edit-form-submit").on("click", function(event) {
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
            $("#edit-form").after("<p id='form-feedback' style='color: green;'>Form submitted successfully!</p>");

           // Reset the form fields
            $("#edit-form")[0].reset();

            // reset all input borders to default
            $("#business_name, #business_description, #category, #phone, #email, #website, #image").css("border", "");
        };
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
