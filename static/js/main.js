"use strict"


function deleteComment (messageId){
            let form = document.getElementById("delete");
            let input = form.children[0];
            input.value = messageId.toString();
            form.submit();
        }

function updateComment(messageId){

            let updateForm = document.createElement("form")
            updateForm.action =window.location.href+"/update/"+messageId.toString();
            updateForm.method="POST"

            let par = document.getElementById("p"+messageId.toString())

            let input_text = document.createElement("input");
            input_text.type = "text";
            input_text.name ="text";
            input_text.required = true;
            input_text.value = par.innerText;

            let input_submit = document.createElement("input");

            input_submit.type="submit";
            input_submit.value="Принять"

            par.remove();

            let token = document.getElementById("csrf_token");
            updateForm.appendChild(token);
            updateForm.appendChild(input_text);
            updateForm.appendChild(input_submit);
            let parent = document.getElementById("m"+messageId);
            parent.appendChild(updateForm);
        }


