$('.table > tbody > tr').click(function() {
    var id = $(this).find('td:eq(0)').text();
    location.href = id;
});

$('#to_courses' ).click(function() {
    location.href = '../';
});
