// ##############################
function validate(callback){
  const form = event.target
  // console.log(form)
  const validate_error = "rgba(255, 0, 0, 0.1)"
  // const _quick_tweet_box = _one("#_quick-tweet")
  
  _all("[data-validate]",form).forEach(function(element){ 
    element.classList.remove("validate_error")
    element.style.backgroundColor = "white"
  })
  _all("[data-validate]",form).forEach( function(element){
    switch(element.getAttribute("data-validate")){
      case "str":
        if( element.value.length < parseInt(element.getAttribute("data-min")) || 
            element.value.length > parseInt(element.getAttribute("data-max")) 
        ){
          element.classList.add("validate_error")
          element.style.backgroundColor = validate_error
          // _quick_tweet_box.style.borderColor = validate_error
        }
      break;
      case "int":
        if( ! /^\d+$/.test(element.value)  ||
            parseInt(element.value) < parseInt(element.getAttribute("data-min")) || 
            parseInt(element.value) > parseInt(element.getAttribute("data-max"))
        ){
          element.classList.add("validate_error")
          element.style.backgroundColor = validate_error
        }
      break;      
      case "email":
        let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if( ! re.test(element.value.toLowerCase()) ){
          element.classList.add("validate_error")
          element.style.backgroundColor = validate_error
        }
      break;
      case "re":       
        var regex = new RegExp(element.getAttribute("data-re"));
        if( ! regex.test(element.value) ){
          console.log("phone error")
          element.classList.add("validate_error")
          element.style.backgroundColor = validate_error
        }
      break;
      case "match":
        if( element.value != _one(`[name='${element.getAttribute("data-match-name")}']`, form).value ){
          element.classList.add("validate_error")
          element.style.backgroundColor = validate_error
        }
      break;
    }
  })
  if( ! _one(".validate_error", form) ){ callback(); return }
  // _one(".validate_error", form).focus()
}

// ##############################
function clear_validate_error(){
  // event.target.classList.remove("validate_error")
  // event.target.value = ""
}

