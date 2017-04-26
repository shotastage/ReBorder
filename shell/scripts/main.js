
var signUpNextButton = document.getElementById("signup_next");


signUpNextButton.addEventListener("click", function () {
    document.getElementById("signup_step1").classList.add("invisible");
    document.getElementById("signup_step2").classList.remove("invisible")
});

$("#reader").html5_qrcode(function(data){
 		 // do something when code is read
 	},
 	function(error){
		//show read errors
	}, function(videoError){
		//the video stream could be opened
	}
);
