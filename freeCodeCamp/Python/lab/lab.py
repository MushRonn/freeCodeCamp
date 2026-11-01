# Building a Travel Weather Planner

distance_mi = 1
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print('False')
elif distance_mi <= 1 and not is_raining:
    print('True')
elif distance_mi <= 1 and is_raining:
    print('False')
elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining:
    print('True')
elif distance_mi > 6 and has_ride_share_app:
    print('True')
elif distance_mi > 6 and has_car:
    print('True')
else:
    print('False')