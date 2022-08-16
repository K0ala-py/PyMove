from pyautogui import *
import keyboard as key

name = prompt('Welcome to my App for move and automate your pc!\nName of the new project!',title='App')
file = open(f'{name}.py','w')
file.write('import pyautogui as p\nimport time\np.hotkey("win","d")\n')

#? KEYBOARD KEY
keyboard_choice = confirm('For confirm your destination enter "ctrl+k"',title='Settings keyboard',buttons=['Ok','Change key'])
if keyboard_choice == 'Change key':
    keyboard = prompt('Enter Custom Key',title='Settings')
else:
    keyboard = 'ctrl+k'

time = confirm('Do you want enter time? (default = 1)','Settings',buttons=['no','yes'])
if time == 'yes':
    time = prompt('Enter time: ','TIME')
else:
    time = 1

x = 1
y = 0
while True:
    key_choice = confirm('Keyboard or mouse?','FUNCTION',buttons=['move','time','mouse','write','Developer','Exit'])
    if x == 1:
        hotkey('win','d')
    x += 1
    #! KEYBOARD FUNCTION
    if key_choice == 'move':
        if y == 0:
            alert(f'Positioned and click "{keyboard}"',title='Message key')
        key.wait(keyboard)
        pos1 = position()
        pos1 = str(pos1)
        pos1 = pos1[6:-1]
        pos1 = pos1.replace('x=','');pos1 = pos1.replace('y=','')
        file.write(f'pos1 = {pos1}\np.moveTo(pos1,duration={time})\n')
        file.write('p.click()\n')
        y += 1

    #! TIME FUNCTION
    if key_choice == 'time':
        time_sleep = prompt('How much time?')
        if time_sleep == '':
            time_sleep = 0
        file.write(f'time.sleep({int(time_sleep)})\n')

    #! WRITE FUNCTION
    if key_choice == 'write':
        file.write('p.click()\n')
        text = prompt('Enter text: ','Settings')
        file.write(f'p.write("{text}")\n')
        write_enter = confirm('Click Enter?','Settings',buttons=['yes','no'])
        if write_enter == 'yes':
            file.write('p.press("enter")\n')


    if key_choice == 'mouse':
        mouse_choice = confirm('Select','Settings',buttons=['left','right','double click'])
    
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

    #! Developer
    if key_choice == 'Developer':
        choice = confirm('Select: ','Developer',buttons=['Add Comment','Add Line Code'])

        # comment
        if choice == 'Add Comment':
            comment = prompt('Comment (not insert #): ','Developer')
            file.write(f'#{comment}\n')
        if choice == 'Add Line Code':
            line = prompt('Line: (pyautogui as p): ','Developer')
            file.write(f'{line}\n')

    #! EXIT
    if key_choice == 'Exit':
        exit()
