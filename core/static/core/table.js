$('.table > tbody > tr').click(function() {
    var id = $(this).find('td:eq(0)').text();
    location.href = id;
});
