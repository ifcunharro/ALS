
function borrarListado()
{
	$('#listado').hide()
}

function ponerListado()
{
	$('#listado').show();
	$('#listado').css('display', 'block');
}


function validarObjeto()
{
	
	if($('#formAttr').length >0){
		$('#formAttr').remove();
		$('#attr').remove()
		$('#value').remove()
		$('#valattr').remove()
		$('label#formObject').text('Nuevo objeto');
	};
	if($('#formMethod').length >0){
		$('#formMethod').remove();
		$('#method').remove()
		$('#valmethod').remove();
		$('#implMethod').remove();
		$('label#formObject').text('Nuevo objeto');
	};
	ponerListado()
	
}

function validarAtributo()
{
	if($('#formObject').length ==0){
		$('<label form="forid="formObject">Nombre objeto</label>\
		<input name= "object" id="object" type="text" required/>\
					')
			.insertAfter('#frmInput')
	};
	if($('#formObject').length >0){
	
		$('label#formObject').text('Nombre objeto');
	}
	if($('#formMethod').length >0) {
		$('#formMethod').remove();
		$('#method').remove()
		$('#valmethod').remove();
		$('#implMethod').remove();
	}

}

function validarMethod()
{
	
	if($('#formObject').length >0){
		$('label#formObject').text('Nombre objeto');
	};
	if($('#formAttr').length >0){
		$('#formAttr').remove();
		$('#attr').remove()
		$('#value').remove()
		$('#valattr').remove()
	}
}

function formnobject()
{
	validarObjeto()
	if($('#formObject').length ==0){
		ponerListado()
		var but;
		but = $('#buttons').detach()
		$('<div><label id="formObject">Nuevo objeto</label>\
			<input name="object" id="object" type="text" required/>\
			</div>')
			.AppendTo('#frmInput')
		but.AppendTo('#frmInput')
	}
	$('#frmInput').attr('action','/addObject')
	
}




function formnattr()
{
	validarAtributo();
	borrarListado();
		if($('#formAttr').length ==0){
		
			$('<label id="formAttr">Nuevo atributo</label>\
			<input name="attr" id="attr" type="text" required/>\
			<label id="value">Valor atributo</label>\
			<input name="valattr" id="valattr" type="text" required/>\
					')
				.insertAfter('#object')
		}
	$('#frmInput').attr('action','/addAttr')
	
}



function formnmethod()
{
	validarMethod();
	
	if($('#formMethod').length ==0){
		$('<label id="formMethod">Nuevo metodo</label>\
		<input name="method" id="method" type="text" required/>\
		<label name="implMethod" id="implMethod">Implementación metodo</label>\
		<textarea name="valmethod" id="valmethod" cols=20 required></textarea>'
				)
				.insertBefore('#object')
		
	}
	$('#frmInput').attr('action','/addMethod')
	
}

window.onload = function() {
	document.getElementById( "nObject" ).onclick = fornobject;
	document.getElementById( "nAttr" ).onclick = formnattr;
	document.getElementById( "nMethod" ).onclick = formnmethod;
}
