// Generate random number / dice roll
function getRandomIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min); 
  }

// Changes img src
function newDice(diceRollResult) {
    var src = "images/dice"+ diceRollResult +".png"
    return src
  }
    
  // new dice rolls generated each time the webpage is refreshed
  var randomDiceRoll = getRandomIntInclusive(1, 6)
  var randomDiceRoll2 = getRandomIntInclusive(1, 6)
 
  var newDice1 = newDice(randomDiceRoll)
  var newDice2 = newDice(randomDiceRoll2)

  // updating dice image
  document.getElementById("dice1").setAttribute("src", newDice1)
  document.getElementById("dice2").setAttribute("src", newDice2)
  
  // Conditions for winner
  if (randomDiceRoll === randomDiceRoll2){
    document.getElementById("result").innerHTML = "DRAW !";
  }
  else if(randomDiceRoll > randomDiceRoll2){
    document.getElementById("result").innerHTML = "Player 1 Wins!";

  }
  else{
    document.getElementById("result").innerHTML = "Player 2 Wins!";
  }