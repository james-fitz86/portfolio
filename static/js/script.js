const navButton = document.querySelector(".navbar-toggler");
const navBar = document.getElementById("navbarNav");

navButton.addEventListener("click", function(){
  navBar.classList.toggle("show");
});

const messages = document.querySelectorAll('.message-container');
const messageContainer = document.getElementById('message-wrapper');
const previousArrow = document.querySelector(".previous");
const nextArrow = document.querySelector(".next");

let presentIndex = 0;
 
function updateDisplay() {
    messages.forEach((message, index) => {
        if (index === presentIndex) {
            message.style.display = 'block';
          } else {
            message.style.display = 'none';
          }
    });
};

updateDisplay();

function navigatePrevious(){
  presentIndex = (presentIndex === 0) ? messages.length - 1 : presentIndex - 1;
  updateDisplay();
};
previousArrow.addEventListener('click', navigatePrevious);
previousArrow.addEventListener("keydown", function(event){
    if ( event.key === "Enter"){
        navigatePrevious();
    }
});

function navigateNext(){
  presentIndex = (presentIndex === messages.length - 1) ? 0 : presentIndex + 1;
  updateDisplay();
};

nextArrow.addEventListener('click', navigateNext);
nextArrow.addEventListener("keydown", function(event){
    if ( event.key === "Enter"){
        navigateNext();
    }
});