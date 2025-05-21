# Effective screen resolution calculator for High DPI screens

def calculate_effective_resolution(width, height, scale_percent):
    scale_factor = scale_percent / 100
    effective_width = width / scale_factor
    effective_height = height / scale_factor
    effective_resolution = f"{int(effective_width)}x{int(effective_height)}"
    return effective_resolution

def calculate_effective_resolution_ui():
    print("\nCalculate the effective resolution of your high dpi screen\n")
    
    try:
        width = int(input("What is the width of your display in pixels? "))
        height = int(input("What is the height of your display in pixels? "))
        scale_percent = int(input("What is the scale in percent your desktop is currently set at? "))
    except ValueError:
        print("Something went wrong calculating. Please enter only numbers.")
        return
    
    effective_resolution = calculate_effective_resolution(width, height, scale_percent)
    
    print(f"\nThe effective resolution of your desktop is {effective_resolution} based on a scale of {int(scale_percent)}%.\n")

if __name__ == "__main__":
    calculate_effective_resolution_ui()
    

