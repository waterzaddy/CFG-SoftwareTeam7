// Virtual pet attributes
let health = 100;
let happiness = 100;

// Function to update virtual pet's health and happiness
function updatePetAttributes() {
    document.getElementById('health').textContent = health;
    document.getElementById('happiness').textContent = happiness;
}

// Function to feed the virtual pet
function feedPet() {
    health += 10;
    updatePetAttributes();
}
// Function to drink water/give water to the virtual pet
function waterPet() {
    health += 10;
    updatePetAttributes();
}

// Function to play with the virtual pet
function playWithPet() {
    happiness += 10;
    updatePetAttributes();
}

// Function to handle self-care actions
function handleSelfCareActions() {
    const action1 = document.getElementById('action1').checked;
    const action2 = document.getElementById('action2').checked;
    const action3 = document.getElementById('action3').checked;

    if (action1) {
        health += 5;
    }
    if (action2) {
        happiness += 5;
    }
    if (action3) {
        happiness += 10;
    }

    updatePetAttributes();
}

// Function to run the app
function run() {
    // Attach event listener to self-care actions checkboxes
    document.getElementById('action1').addEventListener('change', handleSelfCareActions);
    document.getElementById('action2').addEventListener('change', handleSelfCareActions);
    document.getElementById('action3').addEventListener('change', handleSelfCareActions);
}

// Run the app
run();
