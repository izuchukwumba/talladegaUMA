let chatButton = document.querySelector(".chat-button");
let iframe = document.querySelector("iframe");

chatButton.addEventListener("click", () => {
  if (iframe.style.opacity === "0") {
    iframe.style.opacity = "1";
    iframe.style.zIndex = "1";
    chatButton.innerHTML = "Close Chat";
  } else {
    iframe.style.opacity = "0";
    iframe.style.zIndex = "-1";
    chatButton.innerHTML = "Chat Now";
  }
  alert("Your Child's Flight is Now Boarding");
});

document.querySelector(".plan-travel").addEventListener("click", () => {
  alert("Your Child's Flight is Now Boarding");
});

document.querySelector(".travel-info").addEventListener("click", () => {
  alert("Your Child Is Mid-Flight and Everything is Alright!");
});

document.querySelector(".advantage").addEventListener("click", () => {
  alert("Your Child's Flight Arrives in 10 Minutes");
});
document.querySelector(".login").addEventListener("click", () => {
  alert("Plane Landed. Please Head To Baggage Claim.");
});
