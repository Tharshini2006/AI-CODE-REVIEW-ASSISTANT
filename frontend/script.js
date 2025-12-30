async function reviewCode() {
    const code = document.getElementById("code").value;
    const language = document.getElementById("language").value;
    const output = document.getElementById("output");

    // Basic validation
    if (!code.trim()) {
        output.textContent = "Please enter some code for review.";
        return;
    }

    output.textContent = "Reviewing code... Please wait.";

    try {
        const response = await fetch("http://127.0.0.1:8000/review", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: code,
                language: language
            })
        });

        const data = await response.json();
        output.textContent = data.review;

    } catch (error) {
        output.textContent = "Error connecting to backend server.";
    }
}
