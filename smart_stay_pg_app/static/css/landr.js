// Registration
document.getElementById("registerForm")?.addEventListener("submit", function (e) {
  e.preventDefault();

  const userData = {
    username: document.getElementById("username").value,
    name: document.getElementById("name").value,
    mobile: document.getElementById("mobile").value,
    email: document.getElementById("email").value,
    aadhar: document.getElementById("aadhar").value,
    address: document.getElementById("address").value,
    occupation: document.getElementById("occupation").value,
    password: document.getElementById("password").value
  };

  localStorage.setItem("userData", JSON.stringify(userData));
  alert("Registration successful!");
  window.location.href = "login.html";
});

// Login
document.getElementById("loginForm")?.addEventListener("submit", function (e) {
  e.preventDefault();

  const savedData = JSON.parse(localStorage.getItem("userData"));

  const username = document.getElementById("loginUsername").value;
  const password = document.getElementById("loginPassword").value;

  if (savedData && username === savedData.username && password === savedData.password) {
    alert("Login successful!");
  } else {
    alert("Invalid username or password");
  }
});
