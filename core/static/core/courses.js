$("button").click(function() {
    var course = $(this).text();
    location.href = "../" + course + "/view_grades";
});

