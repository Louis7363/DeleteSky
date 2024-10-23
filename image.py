from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import random


def choose_best_option():
    replace_sky()
    blue_count1 = count_blue_pixels("modified_image.png")
    replace_sky_column()
    blue_count2 = count_blue_pixels("modified_image.png")
    
    difference = blue_count2 - blue_count1
    print(difference, blue_count1, blue_count2)

    if difference >= 200:
        replace_sky()
    else:
        replace_sky_column()


def count_blue_pixels(image_path):
    image = Image.open(image_path)
    L, H = image.size
    blue_count = 0

    for y in range(H):
        for x in range(L):
            if (x * y) % 10000 == 0:
                print(x * y)
            r, g, b = image.getpixel((x, y))
            if (b > 150 and r < 200 and g <= 200) or (b > 180 and r < 200 and g >= 200):
                blue_count += 1

    return blue_count


def inverse_colors():
    process_image(pixel_transform=inverse_pixel_transform)


def inverse_pixel_transform(r, g, b):
    return g, b, r


def remove_red():
    process_image(pixel_transform=remove_red_pixel_transform)


def remove_red_pixel_transform(r, g, b):
    if r > 100 and b < 75 and g < 75:
        return 0, 0, 0
    return r, g, b


def randomize_pixels():
    if not file_path:
        print("No image file selected!")
        return

    image = Image.open(file_path)
    L, H = image.size
    new_image = Image.new("RGB", (L, H))

    for y in range(H):
        for x in range(L):
            X2 = random.randint(0, L - 1)
            Y2 = random.randint(0, H - 1)
            if (x * y) % 10000 == 0:
                print(f"Swapping pixels ({x},{y}) with ({X2},{Y2})")

            # Get the pixel from the original location (x, y)
            r, g, b = image.getpixel((x, y))

            # Place it in the new randomized location (X2, Y2)
            new_image.putpixel((X2, Y2), (r, g, b))

    # Save and display the modified image
    new_image.save("modified_image.png")
    display_final_image()


def replace_sky():
    replace_sky_generic(process_by="row")


def replace_sky_column():
    replace_sky_generic(process_by="column")


def replace_sky_generic(process_by="row"):
    if not file_path:
        print("No image file selected!")
        return

    image = Image.open(file_path)
    L, H = image.size
    cosmos = Image.open("cosmos2(1).jpg")
    new_image = Image.new("RGB", (L, H))

    if process_by == "row":
        for y in range(H):
            process_sky_row(image, cosmos, new_image, L, H, y)
    else:
        for x in range(L):
            process_sky_column(image, cosmos, new_image, L, H, x)

    new_image.save("modified_image.png")
    display_final_image()


def process_sky_row(image, cosmos, new_image, L, H, y):
    no_sky_count = 0
    stop = False

    for x in range(L):
        if stop:
            break
        if (x * y) % 10000 == 0:
            print(x * y)
        r, g, b = image.getpixel((x, y))

        is_sky = (b > 150 and r < 200 and g <= 200) or (b > 180 and r < 200 and g >= 200)
        if is_sky and not stop:
            cosmo_r, cosmo_g, cosmo_b = cosmos.getpixel((x, y))
            r, g, b = cosmo_r + 50, cosmo_g + 50, cosmo_b + 50
        else:
            no_sky_count += 1
        if no_sky_count >= L - 10:
            stop = True

        new_image.putpixel((x, y), (r - 50, g - 50, b - 50))


def process_sky_column(image, cosmos, new_image, L, H, x):
    no_sky_count = 0
    stop = False

    for y in range(H):
        if stop:
            break
        if (x * y) % 10000 == 0:
            print(x * y)
        r, g, b = image.getpixel((x, y))

        is_sky = (b > 150 and r < 200 and g <= 200) or (b > 180 and r < 200 and g >= 200)
        if is_sky and not stop:
            cosmo_r, cosmo_g, cosmo_b = cosmos.getpixel((x, y))
            r, g, b = cosmo_r + 50, cosmo_g + 50, cosmo_b + 50
        else:
            no_sky_count += 1
        if no_sky_count >= 60:
            stop = True

        new_image.putpixel((x, y), (r - 50, g - 50, b - 50))


def process_image(pixel_transform):
    if not file_path:
        print("No image file selected!")
        return

    image = Image.open(file_path)
    L, H = image.size
    new_image = Image.new("RGB", (L, H))

    for y in range(H):
        for x in range(L):
            if (x * y) % 10000 == 0:
                print(x * y)
            r, g, b = image.getpixel((x, y))
            new_r, new_g, new_b = pixel_transform(r, g, b)
            new_image.putpixel((x, y), (new_r, new_g, new_b))

    new_image.save("modified_image.png")
    display_final_image()


def display_image(img_path):
    image = Image.open(img_path)
    image.thumbnail((800, 800))
    photo = ImageTk.PhotoImage(image)
    label_image.config(image=photo)
    label_image.image = photo


def display_final_image():
    display_image("modified_image.png")


def open_file():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="/", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("All files", "*.*")])
    if file_path:
        display_image(file_path)
    else:
        file_path = "No file selected"
    label_file_explorer.config(text="Opened file: " + file_path)


def reset_image():
    if file_path:
        display_image(file_path)


# GUI setup
root = Tk()
root.title("Image Modification Tool")
root.geometry("1080x720")

label_file_explorer = Label(root, text="No file opened", width=100, height=4, fg="blue")
label_file_explorer.pack()

menu = Menu(root)
file_menu = Menu(menu, tearoff=0)
mod_menu = Menu(menu, tearoff=0)

file_menu.add_command(label="Open Image", command=open_file)
file_menu.add_command(label="Reset to Original", command=reset_image)
menu.add_cascade(label="File", menu=file_menu)

mod_menu.add_command(label="Replace Sky", command=replace_sky)
mod_menu.add_command(label="Replace Sky (Column-based)", command=replace_sky_column)
mod_menu.add_command(label="Choose Best Sky Replacement", command=choose_best_option)
mod_menu.add_command(label="Invert Colors", command=inverse_colors)
mod_menu.add_command(label="Remove Red", command=remove_red)
mod_menu.add_command(label="Randomize Pixels", command=randomize_pixels)
menu.add_cascade(label="Modify Image", menu=mod_menu)

root.config(menu=menu)

label_image = Label(root)
label_image.pack()

file_path = None  # File path initialized as None

root.mainloop()
