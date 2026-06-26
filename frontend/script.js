async function runCode() {

    const code = document.getElementById("code").value;
    const safeMode = localStorage.getItem("mode") || "malayalam";

    try {

        console.log("Sending Request...");

        const response = await fetch(
            "https://malayalamlang-backend.onrender.com/run",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    code: code,
                    mode: safeMode
                })
            }
        );

        console.log("STATUS:", response.status);

        const text = await response.text();
        console.log("RAW RESPONSE:", text);

        let data;
        try {
            data = JSON.parse(text);
        } catch (e) {
            throw new Error("Backend did not return JSON");
        }

        document.getElementById("output").innerText =
            data.output || "No output received";

        document.getElementById("python").innerText =
            data.python_code || "";

    }
    catch (error) {

        console.error("FULL ERROR:", error);

        document.getElementById("output").innerText =
            error.message;
    }
}