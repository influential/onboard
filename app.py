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
    root.title("Onboard")
    root.geometry("700x700")
    root.configure(background="#9CAFB7")
    # canvas = tk.Canvas(root, height=700, width=700, bg="white")
    # canvas.pack()
    components['root'] = root

    # for x in range(5):
    #     concertTitleEntry = Entry(root)
    #     concertTitleEntry.grid(row=0, column=x, pady=20, padx=5)

    # importContainer = tk.Frame(root, bg="#9CAFB7")
    # importContainer.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    # components['importContainer'] = importContainer

    # Import Buttons and Labels
    inputPathLabel = tk.Label(root, text="Input Path",
                              font=("bold", 14), pady=10)
    inputPathLabel.grid(row=0, column=0)

    toLabel = tk.Label(root, text="TO", font=("bold", 14))
    toLabel.grid(row=0, column=1)

    savePathLabel = tk.Label(root, text="Save Path", font=("bold", 14))
    savePathLabel.grid(row=0, column=2)

    chooseInputPath = tk.Button(
        root, text="Choose where to import from", padx=10, pady=5, fg="black", bg="#EAD2AC", command=lambda: selectInput(components))
    # chooseInputPath.pack()
    components['chooseInputPath'] = chooseInputPath
    chooseInputPath.grid(row=1, column=0, pady=20)

    chooseSavePath = tk.Button(
        root, text="Choose where to save", padx=10, pady=5, fg="black", bg="#EAD2AC", command=lambda: selectSave(components))
    # chooseSavePath.pack()
    components['chooseSavePath'] = chooseSavePath
    chooseSavePath.grid(row=1, column=2)

    # Project Details Notebook (tabs)
    projectDetailsLabel = tk.Label(
        root, text="Project Details", font=('bold', 14))
    projectDetailsLabel.grid(row=2, column=2)

    tabControl = ttk.Notebook(root)
    concertTab = ttk.Frame(tabControl)
    musicVidTab = ttk.Frame(tabControl)

    tabControl.add(concertTab, text='Concert')
    tabControl.add(musicVidTab, text='Music Video')
    # tabControl.pack(expand=1, fill="both")
    tabControl.grid(row=3, column=0, rowspan=6,
                    columnspan=3, pady=20, padx=20)

    # Concert Project Details
    concertTitleLabel = ttk.Label(concertTab, text="Title")
    concertTitleLabel.grid(column=0,
                           row=3,
                           padx=35,
                           pady=0)

    concertTitleEntry = ttk.Entry(concertTitleLabel)
    concertTitleEntry.grid(column=1,
                           row=4,
                           padx=35,
                           pady=0)

    concertDateLabel = ttk.Label(concertTab, text="Date")
    concertDateLabel.grid(column=0,
                          row=4,
                          padx=35,
                          pady=0)
    concertDateEntry = ttk.Entry(concertDateLabel)
    concertDateEntry.grid(column=1,
                          row=4,
                          padx=35,
                          pady=0)

    # Music Video Project Details
    musicVidArtistLabel = ttk.Label(musicVidTab, text="Artist")
    musicVidArtistLabel.grid(column=1,
                             row=4,
                             padx=35)
    musicVidArtistEntry = ttk.Entry(musicVidArtistLabel)
    musicVidArtistEntry.grid(column=1,
                             row=4,
                             padx=35,
                             pady=0)

    musicVidSongLabel = ttk.Label(musicVidTab, text="Song")
    musicVidSongLabel.grid(column=1,
                           row=5,
                           padx=35)
    musicVidSongEntry = ttk.Entry(musicVidSongLabel)
    musicVidSongEntry.grid(column=1,
                           row=5,
                           padx=35,
                           pady=0)

    musicVidDateLabel = ttk.Label(musicVidTab, text="Date")
    musicVidDateLabel.grid(column=1,
                           row=6,
                           padx=35)
    musicVidDateEntry = ttk.Entry(musicVidDateLabel)
    musicVidDateEntry.grid(column=1,
                           row=6,
                           padx=35,
                           pady=0)

    root.mainloop()


buildGUI(paths)
