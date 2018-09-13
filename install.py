#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os

print(" ___  ________   ________  _________  ________  ___       ___       ________  _________  ___  ________  ________  ")
print("|\  \|\   ___  \|\   ____\|\___   ___\\   __  \|\  \     |\  \     |\   __  \|\___   ___\\  \|\   __  \|\   ___  \ ")
print("\ \  \ \  \\ \  \ \  \___|\|___ \  \_\ \  \|\  \ \  \    \ \  \    \ \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \\ \  \ ")
print(" \ \  \ \  \\ \  \ \_____  \   \ \  \ \ \   __  \ \  \    \ \  \    \ \   __  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \ ")
print("  \ \  \ \  \\ \  \|____|\  \   \ \  \ \ \  \ \  \ \  \____\ \  \____\ \  \ \  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \ ")
print("   \ \__\ \__\\ \__\____\_\  \   \ \__\ \ \__\ \__\ \_______\ \_______\ \__\ \__\   \ \__\ \ \__\ \_______\ \__\\ \__\ ")
print("    \|__|\|__| \|__|\_________\   \|__|  \|__|\|__|\|_______|\|_______|\|__|\|__|    \|__|  \|__|\|_______|\|__| \|__| ")
print("                   \|_________|                                                                                        ")

print('Marche seulement sous Debian/Apt-Get\n')
print('Faire tourner avec Python2.7')
print('Faire une mise a jour ?\n')
update = raw_input('Oui | Non\n').lower()
if update == "oui":
	os.system('sudo apt-get dist-upgrade')
	print('/////////////////////')
	os.system('sudo apt-get update')
	print('/////////////////////')
	os.system('sudo apt-get upgrade')
	print('/////////////////////')

print('Verifier l\'installation de zsh ?\n')
zsh = raw_input('Oui | Non\n').lower()
if zsh == "oui":
	os.system('zsh')
	
	print('Est-il installer ?\n')
	zsh_update = raw_input('Oui | Non\n').lower()
	if zsh_update == "non":
		os.system('sudo apt-get install zsh')

print('Verifier l\'installation de curl ?\n')
zsh = raw_input('Oui | Non\n').lower()
if zsh == "oui":
	os.system('curl')
	
	print('Est-il installer ?\n')
	zsh_update = raw_input('Oui | Non\n').lower()
	if zsh_update == "non":
		os.system('sudo apt-get install curl')

print('Install Nvidia, GitHub, Steam, ohmyzsh, PPSSPP, pcsx2, ePSXe, Chrome, Obs, Discord, Kdenlive, Audacity, PlayOnLinux, PcsxR\n')
all_install = raw_input("Tous installer 1 ou 2 pour du cas par cas\n").lower()

if all_install == "2":

	all_software = raw_input('Que voulez vous installer ?:\n').lower()

	# Install GitHub
	if all_software == "github":
		os.system("sudo apt-get install git")

	# Install Nvidia
	if all_software == "nvidia":
		os.system("sudo add-apt-repository ppa:graphics-drivers && sudo apt-get update")
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system("ubuntu-drivers devices")
		nvidia_driver = raw_input("Rentrez le numeros")
		os.system("sudo apt-get install nvidia-" + nvidia_driver)

	# Install Oh My Zsh
	if all_software == "ohmyzsh":
		os.system('sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')

	# Install Steam
	if all_software == "steam":
		os.system("sudo add-apt-repository multiverse")
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system("sudo apt update && sudo apt install steam")

	# Install PPSSPP
	if all_software == "ppsspp":
		os.system("sudo add-apt-repository ppa:ppsspp/stable")
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system("sudo apt-get update && sudo apt-get install ppsspp-qt")

	# Install Chrome
	if all_software == "chrome":
		os.system("sudo sh -c 'echo \"deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main\" > /etc/apt/sources.list.d/google-chrome.list'")
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system('wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -')
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system('sudo apt-get update && sudo apt-get install google-chrome-stable')

	# Install Obs
	if all_software == "obs":
		os.system('sudo add-apt-repository ppa:obsproject/obs-studio')
		print('\n')
		print('Plugin AlertTwitch : https://github.com/bazukas/obs-linuxbrowser/releases')
		print('/////////////////////')
		print('\n')
		os.system('sudo apt-get update && sudo apt-get install obs-studio')

	# Install Discord
	if all_software == "discord":
		os.system('wget -O discord.deb "https://discordapp.com/api/download?platform=linux&format=deb"')
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system('sudo dpkg -i discord.deb')

	# Install Kdenlive 
	if all_software == "kdenlive":
		os.system('sudo apt-get install kdenlive')

	# Intall Audacity
	if all_software == "audacity":
		os.system('sudo add-apt-repository ppa:ubuntuhandbook1/audacity')
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system('sudo apt-get update')
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system('sudo apt-get install audacity')

	# Install Pcsx2
	if all_software == "pcsx2":
		os.system("sudo apt-get install pcsx2")
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system("curl -k https://download.loveroms.com/extras/files/bios/ps2_bios.zip -o ~/.pcsx2/bios/ps2_bios.zip")
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system("unzip ~/.pcsx2/bios/ps2_bios.zip")
		print('\n')
		print('/////////////////////')
		print('\n')
		print('supprimer le dossier ps2_bios mais avant mettez tous les fichiers a l intérieur de /bios')

	# Install ePSXe
	if all_software == "epsxe":
		way = raw_input('Ou mettre le projet ePSXe, exemple : /home/user/\n')
		os.system("curl -k http://www.epsxe.com/files/ePSXe205linux_x64.zip -o "+way+"ePSXe205linux_x64.zip")
		print('\n')
		os.system("unzip"+ way+"ePSXe205linux_x64.zip -o"+ way)
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system("curl -k http://dllyes.com/wp-content/uploads/2015/09/SCPH7502.zip -o ~/.epsxe/bios")
		os.system("unzip ~/.epsxe/bios/SCPH7502.zip && sudo rm -rf SCPH7502.zip")

	# Install PlayOnLinux
	if all_software == "playonlinux":
		os.system('sudo add-apt-repository http://deb.playonlinux.com/')
		os.system('wget -q "http://deb.playonlinux.com/public.gpg" -O- | sudo apt-key add -')
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system('sudo apt-get update')
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system('sudo apt -V install playonlinux')

	# Install PCSX 
	if all_software == "pcsxr":
		os.system('sudo apt-get update')
		print('\n')
		print('/////////////////////')
		print('\n')
		os.system('apt-get install pcsxr')

