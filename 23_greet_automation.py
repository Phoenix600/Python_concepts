#import your modules here 
from datetime import datetime 
import colorama 
from colorama import Fore

nowTime = datetime.now()
Current_Time = nowTime.strftime("%H : %M : %S \n")
str_user = "Pranay"

print( Fore.RED + f'''
          (      )
              ~(^^^^)~
               ) @@ \~_          |/                                         It's a great day to start hitting more goals
              /     | \        \~ /                                             
             ( 0  0  ) \        | |       HEY {str_user}
              ---___/~  \       | |           HOW YOU                       [CURRENT USER]      : {str_user}
               /'__/ |   ~-_____/ |                DOIN?                    [TIME]              : {Current_Time}
o          _   ~----~      ___---~/                                         
  O       //     |         |
         ((~\  _|         -|                Oops! I mean MOOOOOOO
   o  O //-_ \/ |        ~  |
        ^   \_ /         ~  |
               |          ~ |
               |     /     ~ |
               |     (       |
                \     \      /\               
               / -_____-\   \ ~~-*
               |  /       \  \       .==.
               / /         / /       |  |
             /~  |      //~  |       |__|
             ~~~~        ~~~~
        ''')

