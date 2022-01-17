console.log("Loading Staff Registration Scripts");

//elements
const staff_reg_form = document.getElementById('staff_registration_form');
const device_type_options = document.getElementsByName("device_type");
const computer_options = document.getElementsByName("computer");
const in_school_options = document.getElementsByName("in_school");
const dob_element = document.getElementById('id_dob');
const fieldWrapper_device_type = document.getElementById('fieldWrapper_device_type');
const fieldWrapper_computer = document.getElementById('fieldWrapper_computer');


const fieldWrapper_current_education_level = document.getElementById('fieldWrapper_current_education_level');
const fieldWrapper_current_education_class = document.getElementById('fieldWrapper_current_education_class');
const fieldWrapper_current_school = document.getElementById('fieldWrapper_current_school');
const fieldWrapper_highest_education_level = document.getElementById('fieldWrapper_highest_education_level');
const highest_education_level = document.getElementById('id_highest_education_level');
const current_education_level = document.getElementById('id_current_education_level');
const current_education_class = document.getElementById('id_current_education_class');
const current_school_e = document.getElementById('id_current_school');


//event listeners
window.addEventListener('load', (event) => {
  if(staff_reg_form){

	let checked_in_school = document.querySelector('input[name="in_school"]:checked');
	if(checked_in_school){
		if(checked_in_school.value == "Yes"){
			set_education_divs("in_school");
			
		} else if(checked_in_school.value == "No"){
			set_education_divs("not_in_school");
		}
	} else{
		set_education_divs("display_none");		
	}	

	let computer_choice = document.querySelector('input[name="computer"]:checked');

	if(computer_choice){
		if(computer_choice.value == "Yes"){
			fieldWrapper_device_type.classList.remove('d-none');		
		} else{
			fieldWrapper_device_type.classList.add('d-none');			
		}

	} else {
		fieldWrapper_device_type.classList.add('d-none');		
	}
  	
  }//end volunteer form
});//end on window load


for(let option of computer_options){
	option.addEventListener('change', (event) => {	  	
	  	if(event.target.value == "Yes"){
	  		fieldWrapper_device_type.classList.remove('d-none');
		} else if (event.target.value == "No"){
	  		fieldWrapper_device_type.classList.add('d-none');	  
	    	for(let item of device_type_options){
	    		item.checked = false;
	    	}
	  }
	});
}

for(let option of in_school_options){
	option.addEventListener('change', (event) => {
		if(event.target.value == "Yes"){
	  		set_education_divs("in_school");
	  	} else if (event.target.value == "No"){
	  		set_education_divs("not_in_school");
	  	}
	});
}



//functions

function findLabelForField(el) {
   var idVal = el.id;
   labels = document.getElementsByTagName('label');
   for( var i = 0; i < labels.length; i++ ) {
      if (labels[i].htmlFor == idVal)
           return labels[i];
   }
}



function set_education_divs(display_divs){
	let selected_highest = highest_education_level.options[highest_education_level.selectedIndex];	
	let selected_current = current_education_level.options[current_education_level.selectedIndex];	
	let selected_class = current_education_class.options[current_education_class.selectedIndex];
	

	if(display_divs == "in_school"){
		fieldWrapper_current_education_level.classList.remove('d-none');
		fieldWrapper_current_education_class.classList.remove('d-none');
		fieldWrapper_current_school.classList.remove('d-none');
		fieldWrapper_highest_education_level.classList.add('d-none');
		
		
		if(selected_highest){
			selected_highest.selected = false;
		}
		

	}else if(display_divs == "not_in_school"){
		fieldWrapper_current_education_level.classList.add('d-none');
		fieldWrapper_current_education_class.classList.add('d-none');
		fieldWrapper_current_school.classList.add('d-none');
		fieldWrapper_highest_education_level.classList.remove('d-none');
		
		if(selected_current){
			selected_current.selected = false;	
		}		
		
		if(selected_class){
			selected_class.selected = false;	
		}
		
		current_school_e.value = "";

	} else if(display_divs =="display_none"){
		fieldWrapper_current_education_level.classList.add('d-none');
		fieldWrapper_current_education_class.classList.add('d-none');
		fieldWrapper_current_school.classList.add('d-none');
		fieldWrapper_highest_education_level.classList.add('d-none');

		if(selected_highest){
			selected_highest.selected = false;
		}

		if(selected_current){
			selected_current.selected = false;
		}

		if(selected_class){
			selected_class.selected = false;
		}

		current_school_e.value = "";

	}
}



function email_blur(ev, object) {
  	if(ev == "blur"){
  		var email = object.value;
  		if (email != ''){
  			check_vol_email(email)
  		}
    } 
}

function check_vol_email(email){
	payload = {
		'email': email,
		'type_reg': "Staff",
		'reg_lang': "en"
	}

    $.ajax({
      type: 'GET',
      url: "/registration/registration_email_check/",
      data: payload,
      success: function (response) {
        console.log("Success")
        console.log(response)
        if (!response['valid']){
        	email_notifications()
        }
      },
      error: function (response) {
        console.log("Fail")
          console.log(response)
      }
    });

}

function close_notify_modal(){
	// console.log("Closing Notify MOdal")

	let email = document.getElementById('id_email')
	// console.log(email)
	email.value = ""
}

function email_notifications(){
	console.log("Notify Email", )
	if(notifyModalButton){
		let notifyModalLabel = document.getElementById('notifyModalLabel');
		notifyModalLabel.innerHTML = "Registration Notification";
		notifyModalButton.click();
	}
}


function clear_input_errors(input_name){
	let error_div = document.getElementById(input_name +"_errors");
	if(error_div){
		error_div.innerHTML = "";
	}	
}




function submit_staff_reg_form(){
	let staff_reg = document.getElementById('staff_registration_form');
	staff_reg.submit();
}
