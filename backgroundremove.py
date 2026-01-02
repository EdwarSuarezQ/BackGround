import os
import shutil
from datetime import datetime
from rembg import remove
from PIL import Image, ImageSequence

class BackgroundRemover:

    def __init__(self, output_folder):
        self.output_folder = output_folder

    def process_images(self, input_files):
        if not input_files:
            return

        print(f"--- Iniciando procesamiento de {len(input_files)} imagenes ---")

        today = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        process_folder = os.path.join(self.output_folder, today)
        os.makedirs(process_folder, exist_ok=True)

        for i, input_path in enumerate(input_files, 1):
            if os.path.isfile(input_path):
                filename = os.path.basename(input_path)
                output_path = os.path.join(process_folder, filename)
                try:
                    print(f"[{i}/{len(input_files)}] Procesando: {filename} ...", end="", flush=True)
                    self._remove_background(input_path, output_path)
                    print(" ¡Listo!")
                    self._copy_originals(input_path, process_folder)
                except Exception as e:
                    print(f"\nError con {filename}: {e}")
        
        print(f"\n--- Proceso finalizado ---")
        print(f"Resultados guardados en: {process_folder}")


    def _remove_background(self, input_p, output_p):
         if input_p.lower().endswith(".gif"):
             self._remove_gif_background(input_p, output_p)
         else:
             with open(input_p, 'rb') as inp, open(output_p, 'wb') as oupt:
                 background_output = remove(inp.read())
                 oupt.write(background_output)
  

    def _remove_gif_background(self, input_p, output_p):
        with Image.open(input_p) as img:
            frames = []
            for frame in ImageSequence.Iterator(img):
                #convertir cada frame a RGBA para procesar transparencia
                frame_data = frame.convert("RGBA")
                #quitar fondo a cada cuadro con rembg
                processed_frame = remove(frame_data)
                frames.append(processed_frame)
            
            #guardar todos los cuadros de nuevo como un GIF animado
            if frames:
                frames[0].save(
                    output_p,
                    save_all=True,
                    append_images=frames[1:],
                    optimize=False,
                    duration=img.info.get('duration', 100),
                    loop=img.info.get('loop', 0),
                    disposal=2
                )


    def _copy_originals(self, input_p, dest_p):
        originals_folders = os.path.join(dest_p, "originals")
        os.makedirs(originals_folders, exist_ok=True)

        filename = os.path.basename(input_p)
        new_path = os.path.join(originals_folders, filename)
        shutil.copy2(input_p, new_path) #copia la imagen original


if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog
    import sys

    output_folder = "output"

    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    
    print("Por favor, selecciona las imagenes que deseas quitarles el fondo...")

    selected_files = filedialog.askopenfilenames(
        title="Selecciona imagenes para quitarles el fondo",
        filetypes=[
            ("Imagenes", "*.png *.jpg *.jpeg *.bmp *.webp *.tiff *.gif *.ico *.PNG *.JPG *.JPEG *.BMP *.WEBP *.TIFF *.GIF *.ICO")
        ]
    )
    
    root.destroy()

    if selected_files:
        remover = BackgroundRemover(output_folder)
        remover.process_images(selected_files)
    else:
        print("operacion cancelada: No se selecciono ninguna imagen")
        sys.exit()