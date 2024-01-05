// Front End

function submitFeedback() {
    let userCode = document.getElementById("user-code").value;
    let overallSatisfaction = document.getElementById("overall-satisfaction").value;
    let usability = document.getElementById("usability").value;
    let contentQuality = document.getElementById("content-quality").value;

    // Show the alert
    alert(`Thank you for your feedback!
           Overall Satisfaction: ${overallSatisfaction}
           Usability: ${usability}
           Content Quality: ${contentQuality}`);

    // Send data to server
    fetch('/submit_feedback', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            userCode: userCode,
            overallSatisfaction: overallSatisfaction,
            usability: usability,
            contentQuality: contentQuality
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    // Reset the form
    document.getElementById("feedback-form").reset();
}
