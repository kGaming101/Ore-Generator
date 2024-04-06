import math
import random
import tkinter as tk
from tkinter import ttk
import os

class OreGenerator:
    def __init__(self):
        # Initialize the Tkinter window and set its properties
        self.window = tk.Tk()
        self.window.title("Ore Generator")
        self.window.iconphoto(False, tk.PhotoImage(file="assets/stone.png"))
        self.size = min(self.window.winfo_screenwidth(), self.window.winfo_screenheight()) * 0.85
        self.size = int(self.size)
        self.window.geometry(f"{self.size}x{self.size}")
        self.window.resizable(False,False)
        self.max_grid_size = round(os.cpu_count() * 13, -1)

        # Create frames for game menu and pause menu
        self.game_menu = tk.Frame(self.window, width=self.size, height=self.size, bg="azure4")
        self.game_menu.place(relx=0, rely=0)
        self.pause_menu = tk.Frame(self.window, width=self.size, height=self.size, bg="dimgray")
        self.pause_menu.place(relx=0, rely=0)

        self.paused = True
        self.ore_gen = True

        # Create widgets for pause menu
        self.create_widgets()

    def create_widgets(self):
        # Create labels, entry boxes, and buttons for the pause menu
        title = tk.Label(self.pause_menu, text="Ore Generator", font=("Comic Sans MS", round(self.size / 50), "bold"), bg="dimgray")
        title.place(relx=0.5, rely=0, anchor=tk.N)

        world_size_text = tk.Label(self.pause_menu, text="World Size:", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray")
        world_size_text.place(relx=0, rely=0.05)
        self.world_size_entry = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.world_size_entry.place(relx=0.14, rely=0.05)
        self.world_size_error = tk.Label(self.pause_menu, text="", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray", fg="maroon")
        self.world_size_error.place(relx=0.2, rely=0.05)

        bedrock_height_text = tk.Label(self.pause_menu, text="Bedrock Height:", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray")
        bedrock_height_text.place(relx=0, rely=0.1)
        self.bedrock_height_entry = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.bedrock_height_entry.place(relx=0.18, rely=0.1)
        self.bedrock_height_error = tk.Label(self.pause_menu, text="", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray", fg="maroon")
        self.bedrock_height_error.place(relx=0.24, rely=0.1)

        self.ore_gen_tog_text = tk.Label(self.pause_menu, text="Random Ore Generation:", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray")
        self.ore_gen_tog_text.place(relx=0, rely=0.15)
        self.ore_gen_tog_butt = tk.Button(self.pause_menu, command=self.toggle_ore_gen, text="ON ", font=("Comic Sans MS", round(self.size / 80), "bold"), bg="green", fg="black")
        self.ore_gen_tog_butt.place(relx=0.26, rely=0.15)

        self.ore_names_text = tk.Label(self.pause_menu, text="ORE NAMES:", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray")
        self.ore_names_text.place(relx=0, rely=0.2)

        self.coal_ore_names_text = tk.Label(self.pause_menu, text="COAL", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray")
        self.coal_ore_names_text.place(relx=0.235, rely=0.2)
        self.iron_ore_names_text = tk.Label(self.pause_menu, text="IRON", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray")
        self.iron_ore_names_text.place(relx=0.38, rely=0.2)
        self.gold_ore_names_text = tk.Label(self.pause_menu, text="GOLD", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray")
        self.gold_ore_names_text.place(relx=0.53, rely=0.2)
        self.diamond_ore_names_text = tk.Label(self.pause_menu, text="DIAMOND", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray")
        self.diamond_ore_names_text.place(relx=0.66, rely=0.2)
        self.emerald_ore_names_text = tk.Label(self.pause_menu, text="EMERALD", font=("Comic Sans MS", round(self.size / 65), "bold"), bg="dimgray")
        self.emerald_ore_names_text.place(relx=0.81, rely=0.2)

        self.ore_top_chance = tk.Label(self.pause_menu, text="Ore Chance 1 in __ at the top:", font=("Comic Sans MS", round(self.size / 100), "bold"), bg="dimgray")
        self.ore_top_chance.place(relx=0, rely=0.253)
        
        self.coal_ore_top_chance = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.coal_ore_top_chance.place(relx=0.25, rely=0.25)
        self.iron_ore_top_chance = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.iron_ore_top_chance.place(relx=0.4, rely=0.25)
        self.gold_ore_top_chance = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.gold_ore_top_chance.place(relx=0.55, rely=0.25)
        self.diamond_ore_top_chance = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.diamond_ore_top_chance.place(relx=0.70, rely=0.25)
        self.emerald_ore_top_chance = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.emerald_ore_top_chance.place(relx=0.85, rely=0.25)
        

        self.ore_bottom_chance = tk.Label(self.pause_menu, text="Ore Chance 1 in __ at the bottom:", font=("Comic Sans MS", round(self.size / 100), "bold"), bg="dimgray")
        self.ore_bottom_chance.place(relx=0, rely=0.3035)
        
        self.coal_ore_bottom_chance = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.coal_ore_bottom_chance.place(relx=0.25, rely=0.3)
        self.iron_ore_bottom_chance = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.iron_ore_bottom_chance.place(relx=0.4, rely=0.3)
        self.gold_ore_bottom_chance = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.gold_ore_bottom_chance.place(relx=0.55, rely=0.3)
        self.diamond_ore_bottom_chance = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.diamond_ore_bottom_chance.place(relx=0.70, rely=0.3)
        self.emerald_ore_bottom_chance = tk.Entry(self.pause_menu, font=("Comic Sans MS", round(self.size / 65), "bold"), bg="white", width=round(self.size / 300))
        self.emerald_ore_bottom_chance.place(relx=0.85, rely=0.3)
        
        self.new_patch_button = tk.Button(self.pause_menu, text = "NEW" , font=("Comic Sans MS", round(self.size / 80), "bold"), bg="cyan")
        self.new_patch_button.place(relx=0, rely=0.35)
        
        generate_button = tk.Button(self.pause_menu, text="GENERATE WORLD", font=("Comic Sans MS", round(self.size / 50), "bold"), bg="green", command=self.generate_world)
        generate_button.place(relx=0.5, rely=1, anchor=tk.S)

        # Bind escape key to toggle pause menu
        self.window.bind("<Escape>", self.toggle_pause)

    def toggle_pause(self, event):
        # Toggle between game menu and pause menu
        self.paused = not self.paused
        self.pause_menu.lift() if self.paused else self.game_menu.lift()

    def toggle_ore_gen(self):
        # Toggle between game menu and pause menu
        self.ore_gen = not self.ore_gen
        if self.ore_gen:
            self.ore_gen_tog_butt["text"] = "ON "
            self.ore_gen_tog_butt["fg"] = "black"
            self.ore_gen_tog_butt["bg"] = "green"
        else:
            self.ore_gen_tog_butt["text"] = "OFF"
            self.ore_gen_tog_butt["fg"] = "white"
            self.ore_gen_tog_butt["bg"] = "red"

    def generate_world(self):
        error = False
        
        # Generate the world based on user input
        world_size = self.world_size_entry.get()
        bedrock_height = self.bedrock_height_entry.get()

        try:
            world_size = int(world_size)
            self.world_size_error.config(text="")
        except ValueError:
            self.world_size_error.config(text="World Size Must Be An Integer")
            error = True
        
        if world_size > self.max_grid_size or world_size < 1:
            self.world_size_error.config(text=f"World Size Height Must Be In The Range 1 - {self.max_grid_size} (inclusive)")
            error = True

        try:
            bedrock_height = int(bedrock_height)
            self.bedrock_height_error.config(text="")
        except ValueError:
            self.bedrock_height_error.config(text="Bedrock Height Must Be An Integer")
            error = True
        
        if bedrock_height > world_size or bedrock_height < 1:
            self.bedrock_height_error.config(text=f"Bedrock Height Must Be In The Range 1 - {world_size} (inclusive)")
            error = True
        
        if self.ore_gen:
            random_ore_gen_errors = {}
            random_ore_gen_values = {}

            random_ore_gen_values["coal_top"] = self.coal_ore_top_chance.get()
            random_ore_gen_values["coal_bottom"] = self.coal_ore_bottom_chance.get()
            random_ore_gen_values["iron_top"] = self.iron_ore_top_chance.get()
            random_ore_gen_values["iron_bottom"] = self.iron_ore_bottom_chance.get()
            random_ore_gen_values["gold_top"] = self.gold_ore_top_chance.get()
            random_ore_gen_values["gold_bottom"] = self.gold_ore_bottom_chance.get()
            random_ore_gen_values["diamond_top"] = self.diamond_ore_top_chance.get()
            random_ore_gen_values["diamond_bottom"] = self.diamond_ore_bottom_chance.get()
            random_ore_gen_values["emerald_top"] = self.emerald_ore_top_chance.get()
            random_ore_gen_values["emerald_bottom"] = self.emerald_ore_bottom_chance.get()

            for value in random_ore_gen_values:
                try:
                    random_ore_gen_values[value] = int(random_ore_gen_values[value])
                    try:
                        del random_ore_gen_errors[value]
                    except:
                        pass
                except ValueError:
                    random_ore_gen_errors[value] = "Integer"
                    error = True
        
                if random_ore_gen_values[value] > 100 or random_ore_gen_values[value] < 0:
                    random_ore_gen_errors[value] = "Range"
                    error = True

        if error:
            return

        # Generate empty world and add bedrock
        self.generate_empty(world_size)
        self.generate_bedrock(bedrock_height)

        if self.ore_gen:
            self.generate_ore(world_size, random_ore_gen_values["coal_top"], random_ore_gen_values["iron_top"], random_ore_gen_values["diamond_top"], random_ore_gen_values["emerald_top"], random_ore_gen_values["gold_top"], random_ore_gen_values["coal_bottom"], random_ore_gen_values["iron_bottom"], random_ore_gen_values["diamond_bottom"], random_ore_gen_values["emerald_bottom"], random_ore_gen_values["gold_bottom"])

        self.initialize_images()

        self.clear_blocks()

        print(self.blocks)

        # Draw the blocks in the game menu and switch to it
        self.draw_blocks()
        self.game_menu.lift()

    def generate_empty(self, grid_size):
        # Generate an empty grid for the world
        self.blocks = [[0] * grid_size for _ in range(grid_size)]

    def generate_bedrock(self, max_height):
        # Add bedrock layer to the bottom of the world
        for x in range(len(self.blocks)):
            for h in range(random.randint(1, max_height)):
                self.blocks[len(self.blocks) - (h + 1)][x] = 6

    def draw_blocks(self):
        # Draw blocks based on their types in the game menu
        block_length = self.size / len(self.blocks)
        for y in range(len(self.blocks)):
            for x in range(len(self.blocks[y])):
                block_type = self.blocks[y][x]
                if block_type == 0:
                    img = self.stone
                elif block_type == 1:
                    img = self.coal
                elif block_type == 2:
                    img = self.iron
                elif block_type == 3:
                    img = self.diamond
                elif block_type == 4:
                    img = self.emerald
                elif block_type == 5:
                    img = self.gold
                elif block_type == 6:
                    img = self.bedrock

                block = tk.Label(self.game_menu, image=img, width=block_length, height=block_length, borderwidth=0, highlightthickness=0, bg="azure4")
                block.place(relx=x / len(self.blocks), rely=y / len(self.blocks), anchor="nw")

    def initialize_images(self):
        # Resize the all images
        sf = int(self.size / len(self.blocks))
        images = os.listdir("assets")
        for image in images:
            image_name = image.split(".")[0]
            image = tk.PhotoImage(file="assets/"+image_name+".png")
            image = image.zoom(sf)
            image = image.subsample(20)
            setattr(self, image_name, image)
    
    def generate_ore(self, ws, ct, it, dt, et, gt, cb, ib, db, eb, gb):
      blocks = self.blocks
      c = ct
      i = it
      d = dt
      g = gt
      e = et

      cd = ct - cb
      id = it - ib
      dd = dt - db
      gd = gt - gb
      ed = et - eb

      cd /= ws
      id /= ws
      dd /= ws
      gd /= ws
      ed /= ws

      for y_ in range(ws):
        print(c,i,g,d,e)
        for x_ in range(ws):
          if y_ != ws-1 and blocks[y_][x_] != 6:
            coal_chance = random.randint(0, int(c*100))
            iron_chance = random.randint(0, int(i*100))
            gold_chance = random.randint(0, int(g*100))
            diamond_chance = random.randint(0, int(d*100))
            emerald_chance = random.randint(0, int(e*100))

            if 0 < coal_chance <= 100:
              blocks[y_][x_] = 1
            if 0 < iron_chance <= 100:
              blocks[y_][x_] = 2
            if 0 < gold_chance <= 100:
              blocks[y_][x_] = 5
            if 0 < diamond_chance <= 100:
              blocks[y_][x_] = 3
            if 0 < emerald_chance <= 100:
              blocks[y_][x_] = 4
        
        c -= cd
        i -= id
        d -= dd
        g -= gd
        e -= ed
        
    def run(self):
        # Start the Tkinter event loop
        self.window.mainloop()
    
    def clear_blocks(self): 
        for widget in self.game_menu.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    # Create an instance of OreGenerator and run the application
    ore_generator = OreGenerator()
    print(ore_generator.size)
    ore_generator.run()

"""
features to add

def generate_ore_patch(ore_type, count, radius, patch_type):
  global blocks
  global grid_size
  start_y = random.randint(0, grid_size - 1)
  start_x = random.randint(0, grid_size - 1)

  if patch_type == "square":
    end_y = start_y + (2*radius)
    end_x = start_x + (2*radius)

    for y_ in range(start_y, end_y):
      for x_ in range(start_x, end_x):
        try:
          if blocks[y_][x_] != ore_type and blocks[y_][x_] != 6:
            blocks[y_][x_] = ore_type
            count-=1
          if count == 0:
            return
        except:
          pass
          
  if patch_type == "circle":
    end_y = start_y + (2 * radius)
    end_x = start_x + (2 * radius)
    center_x = (start_x + end_x) / 2
    center_y = (start_y + end_y) / 2
    for y_ in range(start_y, end_y):
      for x_ in range(start_x, end_x):
        if math.sqrt((x_ - center_x)**2 + (y_ - center_y)**2) <= radius:
          try:
            if blocks[y_][x_] != ore_type and blocks[y_][x_] != 6:
              blocks[y_][x_] = ore_type
              count-=1
            if count == 0:
              return
          except:
            pass
          
  if patch_type == "random":
    end_y = start_y + (2*radius)
    end_x = start_x + (2*radius)
    for i in range(count):
      try:
        y_ = random.randint(start_y, end_y)
        x_ = random.randint(start_x, end_x)
        if blocks[y_][x_] != ore_type and blocks[y_][x_] != 6:
          blocks[y_][x_] = ore_type
      except:
        pass

        


"""
