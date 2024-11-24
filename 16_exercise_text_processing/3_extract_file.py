file_path = input().split("\\")
filename_and_extencion = file_path[-1]
filename, extension = filename_and_extencion.split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")
