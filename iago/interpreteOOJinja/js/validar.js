
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
		$('<label id="formObject">Nombre objeto</label>\
				<input name= "object" id="object" type="text"/>\
					')
			.insertBefore('#enviar')
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
		$('<div><label id="formObject">Nuevo objeto</label>\
					<input name="object" id="object" type="text"/>\
			</div>')
			.insertBefore('#enviar')
	}
	$('#frmInput').attr('action','/addObject')
	
}




function formnattr()
{
	validarAtributo();
	borrarListado();
		if($('#formAttr').length ==0){
		
			$('<label id="formAttr">Nuevo atributo</label>\
									<input name="attr" id="attr" type="text"/>\
									<label id="value">Valor atributo</label>\
									<input name="valattr" id="valattr" type="text"/>\
					')
				.insertBefore('#enviar')
		}
	$('#frmInput').attr('action','/addAttr')
	
}

function formnmethod()
{
	validarMethod();
	
	if($('#formMethod').length ==0){
		$('<label id="formMethod">Nuevo metodo</label>\
									<input name="method" id="method" type="text"/>\
									<label name="implMethod" id="implMethod">Implementación metodo</label>\
									<input name="valmethod" id="valmethod" type="text"/>'
				)
				.insertBefore('#enviar')
		
	}
	$('#frmInput').attr('action','/addMethod')
	
}

window.onload = function() {
	document.getElementById( "nObject" ).onclick = formnobject;
	document.getElementById( "nAttr" ).onclick = formnattr;
	document.getElementById( "nMethod" ).onclick = formnmethod;
}
