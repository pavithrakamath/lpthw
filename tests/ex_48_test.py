from ex48 import Room, Bedroom

def test_ex48():
    room: Room = Bedroom("Bedroom", "A bedroom with a bed and a dresser")
    room.enter()
    assert room.name == "Bedroom"
    assert room.description == "A bedroom with a bed and a dresser"
