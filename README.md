# rosAuto
- Executer ca pour que git ne redemande pas à chaque fois le user/password : `git config --global credential.helper store`

## Installation du git dans catkin_ws
- Supprimer le dossier `src` de `catkin_ws`
- Aller dans `catkin_ws` 
- Cloner ce repo avec `git clone https://github.com/ECE-BiDuo-OA/rosAuto`
- Renommer ce repo en `src`

## Exam Labs
### TP 4 : Intro
- Aller dans le dossier launch de `tp4_my_turtle_control`
- `roslaunch 1univers.launch` Dans 1 seul univers : Tortue tourne en rond via commandeur + controle clavier
- `roslaunch 2univers.launch` Univers 1 : tourne en rond via commandeur, univers 2 : controle clavier

### TP 5 : drone_control
- Aller dans le dossier launch de `tp5_drone_control`
- `roslaunch drone_control.launch` va se stabiliser en x=-2 y=5 z=4
- `roslaunch mav_rpyt.launch` marche po

### TP 6 : Turtle_follower
- Aller dans le dossier launch de `tp6_Turtle_follower`
- `roslaunch aleat.launch` tortue vitesse et direction aleatoire
- `roslaunch aleatParam.launch` tortue vitesse et direction aleatoire avec parametre passé dans le .launch
- `roslaunch follow.launch` tortue va vers un point, actualisé périodiquement par un script (LEQUEL ?) (A CORRIGER : PREMIER ENVOI QUI NE MARCHE PAS)
- `roslaunch follow_husky.launch` description
- `roslaunch follow_husky_path.launch` description
