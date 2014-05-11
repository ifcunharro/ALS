
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
		$('label#objeto').text('Nuevo objeto');
	};
	if($('#formMethod').length >0){
		$('#formMethod').remove();
		$('label#objeto').text('Nuevo objeto');
	};
	ponerListado()
	
}

function validarAtributo()
{
	if($('#formObject').length ==0){
		$('<div id="formObject" class="row">\
							<div class="col-xs-4">\
								<label id="objeto">Nombre objeto</label>\
								<input id="object" type="text"/>\
							</div>\
					</div>')
			.insertBefore('#enviar')
	};
	if($('#formObject').length >0){
	
		$('label#objeto').text('Nombre objeto');
	}
	if($('#formMethod').length >0) {
		$('#formMethod').remove();
	}

}

function validarMethod()
{
	
	if($('#formObject').length >0){
		$('label#objeto').text('Nombre objeto');
	};
	if($('#formAttr').length >0){
		$('#formAttr').remove();
	}
}

function formnobject()
{
	validarObjeto()
	if($('#formObject').length ==0){
		ponerListado()
		$('<div id="formObject" class="row">\
							<div class="col-xs-4">\
								<label id="objeto">Nuevo objeto</label>\
								<input id="object" type="text"/>\
							</div>\
					</div>')
			.insertBefore('#enviar')
	}
	
}




function formnattr()
{
	validarAtributo();
	borrarListado();
		if($('#formAttr').length ==0){
		
			$('<div id="formAttr" class="row">\
								<div class="col-xs-4">\
									<label>Nuevo atributo</label>\
									<input id="attr" type="text"/>\
								</div>\
								<div>\
									<label id=value">Valor atributo</label>\
									<input id="valattr" type="text"/>\
								</div>\
						</div>')
				.insertBefore('#enviar')
		}
	
}

function formnmethod()
{
	validarMethod();
	
	if($('#formMethod').length ==0){
		$('<div id="formMethod" class="row">\
								<div class="col-xs-4">\
									<label>Nuevo metodo</label>\
									<input id="method" type="text"/>\
								</div>\
								<div>\
									<label>Implementación metodo</label>\
									<input id="valmethod" type="text"/>\
								</div>\
						</div>')
				.insertBefore('#enviar')
		
	}
	
}

window.onload = function() {
	document.getElementById( "nObject" ).onclick = formnobject;
	document.getElementById( "nAttr" ).onclick = formnattr;
	document.getElementById( "nMethod" ).onclick = formnmethod;
}
