#!/data/data/com.termux/files/usr/bin/bash

clear
echo""
echo -e '\e[1;92m ____ ____ _    ____ ____ ____\e[1;91m____ _  _ ___  ____'
echo -e '\e[1;92m| __\| . \||_/\| . \|_ _\|   |\e[1;91m| __\||_|\|  \ |_ _\'
echo -e '\e[1;92m| \__|  <_| __/| __/  || | . |\e[1;91m| \__| _ || . \  ||'
echo -e '\e[1;92m|___/|/\_/|/   |/     |/ |___/\e[1;91m|___/|/ |/|/\_/  |/\e[0m v.global'
echo""
printf "\e[1;90;102m >> github.com/\e[1;97;101mabhackerofficial/\e[1;90;102mOpen-crytochat << \e[0m\n"
sleep 2
echo""

if [[ -e ngrok ]]; then
echo ""
else
command -v unzip > /dev/null 2>&1 || { echo -e >&2 "\033[1;91mI require nano but it's not installed, Now Installing.\e[0m"; pkg install unzip -y; clear; connection="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
if [[ "$connection" != 0 ]]
then clear
echo -e "\033[1;91m[\033[1;92m-\033[1;91m] No Internet\033[1;92m connection!"
   exit
fi ; }
command -v php > /dev/null 2>&1 || { echo -e >&2 "\033[1;91mI require nano but it's not installed, Now Installing.\e[0m"; pkg install php -y; clear; connection="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
if [[ "$connection" != 0 ]]
then clear
echo -e "\033[1;91m[\033[1;92m-\033[1;91m] No Internet\033[1;92m connection!"
   exit
fi ; }
command -v wget > /dev/null 2>&1 || { echo -e >&2 "\033[1;91mI require nano but it's not installed, Now Installing.\e[0m"; pkg install wget -y; clear; connection="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
if [[ "$connection" != 0 ]]
then clear
echo -e "\033[1;91m[\033[1;92m-\033[1;91m] No Internet\033[1;92m connection!"
   exit
fi ;  bash cryptochat.sh; }
printf "\e[1;92m[\e[0m+\e[1;92m] Downloading Ngrok...\n"
arch=$(uname -a | grep -o 'arm' | head -n1)
arch2=$(uname -a | grep -o 'Android' | head -n1)
arch3=$(uname -a | grep -o 'amd64' | head -n1)
if [[ $arch == *'arm'* ]] || [[ $arch2 == *'Android'* ]] ; then
wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1

if [[ -e ngrok-stable-linux-arm.zip ]]; then
unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-stable-linux-arm.zip
else
printf "\e[1;93m[!] Download error... Termux, run:\e[0m\e[1;77m pkg install wget\e[0m\n"
exit 1
fi

elif [[ $arch3 == *'amd64'* ]] ; then

wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip > /dev/null 2>&1

if [[ -e ngrok-stable-linux-amd64.zip ]]; then
unzip ngrok-stable-linux-amd64.zip > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-stable-linux-amd64.zip
else
printf "\e[1;93m[!] Download error... \e[0m\n"
exit 1
fi
else
wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > /dev/null 2>&1 
if [[ -e ngrok-stable-linux-386.zip ]]; then
unzip ngrok-stable-linux-386.zip > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-stable-linux-386.zip
else
printf "\e[1;93m[!] Download error... \e[0m\n"
exit 1
fi
fi
fi

if [[ $checkngrok == *'ngrok'* ]]; then
pkill -f -2 ngrok > /dev/null 2>&1
killall -2 ngrok > /dev/null 2>&1
fi

printf "\e[1;92m[\e[0m\e[1;77m+\e[1;92m] Starting ngrok server \e[0m\e[1;97;101m(http 8080)\e[0m\e[1m...\n"
./ngrok http 8080 > /dev/null 2>&1 &
sleep 5

link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")

if [[ -z $link ]];then
printf "\e[1;91m[!] Ngrok error, debug:\e[0m\e[1;77m ./ngrok http 8080\e[0m\n"
exit 1
fi
printf "\e[1;92m[\e[0m\e[1m+\e[1;92m] Share \e[0m\e[1;97;101mHTTPS\e[0m\e[1;92m link:\e[0m\e[1;77m %s\e[0m\n" $link
echo
printf "\e[1;92m[\e[0m!\e[1;92m] \e[1;90;102mCTRL+C\e[0m\e[1;92m TO EXIT\e[0m"
cd public
php -S localhost:8080 > /dev/null 2>&1
