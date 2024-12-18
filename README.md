# Temporaire-Mail

Système automatisé pour un service de boîte email temporaire (ou permanente) fonctionnant avec des domaines personnalisés. Le code a été produit en utilisant l'API de IONOS, mais il est également possible d'utiliser un autre fournisseur.

## Installation

Pour commencer, nous copions le GIT
   `git clone https://github.com/votre-utilisateur/temporaire-mail.git`

### Sur Linux

1. **Installer Python**  
   Pour faire fonctionner le programme, vous devez avoir [Python](https://www.python.org/downloads/) installé sur votre machine ainsi que la bibliothèque `python-dotenv`.  
   Pour installer Python, exécutez les commandes suivantes selon votre distribution :

   **Debian/Ubuntu : (Sans Python)**
   ```bash
   sudo apt update && upgrade
   sudo apt install python3
   pip install -r requirements.txt
```

  **Fedora : (Sans Python)**
   ```bash
   sudo dnf install python3 python3-pip
   pip install -r requirements.txt
   ```

  **Arch Linux : (Sans Python)**
   ```bash
      sudo pacman -S python python-pip
      pip install -r requirements.txt
```

### Sur Windows

1. **Installer Python**  
   Pour faire fonctionner le programme, vous devez avoir [Python](https://www.python.org/downloads/) installé sur votre machine ainsi que la bibliothèque `python-dotenv`.  
   Pour installer Python, exécutez les commandes suivantes :

   ```bash

2. **Installer les dépendances**  
   Installez les dépendances nécessaires avec `pip` dans l'invite de commande (CMD) ou PowerShell :

   ```bash
   pip install -r requirements.txt
```

---

Ensuite lancer le fichier :
 ```bash
scirpt.py
```
