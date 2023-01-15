function trim(s) {
    if (s == null)
        return '';
    while (s.substring(0, 1) === ' ') {
        s = s.substring(1, s.length);
    }
    while (s.substring(s.length - 1, s.length) === ' ') {
        s = s.substring(0, s.length - 1);
    }
    return s;
}

function checkName(theInput, str) {
    var name = trim(theInput.value);
    if (name==""){
        alert("Please fill in all fields on the form.");
        theInput.focus();
        return false;
    }
    const reg = /^[A-Za-z]*(?: [A-Z][a-z]*)*$/;
    if (!name.match(reg)){
        if (str == "n"){
          alert("Name must consist of letters only.");
        }else{
          alert("Surame must consist of letters only.");
        }
        return false;
    }
    return true;
}

function checkEmail(theInput){
    var name = theInput.value;
    if (name==""){
        alert("Please fill in all fields on the form.");
        theInput.focus();
        return false;
    }
    const reg = /([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|"([]!#-[^-~ \t]|(\\[\t -~]))+")@([0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?(\.[0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?)*|\[((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|IPv6:((((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){6}|::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){5}|[0-9A-Fa-f]{0,4}::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){4}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):)?(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){3}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,2}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){2}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,3}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,4}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::)((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3})|(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3})|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,5}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3})|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,6}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::)|(?!IPv6:)[0-9A-Za-z-]*[0-9A-Za-z]:[!-Z^-~]+)])/;
    if(!name.match(reg)){
        alert("E-mail format is incorrect");
        return false;
    }
    return true;
}

function check_password(theInput) {
    var regex = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})/;
    var name = document.getElementById('name').value.toLowerCase();
    if (!theInput.value.match(regex)) {
        alert("Password doesn't match required pattern.");
        return false; 
    } else if (theInput.value.toLowerCase().includes(name)) {
        alert("Password can't include name.");
        return false;
    }
    return true;
}

function check_pass2(theInput){
    if (theInput.value != document.getElementById("password").value){
        alert("Passwords do not match.");
        return false;
    }else{
        return true;
    }
}

function validate_form(){
    var name = document.getElementById("name")
    var surname = document.getElementById("surname")
    var email = document.getElementById("email")
    var password =  document.getElementById("password")
    var pass2 = document.getElementById("password2")
    var check = document.getElementById("terms")
    if (checkName(name) && checkName(surname) && checkEmail(email) && check_password(password) && check_pass2(pass2) && check.checked){
        return true;
    }else if(!check.checked){
        alert("Need to agree on Terms and Conditions.")
        return false;
    }
    return false;
}
