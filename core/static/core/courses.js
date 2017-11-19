// redirect to grades for specified course
$(".course").click(function() {
    var course = $(this).text();
    location.href = "../" + course + "/view_grades";
});

// redirec to login page
$(".logout").click(function() {
    var course = $(this).text();
    location.href = "../login";
});
