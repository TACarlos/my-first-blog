// Recorrer los elementos y hacer que onchange ejecute una funcion para comprobar el valor de ese input
(function(){

var formulario = document.formulario_registro,
	elementos = formulario.elements;


var focusInput = function(){
	this.parentElement.children[1].className = "label active";
	this.parentElement.children[0].className = this.parentElement.children[0].className.replace("error", "");
};

var blurInput = function(){
	if (this.value <= 0) {
		this.parentElement.children[1].className = "label";
		this.parentElement.children[0].className = this.parentElement.children[0].className + " error";
	}
};

}())