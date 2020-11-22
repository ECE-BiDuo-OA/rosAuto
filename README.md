
# rosAuto
- Executer ca pour que git ne redemande pas à chaque fois le user/password : `git config --global credential.helper store`

## Installation du git dans catkin_ws
- Supprimer le dossier `src` de `catkin_ws`
- Aller dans `catkin_ws` 
- Cloner ce repo avec `git clone https://github.com/ECE-BiDuo-OA/rosAuto`
- Renommer ce repo en `src`


## Exam Labs
### TP 4 : Intro
1) Univers 1 : Tortue tourne en rond via commandeur + control clavier
#### 1ere façon
- Aller dans le dossier launch de `tp4_my_turtle_control`
- `roslaunch 1univers.launch` 
#### 2eme façon
- Aller dans le dossier launch de `catkin_ws`
- Lancer le terminal et faire un `source devel/setup.bash`
- Puis faire `roslaunch tp4_my_turtle_control 1univers.launch` 

2) Univers 2 : Control clavier /!\ LE PROGRAMME OUVRE L'UNIVERS 1 AUSSI
#### 1ere façon
- Aller dans le dossier launch de `tp4_my_turtle_control`
- `roslaunch 2univers.launch` 
#### 2eme façon
- Aller dans le dossier launch de `catkin_ws`
- Lancer le terminal et faire un `source devel/setup.bash`
- Puis faire `roslaunch tp4_my_turtle_control 2univers.launch` 



## TP 5 : drone_control
1) Drone control : Faire en sore que le robot se dirige vers les coordonnées indiqué dans le script `drone_control.py`
#### 1ere façon
- Aller dans le dossier launch de `tp5_drone_control`
- `roslaunch drone_control.launch` va se stabiliser en x=-2 y=5 z=4
#### 2eme façon
- Aller dans le dossier launch de `catkin_ws`
- Lancer le terminal et faire un `source devel/setup.bash`
- Puis faire `roslaunch tp5_drone_control drone_control.launch` 

2) à VERIFIER SI ça SERT VRAIMENT à QQ CHOSE
- `roslaunch mav_rpyt.launch` marche po




## TP 6 : Turtle_follower
1) Tortue Vitesse et direction aléatoire (fichier talker.py)
#### 1ere façon
- Aller dans le dossier launch de `tp6_Turtle_follower`
- Puis faire`roslaunch aleat.launch`
#### 2eme façon
- Aller dans le dossier launch de `catkin_ws`
- Lancer le terminal et faire un `source devel/setup.bash`
- Puis faire `roslaunch tp6_TurtleFollower aleat.launch` 

2) Tortue Vitesse et direction aléatoire avec parametre passé dans le .launch 
#### 1ere façon
- Aller dans le dossier launch de `tp6_Turtle_follower`
- `roslaunch aleatParam.launch` 
#### 2eme façon
- Aller dans le dossier launch de `catkin_ws`
- Lancer le terminal et faire un `source devel/setup.bash`
- Puis faire `roslaunch tp6_TurtleFollower aleatParam.launch` 

3) Tortue va vers un points actualisé périodiquement par un script(Follow.py) 
(A CORRIGER : PREMIER ENVOI QUI NE MARCHE PAS)
#### 1ere façon
- Aller dans le dossier launch de `tp6_Turtle_follower` 
- `roslaunch follow.launch` 
#### 2eme façon
- Aller dans le dossier launch de `catkin_ws`
- Lancer le terminal et faire un `source devel/setup.bash`
- Puis faire `roslaunch tp6_TurtleFollower follow.launch` 

4) Husky va vers un point, actualisé periodiquement par un script (commander husky) (A CORRIGER ? : PREMIER ENVOI QUI NE MARCHE PAS)
#### 1ere façon
- Aller dans le dossier launch de `tp6_Turtle_follower` 
- `roslaunch follow_husky.launch`  
#### 2eme façon
- Aller dans le dossier launch de `catkin_ws`
- Lancer le terminal et faire un `source devel/setup.bash`
- Puis faire `roslaunch tp6_TurtleFollower follow_husky.launch` 

5)Husky suit un chemin de points, puis s'arrete, actualisé périodiquement par un script (commander_husky_path.py)  (A CORRIGER ? : PREMIER ENVOI QUI NE MARCHE PAS)
#### 1ere façon
- Aller dans le dossier launch de `tp6_Turtle_follower` 
- `roslaunch follow_husky_path.launch` 
#### 2eme façon
- Aller dans le dossier launch de `catkin_ws`
- Lancer le terminal et faire un `source devel/setup.bash`
- Puis faire `roslaunch tp6_TurtleFollower follow_husky_path.launch` 



## TP 7 : loc_multicapteurs
1) Filtre de Kalman pour l'estimation angulaire calcul la version lissée du roll
#### 1ere façon
- Aller dans le dossier launch de `attitude_estimation`
- `roslaunch KF_roll_imu_data_roll_only.launch` 
#### 2eme façon
- Aller dans le dossier launch de `catkin_ws`
- Lancer le terminal et faire un `source devel/setup.bash`
- Puis faire `roslaunch attitude_estimation KF_roll_imu_data_roll_only.launch` 

2) Robot mobile husky GPS + ODOM
#### 1ere façon
- Aller dans le dossier launch de `tp6_Turtle_follower` 
- `roslaunch localisation_husky.launch` 
#### 2eme façon
- Aller dans le dossier launch de `catkin_ws`
- Lancer le terminal et faire un `source devel/setup.bash`
- Puis faire `roslaunch tp6_TurtleFollower localisation_husky.launch` 
