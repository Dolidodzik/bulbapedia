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

// Things function replaces every & or && in string with AMPERSAND_MARK
function ReplaceAmpersands(string){
  let return_value = string.replace("&&", "AMPERSAND_MARK");
  return_value = return_value.replace("&", "AMPERSAND_MARK")
  return return_value;
}
// Opposite of above ReplaceAmpersands()
function ReplaceAMPERSAND_MARKS(string){
  return string.replace("AMPERSAND_MARK", "&&");
}

$("#simple_search_form").submit(function(event){
  // I didn't use window.location.href +=, because if user press submit button more than 2 times it may throw a bugs. So I needed to rebulid full path without parameters
  window.location.href = location.protocol + '//' + location.host + location.pathname + "?search_query="+ReplaceAmpersands(event.target[0].value);
});

$("#advanced_search_form").submit(function(event){
  // Getting input values
  formData = []
  // i = 1, because [0] is hidden input, it shouldn't be used to search in databse
  for(let i=1; i < event.target.length; i++){
    // Take only elements that are input[type="text"] 
    if(event.target[i].type == "text"){
      formData.push( ReplaceAmpersands(event.target[i].value) );
    }
  }
  // I didn't use window.location.href +=, because if user press submit button more than 2 times it may throw a bugs. So I needed to rebulid full path without parameters
  window.location.href = location.protocol + '//' + location.host + location.pathname + "?advanced_search_query="+formData.toString();

  // Preventing form from refreses/redirects
  event.preventDefault();
});
