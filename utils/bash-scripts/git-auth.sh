# install xclip for easy copying of ssh key using cat
sudo apt install xclip

# genereate ssh key pair
ssh-keygen -t rsa -b 4096 -C "nacht29.study@gmail.com"

# copy the public key
sudo cat  cd ~/.ssh/id_rsa.pub | xclip -selection clipboard