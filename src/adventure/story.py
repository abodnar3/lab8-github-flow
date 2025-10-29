from adventure.utils import read_events_from_file
from rich import print
import random

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[italic red]You stand still, unsure what to do. The forest swallows you.[/italic red]"

def left_path(event):
    return "[bold blue]You walk left.[/bold blue] [italic blue]" + event + "[/italic blue]"

def right_path(event):
    return "[bold purple]You walk right.[/bold purple] [italic purple]" + event + "[/italic purple]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[italic yellow]You wake up in a dark forest. You can go [italic blue]left[/italic blue] "
    "or [italic purple]right[/italic purple].[/italic yellow]")
    while True:
        print("[bold yellow]Which direction do you choose?[/bold yellow] ([bold blue]left[/bold blue]/"
        "[bold purple]right[/bold purple]/[bold red]exit[/bold red]): ", end="")
        choice = input().strip().lower()
        if choice == 'exit':
            print("[bold red]Goodbye![/bold red]")
            break
        
        print(step(choice, events))
