import cv2

# Store clicked points
points = []

# Mouse callback to collect 4 clicks: 2 for reference, 2 for building
def click_event(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Click 2 points on reference, then 2 on building", img)

        if len(points) == 4:
            # Reference object height in pixels
            ref_pixel_height = abs(points[1][1] - points[0][1])
            # Building height in pixels
            building_pixel_height = abs(points[3][1] - points[2][1])

            print(f"Reference Object Pixel Height: {ref_pixel_height}")
            print(f"Building Pixel Height: {building_pixel_height}")

            # Ask user for real-world height of reference object
            real_ref_height = float(input("Enter real-world height of the reference object (in meters): "))

            # Calculate estimated height
            estimated_building_height = (building_pixel_height / ref_pixel_height) * real_ref_height
            print(f"\n Estimated Building Height: {estimated_building_height:.2f} meters")

            # Save annotated image
            cv2.line(img, points[0], points[1], (255, 0, 0), 2)
            cv2.line(img, points[2], points[3], (0, 0, 255), 2)
            cv2.imwrite("annotated_building_height.png", img)
            print("\n Annotated image saved as 'annotated_building_height.png'.")

# Load image
img_path = "rit.jpg"  # Replace with your filename
img = cv2.imread(img_path)

if img is None:
    print(f" Image '{img_path}' not found. Make sure it's in the same folder.")
    exit()

cv2.imshow("Click 2 points on reference, then 2 on building", img)
cv2.setMouseCallback("Click 2 points on reference, then 2 on building", click_event)

print(" INSTRUCTIONS:")
print("1. Click TOP and BOTTOM of the known object (e.g., a 2m door).")
print("2. Then click TOP and BOTTOM of the building.")
print("3. The program will calculate the building's height.\n")

cv2.waitKey(0)
cv2.destroyAllWindows()