if all_install == "1":
	print('INSTALLATION DE REPOSITORY :')
	print('\n')
	os.system("sudo add-apt-repository ppa:graphics-drivers && sudo apt-get update")
	print('\n')
	os.system("sudo add-apt-repository multiverse")
	print('\n')
	os.system('sudo add-apt-repository ppa:obsproject/obs-studio')
	print('\n')
	os.system('sudo add-apt-repository ppa:ubuntuhandbook1/audacity')
	print('\n')
	os.system('sudo add-apt-repository http://deb.playonlinux.com/')
	print('\n')
	os.system('wget -q "http://deb.playonlinux.com/public.gpg" -O- | sudo apt-key add -')
	print('\n')
	os.system("sudo add-apt-repository ppa:ppsspp/stable")
	print('\n')
	os.system('wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -')
	print('\n')
	os.system("sudo sh -c 'echo \"deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main\" > /etc/apt/sources.list.d/google-chrome.list'")
	print('\n')
	os.system('sudo add-apt-repository ppa:peterlevi/ppa')
	print('\n')
	os.system('sudo apt-get update')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE GIT :')
	print('\n')
	os.system("sudo apt-get install -f git")
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE NVIDIA :')
	print('\n')
	os.system("ubuntu-drivers devices")
	nvidia_driver = raw_input("Rentrez le numeros")
	os.system("sudo apt-get install nvidia-" + nvidia_driver)
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE OH MY ZSH :')
	print('\n')
	os.system('sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE STEAM :')
	print('\n')
	os.system("sudo apt-get install -f steam")
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE GOOGLE CHROME :')
	print('\n')
	os.system('sudo apt-get install -f google-chrome-stable')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE OBS :')
	print('Plugin AlertTwitch : https://github.com/bazukas/obs-linuxbrowser/releases')
	print('\n')
	os.system('sudo apt-get install -f obs-studio')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE DISCORD :')
	print('\n')
	os.system('wget -O discord.deb "https://discordapp.com/api/download?platform=linux&format=deb"')
	print('\n')
	print('/////////////////////')
	print('\n')
	os.system('sudo dpkg -i discord.deb')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE KDENLIVE :')
	print('\n')
	os.system('sudo apt-get install -f kdenlive')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE AUDACITY :')
	print('\n')
	os.system('sudo apt-get install -f audacity')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE PCSX2 :')
	print('\n')
	os.system("sudo apt-get install -f pcsx2")
	print('\n')
	print('/////////////////////')
	print('\n')
	os.system("curl -k https://download.loveroms.com/extras/files/bios/ps2_bios.zip -o ~/.pcsx2/bios/ps2_bios.zip")
	print('\n')
	print('/////////////////////')
	print('\n')
	os.system("unzip ~/.pcsx2/bios/ps2_bios.zip")
	print('\n')
	print('supprimer le dossier ps2_bios mais avant mettez tous les fichiers a l intérieur de /bios')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE EPSXE :')
	print('\n')
	way = raw_input('Ou mettre le projet ePSXe, exemple : /home/user/\n')
	os.system("curl -k http://www.epsxe.com/files/ePSXe205linux_x64.zip -o "+way+"ePSXe205linux_x64.zip")
	print('\n')
	os.system("unzip"+ way+"ePSXe205linux_x64.zip -o"+ way)
	print('\n')
	print('/////////////////////')
	print('\n')
	os.system("curl -k http://dllyes.com/wp-content/uploads/2015/09/SCPH7502.zip -o ~/.epsxe/bios")
	os.system("unzip ~/.epsxe/bios/SCPH7502.zip && sudo rm -rf SCPH7502.zip")
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE PPSSPP')
	print('\n')
	os.system('sudo apt-get install -f ppsspp-qt')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE PLAYONLINUX :')
	print('\n')
	os.system('sudo apt -V install -f playonlinux')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION DE PCSXR :')
	os.system('apt-get install -f pcsxr')
	print('\n')
	print('/////////////////////')
	print('\n')

	print('INSTALLATION OUTILS')
	os.system('sudo apt install gnome-tweak-tool')
	print('\n')
	print('/////////////////////')
	print('\n')
	os.system('sudo apt-get install variety')
	print('\n')
	print('/////////////////////')
	print('\n')

print('\n')
print('/////////////////////')
print('\n')
print('L\'installation est Terminée')
