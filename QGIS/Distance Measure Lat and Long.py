from qgis.core import QgsDistanceArea
from qgis.core import QgsUnitTypes
#Creator:Allen - Distance values from lat long locations 

#locations are subject to your lat and long inputs
Location_1 = (37.7749, -122.4194)
Location_2 = (40.661, -73.944)

d = QgsDistanceArea()
d.setEllipsoid('WGS84')


lat1, lon1 = Location_1
lat2, lon2 = Location_2
# Remember the order is X,Y
point1 = QgsPointXY(lon1, lat1)
point2 = QgsPointXY(lon2, lat2)

distance = d.measureLine([point1, point2])
print('Distance in meters', distance)

distance_km = d.convertLengthMeasurement(distance, QgsUnitTypes.DistanceKilometers)
print('Distance in kilometers', distance_km)

distance_mi = d.convertLengthMeasurement(distance, QgsUnitTypes.DistanceMiles)
print('Distance in miles', distance_mi)

distance_mi = d.convertLengthMeasurement(distance, QgsUnitTypes.DistanceMiles)
print('Distance in nautical miles', distance_mi)

distance_nm = d.convertLengthMeasurement(distance, QgsUnitTypes.DistanceNauticalMiles)
print('Distance in  nautical miles', distance_nm)