import cv2
import os

def save_frames(frame1, frame2, directory1, directory2, frame_count):
    cv2.imwrite(os.path.join(directory1, f"{frame_count}.png"), frame1)
    cv2.imwrite(os.path.join(directory2, f"{frame_count}.png"), frame2)

def main(video_path1, video_path2, output_directory1, output_directory2):
    cap1 = cv2.VideoCapture(video_path1)
    cap2 = cv2.VideoCapture(video_path2)

    if not cap1.isOpened() or not cap2.isOpened():
        print("Error: Unable to open videos.")
        return

    os.makedirs(output_directory1, exist_ok=True)
    os.makedirs(output_directory2, exist_ok=True)

    frame_count = 0

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            print("End of videos.")
            break

        combined_frame = cv2.hconcat([frame1, frame2])
        cv2.imshow("Combined View", combined_frame)

        # cv2.imshow("Video 1", frame1)
        # cv2.imshow("Video 2", frame2)

        key = cv2.waitKey(0)

        if key == ord('s'):
            save_frames(frame1, frame2, output_directory1, output_directory2, frame_count)
        elif key == ord('q'):
            break

        frame_count += 1

    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path1 = "footage/new_black_synced_calib.mp4"
    video_path2 = "footage/new_blue_synced_calib.mp4"
    output_directory1 = "footage/black_calib"
    output_directory2 = "footage/blue_calib"

    video_path1 = "footage/final_black_synced.mp4"
    video_path2 = "footage/final_blue_synced.mp4"
    output_directory1 = "footage/black_bounce_final_2"
    output_directory2 = "footage/blue_bounce_final_2"

    main(video_path1, video_path2, output_directory1, output_directory2)
