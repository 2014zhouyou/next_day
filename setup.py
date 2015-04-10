from cx_Freeze import setup, Executable
setup(
    name = "GUI",
    version = "0.1",
    description = "test",
    executables = [Executable("GUI.py")],
)