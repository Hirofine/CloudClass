
$('.login').on('submit', function () {
    var username = document.getElementById('username').value;
    $('#print').append(username);
    return false;
});
