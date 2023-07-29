#!/var/services/homes/changtman/dev/venv/bin/python3
print("Hello World!")
# use Task Scheduler to automate script each day 
# https://community.synology.com/enu/forum/17/post/70790?page=1&sort=oldest

# make sure requirements.txt satisfied
# set up docker instance
# docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest
# docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome
# run ms farmer script
# python main.py
# close docker?
