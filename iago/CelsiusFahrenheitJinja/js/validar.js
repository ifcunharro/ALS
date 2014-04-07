

function hideError()
{
	$('div#divError').remove();
}

function showError(msg)
{
	$('<div id="divError">Error '+msg+'</div>').insertAfter('div')
	
}
function validate()
{
	var toret = false;
	var frmInput = document.getElementById( "frmInput" );
	// Prepare answer, in case it is needed.
	hideError();
	// Prepare values
	var name = frmInput[ "grados" ].value.trim();
	if ( name.length === 0 ) {
		showError( "debe introducir grados." );
	}
	else
	{
		toret = true;
	}
	return toret;
}
window.onload = function() {
	document.getElementById( "frmInput" ).onsubmit = validate;
}
