let scores, roundScore, activePlayer, gamePlaying;

init();

// round play
document.querySelector('.btn-roll').addEventListener('click', function() {
    if(gamePlaying) {
        // roll random numbers
        let dice1 = Math.floor(Math.random() * 6) + 1;
        let dice2 = Math.floor(Math.random() * 6) + 1;

        // update src path
        document.getElementById('dice-1').src = 'static/img/dice-' + dice1 + '.png';
        document.getElementById('dice-2').src = 'static/img/dice-' + dice2 + '.png';

        // display dice roll result
        document.getElementById('dice-1').style.display = 'block';
        document.getElementById('dice-2').style.display = 'block';

        // update the round score IF a rolled number is NOT a 1
        if (dice1 !== 1 && dice2 !== 1) {
            // add score
            roundScore += dice1 + dice2;
            document.querySelector('#current-' + activePlayer).textContent = roundScore;
        } else {
            // next player
            nextPlayer();
        }
    }    
});

// HOLD procedures
document.querySelector('.btn-hold').addEventListener('click', function() {
    if (gamePlaying) {
        // Add CURRENT score to GLOBAL score
        scores[activePlayer] += roundScore;

        // Update the UI
        document.querySelector('#score-' + activePlayer).textContent = scores[activePlayer];
        
        // get user input winning target score
        let winningScore = document.querySelector('.final-score').value;
        
        // set winning score
        if(winningScore) {
            winningScore = winningScore;
        } else {
            // default winning score
            winningScore = 120;
        }
        
        // check if player won the game
        if (scores[activePlayer] >= winningScore) {
            document.querySelector('#name-' + activePlayer).textContent = 'Winner!';
            document.getElementById('dice-1').style.display = 'none';
            document.getElementById('dice-2').style.display = 'none';
            document.querySelector('.player-' + activePlayer + '-panel').classList.add('winner');
            document.querySelector('.player-' + activePlayer + '-panel').classList.remove('active');
            gamePlaying = false;
        } else {
            // next player
            nextPlayer();
        }
    }
});


function nextPlayer() {
    // active player
    activePlayer === 0 ? activePlayer = 1 : activePlayer = 0;
    roundScore = 0;

    // reset round scores
    document.getElementById('current-0').textContent = '0';
    document.getElementById('current-1').textContent = '0';

    document.querySelector('.player-0-panel').classList.toggle('active');
    document.querySelector('.player-1-panel').classList.toggle('active');

    // hide dice till rolled again
    document.getElementById('dice-1').style.display = 'none';
    document.getElementById('dice-2').style.display = 'none';
}

// new game event
document.querySelector('.btn-new').addEventListener('click', init);

// new game
function init() {

    // initialize scores
    scores = [0, 0];
    roundScore = 0;
 
    // default active player = player 1
    activePlayer = 0;

    gamePlaying = true;

    // hide dice till rolled
    document.getElementById('dice-1').style.display = 'none';
    document.getElementById('dice-2').style.display = 'none';

    // update UI
    document.getElementById('score-0').textContent = '0';
    document.getElementById('score-1').textContent = '0';
    document.getElementById('current-0').textContent = '0';
    document.getElementById('current-1').textContent = '0';
    document.getElementById('name-0').textContent = 'Player 1';
    document.getElementById('name-1').textContent = 'Player 2';
    document.querySelector('.player-0-panel').classList.remove('winner');
    document.querySelector('.player-1-panel').classList.remove('winner');
    document.querySelector('.player-0-panel').classList.remove('active');
    document.querySelector('.player-1-panel').classList.remove('active');
    document.querySelector('.player-0-panel').classList.add('active');
}