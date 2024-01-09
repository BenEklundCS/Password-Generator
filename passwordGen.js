function passwordGen(attempts = 0){
    // Ensure recursion never grows out of control
    const maxAttempts = 10;
    attempts++;
    if (attempts === maxAttempts) {
        console.error("Password generation reached max attempts " + maxAttempts);
        exit(1);
    }
    const minLen = 20;
    const maxLen = 60;
    const acceptable = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).*$/;

    let password = "";
    let len = getRandomInt(minLen, maxLen);

    for (let i = 0; i < len; i++) {
        password += getRandomAlphaNumeric();
    }

    return (acceptable.test(password)) ? password : passwordGen();
}

function getRandomAlphaNumeric() {
    const minDigit = 0;
    const maxDigit = 9;
    let alphaOrInt = getRandomInt(0, 1);
    return (alphaOrInt === 0) ? getRandomChar() :  getRandomInt(minDigit, maxDigit);
}
function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getRandomChar() {
    function randomCaps(c) {
        let willCap = getRandomInt(0, 1);
        return (willCap === 0) ? c.toLowerCase() : c;
    }
    const a = 65;
    const z = 90;
    return randomCaps(String.fromCharCode(getRandomInt(a, z)));
}

console.log(passwordGen());