function animateProgressBar() {
    const progressBars = document.querySelectorAll('.progress-bar');
    
    progressBars.forEach(bar => {
      const targetLevel = parseInt(bar.getAttribute('data-level'));
      let width = 0;
      
      const interval = setInterval(() => {
        if (width >= targetLevel) {
          clearInterval(interval);
        } else {
          width++; 
          bar.style.width = width + '%';
          bar.setAttribute('aria-valuenow', width);
        }
      }, 20);
    });
  }
  
  window.onload = function() {
    animateProgressBar();
  };