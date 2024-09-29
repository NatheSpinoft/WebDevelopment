import sys

def print_modules_cleanly():
    print("Loaded Modules:\n")
    for module_name, module in sys.modules.items():
        print(module_name + ": " + str(module))

if __name__ == "__main__":
    print_modules_cleanly()
