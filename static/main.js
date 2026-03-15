async function selectOption(el, num) {
  // Highlight selected card
  document.querySelectorAll('.option').forEach(o => o.classList.remove('selected'));
  el.classList.add('selected');

  // Send selection to Flask backend
  try {
    const response = await fetch('/select', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ option: num })
    });
    const data = await response.json();
    console.log('Server confirmed:', data);
  } catch (err) {
    console.error('Failed to send selection:', err);
  }
}