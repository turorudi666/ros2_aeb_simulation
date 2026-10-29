# ROS2 alapú automatikus vészfékező rendszer szimuláció

A projekt célja egy ROS2 alapú automatikus vészfékező rendszer (AEB – Automatic Emergency Braking) szimulációjának megvalósítása.

A rendszer egy jármű és egy előtte található akadály mozgását szimulálja, majd a jármű sebessége, az akadály távolsága és relatív mozgása alapján meghatározza az ütközés kockázatát. A rendszer többek között az ütközésig hátralévő időt (Time To Collision – TTC) számítja ki, és szükség esetén figyelmeztetést vagy fékezési parancsot generál.

A projekt Python nyelven, ROS2 Humble környezetben készül.

## Tervezett funkciók

- járműállapot szimuláció
- akadály távolságának és mozgásának szimulációja
- Time To Collision (TTC) számítása
- ütközési kockázat meghatározása
- figyelmeztetési és vészfékezési állapotok
- ROS2 topic alapú kommunikáció
- az aktuális rendszerállapot vizualizációja
- launch fájl a teljes rendszer indításához

## Környezet

- ROS2 Humble
- Python 3
- Ubuntu 22.04
- WSL2

## Build

```bash
cd ~/ros2_ws
colcon build --packages-select ros2_aeb_simulation --symlink-install
```

## Környezet betöltése

```bash
source ~/ros2_ws/install/setup.bash
```

## Futtatás

A futtatáshoz szükséges parancsok a fejlesztés során kerülnek hozzáadásra.