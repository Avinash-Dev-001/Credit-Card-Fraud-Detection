       
        document.getElementById("prediction-form").addEventListener("submit", function(event) {
            event.preventDefault();  

            const features = document.getElementById("features").value.split(',').map(Number); 

            
            fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ features: features })
            })
            .then(response => response.json())  
            .then(data => {
                
                if (data.prediction) {
                    document.getElementById("prediction-result").innerText = "Prediction: " + data.prediction;
                    document.getElementById("prediction-result").style.color = "#27ae60"; 
                } else {
                    document.getElementById("prediction-result").innerText = "Error: " + data.error;
                    document.getElementById("prediction-result").style.color = "#e74c3c"; 
                }
            })
            .catch(error => {
                // Handle error
                document.getElementById("prediction-result").innerText = "Error: " + error;
                document.getElementById("prediction-result").style.color = "#e74c3c";
            });
        });