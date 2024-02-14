import parking_space_counter as psc
import parking_space_picker as psp
import tkinter as tk
from tkinter import Button, Label, Entry

# park alanı ekran çıktısı için bunu çağır:  psc.parking_counter()
# park alanlarını işaretlemek için bunu çağır: psp.parking_picker() (.start() komutu ile örnekle)

class ParkingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Parking Management System")
        self.root.geometry("720x480")

        self.admin_login()

        # self.create_top_bar()
        # self.create_home_page()
        # self.create_bot_bar()

    def create_top_bar(self):
        top_bar = tk.Frame(self.root, bg="gray", height=50)
        top_bar.pack(side="top", fill="x")
        top_bar.pack_propagate(False)

        home_label = Label(top_bar, text="Ana Sayfa", bg="gray", fg="black", font=("Helvetica", 12))
        home_label.pack(side="left", padx=10)
        home_label.bind("<Button-1>", lambda event: self.show_home_page())

        admin_button = Button(top_bar, text="Admin Giriş", bg="gray", fg="black", command=self.admin_login)
        admin_button.pack(side="right", padx=10)

    def create_bot_bar(self):
        bot_bar = tk.Frame(self.root, bg="gray", height=60)
        bot_bar.pack(side="bottom", fill="x")
        bot_bar.pack_propagate(False)

    def create_home_page(self):
        home_frame = tk.Frame(self.root)
        home_frame.pack(expand=True)

        self.live_camera_button = Button(home_frame, text="Canlı Kamera İzle", command=self.show_live_camera_page, font=("Arial", 17), width=20, background="green")
        self.live_camera_button.grid(row=0, column=0, padx=10, pady=10)

        self.park_button = Button(home_frame, text="Park Alanı İşaretleme", command=self.picker_parking, font=("Arial", 17), width=20, background="green")
        self.park_button.grid(row=0, column=1, padx=10, pady=10)

        self.exit_button = Button(home_frame, text="Çıkış Yap", command=self.root.destroy, font=("Arial", 12), width=15, background="red")
        self.exit_button.grid(row=1, column=0, columnspan=2, pady=(20, 0), sticky="s")

    def show_home_page(self):
        self.temizle()
        self.create_top_bar()
        self.create_home_page()
        self.create_bot_bar()

    def dummy_function(self):
        print("Bu buton şu an için işlevsiz.")

    def temizle(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def admin_login(self):
        self.temizle()
        #self.create_bot_bar()
        #self.create_top_bar()
        #back_button = Button(self.root, text="Geri", bg="gray", fg="black", command=lambda: self.show_home_page())
        #back_button.pack(side="right", padx=10)

        self.id_label = Label(self.root, text="Admin Girişi:", font=("Arial", 20), fg="red")
        self.id_label.pack(pady=10)

        self.id_label = Label(self.root, text="Kullanıcı ID:", font=("Arial", 16))
        self.id_label.pack(pady=10)

        self.id_entry = Entry(self.root, font=("Arial", 16))
        self.id_entry.pack(pady=10)

        self.password_label = Label(self.root, text="Şifre:", font=("Arial", 16))
        self.password_label.pack(pady=10)

        self.password_entry = Entry(self.root, font=("Arial", 16))
        self.password_entry.pack(pady=10)

        login_button = Button(self.root, text="Giriş Yap", bg="green", fg="white", command=self.admin_login_process)
        login_button.pack(pady=10)

    def admin_login_process(self):
        self.admin_id = self.id_entry.get()
        self.admin_password = self.password_entry.get()
    
        with open(file="admin.txt", mode="r") as f:
            lines = f.readlines()
            failed_login = Label(None)
            for line in lines:
                # Her satırdaki değerleri virgülle ayır
                values = line.strip().split(",")
                
                # Eğer dosyanızın her zaman iki değer içerdiğini varsayıyorsanız:
                if len(values) == 2:
                    user_id, password = values
                    
                    if self.admin_id == user_id and self.admin_password == password:
                        failed_login.destroy()
                        success_login = Label(self.root, text=f"Hoşgeldiniz {user_id}", font=("Arial", 16), fg="green")
                        success_login.pack(pady=10)
                        # 2 saniye sonra fonksiyonu çağır
                        self.root.after(2000, self.show_home_page)
                        return  # Giriş başarılıysa fonksiyonu sonlandır
                    
                else:
                    print("Geçersiz satır formatı:", line)
                    
        
        failed_login = Label(self.root, text="Bilgileriniz sistemimizle uymadı!", font=("Arial", 16), fg="red")
        failed_login.pack(pady=10)
        self.root.after(2000, failed_login.destroy)
        

    def show_live_camera_page(self):
        # live_camera_window = Toplevel(self.root)
        # live_camera_window.title("Canlı Kamera İzle")
        # live_camera_window.geometry("720x480")

        # top_bar = tk.Frame(live_camera_window, bg="gray", height=60)
        # top_bar.pack(side="top", fill="x")
        # top_bar.pack_propagate(False)

        # back_button = Button(top_bar, text="Geri", bg="gray", fg="black", command=live_camera_window.destroy)
        # back_button.pack(side="right", padx=10)

        self.camera = psc.parking_counter()

    def picker_parking(self):
        # draw_parking = Toplevel(self.root)
        # draw_parking.title("Canlı Kamera İzle")
        # draw_parking.geometry("720x480")

        # top_bar = tk.Frame(draw_parking, bg="gray", height=60)
        # top_bar.pack(side="top", fill="x")
        # top_bar.pack_propagate(False)

        # back_button = Button(top_bar, text="Geri", bg="gray", fg="black", command=draw_parking.destroy)
        # back_button.pack(side="right", padx=10)

        self.draw = psp.parking_picker()
        self.draw.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ParkingApp(root)
    root.mainloop()
