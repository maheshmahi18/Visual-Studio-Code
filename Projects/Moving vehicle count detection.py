import cv2
import numpy as np

def main():
    # Open the video file (you can specify the path to your video file)
    cap = cv2.VideoCapture(r"C:\Users\MAHESH\Downloads\PROJECT\vehicles on road .mp4")

    if not cap.isOpened():
        print("Error: Could not open the video file.")
        return

    # Set the video frame width and height
    cap.set(3, 1280)  # Width
    cap.set(4, 720)   # Height

    # Background subtractor
    subtractor = cv2.createBackgroundSubtractorMOG2()

    # Variables for vehicle counting
    vehicle_count = 0
    last_vehicle_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Perform background subtraction
        fg_mask = subtractor.apply(frame)

        # You can apply other image processing operations here if needed

        # Find contours in the foreground mask
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Count the number of moving vehicles
        moving_vehicle_count = 0

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:  # Adjust this threshold as needed
                moving_vehicle_count += 1

        # Display the frame with the foreground mask
        cv2.imshow("Foreground Mask", fg_mask)

        # Display the moving vehicle count in a new window
        vehicle_count_text = f"Moving Vehicle Count: {moving_vehicle_count}"
        cv2.putText(frame, vehicle_count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Vehicle Count", frame)

        # Check for vehicle count logic (you'll need to implement this part)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
