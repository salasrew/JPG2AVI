# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
import glob
from tkinter import filedialog, StringVar,Button,Label,Entry,Tk
from tkinter import messagebox
from cv2 import imread,VideoWriter,VideoWriter_fourcc

window = Tk()
window.title('JPG2AVI')
window.geometry('250x80')

img_array=[]

def btn_clicked():
    path = filedialog.askdirectory()
    dict_path.set(path)

def pic2avi():
    file_name = text_h8.get()+'.avi'
    folder = (dict_path.get())
    for filename in glob.glob(folder+'/*.jpg'):
        img = imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = VideoWriter(file_name, VideoWriter_fourcc(*'DIVX'), 5, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

    messagebox.showinfo('訊息', '轉換完成')

dict_path = StringVar()

# Button
btn_file_path = Button(window,text = '選擇資料夾',command = btn_clicked)
btn_file_path.place(x=0,y=20)

btn_convert = Button(window,text = '轉換影片',command = pic2avi)
btn_convert.place(x=100,y=20)


# Label
lb_exp = Label(window,text='請輸入影片名稱:')
lb_exp.place(x=0,y=0)

# Entry
text_h8 = Entry(window,width=10,justify='right')
text_h8.insert(0,'default')
text_h8.place(x=95,y=0)

window.mainloop()


#  Progressbar widget