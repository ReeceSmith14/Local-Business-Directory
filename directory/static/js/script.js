/**
 * Initialises the document when fully loaded.
 * Calls the `cardToggle` and `pagination` functions to enable toggling contact
 * details on cards and manage pagination.
 */
$(document).ready(function(){
    cardToggle();  // Initialise card toggle functionality
    pagination();  // Initialise pagination functionality
});

/**
 * Toggles the visibility of the contact details within each card.
 * 
 * Binds a click event to elements with the class `toggle-button`. When a button
 * is clicked, it finds the closest card element and toggles the visibility of
 * the `.contact-details` section within that card.
 */
function cardToggle(){
    $(".toggle-button").click(function(){
        $(this).closest(".card").find(".contact-details").toggle();
    });
}

/**
 * Implements pagination for a list of cards, displaying 10 cards per page.
 * 
 * - Initially, hides all cards and displays only the first 10.
 * - Dynamically generates pagination controls based on the total number of cards.
 * - Allows the user to navigate between pages using pagination arrows.
 *
 * @function pagination
 * @global
 */
function pagination(){
    const cards = $('.card');  // All card elements
    const ul = $('.pagination');  // Pagination <ul> element

    const numberOfCards = cards.length;  // Total number of cards
    const numberOfPages = Math.ceil(numberOfCards / 10);  // Calculate the number of pages required (10 cards per page)

    // Initially show the first 10 cards and hide the rest
    cards.hide();  // Hide all cards
    cards.slice(0, 10).show();  // Show only the first 10 cards

    // Create pagination links based on the number of pages
    for (let i = 1; i < numberOfPages; i++) {  // Generate page numbers starting from the second page
        let newLi = `
        <li class="page-item">
            <p class="page-link">${i + 1}</p>
        </li>`;
        ul.children().last().before(newLi);  // Insert new page links before the last element
    }

    let currentPage = 1;  // Track the current page, initially set to 1

    /**
     * Handles click events for pagination arrows (next and previous).
     * 
     * - Moves forward when the right arrow is clicked (fa-chevron-right).
     * - Moves backward when the left arrow is clicked (fa-chevron-left).
     * - Limits navigation to prevent exceeding the first or last page.
     *
     * @event paginationArrowClick
     */
    $(".pagination").on("click", ".pagination-arrow", function(event) {
        // Check if the right arrow (next page) is clicked
        if ($(this).find(".fa-chevron-right").length > 0) {
            if (currentPage < numberOfPages) {  // Ensure we don't exceed the last page
                currentPage++;  // Increment to the next page
                cards.hide();  // Hide all cards

                // Show the next batch of 10 cards
                let start = (currentPage - 1) * 10;
                let end = currentPage * 10;
                cards.slice(start, end).show();
            }
        } 
        // Check if the left arrow (previous page) is clicked
        else if ($(this).find(".fa-chevron-left").length > 0) {
            if (currentPage > 1) {  // Ensure we're not on the first page
                currentPage--;  // Decrement to the previous page
                cards.hide();  // Hide all cards

                // Show the previous batch of 10 cards
                let start = (currentPage - 1) * 10;
                let end = currentPage * 10;
                cards.slice(start, end).show();
            }
        }
    });
}
