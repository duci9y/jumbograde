/*************************     JQuery     **************************/

/* go to corresponding assignment scorecard */
$('.table > tbody > tr').click(function() {
    var id = $(this).find('td:eq(0)').text();
    location.href = id;
});


/*************************   JavaScript   **************************/

/* go back to previous page */
function go_back() {
    location.href = "courses";
}
