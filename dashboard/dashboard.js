let chatButton = document.querySelector(".chat-button");
let iframe = document.querySelector("iframe");

chatButton.addEventListener("click", () => {
  //   if (iframe.style.display === "none") {
  //     iframe.style.display = "block";
  //     chatButton.innerHTML = "Close Chat";
  //   } else {
  //     iframe.style.display = "none";
  //   }

  if (iframe.style.opacity === "0") {
    iframe.style.opacity = "1";
    iframe.style.zIndex = "1";
    chatButton.innerHTML = "Close Chat";
  } else {
    iframe.style.opacity = "0";
    iframe.style.zIndex = "-1";
    chatButton.innerHTML = "Chat Now";
  }
});

let notif = document.querySelector(".notif");

notif.addEventListener(click, () => {
  alert("Your child's flight is now boarding");
});

let modal = document.querySelector(".modal")


modal.addEventListener("click", ()=>{
    if (modal.style.display === "none"){
        modal.style.display = "block"
        modal.innerHTML = 
    }
})
