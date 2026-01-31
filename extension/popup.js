const output = document.getElementById("output");
const button = document.getElementById("snap");

button.addEventListener("click", async () => {
  output.innerText = "Extracting terms...";

  try {
    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true
    });

    chrome.scripting.executeScript(
      {
        target: { tabId: tab.id },
        func: extractText
      },
      async (results) => {
        if (!results || !results[0] || !results[0].result) {
          output.innerText = "Could not extract text.";
          return;
        }

        const pageText = results[0].result;
        output.innerText = "Summarizing...";

        try {
          const response = await fetch("http://127.0.0.1:5000/summarize", {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: pageText })
          });

          const rawText = await response.text();

          try {
            const data = JSON.parse(rawText);
            output.innerText = data.summary || "No summary returned.";
          } catch (jsonError) {
            console.error("Non-JSON response:", rawText);
            output.innerText = "Backend returned invalid response.";
          }

        } catch (fetchError) {
          console.error("Fetch error:", fetchError);
          output.innerText = "Failed to connect to backend.";
        }
      }
    );

  } catch (err) {
    console.error("Extension error:", err);
    output.innerText = "Something went wrong.";
  }
});

// ✅ MUST be outside the click handler
function extractText() {
  return document.body.innerText;
}
