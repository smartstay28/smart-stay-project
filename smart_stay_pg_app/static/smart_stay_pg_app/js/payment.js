document.getElementById("payBtn").addEventListener("click", processPayment);

function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute("content");
}

async function processPayment() {

    let method = document.querySelector('input[name="payment_method"]:checked');
    let amount = document.getElementById("amount").innerText;
    let statusText = document.getElementById("payment-status");

    if (!method) {
        alert("Please select payment method");
        return;
    }

    // ================= COD =================
    if (method.value === "COD") {

        const response = await fetch("/save-payment/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()
            },
            body: JSON.stringify({
                status: "pending",
                method: "COD",
                amount: amount
            })
        });

        const data = await response.json();

        if (data.status === "success") {
            statusText.innerText = "Order placed successfully! Payment mode: COD";
            statusText.style.color = "green";
        } else {
            statusText.innerText = "Something went wrong!";
            statusText.style.color = "red";
        }

    }

    // ================= RAZORPAY =================
    else {

        // 1️⃣ Create order from backend
        const orderResponse = await fetch("/create-order/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()
            },
            body: JSON.stringify({ amount: amount })
        });

        const orderData = await orderResponse.json();

        if (!orderData.order_id) {
            alert("Order creation failed");
            return;
        }

        // 2️⃣ Razorpay Options
        var options = {
            "key": orderData.key,
            "amount": orderData.amount,
            "currency": "INR",
            "name": "PG Management System",
            "description": "Room Booking Payment",
            "order_id": orderData.order_id,

            "handler": async function (response) {

                // 3️⃣ Verify Payment on Backend
                const verifyResponse = await fetch("/verify-payment/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCSRFToken()
                    },
                    body: JSON.stringify({
                        razorpay_order_id: response.razorpay_order_id,
                        razorpay_payment_id: response.razorpay_payment_id,
                        razorpay_signature: response.razorpay_signature,
                        amount: amount
                    })
                });

                const verifyData = await verifyResponse.json();

                if (verifyData.status === "success") {
                    statusText.innerText = "Payment Successful! Payment ID: " + response.razorpay_payment_id;
                    statusText.style.color = "green";
                } else {
                    statusText.innerText = "Payment verification failed!";
                    statusText.style.color = "red";
                }
            },

            "theme": {
                "color": "#3399cc"
            }
        };

        var rzp = new Razorpay(options);
        rzp.open();
    }
}
