const messages = document.querySelectorAll('.message-container');
const messageContainer = document.getElementById('message-wrapper');
const previousArrow = document.querySelector(".previous");
const nextArrow = document.querySelector(".next");
const commentSections = document.querySelectorAll('.comments-container');
const leftArrows = document.querySelectorAll('.arrow2.left');
const rightArrows = document.querySelectorAll('.arrow2.right');


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

commentSections.forEach((commentsContainer, sectionIndex) => {
  const comments = commentsContainer.querySelectorAll('.comment');
  const deleteButtons = commentsContainer.querySelectorAll('.btn-danger');
  let currentIndex = 0;

  function refreshComments() {
    comments.forEach((comment, idx) => {
      if (idx === currentIndex) {
        comment.style.display = 'block';
        deleteButtons[idx].style.display = 'block';
      } else {
        comment.style.display = 'none';
        deleteButtons[idx].style.display = 'none';
      }
    });
  }

  refreshComments();

  function goToPreviousComment() {
    currentIndex = (currentIndex === 0) ? comments.length - 1 : currentIndex - 1;
    refreshComments();
  }

  function goToNextComment() {
    currentIndex = (currentIndex === comments.length - 1) ? 0 : currentIndex + 1;
    refreshComments();
  }

  leftArrows[sectionIndex].addEventListener('click', goToPreviousComment);
  leftArrows[sectionIndex].addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
      goToPreviousComment();
    }
  });

  rightArrows[sectionIndex].addEventListener('click', goToNextComment);
  rightArrows[sectionIndex].addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
      goToNextComment();
    }
  });
});