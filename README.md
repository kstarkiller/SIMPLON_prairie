# Vivez avec moi mon aventure à **`L’ECOLE IA MICROSOFT BY SIMPLON`**
Ici se trouvent tous les briefs de ma formation SIMPLON.
**`Ici se trouvent tous les briefs de ma formation SIMPLON.`**

[![Page de la formation](Page de la formation)](https://simplon.co/formation/ecole-ia-microsoft/23)

> ## Configuration de GitHub sur Linux
### 1. Installer Git
```bash
sudo apt update
sudo apt install git
```

### 2. Configurer Git 
```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
```

### 3. Generer une clé ssh
```bash
ssh-keygen -t ed25519 -C "votre.email@example.com"
```

### 4. Ajouter la cle ssh à Github
```bash
Ajouter la clé à cette adresse : https://github.com/settings/keys
Donner un nom cohérent à la clé (ex: "PC_PRO")
```

### 5.Tester la connection:
```bash
ssh -T git@github.com
```

> ## Cloner un repo Github sur sa machine
```bash
git clone "lien SSH du repo"
(ex: git clone git@github.com:kstarkiller/SIMPLON_prairie.git)
```

> ## Push des changements
### 1. Tracker les changements
```bash
git add "nom du fichier/dossier"
```
ou
```bash
git add . (pour tracker l'ensemble du dossier courant)
```

### 2. Créer le commit
```bash
git commit -m "Message informatif du commit"
```

### 3. Push le commit
```bash
git push "nom du repository" "nom de la branche"
(ex: git push origin main)
```
