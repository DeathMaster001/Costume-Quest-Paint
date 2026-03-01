import os
import json
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

TILE_SIZE = 64
MAP_WIDTH = 64
MAP_HEIGHT = 64

# Paths to your tile images
TILE_IMAGES = {
    "Fence": "source/images/tiles/fence.png",
    "Grass": "source/images/tiles/grass.png",
    "Road": "source/images/tiles/road.png",
    "Void": "source/images/tiles/void.png"
}

# Paths to your object images grouped by category
OBJECT_IMAGES_TABS = {
    "Battle Stamps": {
        "Fang of the Wolf": "source/images/battle_stamps/stamp_001.png",
        "Black Cat (Card)": "source/images/battle_stamps/stamp_002.png",
        "Moving Tombstone": "source/images/battle_stamps/stamp_003.png",
        "Egg": "source/images/battle_stamps/stamp_004.png",
        "Disembodied Hand": "source/images/battle_stamps/stamp_005.png",
        "Pumpkin Guts": "source/images/battle_stamps/stamp_006.png",
        "Screaming Spider": "source/images/battle_stamps/stamp_007.png",
        "Bloodshot Eyeballs": "source/images/battle_stamps/stamp_008.png",
        "Toilet Paper": "source/images/battle_stamps/stamp_009.png",
        "One-Eyed Vampire Bat": "source/images/battle_stamps/stamp_010.png",
        "Witch's Brew": "source/images/battle_stamps/stamp_011.png",
        "Jawbone of the Wolf": "source/images/battle_stamps/stamp_012.png",
        "Albino Black Cat": "source/images/battle_stamps/stamp_013.png",
        "Banshee": "source/images/battle_stamps/stamp_014.png",
        "Flying Tombstone": "source/images/battle_stamps/stamp_015.png",
        "Rotten Egg": "source/images/battle_stamps/stamp_016.png",
        "Disembodied Six Fingered Hand": "source/images/battle_stamps/stamp_017.png",
        "Moldy Pumpkin Guts": "source/images/battle_stamps/stamp_018.png",
        "Yodeling Black Widow": "source/images/battle_stamps/stamp_019.png",
        "2-Ply Toilet Paper": "source/images/battle_stamps/stamp_020.png",
        "Headless Banshee": "source/images/battle_stamps/stamp_021.png",
        "Vegetarian Witch's Brew": "source/images/battle_stamps/stamp_022.png",
        "No-Eyed Vampire Bat": "source/images/battle_stamps/stamp_023.png",
        "Bowl of Bloodshot Eyeballs": "source/images/battle_stamps/stamp_024.png"
    },
    "Costumes": {
        "Robot": "source/images/costumes/costume_robot.png",
        "Knight": "source/images/costumes/costume_knight.png",
        "Statue of Liberty": "source/images/costumes/costume_statueofliberty.png",
        "Space Warrior": "source/images/costumes/costume_spacewarrior.png",
        "Ninja": "source/images/costumes/costume_ninja.png",
        "Unicorn": "source/images/costumes/costume_unicorn.png",
        "Pumpkin": "source/images/costumes/costume_pumpkin.png",
        "Vampire": "source/images/costumes/costume_vampire.png",
        "French Fries": "source/images/costumes/costume_frenchfries.png",
        "Black Cat": "source/images/costumes/costume_blackcat.png",
        "Grubbin": "source/images/costumes/costume_grubbin.png"
    },
    "Costume Pieces": {
        "Aluminum Foil": "source/images/costume_pieces/aluminumfoil.png",
        "Black Cloth": "source/images/costume_pieces/blackcloth.png",
        "Burlap Sack": "source/images/costume_pieces/burlapsack.png",
        "Cardboard": "source/images/costume_pieces/cardboard.png",
        "Cardboard Box": "source/images/costume_pieces/cardboardbox.png",
        "Dirty Socks": "source/images/costume_pieces/dirtysocks.png",
        "Empty Soda Bottle": "source/images/costume_pieces/emptysodabottle.png",
        "Fabric": "source/images/costume_pieces/fabric.png",
        "Feather Duster": "source/images/costume_pieces/featherduster.png",
        "Glitter": "source/images/costume_pieces/glitter.png",
        "Grubbin Mask": "source/images/costume_pieces/grubbinmask.png",
        "Leaves": "source/images/costume_pieces/leaves.png",
        "Orange Paint": "source/images/costume_pieces/orangepaint.png",
        "Paper Mache": "source/images/costume_pieces/papermache.png",
        "Rope": "source/images/costume_pieces/rope.png",
        "Safety Visor": "source/images/costume_pieces/safetyvisor.png",
        "Scarf": "source/images/costume_pieces/scarf.png",
        "Scary Fangs": "source/images/costume_pieces/scaryfangs.png",
        "Sheets": "source/images/costume_pieces/sheet.png",
        "Snow Boots": "source/images/costume_pieces/snowboots.png",
        "Sweat Pants": "source/images/costume_pieces/sweatpants.png",
        "Wheelies": "source/images/costume_pieces/wheelies.png",
        "White Makeup": "source/images/costume_pieces/whitemakeup.png",
        "Yarn": "source/images/costume_pieces/yarn.png"
    },
    "Creepy Treat Cards": {
        "Raz-Ums": "source/images/cards/trickcard_001.png",
        "Glop": "source/images/cards/trickcard_002.png",
        "Wobblers": "source/images/cards/trickcard_003.png",
        "Choconana": "source/images/cards/trickcard_004.png",
        "Shimmerfizz": "source/images/cards/trickcard_005.png",
        "Chunkwutter": "source/images/cards/trickcard_006.png",
        "Candy Hair": "source/images/cards/trickcard_007.png",
        "Moops": "source/images/cards/trickcard_008.png",
        "Chocolate Carrot": "source/images/cards/trickcard_009.png",
        "Fuds": "source/images/cards/trickcard_010.png",
        "Sweet Tooth": "source/images/cards/trickcard_011.png",
        "Jammie Jams": "source/images/cards/trickcard_012.png",
        "Lollopops": "source/images/cards/trickcard_013.png",
        "Fruity Foam": "source/images/cards/trickcard_014.png",
        "Swedish Noses": "source/images/cards/trickcard_015.png",
        "Box Cake": "source/images/cards/trickcard_016.png",
        "Gooz": "source/images/cards/trickcard_017.png",
        "Fee-Fi-Fo-Fudge": "source/images/cards/trickcard_018.png",
        "Slime Beetles": "source/images/cards/trickcard_019.png",
        "Sour Feet": "source/images/cards/trickcard_020.png",
        "Fish Head": "source/images/cards/trickcard_021.png",
        "Gummy Water": "source/images/cards/trickcard_022.png",
        "Licorice Cables": "source/images/cards/trickcard_023.png",
        "Cinnamon Brain": "source/images/cards/trickcard_024.png",
        "Mossy Log": "source/images/cards/trickcard_025.png",
        "Wood Chips": "source/images/cards/trickcard_026.png",
        "Pizza Sundae": "source/images/cards/trickcard_027.png",
        "Sweet Fat": "source/images/cards/trickcard_028.png",
        "Pimples": "source/images/cards/trickcard_029.png",
        "Frozen Butter": "source/images/cards/trickcard_030.png",
        "Edible Hat": "source/images/cards/trickcard_031.png",
        "Sludge": "source/images/cards/trickcard_032.png",
        "Coffee Toffee Taffee": "source/images/cards/trickcard_033.png",
        "Banana Beard": "source/images/cards/trickcard_034.png",
        "Broccoli Wafers": "source/images/cards/trickcard_035.png",
        "Gingerbread Ham": "source/images/cards/trickcard_036.png",
        "Mice Crispy Treat": "source/images/cards/trickcard_037.png",
        "Jaw Hurters": "source/images/cards/trickcard_038.png",
        "Blobbles": "source/images/cards/trickcard_039.png",
        "Barf Roll-Ups": "source/images/cards/trickcard_040.png",
        "Chocolate Hamburger": "source/images/cards/trickcard_041.png",
        "Clippingz": "source/images/cards/trickcard_042.png",
        "Salmon Rings": "source/images/cards/trickcard_043.png",
        "Street Chews": "source/images/cards/trickcard_044.png",
        "Fried Popcorn": "source/images/cards/trickcard_045.png",
        "Coconuts & Bolts": "source/images/cards/trickcard_046.png",
        "Jelly Has-Beens": "source/images/cards/trickcard_047.png",
        "Unicorn Pellets": "source/images/cards/trickcard_048.png",
        "Misfortune Cookie": "source/images/cards/trickcard_049.png",
        "Sugar Bucket": "source/images/cards/trickcard_050.png",
        "Old Lady Fingers": "source/images/cards/trickcard_051.png",
        "Boogie Pie": "source/images/cards/trickcard_052.png",
        "Human Crackers": "source/images/cards/trickcard_053.png",
        "Gloop": "source/images/cards/trickcard_054.png"
    },
    "Exploration": {
        "Boost": "source/images/exploration/boost.png",
        "Shield": "source/images/exploration/shield.png",
        "Glow": "source/images/exploration/glow.png",
        "Sneak": "source/images/exploration/sneak.png",
        "Lure": "source/images/exploration/lure.png"
    },
    "Houses": {
        "House": "source/images/houses/house.png",
        "Monster House": "source/images/houses/monster_house.png"
    },
    "Quests": {
        "Badge": "source/images/quests/badge.png",
        "Card": "source/images/quests/card.png",
        "Cherries": "source/images/quests/cherries.png",
        "Monster Horn": "source/images/quests/monster_horn.png",
        "NPC": "source/images/quests/npc.png",
        "Store": "source/images/quests/store.png",
        "Tickets": "source/images/quests/tickets.png"
    }
}


