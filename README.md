# Pi Plant Timelapse

Raspberry Pi & webcam setup to upload plant pictures to AWS S3.

----

I inhereted some plants to look after while friends were living abroad and decided it would be nice if they could keep an eye on their progress. I had an unused Raspberry Pi and old USB webcam lying around and wanted to use python and AWS some more. This repo contains scripts for taking images an uploading to S3 which acted as static storage for a simple website.

## Technologies

- fswebcam
- Python 3
	- AWS boto3
- Raspberry Pi 2 Model B v1.1
- Microsoft LifeCam VX-5000

## Launch

Positioned webcam & Pi, uploaded files to Pi, connected to internet, and added rules to crontab:
```
# take pictures on the hour between 8AM and 6PM (no point in the dark)
0 8-18 * * * /home/pi/plantwatcher/snap > /home/pi/plantwatcher/cron.log

# upload images once a day at noon
0 12 * * * python /home/pi/plantwatcher/upload_img.py > /home/pi/plantwatcher/cron.log
```