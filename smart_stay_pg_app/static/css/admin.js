function showSection(id, element) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => section.style.display = 'none');
  
    document.getElementById(id).style.display = 'block';
  
    const menuItems = document.querySelectorAll('.sidebar ul li');
    menuItems.forEach(item => item.classList.remove('active'));
  
    element.classList.add('active');
  }
  