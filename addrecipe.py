from customtkinter import *
from PIL import Image
from recipe import Recipe


def adder(recipe_name,description, recipe_time, recipe_ingredients, recipe_steps):
    ingredients_list = [ingredient.strip() for ingredient in recipe_ingredients.split(',')]
    user_recipe = Recipe(recipe_name,description, int(recipe_time), ingredients_list, recipe_steps)
    print("added")

def reset(name,time,ingredients,steps):
     name.delete(0,'end')
     time.delete(0,'end')
     ingredients.delete(0,'end')
     steps.delete(0,'end')
     print("reset")
def clear_default_text(event, des):
    current_text = des.get("0.0","end")
    if current_text.strip() == "Add a short description":
        des.delete(1.0, "end")
def restore_default_text(event, des):
    current_text = des.get("0.0", "end")
    if not current_text.strip():  # Check if the text is empty
        des.insert("0.0", "Add a short description")
def clear_default_text2(event, des):
    current_text = des.get("0.0","end")
    if current_text.strip() == "Write steps here........":
        des.delete(1.0, "end")
def restore_default_text2(event, des):
    current_text = des.get("0.0", "end")
    if not current_text.strip():  # Check if the text is empty
        des.insert("0.0", "Write steps here........")
class AddRecipeFrame(CTkFrame):
    def __init__(self, parent_frame, **kwargs):
        super().__init__(parent_frame, **kwargs)
        self.configure(fg_color="#1B1C22",bg_color="#44454A")
       
        #label
        ingredientslabel = CTkLabel(self,text="Ingredients required",text_color="#BFBBBB",bg_color="#1B1c22",font=("",14))
        self.Difficultylabel = CTkLabel(self,text="Select Difficulty",text_color="#BFBBBB",bg_color="#1B1c22",font=("",14))
        self.PrepTime = CTkLabel(self,text="Set Preparation Time",text_color="#BFBBBB",bg_color="#1B1c22",font=("",14))
        self.hrlabel = CTkLabel(self,text="hr",text_color="#BFBBBB",bg_color="#1B1c22",font=("",20))
        self.minlabel = CTkLabel(self,text="min",text_color="#BFBBBB",bg_color="#1B1c22",font=("",20))
        self.stepslabel = CTkLabel(self,text="Detail Steps",text_color="#BFBBBB",bg_color="#1B1c22",font=("",16))
        font_size=10
       
        #entries
        name=CTkEntry(self,placeholder_text="Add Title Here...",text_color="white",fg_color="#1B1C22",placeholder_text_color="#BFBBBB", border_width=0,font=("",30),width=350)
        description=CTkTextbox(self,text_color="white",fg_color="#1B1C22", border_width=0,font=("",14),width=350,height=90)
        description.insert("0.0","Add a short description")
        description.bind("<FocusIn>", lambda event, des=description: clear_default_text(event, des))
        description.bind("<FocusOut>", lambda event, des=description: restore_default_text(event, des))
        Steps=CTkTextbox(self,text_color="#BFBBBB",fg_color="#1B1C22", border_width=0,font=("",14),width=350,height=700)
        Steps.insert("0.0","Write steps here........")
        Steps.bind("<FocusIn>", lambda event, des=Steps: clear_default_text2(event, des))
        Steps.bind("<FocusOut>", lambda event, des=Steps: restore_default_text2(event, des))
        self.hr=CTkEntry(self,text_color="white",fg_color="#393A3B", border_width=0,font=("",20),width=60,corner_radius=15)
        self.min=CTkEntry(self,text_color="white",fg_color="#393A3B", border_width=0,font=("",20),width=60,corner_radius=15)
       

        self.ingredient_entries = []  # List to hold ingredient entry fields

        self.difficulty = CTkOptionMenu(self, values=["Easy", "Medium","Hard"],fg_color="#393A3B",button_color="#393A3B",dropdown_fg_color="#393A3B",button_hover_color="#393A3B",dropdown_hover_color="#393A3B",dropdown_text_color="white",text_color="white")

        #buttons
        save_button = CTkButton(self,text="Save",fg_color="#F85656",corner_radius=30, command=lambda: adder(name.get(),description.get("0.0","end"), ingredientName.get(), ingredients.get(), steps.get()))
        reset_button= CTkButton(self,text="Reset",fg_color="#5684F8",corner_radius=30,command=lambda: reset(name,ingredientName,ingredients,steps) )
        self.plus_button = CTkButton(self, text="+", fg_color="#1B1C22", text_color="#848484", font=("", 20), width=20, hover_color="#1B1C22", command=self.add_ingredient_entry)
        self.add_ingredient_entry()  # Initially add one set of ingredient entry fields

        # Layout
        x = 50
        x2 = 440
        y = 50
        y2=50
        name.place(x=x, y=y)
        y += 40

        description.place(x=x, y=y)
        y += 100

        ingredientslabel.place(x=x + 10, y=y)
        y += 40

        self.stepslabel.place(x=x2,y=y2)
        y2+= 30
        Steps.place(x=x2,y=y2)

    def add_ingredient_entry(self):
        ingredient_name_entry = CTkEntry(self, placeholder_text="Ingredient Name", text_color="white", fg_color="#393A3B", placeholder_text_color="#848484", border_width=0, corner_radius=20, font=("", 16), width=200)
        ingredient_qty_entry = CTkEntry(self, placeholder_text="Qty", text_color="white", fg_color="#393A3B", placeholder_text_color="#848484", border_width=0, corner_radius=20, font=("", 16), width=80)
        self.ingredient_entries.append((ingredient_name_entry, ingredient_qty_entry))
        start_y = 230
        x = 50
        for entry_pair in self.ingredient_entries:
            entry_pair[0].place(x=x + 10, y=start_y)
            entry_pair[1].place(x=x + 220, y=start_y)
            start_y += 40
        self.plus_button.place(x=x+100+230, y=start_y-40)
        self.Difficultylabel.place(x=x+10,y=start_y)
        self.difficulty.place(x=x+150,y=start_y)
        start_y+=40
        self.PrepTime.place(x=x+10,y=start_y)
        start_y+=40
        self.hr.place(x=x+10,y=start_y)
        self.min.place(x=x+130,y=start_y)
        self.hrlabel.place(x=x+80,y=start_y)
        self.minlabel.place(x=x+200,y=start_y)
        

# app = CTk()
# app.geometry("1000x700")
# add_recipe_frame = AddRecipeFrame(app,width=650)
# app.mainloop()



   


    

       










        
        


       