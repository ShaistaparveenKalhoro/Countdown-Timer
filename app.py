import time
import os

def clear_screen():
    # Clear screen command for Windows
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(t):
    while t:
        clear_screen()
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Countdown Timer")
        print("=" * 20)
        print(timer)
        print("=" * 20)
        time.sleep(1)
        t -= 1
    
    clear_screen()
    print("Time's up!")

def main():
    try:
        # Get user input for countdown duration
        t = input("Enter the time in seconds: ")
        t = int(t)
        
        if t <= 0:
            print("Please enter a positive number of seconds.")
            return
            
        countdown(t)
        
    except ValueError:
        print("Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nCountdown cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
