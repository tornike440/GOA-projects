



	const addFundsBtn = document.getElementById('addFundsBtn');
    const currentFundsElement = document.getElementById('funds');
function Horse(id, x, y){
	this.element = document.getElementById(id);
	this.speed = Math.random()*10 + 10; 
	this.originX = x;
	this.originY = y;
	this.x = x; 
	this.y = y; 
	this.number = parseInt(id.replace(/[\D]/g, '')); 
	this.lap = 0; 

	this.moveRight = function(){
		var horse = this;

		
		setTimeout(function(){
			
			horse.x ++;
			horse.element.style.left = horse.x +'vw';

			
			if (horse.lap == num_lap && horse.x > horse.originX + 6){
				horse.arrive();
			}else{
				
				if (horse.x < 82.5 - horse.number*2.5){
					horse.moveRight();
				}else{
					
					horse.element.className = 'horse runDown';
					
					horse.speed = Math.random()*10 + 10;
					horse.moveDown();
				}
			}

		}, 1000/this.speed);
		
	}

	
	this.moveDown = function(){
		var horse = this;
		setTimeout(function(){
			horse.y ++;
			horse.element.style.top = horse.y +'vh';
			if (horse.y < horse.originY + 65){
				horse.moveDown();
			}else{
				horse.element.className = 'horse runLeft';
				horse.speed = Math.random()*10 + 10;
				horse.moveLeft();
			}
		}, 1000/this.speed)
	}
	this.moveLeft = function(){
		var horse = this;
		setTimeout(function(){
			horse.x --;
			horse.element.style.left = horse.x +'vw';
			if (horse.x > 12.5 - horse.number*2.5){
				horse.moveLeft();
			}else{
				horse.element.className = 'horse runUp';
				horse.speed = Math.random()*10 + 10;
				horse.moveUp();
			}
		}, 1000/this.speed)
	}
	this.moveUp = function(){
		var horse = this;
		setTimeout(function(){
			horse.y --;
			horse.element.style.top = horse.y +'vh';
			if (horse.y > horse.originY){
				horse.speed = Math.random()*10 + 10;
				horse.moveUp();
			}else{
				horse.element.className = 'horse runRight';
				
				horse.lap ++;
				horse.moveRight();
			}
		}, 1000/this.speed)
	}

	
	this.run = function(){
		this.element.className = 'horse runRight';
		this.moveRight();
	}
	this.arrive = function(){
		
		this.element.className = 'horse standRight';
		this.lap = 0;

		
		var tds = document.querySelectorAll('#results .result');
		
		tds[results.length].className = 'result horse'+this.number;

		
		results.push(this.number);

		
		if (results.length == 1){
			
			if (this.number == bethorse){
				funds += amount;
			}else{
				funds -= amount;
			}
			document.getElementById('funds').innerText = funds;
		}else if (results.length == 4){
			
			document.getElementById('start').disabled = false;
		}
	}
}

var num_lap = 1, results = [], funds = 100, bethorse, amount;


document.addEventListener("DOMContentLoaded", function(event) {

	var horse1 = new Horse('horse1', 20, 4);
	var horse2 = new Horse('horse2', 20, 8);
	var horse3 = new Horse('horse3', 20, 12);
	var horse4 = new Horse('horse4', 20, 16);

	
	document.getElementById('start').onclick = function(){
		amount = parseInt(document.getElementById('amount').value);

		
		if (amount <= 0) {
			alert('Please enter a positive bet amount.');
			return;
		}

		
		if (isNaN(amount)) {
			alert('Please enter a valid bet amount.');
			return;
		}

		num_lap = parseInt(document.getElementById('num_lap').value);
		bethorse = parseInt(document.getElementById('bethorse').value);

		if (funds < amount){
			alert('Not enough funds.');
		}
		else if (num_lap <= 0){
			alert('Number of lap must be greater than 0.');
		}else{

			
			this.disabled = true
			var tds = document.querySelectorAll('#results .result');
			for (var i = 0; i < tds.length; i++) {
				tds[i].className = 'result';
			}

			document.getElementById('funds').innerText = funds;
			results = [];
			horse1.run();
			horse2.run();
			horse3.run();
			horse4.run();
		}
	}
});

addFundsBtn.addEventListener('click', function () {
	
	const addedFunds = parseFloat(prompt('Enter the amount to add:')) || 0;

	if (addedFunds > 0) {
		funds += addedFunds;
		currentFundsElement.innerText = funds;
		alert(`Funds added: £${addedFunds}`);
	} else {
		alert('Please enter a valid amount to add funds.');
	}
});

(function() {
  const userId = localStorage.getItem('currentUserId');
  if (!userId) {
    window.location.href = 'login.html';
    return;
  }

  const userDataRaw = localStorage.getItem(userId);
  if (!userDataRaw) {
    localStorage.removeItem('currentUserId');
    window.location.href = 'login.html';
    return;
  }

  window.currentUser = JSON.parse(userDataRaw);

  if (window.currentUser.coins <= 0) {
    alert("You have 0 coins and cannot play this game.");
    // Here you can disable play buttons or redirect user
  }
})();


