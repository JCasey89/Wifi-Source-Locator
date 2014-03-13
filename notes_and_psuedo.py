# ASSUME0: 1 antenna per node
# ASSUME1: connected to target access point
# ASSUME2: stationary target (for now)

#check if arduino is connected Bader
#init_servos Bader
#   set servos to 0, then sweep full range (0 to 180 to 0 to 90)
#init struct
#   struct data:
#       servoPan degree
#       servoTilt degree
#       nodeGPS co-ord
#       GPS time
#       wifi strength
#       wifiPoll time
#   NOTE: get time from GPS in python time struct for conversion
#           to epoch
#verify wificard exists

#binary search pan/tilt
#   while(some var)
#       wait for stable
#       get strength
#       compare strength with last
#       step half to stronger (make sure slice count is odd)
#   due to ASSUME2 no need to log


#
#binary search Pan
#binary search Tilt
#send final struct to server
