async function translateText() {
    const text = document.getElementById('inputText').value;
    const target_lang = document.getElementById('languageSelect').value;

    const response = await fetch(config.API_KEY + '/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, target_lang })
    });

    const data = await response.json();
    document.getElementById('outputText').innerText - data.translated_text || 'Translation Failed';


}