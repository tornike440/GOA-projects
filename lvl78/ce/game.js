var num_lap = 1,
    results = [],
    funds = 0,
    bethorse,
    amount;

document.addEventListener("DOMContentLoaded", function () {
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
  funds = window.currentUser.coins || 0;

  if (funds <= 0) {
    alert("You have 0 coins and cannot play this game.");
  }

  document.getElementById("funds").innerText = funds;

  const addFundsBtn = document.getElementById('addFundsBtn');
  const currentFundsElement = document.getElementById('funds');

  addFundsBtn.addEventListener('click', function () {
    const addedFunds = parseFloat(prompt('Enter the amount to add:')) || 0;
    if (addedFunds > 0) {
      funds += addedFunds;
      currentFundsElement.innerText = funds;
      saveFunds();
      alert(`Funds added: £${addedFunds}`);
    } else {
      alert('Please enter a valid amount to add funds.');
    }
  });

  document.getElementById('start').onclick = function () {
    amount = parseInt(document.getElementById('amount').value);
    num_lap = parseInt(document.getElementById('num_lap').value);
    bethorse = parseInt(document.getElementById('bethorse').value);

    if (isNaN(amount) || amount <= 0) {
      alert('Please enter a valid, positive bet amount.');
      return;
    }
    if (funds < amount) {
      alert('Not enough funds.');
      return;
    }
    if (num_lap <= 0) {
      alert('Number of laps must be greater than 0.');
      return;
    }

    this.disabled = true;
    results = [];
    resetResultsDisplay();
    document.getElementById('funds').innerText = funds;

    new Horse('horse1', 20, 4).run();
    new Horse('horse2', 20, 8).run();
    new Horse('horse3', 20, 12).run();
    new Horse('horse4', 20, 16).run();
  };
});

function saveFunds() {
  window.currentUser.coins = funds;
  localStorage.setItem(localStorage.getItem('currentUserId'), JSON.stringify(window.currentUser));
}

function resetResultsDisplay() {
  const tds = document.querySelectorAll('#results .result');
  for (let i = 0; i < tds.length; i++) {
    tds[i].className = 'result';
  }
}

function Horse(id, x, y) {
  this.element = document.getElementById(id);
  this.speed = Math.random() * 10 + 10;
  this.originX = x;
  this.originY = y;
  this.x = x;
  this.y = y;
  this.number = parseInt(id.replace(/\D/g, ''));
  this.lap = 0;

  this.moveRight = () => {
    setTimeout(() => {
      this.x++;
      this.element.style.left = this.x + 'vw';

      if (this.lap == num_lap && this.x > this.originX + 6) {
        this.arrive();
      } else if (this.x < 82.5 - this.number * 2.5) {
        this.moveRight();
      } else {
        this.element.className = 'horse runDown';
        this.speed = Math.random() * 5 + 5;
        this.moveDown();
      }
    }, 1000 / this.speed);
  };

  this.moveDown = () => {
    setTimeout(() => {
      this.y++;
      this.element.style.top = this.y + 'vh';
      if (this.y < this.originY + 65) {
        this.moveDown();
      } else {
        this.element.className = 'horse runLeft';
        this.speed = Math.random() * 10 + 10;
        this.moveLeft();
      }
    }, 1000 / this.speed);
  };

  this.moveLeft = () => {
    setTimeout(() => {
      this.x--;
      this.element.style.left = this.x + 'vw';
      if (this.x > 12.5 - this.number * 2.5) {
        this.moveLeft();
      } else {
        this.element.className = 'horse runUp';
        this.speed = Math.random() * 10 + 10;
        this.moveUp();
      }
    }, 1000 / this.speed);
  };

  this.moveUp = () => {
    setTimeout(() => {
      this.y--;
      this.element.style.top = this.y + 'vh';
      if (this.y > this.originY) {
        this.speed = Math.random() * 10 + 10;
        this.moveUp();
      } else {
        this.element.className = 'horse runRight';
        this.lap++;
        this.moveRight();
      }
    }, 1000 / this.speed);
  };

  this.run = () => {
    this.element.className = 'horse runRight';
    this.moveRight();
  };

  this.arrive = () => {
    this.element.className = 'horse standRight';
    this.lap = 0;

    const tds = document.querySelectorAll('#results .result');
    tds[results.length].className = 'result horse' + this.number;

    results.push(this.number);

    if (results.length === 1) {
      if (this.number === bethorse) {
        funds += amount;
      } else {
        funds -= amount;
      }
      document.getElementById('funds').innerText = funds;
      saveFunds();
    } else if (results.length === 4) {
      document.getElementById('start').disabled = false;
    }
  };
}
