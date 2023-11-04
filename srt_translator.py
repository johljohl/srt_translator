import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import spacy
from googletrans import Translator
import re
import threading

# Ladda spaCy-modellen för engelska
nlp = spacy.load("en_core_web_sm")

def translate_srt(file_path, output_path, dest_lang='sv', progress_callback=None):
    translator = Translator()
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.readlines()

    total_lines = len(contents)
    translated_contents = []
    for index, line in enumerate(contents):
        if re.match(r'\d\d:\d\d:\d\d', line) or re.match(r'\d+', line):
            translated_contents.append(line)
        else:
            if line.strip() != "":
                # Använd spaCy för att hitta namn i texten
                doc = nlp(line)
                names = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
                
                # Ersätt namn med placeholders
                temp_line = line
                for name in names:
                    temp_line = temp_line.replace(name, f'{{{names.index(name)}}}')
                
                # Översätt texten
                translated_line = translator.translate(temp_line, dest=dest_lang).text

                # Återställ namnen från placeholders
                for name in names:
                    translated_line = translated_line.replace(f'{{{names.index(name)}}}', name)

                translated_contents.append(translated_line + '\n')
            else:
                translated_contents.append('\n')

        # Uppdatera progressbaren
        if progress_callback:
            progress_callback(index + 1, total_lines)

    # Spara den översatta filen
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(translated_contents)

    return output_path

def update_progressbar(progress, total):
    progress_var.set(progress)
    progress_bar['maximum'] = total
    percent = f"{(progress / total) * 100:.1f}%"
    progress_label.config(text=percent)
    root.update_idletasks()

def translate_thread(file_path, output_path):
    try:
        translated_path = translate_srt(file_path, output_path, progress_callback=update_progressbar)
        messagebox.showinfo("Translation Complete", f"Translated file saved as: {translated_path}")
    except Exception as e:
        messagebox.showerror("Translation Failed", str(e))
    finally:
        progress_var.set(0)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("SRT files", "*.srt")])
    if file_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".srt", filetypes=[("SRT files", "*.srt")])
        if output_path:
            threading.Thread(target=translate_thread, args=(file_path, output_path), daemon=True).start()

def create_gui():
    global root, progress_var, progress_bar, progress_label
    root = tk.Tk()
    root.title("SRT Translator")

    open_button = tk.Button(root, text="Open SRT File", command=open_file)
    open_button.pack(side=tk.TOP, pady=10)

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, variable=progress_var, length=200)
    progress_bar.pack(side=tk.TOP, pady=10)

    progress_label = tk.Label(root, text="0%")
    progress_label.pack(side=tk.TOP, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
