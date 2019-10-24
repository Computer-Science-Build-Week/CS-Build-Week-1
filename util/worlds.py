from adventure.models import Room
import random

rooms = [
    'Krollixath',
    'Gripporune',
    'Kiavala',
    'Acluven',
    'Aelleoros',
    'The Malachite Universe',
    'The Cyber Region',
    'The God Province',
    'The Ghost Isle',
    'The Illusion Domain',
    'Kliorreadran',
    'Qoneonet',
    'Zaeccomos',
    'Igleagana',
    'Votoroth',
    'The Double Lake',
    'The Eclipse Moon',
    'The Golden Terrain',
    'The Aquamarine Vales',
    'The Sanguine Isle',
    'Secianium',
    'Aebbiobis',
    'Oyimelan',
    'Camephere',
    'Xotozan',
    'The Delusion Realm',
    'The Sanguine Land',
    'The Portal Isle',
    'The Shadow Sea',
    'The Calm Region',
    'Acutall',
    'Zoheovion',
    'Achiabis',
    'Kriakkirune',
    'Meossedu',
    'The Fortune Dominion',
    'The Boiling Isle',
    'The Dormant Sanctuary',
    'The Everday Ocean',
    'The Hell Reach',
    'Bacithra',
    'Aeniomel',
    'Klioggala',
    'Drisonium',
    'Xoddethae',
    'The Rain Universe',
    'The Parallel Dominion',
    'The Undying Realm',
    'The Terminal Territory',
    'The Boiling Isles',
    'Ioyerion',
    'Graewitria',
    'Lioppilon',
    'Rommughar',
    'Writtaque',
    'The Iron Nation',
    'The Howling Terrain',
    'The White Valley',
    'The Vision Province',
    'The Forged Isles',
    'Heapiomel',
    'Buweogarth',
    'Rearerus',
    'Kaekkoque',
    'Chopusos',
    'The Hidden Sanctuary',
    'The Rabid Territories',
    'The Harsh Country',
    'The Crimson Plane',
    'The Manifested Earth',
    'Yiqixus',
    'Aeddorune',
    'Yeshoxar',
    'Heoginium',
    'Klinnotopia',
    'The Emerald Planet',
    'The Lonely Expanse',
    'The Mist Universe',
    'The Scarlet Realms',
    'The Aquamarine Reach',
    'Aerriaxar',
    'Shihiogarth',
    'Eolicyre',
    'Aedorah',
    'Dreadduphere',
    'The Invisible Territory',
    'The Savage Reach',
    'The Sinking Country',
    'The Broken Valley',
    'The Sinking Vales',
    'Straebinet',
    'Ekkorynn',
    'Chuyuphere',
    'Saefeonet',
    'Qiaputha',
    'The Scarlet Vale',
    'The Ash Sanctum',
    'The Enigma Dominion',
    'The Cerulean Ocean',
    'The Imagined Sea',
    'Yaeggidin',
    'Pliajeoque',
    'Qeavezan',
    'Yajeatuary',
    'Eadagana',
    'The Parallel Sanctum',
    'The Onyx Sanctum',
    'The Abyss Earth',
    'The Mortal Isle',
    'The Spring Territory',
    'Aestriatuary',
    'Rioglirah',
    'Eojuther',
    'Phitothis',
    'Tabrutara',
    'The Burning Vale',
    'The Dream Land',
    'The Abandoned Isle',
    'The Treacherous Territories',
    'The Calm Fields',
    'Kaenetora',
    'Uyirath',
    'Bleotinys',
    'Egeaver',
    'Pleoxeorion',
    'The Mammoth Realms',
    'The Snow Plane',
    'The Ivory World',
    'The Rabid Sanctuary',
    'The Terminal World',
    'Eglanata',
    'Giocheothae',
    'Gesodell',
    'Qophicia',
    'Cuglodu',
    'The Forged Isle',
    'The Ivory Vales',
    'The Utopia Ocean',
    'The Cerulean Sea',
    'The Thunder Dominion',
    'Iafover',
    'Iaviodolon',
    'Biviatha',
    'Wriaziarah',
    'Miommianica',
    'The Specter Region',
    'The Miracle Region',
    'The Nimbus Valley',
    'The Dream Isles',
    'The Soul Territories',
    'Wrideven',
    'Eyathan',
    'Ioglerial',
    'Vaecliorah',
    'Draekkiocyre',
    'The Covert Sanctuary',
    'The Eclipse Yonder',
    'The Fate Universe',
    'The Parallel Expanse',
    'The Titan Vales',
    'Gleakkether',
    'Aeddiagana',
    'Eakkinon',
    'Hoyenia',
    'Peobrerune',
    'The Everday Region',
    'The Single World',
    'The Monster Forest',
    'The Cerulean Nexus',
    'The Ancestor Sea',
    'Oferia',
    'Veglearhia',
    'Griahuspea',
    'Eobbutria',
    'Fomiothan',
    'The Abyss Universe',
    'The Mock Sanctuary',
    'The Rabid Country',
    'The Destiny World',
    'The Solar Vales',
    'Ikeven',
    'Eogibis',
    'Eonnenon',
    'Preommeasos',
    'Aziothra',
    'The Inferno Sanctuary',
    'The Oblivion Moon',
    'The Ice Empire',
    'The Echo Earth',
    'The Flaming Planet',
    'Zeostriochaeus',
    'Aecunys',
    'Breggeanem',
    'Crunexath',
    'Shilliryon',
    'The Ice Sanctuary',
    'The Winter Ocean',
    'The Invisible Vales',
    'The Specter Nexus',
    'The Riddle Domain',
]


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1  # (this will become 0 on the first step)
        y = 0
        room_count = 0

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west

        # While there are rooms to be created...
        previous_room = None
        while room_count < num_rooms:

            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 1
                direction *= -1

            # Create a room in the given direction
            room = Room(id=room_count, title=rooms[room_count-1],
                        description="A world at stake. The quest for the ultimate prize. Are you ready?", x=x, y=y)
            # Note that in Django, you'll need to save the room after you create it

            room.save()

            # Save the room in the World grid
            self.grid[y][x] = room

            # Connect the new room to the previous room
            if previous_room is not None:
                previous_room.connectRooms(room, room_direction)

            # Update iteration variables
            previous_room = room
            room_count += 1
            room.save()

    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid)  # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)


w = World()
num_rooms = 200
width = 20
height = 20
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(
    f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
