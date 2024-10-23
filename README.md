🌌 Sky Replacement and Image Modifications with Python

🖼️ Description
This project uses Python and Tkinter to provide a simple graphical interface for modifying images. It’s mainly designed to detect and replace the sky in an image, but it also includes other features such as color inversion and red removal.

The tool is user-friendly and is based on the Pillow library for image manipulation.

✨ Features

🌅 Sky Replacement: Automatically replaces the sky in an image with a sky image of your choice.
🧐 Best Replacement Selection: The program can choose the best sky replacement option based on certain analysis criteria.
🎨 Color Inversion: Inverts the colors of the image.
❌ Red Removal: Removes red tones from the image.
🎲 Random Pixel Modification: Applies random changes to the image.
🖥️ Graphical Interface: Uses Tkinter to allow intuitive interaction with the features.
🚀 Installation

Clone the repository
Clone this repository to your local machine with the following command:
```
git clone https://github.com/Louis7363/DeleteSky.git

```

Install dependencies
Make sure you have Python 3.7 or newer. Then, install the required libraries:
```
pip install pillow tkinter
```
Run the program
To start the application, simply run the image.py file:
```
python image.py
```

🛠️ Usage

Launch the application:
A Tkinter window will open with a menu at the top to choose options.

Choose an image:
Click "Files > Choose an image" to select the image you want to modify. The image will appear in the main window.

Apply modifications:
Select one of the available modifications from the "Image Modifications" menu:

🌅 Change Sky: Replaces the sky in the image with another image (by default, "cosmos2(1).jpg").
🌆 Change Sky with Column Processing: Replaces the sky column by column.
🧠 Select Best Sky Replacement Option: Automatically chooses the best sky replacement method.
🎨 Invert Colors: Inverts the colors of the image.
❌ Remove Red: Removes red tones from the image.
🎲 Apply Random Modifications: Randomly modifies pixels in the image.
Save the results:
Modified images will be saved as maNouvelleImage.png.

🖼️ Examples
Here are some examples of possible results:

Original Image

Sky Replaced

🤝 Contribution
Contributions are welcome! If you want to add features, fix bugs, or improve the interface, feel free to fork the project and submit a pull request. 😎

📝 License
This project is licensed under the MIT License. See the LICENSE file for more details.

⚠️ Known Issues

🧐 The program may misidentify the sky in complex images.
📏 The column-based sky replacement method may not give good results on certain images.

