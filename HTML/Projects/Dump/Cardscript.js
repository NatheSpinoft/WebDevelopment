document.addEventListener("DOMContentLoaded", function() {
    const container = document.querySelector('.container');
    const cards = [
        { id: 1, value: 'A' },
        { id: 2, value: 'B' },
        { id: 3, value: 'C' },
        { id: 4, value: 'D' },
        { id: 5, value: 'A' },
        { id: 6, value: 'B' },
        { id: 7, value: 'C' },
        { id: 8, value: 'D' }
    ];

    let flippedCards = [];
    let matchedCards = [];

    // Shuffle the cards
    cards.sort(() => 0.5 - Math.random());

    // Create card elements
    cards.forEach(card => {
        const cardElement = document.createElement('div');
        cardElement.classList.add('card');
        cardElement.dataset.id = card.id;
        cardElement.dataset.value = card.value;

        const front = document.createElement('div');
        front.classList.add('front');
        front.textContent = '?';

        const back = document.createElement('div');
        back.classList.add('back');
        back.textContent = card.value;

        cardElement.appendChild(front);
        cardElement.appendChild(back);

        cardElement.addEventListener('click', flipCard);
        container.appendChild(cardElement);
    });

    function flipCard() {
        if (flippedCards.length < 2 && !this.classList.contains('flipped')) {
            this.classList.add('flipped');
            flippedCards.push(this);

            if (flippedCards.length === 2) {
                setTimeout(checkForMatch, 1000);
            }
        }
    }

    function checkForMatch() {
        const [card1, card2] = flippedCards;

        if (card1.dataset.value === card2.dataset.value) {
            matchedCards.push(card1, card2);
            if (matchedCards.length === cards.length) {
                alert('You win!');
            }
        } else {
            card1.classList.remove('flipped');
            card2.classList.remove('flipped');
        }

        flippedCards = [];
    }
});