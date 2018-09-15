#! /usr/bin/env sh

################################################################################
# install requirements of viman -- [vim,git,pathogen]
################################################################################

#NATIVE_INSTALL='sudo pacman -Sy'
if [ -z "$NATIVE_INSTALL" ]; then 
	echo 'Undefined `NATIVE_INSTALL`!'
	exit 1
fi

# vim
if command -v vim >/dev/null ; then
	# satisfied
	echo 'Vim is satisfied!'
else
	echo 'Installing vim ...'
	if eval ${NATIVE_INSTALL} vim ; then
		echo 'Install vim ok!'
	else
		echo 'Install vim fail!'
		exit 1
	fi
fi

printf "########################################\
########################################\n\n"

# git
if command -v git >/dev/null ; then
	# satisfied
	echo 'Git is satisfied!'
else
	echo 'Installing git ...'
	if eval ${NATIVE_INSTALL} git ; then
		echo 'Install git ok!'
	else 
		echo 'Install git fail!'
		exit 1
	fi
fi

printf "#########################################\
#######################################\n\n"

# pathogen
if mkdir -p ~/.vim/autoload ~/.vim/bundle && \
		curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim 
	then
	echo 'Pathogen is satisfied!'
else
	echo 'Pathogne install faild!'
	exit 1
fi

if echo -e '"pathogen\nexecute pathogen#infect()\ncall pathogen#helptags()\n' >> \
		${HOME}/.vimrc ; then
	echo "Generate basic configuration to ${HOME}/.vimrc ok!"
else
	echo "Generate basic configuration to ${HOME}/.vimrc fail!"
	exit 1
fi

printf "#########################################\
#######################################\n\n"

# viman
if command -v pip3 >/dev/null ; then
	echo 'Pip3 is satisfied!'
else
	echo 'Installing pip3 ...'
	if eval ${NATIVE_INSTALL} python-pip ; then
		echo 'Install pip3 ok!'
	else 
		echo 'Install pip3 fail!'
		exit 1
	fi
fi

if pip3 install --user viman ; then 
	echo 'Viman install ok!'
	if command -v viman ; then
		echo 'Viman is satisfied!'
	else
		echo 'export PATH="$PATH:$HOME/.local/bin"' >> $HOME/.bashrc
		export PATH=$PATH:$HOME/.local/bin
	fi
else
	echo 'Viman install fail!'
fi

