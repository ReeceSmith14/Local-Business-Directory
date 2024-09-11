$(document).ready(function(){
    cardToggle();
    pagination();
});

function cardToggle(){
    $(".toggle-button").click(function(){
        $(this).closest(".card").find(".contact-details").toggle();
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
