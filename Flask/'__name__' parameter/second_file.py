import main_file

print(f"[second_file] __name__ = {__name__}") # Se è questo il file ad essere eseguito, allora il __name__ del file "second_file" viene eseguito, mentre il __name__ del file "main_file" equivale a 'main_file', non entrando quindi nell'if.