function CloseForm(){
  document.getElementsByClassName("form-container")[0].style.display = "none";
}
function OpenForm(){
  if (document.getElementsByClassName("form-container")[0].style.display == "block"){
    document.getElementsByClassName("form-container")[0].style.display = "none";
  }else{
    document.getElementsByClassName("form-container")[0].style.display = "block"
  }
}

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
  function getCookie(name) {
     var cookieValue = null;
     if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
             var cookie = jQuery.trim(cookies[i]);
             if (cookie.substring(0, name.length + 1) == (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
            }
         }
     }
     return cookieValue;
   }
   xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
 }
});

$("#simple_search_form").submit(function(event){
  $.ajax({
    url: "http://localhost:8000",
    method: "post",
    data: {
      search_query: event.target[0].value,
    },
    success: function (response) {
      if(response.results[0]){
        let inner = '';
        response.results.forEach(element => {
          element = JSON.parse(element)[0];
          inner += '<br/> <a href="/creature/'+element.fields.Breed_name+'" target="_blank"> '+element.fields.Breed_name+' </a>'
        });
        console.log(inner)
        document.getElementById("s_results").innerHTML = inner
      }else{
        document.getElementById("s_results").innerHTML = '<b style="color: white;">Nothing found! Try other search query!</b>'
      }
    },
    error: function(jqXHR, textStatus, errorThrown) {
       console.log(textStatus, errorThrown);
    }
  });
});

$("#advanced_search_form").submit(function(event){
  /* Getting input values */
  formData = []
  /* i = 1, because [0] is hidden input, it shouldn't be used to search in databse */
  for(let i=1; i < event.target.length; i++){
    /* Ignore all elements, that aren't input[type="text"] */
    if(event.target[i].type == "text"){
      formData.push(event.target[i].value);
    }
  }

  $.ajax({
    url: "http://localhost:8000",
    method: "post",
    data: {
      formData: formData,
    },
    success: function (response) {
      if(response.results[0]){
        let inner = '';
        response.results.forEach(element => {
          element = JSON.parse(element)[0];
          inner += '<br/>  <a href="/creature/'+element.fields.Breed_name+'" target="_blank"> '+element.fields.Breed_name+' </a>'
        });
        console.log(inner)
        // using div with id = "s_results"
        document.getElementById("s_results").innerHTML = inner
      }else{
        document.getElementById("s_results").innerHTML = '<b style="color: white;">Nothing found! Try other search query!</b>'
      }
    },
    error: function(jqXHR, textStatus, errorThrown) {
       console.log(textStatus, errorThrown);
    }
  });

  event.preventDefault();
});
