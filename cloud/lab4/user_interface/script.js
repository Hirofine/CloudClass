
$('.login').on('submit', function () {
    var username = document.getElementById('title').value;
    $('#print').append(username);
    console.log(username);
    return false;
});


$('.output').on('submit', function () {
   
   //httpGetAsync('https://localhost:8000/books', )
    //fetch('https://localhost:8000/books')
    fetch('http://localhost:8000/books').then(function(response) {
        return response.json();
      }).then(function(data) {
        console.log(data);
      }).catch(function() {
        console.log("Booo");
      })
    return false;
});
//get



    //post
    /*
const params = {
    param1: value1,
    param2: value2
};
const options = {
    method: 'POST',
    body: JSON.stringify(params)
};
fetch('https://domain.com/path/', options)
    .then(response => response.json())
    .then(response => {
        // Do something with response.
    });*/