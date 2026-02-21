
const content = document.getElementById("content-area");
// ROOM BOOKING
function loadRooms(){
content.innerHTML = `
<h2>Book Room</h2>
<div class="card-grid">
${roomCard(2,6000)}
${roomCard(3,5200)}
${roomCard(4,4500)}
${roomCard(5,4000)}
${roomCard(6,3500)}
</div>`;
}

function roomCard(share,price){
return `
<div class="card">
<img src="../images/room${share}.jpg">
<div class="card-body">
<h3>${share} Sharing</h3>
<p>₹${price} / month</p>
<button onclick="alert('Room Booked!')">Book Now</button>
</div>
</div>`;
}

// VEHICLE BOOKING
function loadVehicles(){
content.innerHTML = `
<h2>Book Vehicle</h2>
<div class="card-grid">
${vehicleCard("Bike",200,"bike.jpg")}
${vehicleCard("Car",500,"car.jpg")}
</div>`;
}

function vehicleCard(name,price,img){
return `
<div class="card">
<img src="images/${img}">
<div class="card-body">
<h3>${name}</h3>
<p>₹${price} / hour</p>
<button onclick="alert('${name} Booked!')">Book Now</button>
</div>
</div>`;
}

// EDIT PROFILE
function loadProfile(){
content.innerHTML = `
<h2>Edit Profile</h2>
<input placeholder="Name">
<input placeholder="Mobile Number">
<input placeholder="Email">
<input placeholder="Occupation">
<textarea placeholder="Address"></textarea>
<button>Save Profile</button>`;
}

// INBOX
function loadInbox(){
content.innerHTML = `
<h2>Inbox</h2>
<div class="card">
<div class="card-body">
<p>📢 Admin: Maintenance on Sunday</p>
<p>📢 Admin: New rules updated</p>
</div>
</div>`;
}

// COMPLAINT
function loadComplaint(){
content.innerHTML = `
<h2>Register Complaint</h2>
<select>
<option>Cleaning</option>
<option>Room</option>
<option>Person</option>
</select>
<textarea placeholder="Write your complaint"></textarea>
<button>Submit Complaint</button>`;
}

// FEEDBACK
function loadFeedback(){
content.innerHTML = `
<h2>Feedback</h2>
<div class="star">
<i onclick="rate(1)" class="fa fa-star"></i>
<i onclick="rate(2)" class="fa fa-star"></i>
<i onclick="rate(3)" class="fa fa-star"></i>
<i onclick="rate(4)" class="fa fa-star"></i>
<i onclick="rate(5)" class="fa fa-star"></i>
</div>
<textarea placeholder="Write feedback"></textarea>
<button>Submit Feedback</button>`;
}

function rate(star){
alert("Rated "+star+" Stars");
}
