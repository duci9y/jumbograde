// redirect to corresponding assignment scorecard 
$('.table > tbody > tr').click(function() {
    var id = $(this).find('td:eq(0)').text();
    location.href = id;
});


// redirect back to courses page 
function go_back_to_courses() {
    location.href = "../../courses";
}
