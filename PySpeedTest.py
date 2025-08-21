from tkinter import *
import speedtest

root = Tk()
root.geometry("600x600")
root.title("Speed Test")

TitleLabel = Label(root,text="WIFI Speed Test")
TitleLabel.place(rely=0.25, relx=0.5, anchor=CENTER)

def TestFnc():
    SpeedTest = speedtest.Speedtest()
    DownloadSpeed = round(SpeedTest.download()/1000000,2)
    print(DownloadSpeed)
    DownloadSpeedLabel["text"] = "Download Speed: " + str(DownloadSpeed) + " Mbp/s"
    
    UploadSpeed = round(SpeedTest.upload()/1000000,2)
    print(UploadSpeed)
    UploadSpeedLabel["text"] = "Upload Speed: " + str(UploadSpeed) + " Mbp/s"

TestBtn = Button(root, text="Test", command=TestFnc ,height=10,width=15)
TestBtn.place(rely=0.5, relx=0.5, anchor=CENTER)

DownloadSpeedLabel = Label(root, text="Download Speed: ")
DownloadSpeedLabel.place(rely=0.7, relx=0.5, anchor=CENTER)

UploadSpeedLabel = Label(root, text="Upload Speed: ")
UploadSpeedLabel.place(rely=0.75, relx=0.5, anchor=CENTER)

root.mainloop()