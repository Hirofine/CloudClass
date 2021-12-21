
$('.login').on('submit', function () {
    
    
    let _data = {
        title: document.getElementById('title').value,
        author: document.getElementById('text').value, 
        id:3
    }

    fetch('http://127.0.0.1:8000/books/', {
        method: "POST",
        body: JSON.stringify(_data),
        headers: {"Content-type": "application/json; charset=UTF-8"}
    })
    .then(response => response.json()) 
    .then(json => console.log(json));
    //.catch(err => console.log(err));
    
    return false;
});


$('.output').on('submit', function () {
    fetch('http://127.0.0.1:8000/books/?format=json').then(function(response) {
        return response.json();
      }).then(function(data) {
        console.log(data);
        $('#print').append(JSON.stringify(data));
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
