#!/bin/bash

#random rfc downloader.

#https://tools.ietf.org/rfc/rfc3.txt

#Ask the user for a number between 1 and 7860, if nothing specified download a random rfc
		#if he choose a number display something like: "HAVE FUN READING RFC NO $" else "RANDOM DUDE"
#On Invocation check if wget is installed, if not check if curl is installed, if not exit.
#Let the user specify a dir, if he doesnt care take . 
#download random rfc and display it with less and exit




rfc_downloader()
{
	echo""
  	echo""
  	echo "DOWNLOADING NUMBER $input"

	RFC=$(wget -q https://tools.ietf.org/rfc/rfc$input.txt )

  	echo""
  	echo "---------------------------------------------------"
  	echo "HAVE FUN READING RFC NO $input"

  	clear
  	less rfc$input.txt
  	rm rfc$input.txt	
  	exit
}

#check for curl and wget
if ! type "wget" > /dev/null && ! type "curl" > /dev/null; 
	then
	echo "can't find wget or curl"
	exit		
fi

echo "-----------------------"
echo "REQUEST FOR (THE) COOL."
echo "-----------------------"

echo "You have a special RFC No. in mind? Type in the number between 1 and 7860"
echo "Or are you feeling lucky punk? Hit [ENTER] for a random RFC."
echo ""
echo ""
read input

if  [$input eq ""]; then

  	echo "LET ME CHOOSE FOR YOU!"
  	input=$(shuf -i 1-7860 -n 1)
  	rfc_downloader $input
  	exit
  else
  	rfc_downloader $input
  	exit
fi


