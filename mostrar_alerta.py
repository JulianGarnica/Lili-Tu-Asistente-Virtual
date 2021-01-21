from win10toast import ToastNotifier
import six
import appdirs
import packaging.requirements

def mostrar_alerta_wind(titulo,texto):
    # Example
    toaster = ToastNotifier()
    toaster.show_toast(
        titulo,
        texto,
        icon_path="custom.ico",
        duration=10)





