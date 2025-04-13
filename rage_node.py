import time
import os

frames = [
    r"""
     |\      ________
     ||     | ODIN:  |
     ||     | RAGE / |
     ||     | BUILD  |
    [🔥]    |________|
   /|||\     /\
  /_||_\    /__\    
  \____/   //  \\   
    """,
    r"""
     |\      ________
     ||     | ODIN:  |
     ||     | RAGE / |
     ||     | BUILD  |
    [⚡]    |________|
   /|||\     /\
  /_||_\    /__\    
  \____/   //  \\   
    """,
    r"""
     |\      ________
     ||     | ODIN:  |
     ||     | RAGE / |
     ||     | BUILD  |
    [💥]    |________|
   /|||\     /\
  /_||_\    /__\    
  \____/   //  \\   
    """
]

quotes = [
    "Yes I know my enemies...",
    "They’re the teachers who taught me to fight me.",
    "Compromise. Conformity. Assimilation.",
    "Submission. Ignorance. Hypocrisy.",
    "Brutality. The elites.",
    "All of which are American dreams.",
    "The needle, I'll thread it, radically poetic",
    "Burn, burn, you're gonna burn",
    "'Cause what you reap is what you sow",
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    for frame in frames:
        for quote in quotes:
            clear()
            print(frame)
            print(f"\n🗣️ {quote}")
            time.sleep(0.8)
