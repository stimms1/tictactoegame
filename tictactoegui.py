from tictactoe import symbol, randomizer 
import tkinter as tk


root = tk.Tk()
root.title("Tic Tac Toe") 
root.geometry("800x500")
root.configure(bg="light gray")

label = tk.Label(root, text="Tic Tac Toe", font=("Arial", 24), bg="light gray")
label.pack(pady=15, padx=20)

button1 = tk.Button(root, text="Start Game", font=("Arial", 18), width=10, height=2)
button1.pack()
button1.place(x=325, y=400)

# row 1 
button2 = tk.Button(root, text="", font=("Arial", 18), width=5, height=2) #command=root.quit
button2.pack()
button2.place(x=250, y=100)

button3 = tk.Button(root, text="", font=("Arial", 18), width=5, height=2) #command=root.quit
button3.pack()
button3.place(x=345, y=100)

button4 = tk.Button(root, text="", font=("Arial", 18), width=5, height=2) #command=root.quit
button4.pack()
button4.place(x=440, y=100)

#row 2
button5 = tk.Button(root, text="", font=("Arial", 18), width=5, height=2) #command=root.quit
button5.pack()
button5.place(x=250, y=195)

button6 = tk.Button(root, text="", font=("Arial", 18), width=5, height=2) #command=root.quit
button6.pack()
button6.place(x=345, y=195)

button7 = tk.Button(root, text="", font=("Arial", 18), width=5, height=2) #command=root.quit
button7.pack()
button7.place(x=440, y=195)

#row 3 
button8 = tk.Button(root, text="", font=("Arial", 18), width=5, height=2) #command=root.quit
button8.pack()
button8.place(x=250, y=290)

button9 = tk.Button(root, text="", font=("Arial", 18), width=5, height=2) #command=root.quit
button9.pack()  
button9.place(x=345, y=290)

button10 = tk.Button(root, text="", font=("Arial", 18), width=5, height=2) #command=root.quit  
button10.pack()
button10.place(x=440, y=290)



turnLabel = tk.Label(root, text=f"{symbol}'s turn!", font=("Arial", 18), bg="light gray")
turnLabel.pack()
turnLabel.pack_forget()  # Hide initially

root.mainloop()




if __name__ == "__main__":  
    pass  # mainloop already called above
