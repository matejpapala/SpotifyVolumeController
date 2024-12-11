# SpotifyVolumeController
Controller for the internal spotify volume slider

#### Connects to your spotify app using their web API

1. Download the script
2. Create a spotify app with your account on their website
3. Thats where you get `client-id` and your `client-secret`
4. Change your redirect URL to `http://localhost:8888`
5. Use pyInstaller or any other package to make an .exe from the script or just run it in terminal
6. the first time you run it, its gonna open a website and you will need to authorize with your account
7. Youre good to go now `page up` and `page down` controlls your spotify volume slider
8. You can create a .vbs and put it in `shell:startup` so it will automaticaly launch everytime you start your PC
