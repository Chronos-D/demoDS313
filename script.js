document.addEventListener("DOMContentLoaded", function() {
    const modelSelect = document.getElementById("model");
    const textInput = document.getElementById("text");
    const audioOutput = document.getElementById("audio");
    const convertButton = document.querySelector(".btn");

    async function generateSpeech() {
        const model = modelSelect.value;
        const text = textInput.value.trim();

        if (text === "") {
            alert("Please enter some text.");
            return;
        }

        // Disable button to prevent multiple requests
        convertButton.disabled = true;
        convertButton.textContent = "Converting...";

        try {
            const response = await fetch("https://your-tts-api-endpoint.com/generate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ model: model, text: text })
            });

            if (!response.ok) {
                throw new Error("Failed to generate speech");
            }

            const data = await response.json();
            audioOutput.src = data.audioUrl;
            audioOutput.style.display = "block";
        } catch (error) {
            console.error("Error:", error);
            alert("An error occurred while generating the speech. Please try again.");
        } finally {
            // Re-enable button after request completes
            convertButton.disabled = false;
            convertButton.textContent = "Convert to Speech";
        }
    }

    convertButton.addEventListener("click", generateSpeech);
});
