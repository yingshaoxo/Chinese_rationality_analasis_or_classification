clear() {
    ls
}

pull() {
	git fetch --all
	git reset --hard origin/master
}

push() {
	clear
	git config --global user.email "yingshaoxo@gmail.com"
	git config --global user.name "yingshaoxo"
	git add .
	git commit -m "update"
	git push origin
}


if [ "$1" == "clear" ]; then
    clear

elif [ "$1" == "pull" ]; then
    pull

elif [ "$1" == "push" ]; then
    push

elif [ "$1" == "" ]; then
    echo "
pull
push
"

fi
