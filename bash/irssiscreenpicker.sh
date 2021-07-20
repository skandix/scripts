#!/usr/bin/env sh
show_menu(){
    NORMAL=`echo "\033[m"`
    MENU=`echo "\033[36m"` #Blue
    NUMBER=`echo "\033[33m"` #yellow
    FGRED=`echo "\033[41m"`
    RED_TEXT=`echo "\033[31m"`
    ENTER_LINE=`echo "\033[33m"`
    README=`echo "\033[069m"`
    echo -e "${MENU}*********************************************${NORMAL}"
    echo -e "${MENU}**${NUMBER} 1)${MENU} EFnet ${NORMAL}"
    echo -e "${MENU}**${NUMBER} 2)${MENU} FreeNode ${NORMAL}"
    echo -e "${MENU}**${NUMBER} 3)${MENU} Hexagons ${NORMAL}"
    echo -e "${MENU}**${NUMBER} 4)${MENU} Quakenet ${NORMAL}"
    echo -e "${MENU}**${NUMBER} 5)${MENU} Blucoders ${NORMAL}"
    echo -e "${MENU}**${NUMBER} 6)${MENU} illumine ${NORMAL}"
    echo -e "${MENU}**${NUMBER} 7)${MENU} Hak5         ${NORMAL}"
    echo -e "${MENU}*********************************************${NORMAL}"
    echo -e "${ENTER_LINE}Please enter a menu option and enter or ${RED_TEXT}ent                                                                                                                                                                                               er to exit. ${NORMAL}"
    echo -e "${README} Combination to Deattach screens <ctrl> + a + d "
    read opt
}
function option_picked() {
    COLOR='\033[01;31m' # bold red
    RESET='\033[00;00m' # normal white
    MESSAGE=${@:-"${RESET}Error: No message passed"}
    echo -e "${COLOR}${MESSAGE}${RESET}"
}

clear
show_menu
while [ opt != '' ]
    do
    if [[ $opt = "" ]]; then
            exit;
    else
        case $opt in

         1) clear;
        option_picked "Option 1 Picked";
       screen -Rds EFnet irssi;
        menu;
        ;;

        2) clear;
            option_picked "Option 2 Picked";
            screen -Rds IRCnet irssi;
            menu;
            ;;

        3) clear;
            option_picked "Option 3 Picked";
            screen -Rds Hexanet irssi;
            show_menu;
            ;;

        4) clear;
            option_picked "Option 4 Picked";
            screen -Rds Quakenet irssi;
            show_menu;
            ;;


        5) clear;
            option_picked "Option 4 Picked";
            screen -Rds BLUcoders irssi;
            show_menu;
            ;;

         6) clear;
            option_picked "Option 4 Picked";
            screen -Rds Illumine irssi;
            show_menu;
            ;;

        7) clear;
        option_picked "option 7 Picked";
        screen -Rds Hak5 irssi
        show_menu;
        ;;

        x)exit;
        ;;

        \n)exit;
        ;;

        *)clear;
        option_picked "Pick an option from the menu";
        show_menu;
        ;;
    esac
fi
done
