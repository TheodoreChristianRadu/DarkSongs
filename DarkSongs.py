import tkinter
import Music

window = tkinter.Tk()

Music.start(lambda note, ratio, interval: print(note, ratio, interval))

window.mainloop()
