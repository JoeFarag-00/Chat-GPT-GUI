from tkinter import*
import random
import openai
import os
from tkinter import messagebox
openai.api_key = "Use your API key LOL"

#===============main=====================
class CON_AI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x560")
        self.root.title("Chat GPT API")
        title = Label(self.root, text="Chat GPT API", font=('Arial', 30, 'bold'), pady=2, bd=12, bg="#8A8A8A", fg="Black", relief=GROOVE)
        title.pack(fill=X)

        Input_Frame = LabelFrame(self.root, text="Input Tab", font=('Arial', 15, 'bold'), bd=10, fg="Black", bg="grey")
        Input_Frame.place(x=0, y=78, width=625, height=480)
        
        self.Input_txt=Text(Input_Frame, height=12, width=50,font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        self.Input_txt.grid(row=0, column=1, padx=20, pady=10)

        Output_Frame = Frame(self.root, bd=10, relief=GROOVE)
        Output_Frame.place(x=625, y=78, width=625, height=480)

        Reponse_LB = Label(Output_Frame, text="Response", font='arial 15 bold', bd=7,bg="grey", relief=GROOVE)
        Reponse_LB.pack(fill=X)
        scroll_y = Scrollbar(Output_Frame, orient=VERTICAL)
        self.Response_txt = Text(Output_Frame, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.Response_txt.yview)
        self.Response_txt.pack(fill=BOTH, expand=1)
        
        self.clear = False
        self.detect = False
        self.Qct=0
        
        SubInput_Frame = LabelFrame(Input_Frame, text="Options", font=('arial', 14, 'bold'), bd=10, fg="Black", bg="grey")
        SubInput_Frame.place(x=0, y=325, relwidth=1, height=120)
        
        Response_BTN = Button(SubInput_Frame, command=self.Permit_Response, text="Input", bg="#13B10F", bd=2, fg="black", pady=15, width=12, font='arial 13 bold')
        Response_BTN.grid(row=1, column=1, padx=5, pady=10)
        
        Clear_BTN = Button(SubInput_Frame, command=self.Clear_Data, text="Clear", bg="red", bd=2, fg="black", pady=15, width=12, font='arial 13 bold')
        Clear_BTN.grid(row=1, column=2, padx=5, pady=10)
        
        Reset_BTN = Button(SubInput_Frame, command=self.ResetWindow, text="Reset", bg="red", bd=2, fg="black", pady=15, width=12, font='arial 13 bold')
        Reset_BTN.grid(row=1, column=3, padx=5, pady=10)
        
        self.Response_txt.delete('1.0', END)
        self.Response_txt.insert(END, "\t \t     No Inputs Recieved...")
        self.Response_txt.insert(END, f"\n=====================================================================")
        self.Response_txt.insert(END, f"\n \t\tStart entering your questions!")
        self.Response_txt.insert(END, f"\n \t\tMake sure your API key is applied!")
    
    def Filter_Breaks(self,Input):
        return ''.join(Input.splitlines())

    def Permit_Response(self):
        self.Input = self.Input_txt.get("1.0","end-1c")
        self.Input = self.Filter_Breaks(self.Input)
        if self.Input == "":
            self.Response_txt.insert(END, f"\n")
            self.Response_txt.insert(END, f"\n Q{self.Qct}: No Input Question")  
        else:
            if not self.clear:    
                self.Response_txt.delete('1.0', END)
                self.Response_txt.insert(END, "\t \t Input Detected...")
                self.Response_txt.insert(END, f"\n=====================================================================") 
                self.clear=True
            self.Output_Response()
            
        
    def Output_Response(self):
        self.Qct+=1
        self.Response_txt.insert(END, f"\nQ{self.Qct}: {self.Input}")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.Input,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
            )
        Output = response['choices'][0]['text']
        # Response_Output = self.Filter_Breaks(Output)
        # self.Response_txt.insert(END, f"\n")
        self.Response_txt.insert(END, f"\nA: {Output}")
        self.Response_txt.insert(END, f"\n")
        self.Input_txt.delete('1.0', END)
   
    def Clear_Data(self):
        self.Response_txt.delete('1.0', END)
        self.Qct = 0
        

    def ResetWindow(self):
        root.destroy()
        os.system('Main_GUI.py')


root = Tk()
obj = CON_AI(root)
root.mainloop()


