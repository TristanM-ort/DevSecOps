from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "🛡️ DevSecure API - Alpine Edition",
        "status": "active", 
        "version": "1.0.0",
        "environment": "Alpine Linux"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/info')
def info():
    return jsonify({
        "framework": "Flask",
        "python_version": "3.11",
        "base_image": "Alpine Linux",
        "security": "DevSecOps"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    # Désactiver le debug mode pour la production
    app.run(host='0.0.0.0', port=port, debug=False)

# Version erreur

# import os
# from flask import Flask, request
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello from Flask!"

# @app.route('/ping')
# def ping():
#     # Vulnérabilité : Commande système basée sur l'entrée utilisateur
#     host = request.args.get('host', '127.0.0.1')
#     os.system(f"ping -c 1 {host}")  # Command injection possible
#     return f"Pinging {host}"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3000)
 
