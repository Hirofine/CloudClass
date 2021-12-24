
$('.login').on('submit', function () {
    
    
    let _data = {
        note_id: 3,
        title: document.getElementById('title').value,
        author: document.getElementById('text').value, 
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
    
    //adress = 'http://127.0.0.1:8000/book/'  + document.getElementById('element').value;
    console.log("GET function");
    fetch('http://127.0.0.1:8000/books/').then(function(response) {
        return response.json();
      }).then(function(data) {
        console.log(data);
        console.log(data.length);
        res = '<div>';
        for(let i=0; i<data.length; i++){
            console.log("itteration : " + i);
            res+='<div> <ul>' + data[i].title + '</ul><ul>' + data[i].author + '</ul></div>';
        }
        res+='</div>';
        $('#print').html(res);
      }).catch(function() {
        console.log("fuck it");
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
