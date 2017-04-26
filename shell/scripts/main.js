
var signUpNextButton = document.getElementById("signup_next");


signUpNextButton.addEventListener("click", function () {
    document.getElementById("signup_step1").classList.add("invisible");
    document.getElementById("signup_step2").classList.remove("invisible")
});
