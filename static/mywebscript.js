let RunSentimentAnalysis = () => {
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            try {
                let response = JSON.parse(xhttp.responseText);
                displayTable(response);
            } catch (error) {
                displayTable(xhttp.responseText);
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze" + "=" + textToAnalyze, true);
    xhttp.send();
}

function displayTable(data) {
    let max = 0;
    let maxEmotion = "";
    console.log(data);
    if (typeof(data) === "string") {
        document.getElementById("system_response").innerHTML = data;
    }
    else {
    
        let tableHtml = "<table border='1'><tr><th>Emotion</th><th>Score</th></tr>";

        for (const [key, value] of Object.entries(data)) {
            tableHtml += `<tr><td>${key}</td><td>${value}</td></tr>`;
            if (value > max) {
                max = value;
                maxEmotion = key;
            }
        }
        tableHtml += "</table>";
        document.getElementById("system_response").innerHTML = tableHtml;
        document.getElementById("maxEmotion").innerHTML = maxEmotion;
    }
}
// }
