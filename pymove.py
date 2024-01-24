from pyautogui import *
import keyboard as key
import webbrowser as web
import os

name = prompt('Welcome to my App for move and automate your pc!\nName of the new project!',title='App')
file = open(f'{name}.py','w')
file.write('import pyautogui as p\nimport time\np.hotkey("win","d")\n')


def main():
    x = 1
    y = 0
    z = 0
    cm = 0
    sk = 0
    ttm = 0

    if ttm == 0:
        time = 1
    ttm += 1
    if sk == 0:
        default_key = 'ctrl+k'
    sk += 1
    if cm == 0:
        click_mouse = False
    cm += 1


    while True:

        if x == 1:
            hotkey('win','d')
        x += 1
        key_choice = confirm('Select Function: ','FUNCTION',buttons=['Move','Time','Mouse','Write','Developer','Settings','Exit'])


        #! SETTINGS
        #? MOUSE

        if key_choice == 'Settings':
            settings_config = confirm('Select Setting: ','SETTINGS',buttons=['Mouse','General','Back'])
            if settings_config == 'Mouse':
                click_after_move = confirm(f'Click after moving the mouse?\nNow is {click_mouse}','SETTINGS',buttons=['True','False'])
                if click_after_move == 'True':
                    click_mouse = True
                else:
                    click_mouse = False
            
            if settings_config == 'Back':
                main()

            #? GENERAL
            if settings_config == 'General':
                keyboard_choice = confirm(f'Select: ',title='Settings keyboard',buttons=['Time to move','Change key','Back'])
                if keyboard_choice == 'Change key':
                    default_key = prompt(f'Enter New shortcut(use ctrl):\nNow is {default_key}','SETTINGS')

                if keyboard_choice == 'Time to move':
                    time = prompt(f'Enter Time:\nNow is {time}','SETTINGS')
                    try:
                        time = int(time)
                    except:
                        main()


                if keyboard_choice == 'Back':
                    main()
        #! KEYBOARD FUNCTION
        if key_choice == 'Move':
            key_choice_set = confirm('Select: ','FUNCTION',buttons=['Move','Drag To','Back'])
            if key_choice_set == 'Move':            
                if y == 0:
                    alert(f'Positioned and click "{default_key}"',title='Message key')
                key.wait(default_key)
                pos1 = position()
                pos1 = str(pos1)
                pos1 = pos1[6:-1]
                pos1 = pos1.replace('x=','');pos1 = pos1.replace('y=','')
                file.write(f'pos1 = {pos1}\np.moveTo(pos1,duration={time})\n')
                if click_mouse:
                    file.write('p.click()\n')
                y += 1
            #! TO DRAG FUNCTION
            if key_choice_set == 'Drag To':
                if z == 0:
                    alert(f'Positioned and click "{default_key}"',title='Message key')
                key.wait(default_key)
                pos = position()
                pos = str(pos)
                pos = pos[6:-1]
                pos = pos.replace('x=','');pos = pos.replace('y=','')
                file.write(f'pos = {pos}\np.dragTo(pos,duration={time})\n')
                z += 1
            if key_choice_set == 'Back':
                main()


        #! TIME FUNCTION
        if key_choice == 'Time':
            time_sleep = prompt('How much time?')
            if time_sleep == '':
                time_sleep = 0
            file.write(f'time.sleep({int(time_sleep)})\n')

        if key_choice == 'Write':

            #! WRITE FUNCTION

            key_choice_write = confirm('Select: ','Write',buttons=['Write','Press','Info Press','Back'])
            if key_choice_write == 'Write':
                file.write('p.click()\n')
                text = prompt('Enter text: ','Settings')
                file.write(f'p.write("{text}",interval=0.02)\n')
                write_enter = confirm('Click Enter?','Settings',buttons=['yes','no'])
                if write_enter == 'yes':
                    file.write('p.press("enter")\n')

            if key_choice_write == 'Press':
                press_key = prompt('Enter Key Press: ','Write')
                file.write(f'p.press("{press_key}")\n')

            if key_choice_write == 'Info Press':
                visit = confirm("All Press Key: https://pytutorial.com/pyautogui-keyboard-keys",buttons=['Back','Visit'])
                if visit == 'Back':
                    main()
                if visit == 'Visit':
                    web.open('https://pytutorial.com/pyautogui-keyboard-keys')

            if key_choice_write == 'Back':
                main()


        if key_choice == 'Mouse':
            mouse_choice = confirm('Select','Settings',buttons=['left','right','double click','Back'])
        
        #! MOUSE FUNCTION LEFT
            if mouse_choice == 'left':
                alert(f'Mouse Function Completed!"',title='Message mouse')
                file.write('p.click()\n')
        #! MOUSE FUNCTION RIGHT
            if mouse_choice == 'right':
                alert(f'Mouse Function Completed!"',title='Message mouse')
                file.write('p.click(button="right")\n')
        #! MOUSE FUNCION DOUBLE CLICK
            if mouse_choice == 'double click':
                alert(f'Mouse Function Completed!"',title='Message mouse')
                file.write('p.doubleClick()\n')
                file.write('time.sleep(0.5)\n')

            if mouse_choice == 'Back':
                main()

        #! Developer
        if key_choice == 'Developer':
            choice = confirm('Select: ','Developer',buttons=['Add Comment','Add Line Code','Back'])


            # comment
            if choice == 'Add Comment':
                comment = prompt('Comment (not insert #): ','Developer')
                file.write(f'#{comment}\n')
            if choice == 'Add Line Code':
                line = prompt('Line: (pyautogui as p): ','Developer')
                file.write(f'{line}\n')
            if  choice == 'Back':
                main()


main()
