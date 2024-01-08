from django.http import HttpResponse
from room.models import RoomType, Room
from django.db.utils import IntegrityError

def initialize_rooms_without_request():
    room_data = {
        'Glamping': {
            'units': [('Unit A', 8), ('Unit B', 8)],
            'max_capacity': 3,
            'prices': [(275000, 300000, False), (325000, 350000, True)]
        },
        'New Glamping': {
            'units': [('Standard', 7)],
            'max_capacity': 3,
            'prices': [(300000, 325000, False), (350000, 375000, True)]
        },
        'Family Tent': {
            'units': [('Standard', 3)],
            'max_capacity': 6,
            'prices': [(450000, 500000, False), (500000, 550000, True)]
        },
        'VIP Glamping': {
            'units': [('Standard', 5)],
            'max_capacity': 3,
            'prices': [(450000, 500000, False), (500000, 550000, True)]
        },
        'Oemah Kayu': {
            'units': [('Standard', 5)],
            'max_capacity': 3,
            'prices': [(500000, 550000, False), (550000, 600000, True)]
        },
        'Suite Room': {
            'units': [('Standard', 1)],
            'max_capacity': 3,
            'prices': [(650000, 700000, False), (700000, 750000, True)]
        },
    }

    for room_type_name, details in room_data.items():
        room_type, created = RoomType.objects.get_or_create(name=room_type_name, max_capacity=details['max_capacity'])
        
        for unit_name, unit_count in details['units']:
            for i in range(1, unit_count + 1):
                unit_full_name = f"{unit_name} {i}"
                for weekday_price, weekend_price, with_breakfast in details['prices']:
                    unique_id = f"{room_type_name}-{unit_full_name}-{weekday_price}-{weekend_price}-{with_breakfast}"
                    try:
                        Room.objects.create(
                            room_type=room_type,
                            unit_name=unit_full_name,
                            weekday_price=weekday_price,
                            weekend_price=weekend_price,
                            with_breakfast=with_breakfast,
                            unique_id=unique_id
                        )
                    except IntegrityError:
                        # Skip creation if room already exists
                        continue

    return HttpResponse("Room initialization completed.")
#South–South cooperation (Kerja sama Selatan-Selatan)
