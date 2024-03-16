function answer_check(cipher, e){
    user_input = document.querySelector("input[type=text]").value;
    if (user_input.toLowerCase() != cipher.toLowerCase()){
        document.querySelector("span[name=error]").style.visibility = "visible";
        e.preventDefault();
    }
    else{
        return true;
    }
}

document.getElementById("answer-submit").onclick = (e) => {
    answer_check(cipher, e);
}