$(function(){
var url= 'http://localhost:8000/api';
  requestJSON(url, function(response) {
    console.log(response);
    var output = '<div class="col-md-10 col-md-offset-1"><div class="home-content"><h1 class="white-text"><a style="color:white" href="'+response.data.url+'">'+response.data.name+'</a></h1><button class="main-btn">Type - '+response.data.type+'</button><a href="'+response.data.submit_url+'"><button class="main-btn">Code - '+response.data.code+'</button></a><button class="main-btn">Submissions - '+response.data.submissions+'</button><a href="'+response.data.status+'"><button class="main-btn">Accuracy - '+response.data.accuracy+'</button></a></div></div>' 
    $('#add_content').html(output);
});

function requestJSON(url, callback) {
    $.ajax({
      url: url,
      complete: function(xhr) {
        callback.call(null, xhr.responseJSON);
      }
    });
  }
});