class TileMapEditor(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.root = self.winfo_toplevel()
        self.pack(fill="both", expand=True)
        self._initialized = False

        # --- Map state ---
        self.zoom = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.selected_object = None
        self.selected_tile = None
        self.is_painting = False
        self.is_erasing = False
        self.is_erasing_tile = False
        self.is_panning = False
        self.pan_start = (0, 0)
        self.tile_items = [[None for _ in range(
            MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.object_items = [[None for _ in range(
            MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

        # --- Undo / Redo ---
        self.undo_stack = []
        self.redo_stack = []

        # Persistent images
        self.tk_tiles_full = {}
        self.tk_objects_full = {}
        self.objects = {}

        # --- Main canvas ---
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(side="left", fill="both", expand=True)

        # --- Side panel ---
        self.panel = ttk.Frame(self)
        self.panel.pack(side="right", fill="y", padx=5, pady=5)

        # --- Map Controls ---
        controls_frame = ttk.Frame(self.panel)
        controls_frame.pack(pady=(0, 10))  # spacing before Tiles

        ttk.Button(controls_frame, text="Load Map",
                   command=self.load_map).pack(side="left", padx=2)
        ttk.Button(controls_frame, text="Save Map",
                   command=self.save_map).pack(side="left", padx=2)
        ttk.Button(controls_frame, text="Export as PNG",
                   command=self.export_png).pack(side="left", padx=2)
        ttk.Button(controls_frame, text="Zoom +",
                   command=lambda: self.change_zoom(0.25)).pack(side="left", padx=2)
        ttk.Button(controls_frame, text="Zoom -",
                   command=lambda: self.change_zoom(-0.25)).pack(side="left", padx=2)

        # --- Tiles ---
        ttk.Label(self.panel, text="Tiles", font=(
            "Segoe UI", 11, "bold")).pack(pady=(0, 5))
        self.tiles = {k: Image.open(v) for k, v in TILE_IMAGES.items()}
        for tile_name, img in self.tiles.items():
            frame = ttk.Frame(self.panel)
            frame.pack(pady=2)
            tk_img = ImageTk.PhotoImage(img.resize(
                (TILE_SIZE, TILE_SIZE), Image.NEAREST))
            self.tk_tiles_full[(tile_name, 1.0)] = tk_img
            btn = ttk.Button(frame, image=tk_img,
                             command=lambda t=tile_name: self.select_tile(t))
            btn.pack()
            lbl = ttk.Label(frame, text=tile_name, font=("Segoe UI", 9))
            lbl.pack()

        # --- Objects notebook ---
        ttk.Label(self.panel, text="Objects", font=(
            "Segoe UI", 11, "bold")).pack(pady=(10, 5))
        self.object_notebook = ttk.Notebook(self.panel)
        self.object_notebook.pack(fill="both", expand=True)

        for category, items in OBJECT_IMAGES_TABS.items():
            tab_frame = ttk.Frame(self.object_notebook)
            self.object_notebook.add(tab_frame, text=category)

            # Canvas + scrollbar
            canvas = tk.Canvas(tab_frame)
            scrollbar = ttk.Scrollbar(
                tab_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = ttk.Frame(canvas)
            scrollable_frame.bind(
                "<Configure>", lambda e, c=canvas: c.configure(scrollregion=c.bbox("all")))
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # 2-column layout for buttons
            col = 0
            row = 0
            for obj_name, path in items.items():
                self.objects[obj_name] = Image.open(path)
                frame = ttk.Frame(scrollable_frame)
                frame.grid(row=row, column=col, padx=2, pady=2)
                tk_img = ImageTk.PhotoImage(self.objects[obj_name].resize(
                    (TILE_SIZE, TILE_SIZE), Image.NEAREST))
                self.tk_objects_full[(obj_name, 1.0)] = tk_img
                btn = ttk.Button(
                    frame, image=tk_img, command=lambda o=obj_name: self.select_object(o))
                btn.pack()
                lbl = ttk.Label(frame, text=obj_name, font=("Segoe UI", 9))
                lbl.pack()

                col += 1
                if col >= 2:
                    col = 0
                    row += 1

        # --- Map data ---
        self.tile_map = [["Grass" for _ in range(
            MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.object_map = [[None for _ in range(
            MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

        # --- Bindings ---
        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.stop_paint)
        self.canvas.bind("<Button-3>", self.start_erase)
        self.canvas.bind("<B3-Motion>", self.erase)
        self.canvas.bind("<ButtonRelease-3>", self.stop_erase)
        self.canvas.bind("<Shift-Button-3>", self.start_erase_tile)
        self.canvas.bind("<Shift-B3-Motion>", self.erase_tile)
        self.canvas.bind("<Shift-ButtonRelease-3>", self.stop_erase_tile)
        self.canvas.bind("<ButtonPress-2>", self.start_pan)
        self.canvas.bind("<B2-Motion>", self.pan)
        self.canvas.bind("<ButtonRelease-2>", self.stop_pan)
        self.canvas.bind("<MouseWheel>", self.mouse_zoom)
        self.canvas.bind("<Button-4>", self.mouse_zoom)
        self.canvas.bind("<Button-5>", self.mouse_zoom)
        self.canvas.bind("<Configure>", self.on_canvas_resize)
        self.root.bind("<Control-z>", self.undo)
        self.root.bind("<Control-y>", self.redo)
        self.root.bind("<Control-plus>", lambda e: self.change_zoom(0.25))
        # some keyboards
        self.root.bind("<Control-equal>", lambda e: self.change_zoom(0.25))
        self.root.bind("<Control-minus>", lambda e: self.change_zoom(-0.25))

        # Draw initial map
        self.draw_map()

    def record_action(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()

        # limit undo size
        if len(self.undo_stack) > 200:
            self.undo_stack.pop(0)

    def init_map_view(self):
        self.fit_map_to_canvas()
        self.draw_map()

    def on_canvas_resize(self, event):
        if not self._initialized:
            self.fit_map_to_canvas()
            self.draw_map()
            self._initialized = True

    def center_map(self):
        canvas_width = self.canvas.winfo_width() or self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_height() or self.canvas.winfo_reqheight()

        map_pixel_width = MAP_WIDTH * TILE_SIZE * self.zoom
        map_pixel_height = MAP_HEIGHT * TILE_SIZE * self.zoom

        # Offsets to center the map
        self.offset_x = (canvas_width - map_pixel_width) / 2
        self.offset_y = (canvas_height - map_pixel_height) / 2

    def fit_map_to_canvas(self):
        canvas_width = self.canvas.winfo_width() or self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_height() or self.canvas.winfo_reqheight()

        zoom_x = canvas_width / (MAP_WIDTH * TILE_SIZE)
        zoom_y = canvas_height / (MAP_HEIGHT * TILE_SIZE)

        # Choose the smaller one to fit both width and height
        self.zoom = min(zoom_x, zoom_y)

        # Center the map
        self.center_map()

    # --- Selection ---
    def select_object(self, obj_name):
        self.selected_object = obj_name
        self.selected_tile = None

    def select_tile(self, tile_name):
        self.selected_tile = tile_name
        self.selected_object = None

    # --- Draw map ---
    def draw_map(self):
        self.canvas.delete("all")

        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):

                tile_img = self.get_tk_tile(self.tile_map[y][x])
                self.tile_items[y][x] = self.canvas.create_image(
                    int(round(x * TILE_SIZE * self.zoom + self.offset_x)),
                    int(round(y * TILE_SIZE * self.zoom + self.offset_y)),
                    anchor="nw",
                    image=tile_img
                )

                obj = self.object_map[y][x]
                if obj:
                    obj_img = self.get_tk_object(obj)
                    self.object_items[y][x] = self.canvas.create_image(
                        int(round(x * TILE_SIZE * self.zoom + self.offset_x)),
                        int(round(y * TILE_SIZE * self.zoom + self.offset_y)),
                        anchor="nw",
                        image=obj_img
                    )

    def update_tile(self, x, y):
        tile_img = self.get_tk_tile(self.tile_map[y][x])
        self.canvas.itemconfig(self.tile_items[y][x], image=tile_img)

    def update_object(self, x, y):
        # delete old object
        if self.object_items[y][x]:
            self.canvas.delete(self.object_items[y][x])
            self.object_items[y][x] = None

        obj = self.object_map[y][x]
        if obj:
            obj_img = self.get_tk_object(obj)
            self.object_items[y][x] = self.canvas.create_image(
                x * TILE_SIZE * self.zoom + self.offset_x,
                y * TILE_SIZE * self.zoom + self.offset_y,
                anchor="nw",
                image=obj_img
            )

    def get_tk_tile(self, tile_name):
        key = (tile_name, self.zoom)
        if key not in self.tk_tiles_full:
            size = round(TILE_SIZE * self.zoom)
            img = self.tiles[tile_name].resize((size, size), Image.NEAREST)
            self.tk_tiles_full[key] = ImageTk.PhotoImage(img)
        return self.tk_tiles_full[key]

    def get_tk_object(self, obj_name):
        key = (obj_name, self.zoom)
        if key not in self.tk_objects_full:
            size = round(TILE_SIZE * self.zoom)
            img = self.objects[obj_name].resize((size, size), Image.NEAREST)
            self.tk_objects_full[key] = ImageTk.PhotoImage(img)
        return self.tk_objects_full[key]

    # --- Paint / erase ---
    def start_paint(self, event):
        self.current_stroke = []
        self.is_painting = True
        self.paint(event)

    def paint(self, event):
        if not self.is_painting:
            return
        self._place_or_tile(event)

    def stop_paint(self, event):
        if self.current_stroke:
            self.record_action(self.current_stroke)
        self.current_stroke = []
        self.is_painting = False

    def start_erase(self, event):
        self.current_stroke = []
        self.is_erasing = True
        self.erase(event)

    def erase(self, event):
        if not self.is_erasing:
            return
        x = int((event.x - self.offset_x) // (TILE_SIZE * self.zoom))
        y = int((event.y - self.offset_y) // (TILE_SIZE * self.zoom))

        if any(a[1] == x and a[2] == y for a in self.current_stroke):
            return

        if not (0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT):
            return

        old = self.object_map[y][x]
        if old is not None:
            self.current_stroke.append(("object", x, y, old, None))
            self.object_map[y][x] = None
            self.update_object(x, y)

    def stop_erase(self, event):
        if self.current_stroke:
            self.record_action(self.current_stroke)
        self.current_stroke = []
        self.is_erasing = False

    def start_erase_tile(self, event):
        self.current_stroke = []
        self.is_erasing_tile = True
        self.erase_tile(event)

    def erase_tile(self, event):
        if not self.is_erasing_tile:
            return
        x = int((event.x - self.offset_x) // (TILE_SIZE * self.zoom))
        y = int((event.y - self.offset_y) // (TILE_SIZE * self.zoom))

        if any(a[1] == x and a[2] == y for a in self.current_stroke):
            return

        if not (0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT):
            return

        old = self.tile_map[y][x]
        new = "Void"
        if old != new:
            self.current_stroke.append(("tile", x, y, old, new))
            self.tile_map[y][x] = new
            self.update_tile(x, y)

    def stop_erase_tile(self, event):
        if self.current_stroke:
            self.record_action(self.current_stroke)
        self.current_stroke = []
        self.is_erasing_tile = False

    def _place_or_tile(self, event):
        x = int((event.x - self.offset_x) // (TILE_SIZE * self.zoom))
        y = int((event.y - self.offset_y) // (TILE_SIZE * self.zoom))

        if any(a[1] == x and a[2] == y for a in self.current_stroke):
            return

        if 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT:

            if self.selected_object:
                old = self.object_map[y][x]
                new = self.selected_object
                if old != new:
                    self.current_stroke.append(("object", x, y, old, new))
                    self.object_map[y][x] = new
                    self.update_object(x, y)

            elif self.selected_tile:
                old = self.tile_map[y][x]
                new = self.selected_tile
                if old != new:
                    self.current_stroke.append(("tile", x, y, old, new))
                    self.tile_map[y][x] = new
                    self.update_tile(x, y)

    def undo(self, event=None):
        if not self.undo_stack:
            return

        action = self.undo_stack.pop()
        self.redo_stack.append(action)

        # --- Handle stroke ---
        if isinstance(action, list):
            for kind, x, y, old, new in reversed(action):
                if kind == "tile":
                    self.tile_map[y][x] = old
                    self.update_tile(x, y)
                else:
                    self.object_map[y][x] = old
                    self.update_object(x, y)
            return

        # --- Handle single ---
        kind, x, y, old, new = action

        if kind == "tile":
            self.tile_map[y][x] = old
            self.update_tile(x, y)
        else:
            self.object_map[y][x] = old
            self.update_object(x, y)

    def redo(self, event=None):
        if not self.redo_stack:
            return

        action = self.redo_stack.pop()
        self.undo_stack.append(action)

        # --- Handle stroke ---
        if isinstance(action, list):
            for kind, x, y, old, new in action:
                if kind == "tile":
                    self.tile_map[y][x] = new
                    self.update_tile(x, y)
                else:
                    self.object_map[y][x] = new
                    self.update_object(x, y)
            return

        # --- Handle single ---
        kind, x, y, old, new = action

        if kind == "tile":
            self.tile_map[y][x] = new
            self.update_tile(x, y)
        else:
            self.object_map[y][x] = new
            self.update_object(x, y)

    # --- Pan ---
    def start_pan(self, event):
        self.is_panning = True
        self.pan_start = (event.x, event.y)

    def pan(self, event):
        if not self.is_panning:
            return

        dx = event.x - self.pan_start[0]
        dy = event.y - self.pan_start[1]

        self.offset_x += dx
        self.offset_y += dy

        self.canvas.move("all", dx, dy)

        self.pan_start = (event.x, event.y)

    def stop_pan(self, event):
        self.is_panning = False

    # --- Zoom ---
    def change_zoom(self, delta):
        old_zoom = self.zoom
        new_zoom = max(0.25, min(2.0, self.zoom + delta))

        # Center of the canvas in canvas coordinates
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        center_x = canvas_width / 2
        center_y = canvas_height / 2

        # Map coordinates under canvas center before zoom
        map_x = (center_x - self.offset_x) / old_zoom
        map_y = (center_y - self.offset_y) / old_zoom

        # Update zoom
        self.zoom = new_zoom

        # Adjust offsets so center stays at the same map point
        self.offset_x = center_x - map_x * self.zoom
        self.offset_y = center_y - map_y * self.zoom

        # Redraw everything
        self.draw_map()

    def mouse_zoom(self, event):
        # Determine zoom direction
        if hasattr(event, "delta"):
            direction = 1 if event.delta > 0 else -1
        elif hasattr(event, "num"):
            direction = 1 if event.num == 4 else -1
        else:
            return

        old_zoom = self.zoom
        new_zoom = max(0.25, min(2.0, self.zoom + 0.25 * direction))

        # Cursor position in canvas coordinates
        cursor_x = self.canvas.canvasx(event.x)
        cursor_y = self.canvas.canvasy(event.y)

        # Map coordinates under cursor before zoom
        map_x = (cursor_x - self.offset_x) / old_zoom
        map_y = (cursor_y - self.offset_y) / old_zoom

        # Update zoom
        self.zoom = new_zoom

        # Adjust offsets so the map point under cursor stays the same
        self.offset_x = cursor_x - map_x * self.zoom
        self.offset_y = cursor_y - map_y * self.zoom

        # Redraw everything at new zoom
        self.draw_map()

    def refresh_zoom_images(self):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                self.update_tile(x, y)
                if self.object_map[y][x]:
                    self.update_object(x, y)

    # --- Save / Load ---
    def save_map(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON Files", "*.json")])
        if not file_path:
            return
        data = {"tiles": self.tile_map, "objects": self.object_map}
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)

    def load_map(self):
        file_path = filedialog.askopenfilename(defaultextension=".json",
                                               filetypes=[("JSON Files", "*.json")])
        if not file_path:
            return
        with open(file_path, "r") as f:
            data = json.load(f)
        self.tile_map = data.get("tiles", self.tile_map)
        self.object_map = data.get("objects", self.object_map)
        self.draw_map()
        self.undo_stack.clear()
        self.redo_stack.clear()

    def export_png(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")]
        )
        if not file_path:
            return

        # Final image size (full resolution, not zoomed)
        width = MAP_WIDTH * TILE_SIZE
        height = MAP_HEIGHT * TILE_SIZE

        # Create blank image
        final_image = Image.new("RGBA", (width, height))

        # Draw tiles first
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                tile_name = self.tile_map[y][x]
                tile_img = self.tiles[tile_name]

                final_image.paste(
                    tile_img,
                    (x * TILE_SIZE, y * TILE_SIZE)
                )

        # Draw objects on top
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                obj_name = self.object_map[y][x]
                if obj_name:
                    obj_img = self.objects[obj_name]

                    # Use alpha so transparency works
                    final_image.paste(
                        obj_img,
                        (x * TILE_SIZE, y * TILE_SIZE),
                        obj_img
                    )

        final_image.save(file_path)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tile Map Editor")
    root.state("zoomed")
    editor = TileMapEditor(root)
    root.mainloop()
