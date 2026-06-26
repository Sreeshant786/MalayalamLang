// Detect selected mode
const mode = localStorage.getItem("mode");

// Page Load
window.onload = function () {

    const modeTitle = document.getElementById("modeTitle");
    const editor = document.getElementById("code");

    if (mode === "latin") {

        modeTitle.innerText = "Latin Script Mode";

        editor.value =
`flag = sathyam

kanikkuka(flag)`;

    } else {

        modeTitle.innerText = "Malayalam Script Mode";

        editor.value =
`flag = സത്യം

കാണിക്കുക(flag)`;
    }
};


// Run Button
async function runCode() {

    const code =
        document.getElementById("code").value;

    try {

        console.log("Sending Request...");

        const response = await fetch(
    "https://malayalamlang.onrender.com/run",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    code: code,
                    mode: localStorage.getItem("mode") || "malayalam"
                })
            }
        );

        console.log("Response Status:", response.status);

        const data = await response.json();
        

        document.getElementById("output").innerText =
            data.output || "No output received";

    }
    catch (error) {

        console.error("ERROR:");
        console.error(error);


        document.getElementById("output").innerText =
            "Error connecting to backend";
    }
}