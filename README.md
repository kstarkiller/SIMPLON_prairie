# Début de l'aventure SIMPLON
Ici se trouvent tous les briefs des premières semaines de ma formation SIMPLON.

## Configuration de GitHub sur WSL Ubuntu
> ### 1. Installer Git
sudo apt update
sudo apt install git

> ### 2. Configurer Git 
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"

> ### 3. Generer une clé ssh
ssh-keygen -t ed25519 -C "votre.email@example.com"

> ### 4. Ajouter la cle ssh à Github
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519


> ### 5.Tester la connection:
ssh -T git@github.com
