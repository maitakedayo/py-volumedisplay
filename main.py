import tkinter as tk
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def get_system_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume.GetMasterVolumeLevelScalar()

def show_volume_window():
    root = tk.Tk()
    root.title("System Volume")

    def update_volume():
        volume_label['text'] = f"現在の音量: {get_system_volume()}"
        volume_label['font'] = ('Arial', 24)  # フォントサイズを3倍に変更
        root.after(1000, update_volume)

    volume_label = tk.Label(root, text="")
    volume_label.pack(padx=40, pady=40)
    
    update_volume()
    root.mainloop()

if __name__ == "__main__":
    show_volume_window()