import geometry
from geometry.flat import triangle_area
from geometry import sphere_volume, hemisphere_area

def main():
    print(f"geometry.__version__ = {geometry.__version__}")
    print(f"geometry.circle_area(3) = {geometry.circle_area(3):.4f}")
    print(f"triangle_area(6, 4) = {triangle_area(6, 4)}")
    print(f"sphere_volume(3) = {sphere_volume(3):.4f}")
    print(f"hemisphere_area(3) = {hemisphere_area(3):.3f}")
    
    print(f"\geometry.__all__ = {geometry.__all__}")
    print(f"geometry.__file__ = {geometry.__file__}")

if __name__ == '__main__':
    main()
