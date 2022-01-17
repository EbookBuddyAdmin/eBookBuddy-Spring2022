console.log("Loading Child Registration Scripts")

let lang_form;
let span_select_one = '(Seleccione uno)';
let eng_select_one = '(Select One)';
let other_specify_span = '  Otro (por favor especifique)';
let span_yes = '  Sí';
let span_none = '  Ninguno';
let span_high = '  Alto';
let span_med = '  Medio';
let span_low = '  Bajo';

const gender_options = document.getElementsByName("gender");
const school_options = document.getElementsByName("school");
const primary_lang_options = document.getElementsByName("primary_language");
const secondary_lang_options = document.getElementsByName("secondary_language");
const session_device_options = document.getElementsByName("session_device");

window.addEventListener('load', (event) => { 

	let choosen_registration_language = document.querySelector('input[name="registration_language"]:checked');

	lang_form = choosen_registration_language.parentElement.textContent.trim();

	let all_registration_radios = document.querySelectorAll('.registration_radio');

	// let ethnicity_select = document.getElementById('id_ethnicity')



	if(lang_form == "Spanish"){
		// ethnicity_select.options[0].text = span_select_one;

		for(let item of all_registration_radios){
			let the_label = item.parentElement;
			let the_child_nodes = the_label.childNodes;
			for(let item of the_child_nodes){
				if(item.nodeName === '#text'){
					if(item.textContent.trim() == 'Yes'){
						item.textContent = span_yes;
					}
					else if(item.textContent.trim() == 'Other (Please Specify)'){
						item.textContent = other_specify_span;
					}else if(item.textContent.trim() == 'None'){
						item.textContent = span_none;
					}else if(item.textContent.trim() == 'High'){
						item.textContent = span_high;
					}else if(item.textContent.trim() == 'Medium'){
						item.textContent = span_med;
					}else if(item.textContent.trim() == 'Low'){
						item.textContent = span_low;
					}
				}
			}
		}

		for(let item of gender_options){
			let the_label = item.parentElement;
			let the_child_nodes = the_label.childNodes;
			for(let item of the_child_nodes){
				if(item.nodeName === '#text'){
					if(item.textContent.trim() == 'Female'){
						item.textContent = "  Femenino";
					} else if(item.textContent.trim() == 'Male'){
						item.textContent = "  Masculino";
					}

				}
			}
		}
	}
});

for(let option of school_options){
	option.addEventListener('change', (event) => {
		clear_input_errors('other_school')
		let the_option = document.getElementById(event.target.id);
		let the_label = the_option.parentElement.textContent.trim();
		console.log("the_label", the_label);
	  	if(the_label == "Other (Please Specify)" || the_label == 'Otro (por favor especifique)'){
	  		let other_school_input = document.getElementById('id_other_school');
	  		other_school_input.focus();  	
	  	} 
	});
}

for(let option of session_device_options){
	option.addEventListener('change', (event) => {
		clear_input_errors('other_session_device')
		let the_option = document.getElementById(event.target.id);
		let the_label = the_option.parentElement.textContent.trim();
		console.log("the_label", the_label);
	  	if(the_label == "Other (Please Specify)" || the_label == 'Otro (por favor especifique)'){
	  		let other_session_device_input = document.getElementById('id_other_session_device');
	  		other_session_device_input.focus();  	
	  	} 
	});
}

for(let option of secondary_lang_options){
	option.addEventListener('change', (event) => {
		clear_input_errors('other_secondary_language')
		let the_option = document.getElementById(event.target.id);
		let the_label = the_option.parentElement.textContent.trim();
		console.log("the_label", the_label);
	  	if(the_label == "Other (Please Specify)" || the_label == 'Otro (por favor especifique)'){
	  		let other_secondary_language_input = document.getElementById('id_other_secondary_language');
	  		other_secondary_language_input.focus();  	
	  	} 
	});
}

for(let option of primary_lang_options){
	option.addEventListener('change', (event) => {
		clear_input_errors('other_primary_language')
		let the_option = document.getElementById(event.target.id);
		let the_label = the_option.parentElement.textContent.trim();
		console.log("the_label", the_label);
	  	if(the_label == "Other (Please Specify)" || the_label == 'Otro (por favor especifique)'){
	  		let other_primary_language_input = document.getElementById('id_other_primary_language');
	  		other_primary_language_input.focus();  	
	  	} 
	});
}


function clear_input_errors(input_name){
	let error_div = document.getElementById(input_name +"_errors");
	if(error_div){
		error_div.innerHTML = "";
	}	
}


function set_form_language(lang_id){
	console.log('lang_id', lang_id)
	lang_options = document.getElementsByName('language')
	for(let item of lang_options){
		if(item.value == parseInt(lang_id)){
			item.checked = true;
		}
	}
	let pre_form = document.getElementById('pre_form')
	pre_form.submit()
}

function submit_child_form(){
	let child_reg = document.getElementById('child_form');
	child_reg.submit();
}