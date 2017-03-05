import Tkinter as tk
from PIL import Image, ImageTk
import constants
from attacks import *
import threading
from exitable_process import *
class GraphicMain():
    """docstring for GraphicMain"""
    def __init__(self, root, components, graphic_locationer):
        self.possible_attacks = NetworkAttacks() # set the attacks instance
        self.selected_component = None # current component
        self.components = components
        self.graphic_locationer = graphic_locationer
        self.root = root
        self.canvas = tk.Canvas(self.root, width = constants.WINDOW_WIDTH, height = constants.WINDOW_HEIGHT)
        self.pc_img = ImageTk.PhotoImage(Image.open("resources/pc-icon.png").resize((constants.IMG_HEIGHT, constants.IMG_WIDTH)))
        self.router_img = ImageTk.PhotoImage(Image.open("resources/router-icon.png").resize((constants.IMG_HEIGHT + 32, constants.IMG_WIDTH + 32)))
        self.canvas.pack()
        self.canvas.bind("<Button-1>",self.on_click)
        self.textbox = tk.Text(self.root, height = 8, width= 100)
        self.textbox.pack()
        self.create_popup_menus()
        self.canvas.bind("<Button-3>", self.do_popup)
        for i in range(len(components)):#send the coordinates and identifying index
            if components[i].IsRouter():
                self.add_router(components[i], i)   
            else:   
                self.add_pc(components[i], i)


    def create_popup_menus(self):
        self.popup = tk.Menu(self.root, tearoff=0)
        self.popup.add_command(label="Smurf", command=lambda:self.possible_attacks.smurf_attack(self.selected_component)) # smurf the target
        self.popup.add_separator()
        self.popup.add_command(label="Previous")
        self.popup.add_separator()
        self.popup.add_command(label="Home")
        self.router_popup = tk.Menu(self.root, tearoff=0)
        self.router_popup.add_command(label="Starve", command=self.possible_attacks.DHCP_starvation) # starving the dhcp server near me
        self.router_popup.add_separator()
        self.router_popup.add_command(label="Previous")
        self.router_popup.add_separator()
        self.router_popup.add_command(label="Home")


    def do_popup(self,event):
        # display the popup menu
        is_router = self.on_click(None) # switches to the selected component
        if is_router: # get the router menu
            try:
                self.router_popup.tk_popup(event.x_root, event.y_root, 0)
            finally:
                # make sure to release the grab (Tk 8.0a1 only)
                self.router_popup.grab_release()
                
        else: # if not router
            try:
                self.popup.tk_popup(event.x_root, event.y_root, 0)
            finally:
                # make sure to release the grab (Tk 8.0a1 only)
                self.popup.grab_release()


    def add_pc(self,pc, i):
        locations = self.graphic_locationer.get_location(pc)
        self.canvas.create_image(locations[0], locations[1], anchor = 'nw', image = self.pc_img, tags = str(i))# sends index in components' list as tag



    def add_router(self, router ,i):
        locations = self.graphic_locationer.get_location(router)
        self.canvas.create_image(locations[0], locations[1], anchor = 'nw', image = self.router_img, tags = str(i))# sends index in components' list as tag


    def get_component_by_id(self, i):
        return self.components[int(i)] 


    def on_click(self,event):
        if self.canvas.find_withtag("current"):
            self.textbox.delete(1.0,tk.END)
            component = self.get_component_by_id(self.canvas.gettags("current")[0])
            print component.get_string()
            self.textbox.insert(tk.END , component.get_string())
            self.selected_component = component
            return component.IsRouter()
        return False




