function (element, parametro){
	var x = "";
	switch(parametro){
		default:
			x = document.querySelector("#com_ibm_team_workitem_web_mvvm_view_queryable_combo_QueryableComboView_6 > div.ValueHolder.ViewBorder > span.ValueLabelHolder");
			return x.innerText;
			
		case "contexto":
			x = document.querySelector("#com_ibm_team_workitem_web_mvvm_view_editor_RichTextEditorView_0 > div.RichTextEditorWidget.ViewBorder.com-ibm-team-workitem-shared-RichText.cke_editable.cke_editable_inline.cke_contents_ltr");
		    var texto = x.innerText;
			return texto.replace(/\n|\r/g,"");
			
		case "necessidade":
			x = document.querySelector("#com_ibm_team_workitem_web_mvvm_view_editor_RichTextEditorView_1 > div.RichTextEditorWidget.ViewBorder.com-ibm-team-workitem-shared-RichText.cke_editable.cke_editable_inline.cke_contents_ltr"); 
	        var texto = x.innerText; 
			return texto.replace(/\n|\r/g, "");
			
		case "expectativa":
			x = document.querySelector("#com_ibm_team_workitem_web_mvvm_view_editor_RichTextEditorView_2 > div.RichTextEditorWidget.ViewBorder.com-ibm-team-workitem-shared-RichText.cke_editable.cke_editable_inline.cke_contents_ltr"); 		
			var texto = x.innerText; 
			return texto.replace(/\n|\r/g, "");
	}
	return "Falha";
 }
 

 