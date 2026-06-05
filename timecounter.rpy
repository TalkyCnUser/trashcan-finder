default time_counter = 0.0
default timer_running = False
default picked_names = []
default name_list = []
default new_name_input = ""
default pick_number_input = "1"
default pick_count = 0

def increment_time():
    global time_counter
    if timer_running:
        time_counter += 0.1

def pick_random_names():
    global picked_names, pick_count
    if not name_list:
        picked_names = ["(No names in list!)"]
        return
    try:
        count = int(pick_number_input.strip())
    except:
        count = 1
    if count < 1:
        count = 1
    if count > len(name_list):
        count = len(name_list)
    picked_names = []
    available = list(name_list)
    for i in range(count):
        name = renpy.random.choice(available)
        picked_names.append(name)
        available.remove(name)
    pick_count += count

def add_name():
    global new_name_input
    name = new_name_input.strip()
    if name and name not in name_list:
        name_list.append(name)
        new_name_input = ""

def remove_name(name):
    if name in name_list:
        name_list.remove(name)
    global picked_names
    if name in picked_names:
        picked_names.remove(name)

def clear_names():
    global name_list, picked_names
    name_list = []
    picked_names = []

def reset_timer():
    global time_counter, timer_running, pick_count, picked_names
    time_counter = 0.0
    timer_running = False
    pick_count = 0
    picked_names = []

def toggle_timer():
    global timer_running
    timer_running = not timer_running

screen combined():
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 700
        has vbox
        spacing 20

        # Title
        text "Time Counter & Random Name Picker" size 36 xalign 0.5

        # Timer Section
        frame:
            xfill True
            has vbox
            spacing 10
            xalign 0.5

            text "Timer" size 28 xalign 0.5
            text "[time_counter:.1f] seconds" size 48 xalign 0.5 color "#FFD700"
            hbox:
                xalign 0.5
                spacing 10
                textbutton "Start / Pause" action Function(toggle_timer)
                textbutton "Reset" action Function(reset_timer)

        # Name Picker Section
        frame:
            xfill True
            has vbox
            spacing 15
            xalign 0.5

            text "Random Name Picker" size 28 xalign 0.5

            # Pick count input
            hbox:
                xalign 0.5
                spacing 10
                text "How many to pick:" size 24
                input value VariableInputValue("pick_number_input") length 5 allow "0123456789"
                text "([len(name_list)] names available)" size 20 color "#AAAAAA"

            # Picked names display
            hbox:
                xalign 0.5
                spacing 10
                text "Picked Names:" size 24
                if picked_names:
                    text ", ".join(picked_names) size 28 color "#00FF00"
                else:
                    text "---" size 28 color "#888888"

            if pick_count > 0:
                text "Total picks: [pick_count]" size 20 xalign 0.5 color "#AAAAAA"

            textbutton "Pick Random Name(s)" action Function(pick_random_names) xalign 0.5

            # Name List Management
            hbox:
                xalign 0.5
                spacing 10
                text "Add name:" size 22
                input value VariableInputValue("new_name_input") length 25 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_- "
                textbutton "Add" action Function(add_name)
                textbutton "Clear All" action Function(clear_names)

            # Scrollable name list
            text "Your Name List ([len(name_list)])" size 22 xalign 0.5 color "#CCCCCC"
            viewport:
                xalign 0.5
                xsize 600
                ysize 150
                scrollbars "vertical"
                mousewheel True
                has vbox
                spacing 5
                for name in name_list:
                    hbox:
                        xfill True
                        text name size 22
                        textbutton "Remove" action Function(remove_name, name) xalign 1.0

        textbutton "Close" action Return() xalign 0.5

    # Background timer update
    timer 0.1 action Function(increment_time) repeat True

label start:
    $ reset_timer()
    show screen combined
    "Add your own names, set how many to pick, then start the timer and pick away!"
    $ renpy.pause()
    hide screen combined
    "Goodbye!"
    return
