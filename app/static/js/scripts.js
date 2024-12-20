document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const captureButton = document.getElementById('capture-qr');
    const context = canvas.getContext('2d');
    const capturedImage = document.getElementById('captured-image');
    const captureInput = document.getElementById('capture');

    // Access the device camera
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            video.srcObject = stream;
            video.play();
            console.log("Camera access granted");
        })
        .catch(function(err) {
            console.error("Error accessing the camera: " + err);
        });

    // Capture image and validate QR code
    captureButton.addEventListener('click', function() {
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
        const code = jsQR(imageData.data, canvas.width, canvas.height);

        if (code) {
            console.log("QR Code detected:", code.data);
            // Validate the QR code with the server
            fetch('/validate_qr', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ qr_code: code.data })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log("QR code validated successfully");
                    // Handle successful login
                } else {
                    console.error("QR code validation failed");
                    // Handle failed login
                }
            })
            .catch(error => {
                console.error("Error validating QR code: " + error);
            });
        } else {
            console.error("No QR code detected");
        }
    });
    });
    
    // Handle image capture
    captureInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                capturedImage.src = e.target.result;
                capturedImage.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    });
