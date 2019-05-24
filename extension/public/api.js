$(function(){
var url1='https://api.progressdash.xyz/v1/images/random';
requestJSON(url1, function(response) {
  console.log(response);
  var output = 'url('+response.image+')' 
  $('#maindiv').css('background-image',output);
});

var url= 'https://rancode.herokuapp.com/api';
  requestJSON(url, function(response) {
    console.log(response);
    var output = '<div class="col-md-10 col-md-offset-1"><div class="home-content"><h1 class="white-text"><a target="_blank" style="color:white" href="'+response.data.url+'">'+response.data.name+'</a></h1><button class="main-btn">Type - '+response.data.type+'</button><a target="_blank" href="'+response.data.submit_url+'"><button class="main-btn">Code - '+response.data.code+'</button></a><button class="main-btn">Submissions - '+response.data.submissions+'</button><a target="_blank" href="'+response.data.status+'"><button class="main-btn">Accuracy - '+response.data.accuracy+'</button></a></div></div>' 
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