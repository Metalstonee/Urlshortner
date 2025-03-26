from os import system
def ClipBoard(url):
    command = 'echo ' + url.strip() + '| clip'
    system(command)