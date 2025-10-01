from flask import Flask
import threading
import main  # <-- il tuo file dove gira il bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot attivo e funzionante! 🚀"

def run_bot():
    main.run_bot()  # funzione che avvia il bot

if __name__ == "__main__":
    # avvia il bot in un thread separato
    threading.Thread(target=run_bot).start()
    # avvia il server Flask
    app.run(host="0.0.0.0", port=10000)
