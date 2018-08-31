#! /usr/bin/env sh

################################################################################
# install requirements of viman -- [vim,git,pathogen]
################################################################################

NATIVE_INSTALL='sudo pacman -Sy'

# vim
if command -v vim >/dev/null ; then
	# satisfied
	echo 'Vim is satisfied!'
else
	echo 'Installing vim ...'
	if ${NATIVE_INSTALL} vim ; then
		echo 'Install vim ok!'
	else
		echo 'Install vim fail!'
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
	if ${NATIVE_INSTALL} git ; then
		echo 'Install git ok!'
	else 
		echo 'Install git fail!'
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
fi

if printf 'execute pathogen#infect()\ncall pathogen#helptags()\n' >> \
		${HOME}/.vimrc ; then
	echo "Generate basic configuration to ${HOME}/.vimrc ok!"
else
	echo "Generate basic configuration to ${HOME}/.vimrc fail!"
fi


