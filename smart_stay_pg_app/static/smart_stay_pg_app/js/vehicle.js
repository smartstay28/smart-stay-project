function handleBooking() {
  const vehicle = document.getElementById("vehicleType").value;
  const date = document.getElementById("date").value;
  const time = document.getElementById("time").value;
  const amount = document.getElementById("amount").value;
  const paymentMode = document.getElementById("paymentMode").value;

  if (!date || !time) {
    document.getElementById("result").innerText = "❌ Select date & time!";
    return;
  }

  if (paymentMode === "COD") {
    document.getElementById("result").innerText =
      `✅ ${vehicle} booked on ${date} at ${time}. Payment Mode: COD (₹${amount})`;
  } else {
    openRazorpay(vehicle, date, time, amount);
  }
}

function openRazorpay(vehicle, date, time, amount) {
  var options = {
    "key": "rzp_test_1234567890",   // 🔴 Replace with your Razorpay TEST Key
    "amount": amount * 100,
    "currency": "INR",
    "name": "Vehicle Rental System",
    "description": "Vehicle Booking Payment",
    "handler": function (response) {
      document.getElementById("result").innerText =
        `✅ Payment Successful!\nVehicle: ${vehicle}\nDate: ${date}\nTime: ${time}\nPayment ID: ${response.razorpay_payment_id}`;
    },
    "prefill": {
      "name": "Demo User",
      "email": "demo@gmail.com",
      "contact": "9999999999"
    },
    "theme": {
      "color": "#22c55e"
    }
  };

  var rzp = new Razorpay(options);
  rzp.open();
}

function updateAvailability() {
  const vehicle = document.getElementById("adminVehicle").value;
  const availability = document.getElementById("availability").value;

  document.getElementById("adminResult").innerText =
    `🔄 ${vehicle} is now marked as ${availability}`;
}
