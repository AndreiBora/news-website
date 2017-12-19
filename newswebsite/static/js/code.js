function clearForm(){
  document.getElementById('fullName').value ="";
  document.getElementById('commentArea').value = "";
  document.getElementById('emailAdr').value = "";
  document.getElementById('phoneNr').value = "";
}

function addComment() {
  var parent = document.getElementById('comment-zone');
  let name = document.getElementById('fullName').value;
  let comment =document.getElementById('commentArea').value;
  var text = "<div class=\"panel panel-default\"> \
                <div class=\"panel-body\"> \
              <header class=\"text-left\"> \
                <div class=\"comment-user\"> \
                <i class=\"fa fa-user\"> \
                </i>"+ name + "</div> \
                <time class=\"comment-date\" datetime=\"16-12-2014 01:05\"><i class=\"fa fa-clock-o\"></i> Dec 16, 2014</time><br><br> \
              </header> \
              <div class=\"comment-post text-left\"> \
                <p>" + comment + "</p> \
              </div> \
            </div> \
          </div>";
  parent.insertAdjacentHTML('beforeend', text);
  clearForm();
}
