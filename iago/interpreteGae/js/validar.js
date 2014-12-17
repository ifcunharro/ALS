
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
	$('#dinamic br').remove()
	if($('#formAttr').length >0){
		$('#formAttr').remove();
		$('label#lbObject').text('Nuevo objeto');
	};
	if($('#formMethod').length >0){
		$('#formMethod').remove();
		$('label#lbObject').text('Nuevo objeto');
	};
	ponerListado()
	
}

function validarAtributo()
{	$('#dinamic br').remove()
	if($('#formObject').length ==0){
		$('#dinamic')
			.append('<div id="formObject"><label id="lbObject">\
			Nuevo objeto</label><br><input title="No debe comenzar por _ \
			o numero" name="object" id="object" type="text" required/><br>\
			</div><div class="buttons">\
                <input id="enviar" class="btn btn-default" name="enviar" \
				type="submit" value="Enviar" onclick="m();"></input>\
            </div>\
			')
	};
	if($('#formObject').length >0){
	
		$('label#lbObject').text('Nombre objeto');
	}
	if($('#formMethod').length >0) {
		$('#formMethod').remove();
	}

}

function validarMethod()
{
	$('#dinamic br').remove()
	if($('#formObject').length >0){
		$('label#lbObject').text('Nombre objeto');
	};
	if($('#formObject').length ==0){
		$('br').remove()
		$('#dinamic')
			.append('<div id="formObject"><label id="lbObject">Nuevo objeto\
			</label><br><input title="No debe comenzar por _ o numero" \
			name="object" id="object" type="text" required/><br>\
			</div><div class="buttons">\
                <input id="enviar" class="btn btn-default" name="enviar" \
				type="submit" value="Enviar" onclick="m();"></input>\
            </div>\
			')
	};
	if($('#formAttr').length >0){
		$('#formAttr').remove();
	}
}

function formnobject()
{
	validarObjeto()
	if($('#formObject').length ==0){
		$('#dinamic')
			.append('<div id="formObject"><label id="lbObject">Nuevo objeto\
			</label><br><input title="No debe comenzar por _ o numero" \
			name="object" id="object" type="text" required/><br></div><div class="buttons">\
                <input id="enviar" class="btn btn-default" name="enviar" \
				type="submit" value="Enviar" onclick="m();"></input>\
            </div>\
			')
	}
		$('#frmInput').attr('action','/addObject')
	
	
	
}




function formnattr()
{
	validarAtributo();
	borrarListado();
	
		if($('#formAttr').length ==0){
			$('<div id="formAttr"><label>Nuevo atributo</label><br>\
			<input title="debe ser un string o un char" name="attr" \
			id="attr" type="text" required/><br>\
			<label id="value">Valor atributo</label><br>\
			<input name="valattr" id="valattr" type="text" required/><br>\
			</div>\
					')
				.insertAfter('#formObject')
		}
	
		$('#frmInput').attr('action','/addAttr')
	
	
}



function formnmethod()
{
	validarMethod();
	borrarListado()
	if($('#formMethod').length ==0){
		$('<div id="formMethod"><label>Nuevo metodo</label><br>\
		<input name="method" id="method" type="text" required/><br>\
		<label name="implMethod" id="implMethod">Implementación metodo\
		</label><br><textarea title="Debe tener self como param" \
		name="valmethod" id="valmethod" row=1 cols=20 required></textarea>\
		<br></div>\
				')
				.insertAfter('#formObject')
		
	}
	
	$('#frmInput').attr('action','/addMethod')
		
	
}

function alertTimeout(w){
			setTimeout(function(){
				$("#msg").remove();document.location.reload();}, w);
			
			
		}
	



window.onload = function() {
	$(function(){
			$('#header').load("static/header.html")
			$('#footer').load("static/footer.html")
			m()	
		});
	
	
	
	document.getElementById( 'nObject' ).onclick = formnobject;
	document.getElementById( 'nAttr' ).onclick = formnattr;
	document.getElementById( 'nMethod' ).onclick = formnmethod;

}
