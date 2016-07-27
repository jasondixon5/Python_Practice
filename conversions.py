def meter2inch(meters):
    t = type(meters)
    
    if t == float or t == int:
        return meters * 39.3701
    elif t == list or t == set:
        return [i * 39.3701 for i in meters]
    else:
        print("Input type not supported. Please enter an integer, float, list, or set.")

def inch2meter(inches):
    t = type(inches)
    
    if t == float or t == int:
        return inches / 39.3701
    elif t == list or t == set:
        return [i / 39.3701 for i in inches]
    else:
        print("Input type not supported. Please enter an integer, float, list, or set.")

def pound2kilo(pound):
    t = type(pound)
    
    if t == float or t == int:
        return pound * 0.453592
    elif t == list or t == set:
        return [i * 0.453592 for i in pound]
    else:
        print("Input type not supported. Please enter an integer, float, list, or set.")

def kilo2pound(kilo):
    t = type(kilo)
    
    if t == float or t == int:
        return kilo * 2.20462
    elif t == list or t == set:
        return [i * 2.20462 for i in kilo]
    else:
        print("Input type not supported. Please enter an integer, float, list, or set.")

#bmiUS takes weight in pounds and height in inches
def bmiUS(weight, height):
    return (weight / height ** 2) * 703

# bmiEuro takes weight in kilograms and height in meters    
def bmiEuro(weight, height):
    return (weight / height **2)