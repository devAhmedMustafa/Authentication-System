const input = document.querySelector('.chat-input input');
const button = document.querySelector('.chat-input button');
const messages = document.querySelector('.chat-messages ul');

button.addEventListener('click', function() {
  const text = input.value.trim();

  if (text !== '') {
    const li = document.createElement('li');
    li.classList.add('message', 'sent');
    li.innerHTML = '<span class="message-text">' + text + '</span>';
    messages.appendChild(li);

    input.value = '';
  }
});

input.addEventListener('keyup', function(event) {
  if (event.key === 'Enter') {
    button.click();
  }
});
