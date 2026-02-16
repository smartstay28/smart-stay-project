function processPayment() {

    let method = document.querySelector('input[name="payment_method"]:checked');

    if (!method) {
        alert("Please select payment method");
        return;
    }

    if (method.value === "cod") {
        document.getElementById("payment-status").innerText =
            "Order placed successfully! Payment mode: COD";
        
        // Send AJAX to backend
        fetch("/save-payment/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                status: "pending",
                method: "COD"
            })
        });

    } else {

        var options = {
            "key": "YOUR_RAZORPAY_KEY",
            "amount": 5000 * 100,
            "currency": "INR",
            "name": "PG Management",
            "description": "Room Booking Payment",
            "handler": function (response){
                
                document.getElementById("payment-status").innerText =
                    "Payment Successful! Payment ID: " + response.razorpay_payment_id;

                fetch("/save-payment/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        status: "paid",
                        method: "Razorpay",
                        payment_id: response.razorpay_payment_id
                    })
                });
            }
        };

        var rzp1 = new Razorpay(options);
        rzp1.open();
    }
}
