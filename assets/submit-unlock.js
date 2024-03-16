document.getElementById("submitBtn").onclick = (e) => {
    const input = prompt("Enter Passcode: ");
    if (input == 7192) {
        return true;
    }
    else {
        window.alert("Passcode Invalid!");
        e.preventDefault();
    }
}
