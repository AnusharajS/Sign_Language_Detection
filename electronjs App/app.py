from flask import Flask, render_template, Response
import cv2
import numpy as np

app = Flask(__name__)

camera = cv2.VideoCapture(0)  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# for local webcam use cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    global var
    var =1
    while True:

        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            from keras.models import load_model
            model = load_model('adam_50_15.h5')
            test_image = cv2.imread(frame)
            test_image = cv2.resize(test_image, (200, 200))
            test_image = np.expand_dims(test_image, axis=0)

            # Make predictions
            predictions = model.predict(test_image)

            # Get the predicted class label
            class_label = np.argmax(predictions, axis=1)
            position = (10,50)
            cv2.putText(frame,class_label,position,cv2.FONT_HERSHEY_SIMPLEX,1,(209, 80, 0, 255),3)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    var='1'
    return render_template('index.html',message= str(var) )

        



if __name__ == '__main__':
    app.run(debug=True)