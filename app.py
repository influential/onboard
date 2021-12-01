import tkinter as tk
from tkinter import filedialog, Text, Entry, ttk
from tkinter.messagebox import showinfo

paths = {}


def selectInput(components):
    # This will grab the selected directory path
    selectedPath = filedialog.askdirectory()

    # Save the path to the main paths dictionary
    paths['inputPath'] = selectedPath
    print(paths['inputPath'])

    # Display the selected path
    label = tk.Label(components['importContainer'],
                     text=selectedPath, bg="gray")
    label.pack()


def selectSave(components):
     # This will grab the selected directory path
    selectedPath = filedialog.askdirectory()

    # Save the path to the main paths dictionary
    paths['savePath'] = selectedPath
    print(paths['savePath'])

    # Display the selected path
    label = tk.Label(components['importContainer'],
                     text=selectedPath, bg="gray")
    label.pack()


def buildGUI(paths):
    print("Building GUI")
    components = {}  # stores all of the components for the UI
    root = tk.Tk()

    w = 425
    h = 500
    screenW = root.winfo_screenwidth()
    screenH = root.winfo_screenheight()
    x = (screenW/2) - (w/2)
    y = (screenH/2) - (h/2)

    dimensions = f'{int(w)}x{int(h)}+{int(x)}+{int(y)}'

    root.title("Onboard")
    # root.geometry("700x700 + 400 + 300")
    root.geometry(dimensions)
    root.configure(background="#9CAFB7")
    components['root'] = root

    # Import Buttons and Labels

    # toLabel = tk.Label(root, text="TO", font=("bold", 14))
    # toLabel.grid(row=0, column=1)

    inputContainer = tk.Frame(root)
    inputContainer.grid(row=6, columnspan=3, sticky="N", pady=0)

    # inputPathLabel = tk.Label(root, text="Input Path", font=("bold", 14))
    # inputPathLabel.grid(row=0, column=0)

    chooseInputPath = tk.Button(
        inputContainer,  cursor="hand", text="Select Input Folder", padx=10, pady=15, fg="black", bg="#EAD2AC",
        command=lambda: selectInput(components))
    # chooseInputPath.pack()
    components['chooseInputPath'] = chooseInputPath
    chooseInputPath.grid(row=0, column=1)

    # savePathLabel = tk.Label(root, text="Save Path", font=("bold", 14))
    # savePathLabel.grid(row=0, column=2)

    chooseSavePath = tk.Button(
        inputContainer, cursor="hand", text="Select Save Folder", padx=10, pady=15, fg="black", bg="#EAD2AC",
        command=lambda: selectSave(components))
    # chooseSavePath.pack()
    components['chooseSavePath'] = chooseSavePath
    chooseSavePath.grid(row=0, column=2)

    # Project Details Notebook (tabs)
    # projectDetailsLabel = tk.Label(
    #     root, text="Project Details", font=('bold', 14))
    # projectDetailsLabel.grid(row=2, column=0)

    tabControl = ttk.Notebook(root)
    concertTab = ttk.Frame(tabControl)
    musicVidTab = ttk.Frame(tabControl)

    tabControl.add(concertTab, text='Concert')
    tabControl.add(musicVidTab, text='Music Video')
    # tabControl.pack(expand=1, fill="both")
    tabControl.grid(row=0, column=0, rowspan=6,
                    columnspan=3, pady=20, padx=20)

    # Concert Project Details
    concertTitleLabel = ttk.Label(concertTab, text="Title")
    concertTitleLabel.grid(column=0,
                           row=0,
                           padx=35,
                           pady=0)

    concertTitleEntry = ttk.Entry(concertTitleLabel)
    concertTitleEntry.grid(column=1,
                           row=1,
                           padx=35,
                           pady=0)

    concertDateLabel = ttk.Label(concertTab, text="Date")
    concertDateLabel.grid(column=0,
                          row=1,
                          padx=35,
                          pady=0)
    concertDateEntry = ttk.Entry(concertDateLabel)
    concertDateEntry.grid(column=1,
                          row=1,
                          padx=35,
                          pady=0)

    concertGo = ttk.Button(concertTab, text="GO")
    concertGo.grid(column=0,
                   row=2,
                   padx=35,
                   pady=0)

    # Music Video Project Details
    musicVidArtistLabel = ttk.Label(musicVidTab, text="Artist")
    musicVidArtistLabel.grid(column=1,
                             row=1,
                             padx=35)
    musicVidArtistEntry = ttk.Entry(musicVidArtistLabel)
    musicVidArtistEntry.grid(column=1,
                             row=1,
                             padx=35,
                             pady=0)

    musicVidSongLabel = ttk.Label(musicVidTab, text="Song")
    musicVidSongLabel.grid(column=1,
                           row=2,
                           padx=35)
    musicVidSongEntry = ttk.Entry(musicVidSongLabel)
    musicVidSongEntry.grid(column=1,
                           row=2,
                           padx=35,
                           pady=0)

    musicVidDateLabel = ttk.Label(musicVidTab, text="Date")
    musicVidDateLabel.grid(column=1,
                           row=3,
                           padx=35)
    musicVidDateEntry = ttk.Entry(musicVidDateLabel)
    musicVidDateEntry.grid(column=1,
                           row=3,
                           padx=35,
                           pady=0)

    musicVidGo = ttk.Button(musicVidTab, text="GO")
    musicVidGo.grid(column=1,
                    row=4,
                    padx=35,
                    pady=0)

    # root.grid_columnconfigure((0, 4), weight=1)
    root.mainloop()


buildGUI(paths)
