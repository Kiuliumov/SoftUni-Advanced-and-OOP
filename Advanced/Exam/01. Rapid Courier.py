from collections import deque

packages = list(map(int, input().split()))
couriers = deque(map(int, input().split()))
delivered_packages_weight = 0

while packages and couriers:
    current_courier = couriers.popleft()
    current_package = packages.pop()

    if current_package == current_courier:
        delivered_packages_weight += current_package

    elif current_package > current_courier:
        current_package -= current_courier
        delivered_packages_weight += current_courier
        packages.append(current_package)

    else:
        current_courier -= current_package * 2
        delivered_packages_weight += current_package

        if current_courier > 0:
            couriers.append(current_courier)




print('Total weight: {} kg'.format(delivered_packages_weight))

if packages:
    print('Unfortunately, there are no more available couriers to deliver the following packages: {}'.format(', '.join(map(str, packages))))
if couriers:
   print('Couriers are still on duty: {} but there are no more packages to deliver.'.format(', '.join(map(str, couriers))))
if not packages and not couriers:
    print('Congratulations, all packages were delivered successfully by the couriers today.')
