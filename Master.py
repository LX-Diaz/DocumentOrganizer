#!/usr/bin/env python3
"""
Main program in my LXMasterTool toolset. Handles GUI and overall functionality and will serve as the core program to manage all my tools
Written by Luis Diaz
12/30/2020
"""
import pyglet, glooey
from Modules import DocOrganizerClass


pyglet.resource.path = ['./Resources/BlueGlass_Frosted']
pyglet.resource.reindex()


# Initialize Classes
DocOrg = DocOrganizerClass.DocumentOrganizer()

# GUI window setup
window = pyglet.window.Window(caption="LX Master Tool",style='dialog')
gui = glooey.Gui(window)

class TitleLabel(glooey.Label):
    custom_font_name = "Lato-Regular"
    custom_font_size = 12
    custom_color = "#009EFF"
    custom_alignment = 'center'

class ButtonLabel(glooey.Label):
    custom_font_name = "Calibri"
    custom_font_size = 8
    custom_color = "#009EFF"
    custom_alignment = 'center'

class CustomButton(glooey.Button):
    Foreground = ButtonLabel

    class Base(glooey.Image):
        custom_image = pyglet.resource.image('base.png')

    class Over(glooey.Image):
        custom_image = pyglet.resource.image('over.png')

    class Down(glooey.Image):
        custom_image = pyglet.resource.image('down.png')

class TemplateButtonLabel(glooey.Label):
    custom_font_name = "Calibri"
    custom_font_size = 9
    custom_color = "0080ff"
    custom_alignment = 'center'



# Document Organizer section
DocOrgVbox = glooey.VBox()
DocOrgVbox.alignment = 'top'
DocOrgLabel = TitleLabel("Document Organizer")
CheckDirBttn = CustomButton('Check Directories')
CheckDirBttn.push_handlers(on_click=lambda w: DocOrg.ChkDir())
OrganizeBttn = CustomButton('Organize')
OrganizeBttn.push_handlers(on_click=lambda w: DocOrg.Organize())
CCleanBttn = CustomButton('C Cleaner')
CCleanBttn.push_handlers(on_click=lambda w: DocOrg.CCleaner())
DocOrgVbox.add(DocOrgLabel)
DocOrgVbox.add(CheckDirBttn)
DocOrgVbox.add(OrganizeBttn)
DocOrgVbox.add(CCleanBttn)

# Add objects to grid
grid = glooey.Grid()
grid.add(0, 0, DocOrgVbox)
gui.add(grid)


#Adjust window size to grid width and height
print(f"Contents Size{grid.claimed_size}")
WindowWidth = grid.claimed_width
WindowHeight = grid.claimed_height
window.set_size(WindowWidth,WindowHeight)


# Run Pyglet App
pyglet.app.run()
