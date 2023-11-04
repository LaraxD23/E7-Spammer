from functions.main import main

if __name__ == "__main__":
    print("\33[1m \33[92m")
    print("""
    ___________   _____                                          
   / ____/__  /  / ___/____  ____ _____ ___  ____ ___  ___  _____
  / __/    / /   \__ \/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/
 / /___   / /   ___/ / /_/ / /_/ / / / / / / / / / / /  __/ /    
/_____/  /_/   /____/ .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/     
                   /_/       

    """)
    
    VICTIM_EMAIL = input ("[+] ENTER VICTIM EMAIL >> ")
    print("[+] BOMBING ...")
    main(VICTIM_EMAIL)
    print("[✓] SENT "); print()
