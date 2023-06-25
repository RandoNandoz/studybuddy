const startbtn = document.querySelector(".startbtn");
const timeSpan = document.querySelector(".time");
const progress = document.querySelector(".progress");

startbtn.addEventListener("click", ()=> {
    let interval = 5; //make this user input
    var countdown = setInterval(() => {
        interval--;
        let progresswidth= interval/10 * 100

        if(interval>0){
            progress.style.width = progresswidth + "%";
            timeSpan.innerHTML=interval + "s";
        }
        else{
            clearInterval(countdown);
            progress.style.width = "0%"
            timeSpan.innerHTML = "completed";
        }
    }, 1000);
})