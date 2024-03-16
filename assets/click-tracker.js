let clickCount = 0;
const element = document; // Replace with desired element selector (e.g., document.getElementById("my-button"))

element.addEventListener("click", function() {
    clickCount++;
    document.getElementById("click-count").textContent = "Clicks: " + clickCount + " / 10";
});